"""Utilitário legado preservado por compatibilidade.

As regras clínicas ativas do pré-natal estão em:
    modulos/regras_clinicas/prenatal/

Este módulo não altera mais o banco automaticamente ao ser importado.
"""

from modulos.banco_prenatal import BANCO_PRENATAL


def resumo() -> dict[str, int]:
    """Retorna a quantidade de regras por categoria."""
    contagem: dict[str, int] = {}
    for regra in BANCO_PRENATAL:
        categoria = regra.get("categoria", "Sem categoria")
        contagem[categoria] = contagem.get(categoria, 0) + 1
    return contagem


if __name__ == "__main__":
    print("Regras clínicas ativas do pré-natal:", len(BANCO_PRENATAL))
    for categoria, quantidade in sorted(resumo().items()):
        print(f"- {categoria}: {quantidade}")
