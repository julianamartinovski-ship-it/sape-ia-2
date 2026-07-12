from modulos.banco_prenatal import BANCO_PRENATAL
import unicodedata


def _lista(valor):
    if not valor:
        return []
    return valor if isinstance(valor, list) else [valor]


def _normalizar(texto):
    texto = str(texto or "")
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return " ".join(texto.casefold().split())


def _achado_presente(criterio, achados):
    c = _normalizar(criterio)
    for achado in achados:
        a = _normalizar(achado)
        if c == a or (len(c) >= 5 and c in a) or (len(a) >= 5 and a in c):
            return True
    return False


def _flatten(valor):
    if not valor:
        return []
    if isinstance(valor, list):
        return valor
    if isinstance(valor, dict):
        saida = []
        for item in valor.values():
            saida.extend(_flatten(item))
        return saida
    return [valor]


def _item_cipe(valor):
    if not valor:
        return []
    itens = _lista(valor)
    saida = []
    for item in itens:
        if isinstance(item, dict):
            codigo = item.get("codigo")
            termo = item.get("termo") or item.get("nome") or ""
            saida.append({"codigo": codigo, "termo": termo})
        else:
            saida.append({"codigo": None, "termo": str(item)})
    return saida


def executar_inferencia(achados, transcultural, linguagem):
    todos_achados = list(achados or []) + _flatten(transcultural)
    sugestoes = []
    vistos = set()

    for indice, regra in enumerate(BANCO_PRENATAL, start=1):
        obrigatorios = _lista(regra.get("criterios_obrigatorios"))
        if not obrigatorios:
            obrigatorios = _lista(regra.get("achado_clinico"))
        associados = _lista(regra.get("criterios_associados"))

        if not obrigatorios or not all(_achado_presente(x, todos_achados) for x in obrigatorios):
            continue

        associados_encontrados = [x for x in associados if _achado_presente(x, todos_achados)]
        titulo = regra.get("titulo") or regra.get("regra") or regra.get("achado_clinico") or f"Regra {indice}"
        diag = _item_cipe(regra.get("diagnostico") or regra.get("cipe", {}).get("diagnostico") or regra.get("cipe", {}).get("diagnosticos"))
        res = _item_cipe(regra.get("resultado") or regra.get("cipe", {}).get("resultado") or regra.get("cipe", {}).get("resultados"))
        inter = _item_cipe(regra.get("intervencao") or regra.get("cipe", {}).get("intervencao") or regra.get("cipe", {}).get("intervencoes"))

        chave = (_normalizar(titulo), tuple((x.get("codigo"), _normalizar(x.get("termo"))) for x in diag))
        if chave in vistos:
            continue
        vistos.add(chave)

        sugestoes.append({
            "id": regra.get("id") or f"PN{indice:04d}",
            "titulo": titulo,
            "regra": titulo,
            "categoria": regra.get("categoria", "Pré-natal"),
            "prioridade": regra.get("prioridade", ""),
            "gravidade": regra.get("gravidade") or regra.get("prioridade", ""),
            "grau": regra.get("grau") or regra.get("prioridade", ""),
            "evidencia": regra.get("evidencia", ""),
            "justificativa": regra.get("justificativa") or regra.get("fundamentacao") or regra.get("evidencia", ""),
            "fundamentacao": regra.get("fundamentacao") or regra.get("evidencia", ""),
            "achados": obrigatorios + associados_encontrados,
            "achados_ativadores": obrigatorios + associados_encontrados,
            "cipe_diag": diag,
            "cipe_res": res,
            "cipe_int": inter,
            "nanda": _lista(regra.get("nanda")),
            "noc": _lista(regra.get("noc")),
            "nic": _lista(regra.get("nic")),
            "transcultural": regra.get("transcultural", {}),
            "referencias": regra.get("referencias", []),
            "linguagem": linguagem,
        })
    return sugestoes
