from pathlib import Path
import ast
import re
import pprint

BASE = Path(__file__).resolve().parent
ARQUIVO_RECUPERADO = BASE / "regras_recuperadas_limpa.py"

PASTA_PRENATAL = BASE / "modulos" / "regras_clinicas" / "prenatal"
PASTA_PRENATAL.mkdir(parents=True, exist_ok=True)

MAPA_CATEGORIAS = {
    "Captação e vínculo": "captacao_vinculo.py",
    "Fatores de risco": "fatores_risco.py",
    "Exames laboratoriais": "exames_laboratoriais.py",
    "Vacinação": "vacinacao.py",
    "Sinais e sintomas": "sinais_sintomas.py",
    "Intercorrências obstétricas": "intercorrencias.py",
    "Medicações e suplementação": "medicacoes.py",
    "Exames de imagem": "exames_imagem.py",
}

def extrair_blocos_dict(texto):
    blocos = []
    inicio = None
    nivel = 0
    dentro_string = False
    string_char = ""
    escape = False

    for i, ch in enumerate(texto):
        if dentro_string:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == string_char:
                dentro_string = False
            continue

        if ch in ("'", '"'):
            dentro_string = True
            string_char = ch
            continue

        if ch == "{":
            if nivel == 0:
                inicio = i
            nivel += 1

        elif ch == "}":
            nivel -= 1
            if nivel == 0 and inicio is not None:
                blocos.append(texto[inicio:i+1])
                inicio = None

    return blocos

def carregar_regras():
    texto = ARQUIVO_RECUPERADO.read_text(encoding="utf-8", errors="ignore")
    blocos = extrair_blocos_dict(texto)

    regras = []
    for bloco in blocos:
        if '"categoria"' not in bloco and "'categoria'" not in bloco:
            continue
        try:
            regra = ast.literal_eval(bloco)
            if isinstance(regra, dict) and "categoria" in regra:
                regras.append(regra)
        except Exception:
            continue

    return regras

def salvar_modulo(nome_arquivo, regras):
    caminho = PASTA_PRENATAL / nome_arquivo
    conteudo = (
        "# Arquivo reconstruído automaticamente para o SAPE IA 2.0\n"
        "# Linha de cuidado: Pré-natal\n\n"
        "REGRAS = "
        + pprint.pformat(regras, width=120, sort_dicts=False)
        + "\n"
    )
    caminho.write_text(conteudo, encoding="utf-8")

def main():
    if not ARQUIVO_RECUPERADO.exists():
        raise FileNotFoundError("Arquivo regras_recuperadas_limpa.py não encontrado.")

    regras = carregar_regras()

    if not regras:
        raise RuntimeError("Nenhuma regra foi encontrada no arquivo recuperado.")

    por_categoria = {}
    for regra in regras:
        categoria = regra.get("categoria", "Sem categoria")
        por_categoria.setdefault(categoria, []).append(regra)

    for categoria, nome_arquivo in MAPA_CATEGORIAS.items():
        salvar_modulo(nome_arquivo, por_categoria.get(categoria, []))

    init_prenatal = PASTA_PRENATAL / "__init__.py"
    init_prenatal.write_text(
        """from .captacao_vinculo import REGRAS as CAPTACAO_VINCULO
from .fatores_risco import REGRAS as FATORES_RISCO
from .exames_laboratoriais import REGRAS as EXAMES_LABORATORIAIS
from .vacinacao import REGRAS as VACINACAO
from .sinais_sintomas import REGRAS as SINAIS_SINTOMAS
from .intercorrencias import REGRAS as INTERCORRENCIAS
from .medicacoes import REGRAS as MEDICACOES
from .exames_imagem import REGRAS as EXAMES_IMAGEM

REGRAS = (
    CAPTACAO_VINCULO
    + FATORES_RISCO
    + EXAMES_LABORATORIAIS
    + VACINACAO
    + SINAIS_SINTOMAS
    + INTERCORRENCIAS
    + MEDICACOES
    + EXAMES_IMAGEM
)
""",
        encoding="utf-8"
    )

    init_regras = BASE / "modulos" / "regras_clinicas" / "__init__.py"
    init_regras.write_text(
        "from .prenatal import REGRAS as REGRAS_PRENATAL\n",
        encoding="utf-8"
    )

    banco_prenatal = BASE / "modulos" / "banco_prenatal.py"
    banco_prenatal.write_text(
        "from modulos.regras_clinicas.prenatal import REGRAS\n\nBANCO_PRENATAL = REGRAS\n",
        encoding="utf-8"
    )

    print("Reconstrução concluída.")
    print(f"Total de regras recuperadas: {len(regras)}")
    for categoria in sorted(por_categoria):
        print(f"{categoria}: {len(por_categoria[categoria])}")

if __name__ == "__main__":
    main()