from __future__ import annotations

import csv
import difflib
import re
import sqlite3
import unicodedata
from pathlib import Path
from typing import Any

from modulos.banco_prenatal import BANCO_PRENATAL


BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "banco_dados" / "cipe.db"

CSV_PATH = BASE_DIR / "auditoria_45_regras_cipe.csv"
TXT_PATH = BASE_DIR / "auditoria_45_regras_cipe.txt"


TABELAS = {
    "diagnostico": "cipe_diagnosticos",
    "resultado": "cipe_resultados",
    "intervencao": "cipe_intervencoes",
}


def normalizar(texto: Any) -> str:
    texto = str(texto or "").strip().casefold()
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(
        caractere
        for caractere in texto
        if not unicodedata.combining(caractere)
    )
    texto = re.sub(r"[^\w\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto


def tokens(texto: Any) -> set[str]:
    palavras = normalizar(texto).split()

    palavras_ignoradas = {
        "de", "da", "do", "das", "dos",
        "a", "ao", "aos", "e", "em",
        "com", "para", "por", "na", "no",
        "nas", "nos", "contra", "relacionado",
        "relacionada",
    }

    return {
        palavra
        for palavra in palavras
        if len(palavra) >= 3 and palavra not in palavras_ignoradas
    }


def calcular_pontuacao(termo_regra: str, termo_cipe: str) -> float:
    regra_normalizada = normalizar(termo_regra)
    cipe_normalizada = normalizar(termo_cipe)

    similaridade = difflib.SequenceMatcher(
        None,
        regra_normalizada,
        cipe_normalizada,
    ).ratio()

    tokens_regra = tokens(termo_regra)
    tokens_cipe = tokens(termo_cipe)

    if tokens_regra or tokens_cipe:
        intersecao = len(tokens_regra & tokens_cipe)
        uniao = len(tokens_regra | tokens_cipe)
        sobreposicao = intersecao / uniao if uniao else 0
    else:
        sobreposicao = 0

    bonus_contem = 0
    if regra_normalizada in cipe_normalizada:
        bonus_contem = 0.10
    elif cipe_normalizada in regra_normalizada:
        bonus_contem = 0.08

    pontuacao = (
        similaridade * 0.65
        + sobreposicao * 0.35
        + bonus_contem
    )

    return min(pontuacao, 1.0)


def carregar_termos_cipe(
    conexao: sqlite3.Connection,
    tabela: str,
) -> list[tuple[str, str]]:
    consulta = f"""
        SELECT codigo, termo
        FROM {tabela}
        WHERE codigo IS NOT NULL
          AND termo IS NOT NULL
          AND TRIM(termo) <> ''
        ORDER BY termo
    """

    return conexao.execute(consulta).fetchall()


def obter_candidatos(
    termo_atual: str,
    termos_cipe: list[tuple[str, str]],
    limite: int = 5,
) -> list[dict]:
    candidatos = []

    for codigo, termo_cipe in termos_cipe:
        pontuacao = calcular_pontuacao(
            termo_atual,
            termo_cipe,
        )

        candidatos.append(
            {
                "codigo": codigo,
                "termo": termo_cipe,
                "pontuacao": pontuacao,
            }
        )

    candidatos.sort(
        key=lambda item: item["pontuacao"],
        reverse=True,
    )

    return candidatos[:limite]


def extrair_item(regra: dict, tipo: str) -> dict:
    item = regra.get(tipo)

    if isinstance(item, dict):
        return item

    bloco_cipe = regra.get("cipe", {})

    if isinstance(bloco_cipe, dict):
        singular = bloco_cipe.get(tipo)

        if isinstance(singular, dict):
            return singular

        plural = bloco_cipe.get(f"{tipo}s")

        if isinstance(plural, list) and plural:
            primeiro = plural[0]
            if isinstance(primeiro, dict):
                return primeiro

    return {}


def regra_sem_codigo_diagnostico(regra: dict) -> bool:
    diagnostico = extrair_item(regra, "diagnostico")

    return bool(
        diagnostico.get("termo")
        and not diagnostico.get("codigo")
    )


def main() -> None:
    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"Banco CIPE não encontrado em: {DB_PATH}"
        )

    regras_sem_codigo = [
        regra
        for regra in BANCO_PRENATAL
        if isinstance(regra, dict)
        and regra_sem_codigo_diagnostico(regra)
    ]

    with sqlite3.connect(DB_PATH) as conexao:
        bases_cipe = {
            tipo: carregar_termos_cipe(
                conexao,
                tabela,
            )
            for tipo, tabela in TABELAS.items()
        }

    linhas_csv = []
    linhas_txt = []

    linhas_txt.append(
        f"TOTAL DE REGRAS SEM CÓDIGO NO DIAGNÓSTICO: "
        f"{len(regras_sem_codigo)}"
    )
    linhas_txt.append("=" * 100)

    for indice, regra in enumerate(
        regras_sem_codigo,
        start=1,
    ):
        titulo = (
            regra.get("titulo")
            or regra.get("regra")
            or regra.get("achado_clinico")
            or f"Regra {indice}"
        )

        linhas_txt.append("")
        linhas_txt.append(
            f"{indice:02d} | REGRA: {titulo}"
        )

        for tipo in (
            "diagnostico",
            "resultado",
            "intervencao",
        ):
            item = extrair_item(regra, tipo)
            termo_atual = str(
                item.get("termo") or ""
            ).strip()

            linhas_txt.append(
                f"  {tipo.upper()}: {termo_atual}"
            )

            if not termo_atual:
                linhas_txt.append(
                    "    Nenhum termo encontrado."
                )
                continue

            candidatos = obter_candidatos(
                termo_atual,
                bases_cipe[tipo],
                limite=5,
            )

            for posicao, candidato in enumerate(
                candidatos,
                start=1,
            ):
                percentual = (
                    candidato["pontuacao"] * 100
                )

                linhas_txt.append(
                    f"    {posicao}. "
                    f"{percentual:.1f}% | "
                    f"{candidato['codigo']} | "
                    f"{candidato['termo']}"
                )

                linhas_csv.append(
                    {
                        "numero_regra": indice,
                        "regra": titulo,
                        "tipo": tipo,
                        "termo_atual": termo_atual,
                        "posicao_candidato": posicao,
                        "pontuacao_percentual": (
                            f"{percentual:.1f}"
                        ),
                        "codigo_candidato": (
                            candidato["codigo"]
                        ),
                        "termo_candidato": (
                            candidato["termo"]
                        ),
                        "decisao_revisao": "",
                        "observacao": "",
                    }
                )

    with CSV_PATH.open(
        "w",
        encoding="utf-8-sig",
        newline="",
    ) as arquivo_csv:
        campos = [
            "numero_regra",
            "regra",
            "tipo",
            "termo_atual",
            "posicao_candidato",
            "pontuacao_percentual",
            "codigo_candidato",
            "termo_candidato",
            "decisao_revisao",
            "observacao",
        ]

        escritor = csv.DictWriter(
            arquivo_csv,
            fieldnames=campos,
            delimiter=";",
        )

        escritor.writeheader()
        escritor.writerows(linhas_csv)

    TXT_PATH.write_text(
        "\n".join(linhas_txt),
        encoding="utf-8",
    )

    print("AUDITORIA CONCLUÍDA")
    print(
        "Regras analisadas:",
        len(regras_sem_codigo),
    )
    print("Arquivo CSV:", CSV_PATH)
    print("Arquivo TXT:", TXT_PATH)
    print("")
    print(
        "Nenhum código foi inserido e nenhum arquivo "
        "do SAPE foi alterado."
    )


if __name__ == "__main__":
    main()