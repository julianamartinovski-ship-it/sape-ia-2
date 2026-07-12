import streamlit as st
from datetime import date, datetime
from modulos.estado import calcular_idade, classificar_faixa_etaria

def tela_identificacao():
    st.header("🏥 Identificação da Pessoa e da Consulta")
    st.progress(20)
    with st.container(border=True):
        st.subheader("Dados da pessoa")
        col1, col2 = st.columns(2)
        with col1:
            nome = st.text_input("Nome")
            data_nascimento = st.date_input("Data de nascimento", value=date(1990, 1, 1))
            idade = calcular_idade(data_nascimento)
            faixa = classificar_faixa_etaria(idade)
            st.text_input("Idade calculada", value=f"{idade} anos", disabled=True)
            st.text_input("Faixa etária", value=faixa, disabled=True)
        with col2:
            sexo = st.selectbox("Sexo atribuído ao nascimento", ["Feminino", "Masculino", "Intersexo", "Prefere não informar"])
            genero = st.selectbox("Identidade de gênero", ["Mulher cisgênero", "Homem cisgênero", "Mulher trans", "Homem trans", "Pessoa não binária", "Outra identidade", "Prefere não informar"])
            data_pe = st.date_input("Data do Processo de Enfermagem", value=date.today())
            hora_pe = st.text_input("Hora do Processo de Enfermagem", value=datetime.now().strftime("%H:%M"), disabled=True)
    with st.container(border=True):
        st.subheader("Configuração da consulta")
        col3, col4, col5 = st.columns(3)
        with col3:
            contexto = st.selectbox("Contexto de atuação", ["Atenção Primária à Saúde", "Ambulatório", "Hospital"])
        with col4:
            linha = st.selectbox("Linha de cuidado", ["Saúde da Mulher", "Saúde da Criança", "Pessoa Idosa", "DCNT", "Saúde Mental", "Cuidados Paliativos"])
        with col5:
            tipo_consulta = st.selectbox("Tipo de consulta", ["Pré-natal", "Puerpério", "Planejamento sexual e reprodutivo", "Climatério", "Rastreamento do câncer do colo do útero", "Rastreamento do câncer de mama"])
        col6, col7 = st.columns(2)
        with col6:
            teoria = st.selectbox("Teoria de Enfermagem", ["Leininger", "Orem", "Roy", "Watson", "Peplau", "King"])
        with col7:
            linguagem = st.selectbox("Linguagem padronizada", ["CIPE®", "NANDA-I / NOC / NIC", "Comparativo"])
    if st.button("Salvar identificação"):
        st.session_state.dados.update({"nome": nome, "data_nascimento": data_nascimento, "idade": idade, "faixa": faixa, "sexo": sexo, "genero": genero, "data_pe": data_pe, "hora_pe": hora_pe, "contexto": contexto, "linha": linha, "tipo_consulta": tipo_consulta, "teoria": teoria, "linguagem": linguagem})
        st.success("Identificação salva.")
