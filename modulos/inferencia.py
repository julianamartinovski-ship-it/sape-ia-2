from __future__ import annotations

import unicodedata
from typing import Any

from modulos.banco_prenatal import BANCO_PRENATAL


def _lista(valor: Any) -> list:
    """Converte valores simples, tuplas e conjuntos em lista."""
    if valor is None or valor == "":
        return []

    if isinstance(valor, list):
        return valor

    if isinstance(valor, (tuple, set)):
        return list(valor)

    return [valor]


def _normalizar(texto: Any) -> str:
    """
    Normaliza texto para comparação:
    - remove acentos;
    - converte para minúsculas;
    - remove espaços duplicados.
    """
    texto = str(texto or "").strip()
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(
        caractere
        for caractere in texto
        if not unicodedata.combining(caractere)
    )
    return " ".join(texto.casefold().split())


def _flatten(valor: Any) -> list:
    """Transforma estruturas aninhadas em uma lista simples de achados."""
    if valor is None or valor == "":
        return []

    if isinstance(valor, dict):
        saida = []
        for item in valor.values():
            saida.extend(_flatten(item))
        return saida

    if isinstance(valor, (list, tuple, set)):
        saida = []
        for item in valor:
            saida.extend(_flatten(item))
        return saida

    return [valor]


def _achado_presente(criterio: Any, achados: list) -> bool:
    """
    Verifica correspondência entre um critério da regra e os achados
    selecionados pelo profissional.
    """
    criterio_normalizado = _normalizar(criterio)

    if not criterio_normalizado:
        return False

    for achado in achados:
        achado_normalizado = _normalizar(achado)

        if not achado_normalizado:
            continue

        # Correspondência exata
        if criterio_normalizado == achado_normalizado:
            return True

        # Correspondência por expressão composta.
        # Evita que palavras curtas provoquem ativações indevidas.
        if (
            len(criterio_normalizado) >= 8
            and " " in criterio_normalizado
            and criterio_normalizado in achado_normalizado
        ):
            return True

        if (
            len(achado_normalizado) >= 8
            and " " in achado_normalizado
            and achado_normalizado in criterio_normalizado
        ):
            return True

    return False


def _item_cipe(valor: Any) -> list[dict]:
    """
    Converte diagnóstico, resultado ou intervenção em uma lista
    padronizada no formato:

    {
        "codigo": "...",
        "termo": "..."
    }
    """
    if not valor:
        return []

    saida = []

    for item in _lista(valor):
        if isinstance(item, dict):
            codigo = (
                item.get("codigo")
                or item.get("code")
                or item.get("id_cipe")
            )

            termo = (
                item.get("termo")
                or item.get("nome")
                or item.get("descricao")
                or item.get("label")
                or ""
            )

            codigo = str(codigo).strip() if codigo not in (None, "", "None") else None
            termo = str(termo).strip()

            if termo or codigo:
                saida.append({
                    "codigo": codigo,
                    "termo": termo,
                })

        elif item not in (None, "", "None"):
            saida.append({
                "codigo": None,
                "termo": str(item).strip(),
            })

    return _deduplicar_itens_cipe(saida)


def _deduplicar_itens_cipe(itens: list[dict]) -> list[dict]:
    """
    Remove duplicações e prioriza a versão que possui código CIPE.

    Exemplo:
    - Pressão arterial alterada, sem código
    - Pressão arterial alterada, código 100...

    Resultado:
    - permanece apenas a versão com código.
    """
    consolidados: dict[str, dict] = {}

    for item in itens:
        termo = str(item.get("termo") or "").strip()
        codigo = item.get("codigo")
        chave = _normalizar(termo) or str(codigo or "").strip()

        if not chave:
            continue

        atual = consolidados.get(chave)

        if atual is None:
            consolidados[chave] = {
                "codigo": codigo,
                "termo": termo,
            }
            continue

        # Substitui a versão sem código pela versão codificada.
        if not atual.get("codigo") and codigo:
            consolidados[chave] = {
                "codigo": codigo,
                "termo": termo or atual.get("termo", ""),
            }

    return list(consolidados.values())


def _extrair_cipe(regra: dict, tipo: str) -> list[dict]:
    """
    Localiza conteúdo CIPE tanto no formato atual quanto em estruturas
    antigas que ainda possam existir no banco.
    """
    bloco_cipe = regra.get("cipe")

    if not isinstance(bloco_cipe, dict):
        bloco_cipe = {}

    nomes = {
        "diagnostico": ("diagnostico", "diagnosticos"),
        "resultado": ("resultado", "resultados"),
        "intervencao": ("intervencao", "intervencoes"),
    }

    singular, plural = nomes[tipo]

    valor = (
        regra.get(singular)
        or regra.get(plural)
        or bloco_cipe.get(singular)
        or bloco_cipe.get(plural)
    )

    return _item_cipe(valor)


def _quantidade_codigos(sugestao: dict) -> int:
    """Conta quantos itens CIPE válidos existem em uma sugestão."""
    total = 0

    for campo in ("cipe_diag", "cipe_res", "cipe_int"):
        for item in sugestao.get(campo, []):
            if item.get("codigo"):
                total += 1

    return total


