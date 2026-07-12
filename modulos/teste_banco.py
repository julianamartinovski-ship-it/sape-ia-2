import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "banco_dados" / "cipe.db"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

tabelas = [
    "cipe",
    "cipe_diagnosticos",
    "cipe_resultados",
    "cipe_intervencoes",
    "regras_clinicas_cipe",
]

for tabela in tabelas:
    cur.execute(f"SELECT COUNT(*) FROM {tabela}")
    total = cur.fetchone()[0]
    print(f"{tabela}: {total}")

print("\nRegras cadastradas:\n")

cur.execute("""
SELECT
    linha_cuidado,
    achado_clinico,
    codigo_diagnostico,
    codigo_intervencao
FROM regras_clinicas_cipe
""")

for linha in cur.fetchall():
    print(linha)

conn.close()