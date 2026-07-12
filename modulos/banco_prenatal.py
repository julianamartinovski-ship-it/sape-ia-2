from __future__ import annotations

import sqlite3
from pathlib import Path

from modulos.regras_clinicas.prenatal import REGRAS

_DB_PATH = Path(__file__).resolve().parent.parent / "banco_dados" / "cipe.db"


def _indice_cipe() -> dict[str, str]:
    if not _DB_PATH.exists():
        return {}
    with sqlite3.connect(_DB_PATH) as conexao:
        return {codigo: termo for codigo, termo in conexao.execute("SELECT codigo, termo FROM cipe").fetchall()}


def _validar_item(item: object, indice: dict[str, str]) -> object:
    if not isinstance(item, dict):
        return item
    codigo = item.get("codigo")
    if not codigo:
        return item
    codigo = str(codigo).strip()
    termo_oficial = indice.get(codigo)
    if not termo_oficial:
        novo = dict(item)
        novo["codigo"] = None
        novo["alerta_validacao"] = f"Código CIPE não localizado no banco: {codigo}"
        return novo
    novo = dict(item)
    novo["codigo"] = codigo
    novo["termo"] = termo_oficial
    return novo


def carregar_banco_prenatal() -> list[dict]:
    indice = _indice_cipe()
    banco = []
    for regra in REGRAS:
        if not isinstance(regra, dict):
            continue
        nova = dict(regra)
        for campo in ("diagnostico", "resultado", "intervencao"):
            nova[campo] = _validar_item(nova.get(campo), indice)
        banco.append(nova)
    return banco


BANCO_PRENATAL = carregar_banco_prenatal()
