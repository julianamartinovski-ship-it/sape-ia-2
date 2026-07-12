import re
import sqlite3
from pathlib import Path

import requests
from pypdf import PdfReader


URL_CIPE = "https://www.icn.ch/sites/default/files/inline-files/ICNP%202019%20Portugu%C3%AAs%20do%20Brasil.pdf"

BASE_DIR = Path(__file__).resolve().parent.parent
PASTA_DADOS = BASE_DIR / "banco_dados"
PASTA_DADOS.mkdir(exist_ok=True)

PDF_PATH = PASTA_DADOS / "cipe_2019_ptbr.pdf"
DB_PATH = PASTA_DADOS / "cipe.db"


def baixar_pdf():
    if PDF_PATH.exists():
        return
    resposta = requests.get(URL_CIPE, timeout=60)
    resposta.raise_for_status()
    PDF_PATH.write_bytes(resposta.content)


def definir_tipo(eixo):
    if eixo == "DC":
        return "Diagnóstico/Resultado CIPE"
    if eixo == "IC":
        return "Intervenção CIPE"
    return "Conceito CIPE"


def extrair_linhas():
    reader = PdfReader(str(PDF_PATH))
    linhas = []

    for page in reader.pages:
        texto = page.extract_text() or ""
        for linha in texto.splitlines():
            linha = linha.strip()
            if linha:
                linhas.append(linha)

    return linhas


def montar_registros(linhas):
    registros = []
    atual = None
    padrao = re.compile(r"^(100\d{5})\s+([A-Z]{1,3})\s+(.+)$")

    for linha in linhas:
        if "código eixo termo definição" in linha.lower():
            continue
        if linha.startswith("CIPE"):
            continue

        achou = padrao.match(linha)

        if achou:
            if atual:
                registros.append(atual)

            eixo = achou.group(2)
            atual = {
                "codigo": achou.group(1),
                "eixo": eixo,
                "termo": achou.group(3).strip(),
                "definicao": "",
                "tipo": definir_tipo(eixo),
                "taxonomia": "CIPE/ICNP",
                "versao": "2019 Português do Brasil",
                "status": "validado",
                "referencia": "ICN. CIPE - Português do Brasil, 2019."
            }
        else:
            if atual:
                atual["definicao"] += " " + linha

    if atual:
        registros.append(atual)

    return registros


def criar_banco(registros):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS cipe")
    cur.execute("DROP TABLE IF EXISTS cipe_diagnosticos")
    cur.execute("DROP TABLE IF EXISTS cipe_resultados")
    cur.execute("DROP TABLE IF EXISTS cipe_intervencoes")
    cur.execute("DROP TABLE IF EXISTS regras_clinicas_cipe")

    cur.execute("""
        CREATE TABLE cipe (
            codigo TEXT PRIMARY KEY,
            eixo TEXT,
            termo TEXT,
            definicao TEXT,
            tipo TEXT,
            taxonomia TEXT,
            versao TEXT,
            status TEXT,
            referencia TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE cipe_diagnosticos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT,
            termo TEXT,
            eixo TEXT,
            linha_cuidado TEXT,
            referencia TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE cipe_resultados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT,
            termo TEXT,
            eixo TEXT,
            linha_cuidado TEXT,
            referencia TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE cipe_intervencoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT,
            termo TEXT,
            eixo TEXT,
            linha_cuidado TEXT,
            referencia TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE regras_clinicas_cipe (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            linha_cuidado TEXT,
            achado_clinico TEXT,
            codigo_diagnostico TEXT,
            codigo_resultado TEXT,
            codigo_intervencao TEXT,
            prioridade TEXT,
            justificativa TEXT
        )
    """)

    cur.executemany("""
        INSERT OR REPLACE INTO cipe
        (codigo, eixo, termo, definicao, tipo, taxonomia, versao, status, referencia)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [
        (
            r["codigo"],
            r["eixo"],
            r["termo"],
            r["definicao"].strip(),
            r["tipo"],
            r["taxonomia"],
            r["versao"],
            r["status"],
            r["referencia"]
        )
        for r in registros
    ])

    diagnosticos = [r for r in registros if r["eixo"] == "DC"]
    intervencoes = [r for r in registros if r["eixo"] == "IC"]

    cur.executemany("""
        INSERT INTO cipe_diagnosticos
        (codigo, termo, eixo, linha_cuidado, referencia)
        VALUES (?, ?, ?, ?, ?)
    """, [
        (r["codigo"], r["termo"], r["eixo"], "APS", r["referencia"])
        for r in diagnosticos
    ])

    cur.executemany("""
        INSERT INTO cipe_resultados
        (codigo, termo, eixo, linha_cuidado, referencia)
        VALUES (?, ?, ?, ?, ?)
    """, [
        (r["codigo"], r["termo"], r["eixo"], "APS", r["referencia"])
        for r in diagnosticos
    ])

    cur.executemany("""
        INSERT INTO cipe_intervencoes
        (codigo, termo, eixo, linha_cuidado, referencia)
        VALUES (?, ?, ?, ?, ?)
    """, [
        (r["codigo"], r["termo"], r["eixo"], "APS", r["referencia"])
        for r in intervencoes
    ])

    regras_prenatal = [
        (
            "Pré-natal",
            "Hipertensão arterial",
            "Pressão arterial alterada",
            "Pressão arterial controlada",
            "Monitorar pressão arterial",
            "Alta",
            "Gestante com pressão arterial elevada requer avaliação de risco gestacional."
        ),
        (
            "Pré-natal",
            "Proteinúria",
            "Risco de condição hipertensiva na gestação",
            "Risco reduzido",
            "Avaliar sinais de gravidade",
            "Alta",
            "Proteinúria associada à hipertensão pode indicar risco de pré-eclâmpsia."
        ),
        (
            "Pré-natal",
            "Cefaleia persistente",
            "Risco de condição hipertensiva na gestação",
            "Estado neurológico preservado",
            "Encaminhar conforme protocolo de risco gestacional",
            "Alta",
            "Cefaleia persistente em gestante exige avaliação clínica imediata."
        ),
        (
            "Pré-natal",
            "Corrimento vaginal",
            "Corrimento vaginal",
            "Conforto melhorado",
            "Avaliar características do corrimento vaginal",
            "Média",
            "Corrimento vaginal deve ser avaliado conforme sinais associados e protocolo de IST/vulvovaginites."
        ),
        (
            "Pré-natal",
            "Prurido vaginal",
            "Prurido genital",
            "Conforto melhorado",
            "Orientar higiene íntima",
            "Média",
            "Prurido associado a corrimento pode indicar vulvovaginite."
        ),
        (
            "Pré-natal",
            "Área descoberta pela ESF",
            "Acesso ao serviço de saúde prejudicado",
            "Acesso ao cuidado melhorado",
            "Organizar seguimento do pré-natal",
            "Alta",
            "Dificuldade de acesso exige planejamento do cuidado e seguimento longitudinal."
        ),
    ]

    cur.executemany("""
        INSERT INTO regras_clinicas_cipe
        (linha_cuidado, achado_clinico, codigo_diagnostico, codigo_resultado, codigo_intervencao, prioridade, justificativa)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, regras_prenatal)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    baixar_pdf()
    linhas = extrair_linhas()
    registros = montar_registros(linhas)
    criar_banco(registros)

    print("Banco CIPE criado com sucesso!")
    print(f"Arquivo: {DB_PATH}")
    print(f"Total de registros importados: {len(registros)}")