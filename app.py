import streamlit as st
from paginas.identificacao import tela_identificacao
from paginas.avaliacao_clinica import tela_avaliacao_clinica
from paginas.avaliacao_transcultural import tela_avaliacao_transcultural
from paginas.apoio_decisao import tela_apoio_decisao
from paginas.processo_enfermagem import tela_processo_enfermagem
from modulos.estado import iniciar_estado

st.set_page_config(page_title="SAPE IA 2.0", page_icon="🏥", layout="wide")
iniciar_estado()

MENU = [
    "🏥 Identificação da Pessoa e da Consulta",
    "🩺 Avaliação Clínica de Enfermagem",
    "🌿 Avaliação Transcultural",
    "🧠 Apoio à Decisão Clínica de Enfermagem",
    "📋 Processo de Enfermagem",
]

st.sidebar.title("🏥 SAPE IA 2.0")
st.sidebar.caption("Sistema de Apoio ao Processo de Enfermagem")
pagina = st.sidebar.radio("Menu", MENU)

st.title("🏥 SAPE IA 2.0")
st.caption("Sistema de Apoio ao Processo de Enfermagem")

if pagina == MENU[0]:
    tela_identificacao()
elif pagina == MENU[1]:
    tela_avaliacao_clinica()
elif pagina == MENU[2]:
    tela_avaliacao_transcultural()
elif pagina == MENU[3]:
    tela_apoio_decisao()
elif pagina == MENU[4]:
    tela_processo_enfermagem()
