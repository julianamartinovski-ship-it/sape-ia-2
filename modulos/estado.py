import streamlit as st
from datetime import date


def iniciar_estado():
    if "dados" not in st.session_state:
        st.session_state.dados = {"sugestoes": []}


def calcular_idade(data_nascimento):
    if data_nascimento is None:
        return 0
    hoje = date.today()
    return hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))


def classificar_faixa_etaria(idade):
    if idade < 1: return "Lactente"
    if idade < 10: return "Criança"
    if idade <= 19: return "Adolescente"
    if idade <= 59: return "Adulto"
    return "Pessoa idosa"


def obter_achados_clinicos():
    bloco = st.session_state.dados.get("avaliacao_clinica", {})
    achados = []
    for chave in ["obstetricas", "sinais_vitais", "exame_fisico", "laboratoriais", "fatores_risco", "vulnerabilidades"]:
        valor = bloco.get(chave, [])
        if isinstance(valor, list):
            achados.extend(valor)
    return list(dict.fromkeys(achados))


def obter_resumo_transcultural():
    bloco = st.session_state.dados.get("avaliacao_transcultural", {})
    resumo = []
    for itens in bloco.values():
        if isinstance(itens, list):
            resumo.extend(itens)
    return list(dict.fromkeys(resumo))