def _pontuacao_sugestao(sugestao: dict) -> tuple:
    """
    Pontua uma sugestão para escolher a melhor versão quando houver
    duplicação entre regra antiga e regra nova.
    """
    quantidade_codigos = _quantidade_codigos(sugestao)
    quantidade_itens = sum(
        len(sugestao.get(campo, []))
        for campo in ("cipe_diag", "cipe_res", "cipe_int")
    )
    tamanho_fundamentacao = len(
        str(sugestao.get("fundamentacao") or "")
    )
    possui_transcultural = bool(sugestao.get("transcultural"))

    return (
        quantidade_codigos,
        quantidade_itens,
        possui_transcultural,
        tamanho_fundamentacao,
    )


def _chave_da_regra(sugestao: dict) -> tuple:
    """
    Cria uma assinatura clínica para detectar regras repetidas.

    Regras com o mesmo título e os mesmos achados ativadores são
    consideradas versões da mesma regra.
    """
    titulo = _normalizar(
        sugestao.get("titulo")
        or sugestao.get("regra")
    )

    achados = tuple(sorted({
        _normalizar(item)
        for item in sugestao.get("achados_ativadores", [])
        if _normalizar(item)
    }))

    return titulo, achados


def executar_inferencia(
    achados: list | None,
    transcultural: dict | list | None,
    linguagem: str | None,
) -> list[dict]:
    """
    Cruza achados clínicos e transculturais com o banco de regras
    clínicas do pré-natal.

    Mantém compatibilidade com as telas atuais do SAPE IA 2.0.
    """
    todos_achados = _flatten(achados) + _flatten(transcultural)

    # Remove repetições entre avaliação clínica e transcultural.
    achados_unicos = []
    achados_vistos = set()

    for achado in todos_achados:
        chave = _normalizar(achado)

        if chave and chave not in achados_vistos:
            achados_vistos.add(chave)
            achados_unicos.append(achado)

    sugestoes_consolidadas: dict[tuple, dict] = {}

    for indice, regra in enumerate(BANCO_PRENATAL, start=1):
        if not isinstance(regra, dict):
            continue

        obrigatorios = _lista(regra.get("criterios_obrigatorios"))

        if not obrigatorios:
            obrigatorios = _lista(
                regra.get("achado_clinico")
                or regra.get("gatilho")
                or regra.get("achado")
            )

        associados = _lista(regra.get("criterios_associados"))

        # Regra sem gatilho clínico não deve ser ativada automaticamente.
        if not obrigatorios:
            continue

        if not all(
            _achado_presente(criterio, achados_unicos)
            for criterio in obrigatorios
        ):
            continue

        associados_encontrados = [
            criterio
            for criterio in associados
            if _achado_presente(criterio, achados_unicos)
        ]

        titulo = (
            regra.get("titulo")
            or regra.get("regra")
            or regra.get("achado_clinico")
            or regra.get("gatilho")
            or f"Regra {indice}"
        )

        diagnosticos = _extrair_cipe(regra, "diagnostico")
        resultados = _extrair_cipe(regra, "resultado")
        intervencoes = _extrair_cipe(regra, "intervencao")

        sugestao = {
            "id": regra.get("id") or f"PN{indice:04d}",
            "titulo": str(titulo).strip(),
            "regra": str(titulo).strip(),
            "categoria": regra.get("categoria") or "Pré-natal",
            "prioridade": regra.get("prioridade") or "",
            "gravidade": (
                regra.get("gravidade")
                or regra.get("prioridade")
                or ""
            ),
            "grau": (
                regra.get("grau")
                or regra.get("prioridade")
                or ""
            ),
            "evidencia": regra.get("evidencia") or "",
            "justificativa": (
                regra.get("justificativa")
                or regra.get("fundamentacao")
                or regra.get("evidencia")
                or ""
            ),
            "fundamentacao": (
                regra.get("fundamentacao")
                or regra.get("justificativa")
                or regra.get("evidencia")
                or ""
            ),
            "achados": obrigatorios + associados_encontrados,
            "achados_ativadores": obrigatorios + associados_encontrados,
            "cipe_diag": diagnosticos,
            "cipe_res": resultados,
            "cipe_int": intervencoes,
            "nanda": _lista(regra.get("nanda")),
            "noc": _lista(regra.get("noc")),
            "nic": _lista(regra.get("nic")),
            "transcultural": (
                regra.get("transcultural")
                if isinstance(regra.get("transcultural"), dict)
                else {}
            ),
            "referencias": _lista(regra.get("referencias")),
            "linguagem": linguagem or "CIPE",
        }

        chave = _chave_da_regra(sugestao)
        sugestao_existente = sugestoes_consolidadas.get(chave)

        if sugestao_existente is None:
            sugestoes_consolidadas[chave] = sugestao
            continue

        # Entre a regra antiga e a nova, mantém a mais completa,
        # priorizando aquela que possui códigos CIPE.
        if _pontuacao_sugestao(sugestao) > _pontuacao_sugestao(
            sugestao_existente
        ):
            sugestoes_consolidadas[chave] = sugestao

    sugestoes = list(sugestoes_consolidadas.values())

    prioridade_ordem = {
        "alta": 0,
        "media": 1,
        "média": 1,
        "baixa": 2,
    }

    sugestoes.sort(
        key=lambda item: (
            prioridade_ordem.get(
                _normalizar(item.get("prioridade")),
                3,
            ),
            _normalizar(item.get("titulo")),
        )
    )

    return sugestoes