from modulos.pdf import gerar_pdf_processo_enfermagem
import streamlit as st

from modulos.estado import obter_achados_clinicos, obter_resumo_transcultural
from modulos.regras import gerar_planejamento_transcultural
from modulos.inferencia import executar_inferencia


def formatar_lista(itens):
    if not itens:
        return "Não informado."

    texto = ""
    for item in itens:
        if isinstance(item, dict):
            codigo = item.get("codigo", "")
            nome = item.get("termo") or item.get("nome", "")
            if codigo and nome:
                texto += f"- {codigo} — {nome}\n"
            elif nome:
                texto += f"- {nome}\n"
            else:
                texto += f"- {item}\n"
        else:
            texto += f"- {item}\n"
    return texto


def tela_processo_enfermagem():
    st.header("📋 Processo de Enfermagem")
    st.caption("Estrutura conforme Resolução COFEN nº 736/2024")
    st.progress(100)

    dados = st.session_state.get("dados", {})
    achados = obter_achados_clinicos()
    bloco_b = dados.get("avaliacao_transcultural", {})

    sugestoes = (
        dados.get("sugestoes_selecionadas")
        or dados.get("sugestoes")
        or executar_inferencia(achados, bloco_b, dados.get("linguagem", "CIPE®"))
    )
    planejamento = dados.get("planejamento_transcultural") or gerar_planejamento_transcultural(bloco_b, sugestoes)
    linguagem = dados.get("linguagem", "Comparativo")

    historico = f"""
Paciente: {dados.get('nome', 'Não informado')}
Idade: {dados.get('idade', 'Não informada')} anos
Faixa etária: {dados.get('faixa', 'Não informada')}
Sexo atribuído ao nascimento: {dados.get('sexo', 'Não informado')}
Identidade de gênero: {dados.get('genero', 'Não informada')}
Data do Processo de Enfermagem: {dados.get('data_pe', 'Não informada')}
Hora: {dados.get('hora_pe', 'Não informada')}
Contexto de atuação: {dados.get('contexto', 'Não informado')}
Linha de cuidado: {dados.get('linha', 'Não informada')}
Tipo de consulta: {dados.get('tipo_consulta', 'Não informado')}
Teoria de Enfermagem: {dados.get('teoria', 'Não informada')}
Linguagem padronizada: {dados.get('linguagem', 'Não informada')}

Achados clínicos identificados:
{achados}

Avaliação transcultural:
{obter_resumo_transcultural()}
"""

    diagnosticos_txt = ""
    resultados_txt = ""
    intervencoes_txt = ""

    with st.expander("1. Avaliação de Enfermagem", expanded=True):
        st.text_area("Avaliação de Enfermagem", value=historico, height=240)

    with st.expander("2. Diagnóstico de Enfermagem", expanded=True):
        if sugestoes:
            for s in sugestoes:
                titulo = s.get("titulo", "Sem título")
                st.markdown(f"**{titulo}**")
                diagnosticos_txt += f"\nREGRA: {titulo}\n"

                if linguagem == "CIPE®":
                    itens = s.get("cipe_diag", [])
                elif linguagem == "NANDA-I / NOC / NIC":
                    itens = s.get("nanda", [])
                else:
                    itens = s.get("cipe_diag", []) + s.get("nanda", [])

                for item in itens:
                    st.write(f"• {formatar_lista([item]).strip().lstrip('- ')}")
                diagnosticos_txt += formatar_lista(itens)
        else:
            st.info("Nenhum diagnóstico sugerido.")
            diagnosticos_txt = "Nenhum diagnóstico sugerido."

    with st.expander("3. Planejamento de Enfermagem", expanded=True):
        st.subheader("I – Priorização dos Diagnósticos de Enfermagem")
        priorizacao = st.text_area(
            "Descreva a priorização dos diagnósticos conforme julgamento clínico",
            height=100
        )

        st.subheader("II – Resultados Esperados")
        if sugestoes:
            for s in sugestoes:
                titulo = s.get("titulo", "Sem título")
                resultados_txt += f"\nREGRA: {titulo}\n"

                if linguagem == "CIPE®":
                    itens = s.get("cipe_res", [])
                elif linguagem == "NANDA-I / NOC / NIC":
                    itens = s.get("noc", [])
                else:
                    itens = s.get("cipe_res", []) + s.get("noc", [])

                for item in itens:
                    st.write(f"• {formatar_lista([item]).strip().lstrip('- ')}")
                resultados_txt += formatar_lista(itens)
        else:
            resultados_txt = "Nenhum resultado sugerido."

        st.subheader("III – Prescrição / Intervenções de Enfermagem")
        if sugestoes:
            for s in sugestoes:
                titulo = s.get("titulo", "Sem título")
                intervencoes_txt += f"\nREGRA: {titulo}\n"

                if linguagem == "CIPE®":
                    itens = s.get("cipe_int", [])
                elif linguagem == "NANDA-I / NOC / NIC":
                    itens = s.get("nic", [])
                else:
                    itens = s.get("cipe_int", []) + s.get("nic", [])

                for item in itens:
                    st.write(f"• {formatar_lista([item]).strip().lstrip('- ')}")
                intervencoes_txt += formatar_lista(itens)
        else:
            intervencoes_txt = "Nenhuma intervenção sugerida."

    with st.expander("4. Planejamento Transcultural", expanded=True):
        st.markdown("**Preservação / Manutenção do cuidado cultural**")
        for item in planejamento.get("preservacao", []):
            st.write(f"• {formatar_lista([item]).strip().lstrip('- ')}")

        st.markdown("**Acomodação / Negociação do cuidado cultural**")
        for item in planejamento.get("negociacao", []):
            st.write(f"• {formatar_lista([item]).strip().lstrip('- ')}")

        st.markdown("**Repadronização / Reestruturação do cuidado cultural**")
        for item in planejamento.get("reestruturacao", []):
            st.write(f"• {formatar_lista([item]).strip().lstrip('- ')}")

    with st.expander("5. Implementação de Enfermagem", expanded=True):
        implementacao = st.text_area(
            "Registro das ações executadas, orientações realizadas e encaminhamentos",
            height=120
        )

    with st.expander("6. Evolução de Enfermagem", expanded=True):
        evolucao = st.text_area(
            "Resposta da pessoa ao cuidado, reavaliação dos resultados e revisão do plano",
            height=120
        )

    texto_final = f"""
SAPE IA 2.0
PROCESSO DE ENFERMAGEM
Conforme Resolução COFEN nº 736/2024

1. AVALIAÇÃO DE ENFERMAGEM

{historico}

2. DIAGNÓSTICO DE ENFERMAGEM

{diagnosticos_txt}

3. PLANEJAMENTO DE ENFERMAGEM

I – Priorização dos Diagnósticos de Enfermagem

{priorizacao}

II – Resultados Esperados

{resultados_txt}

III – Prescrição / Intervenções de Enfermagem

{intervencoes_txt}

4. PLANEJAMENTO TRANSCULTURAL
Teoria de Madeleine Leininger

Preservação / Manutenção:
{formatar_lista(planejamento.get("preservacao", []))}

Acomodação / Negociação:
{formatar_lista(planejamento.get("negociacao", []))}

Repadronização / Reestruturação:
{formatar_lista(planejamento.get("reestruturacao", []))}

5. IMPLEMENTAÇÃO DE ENFERMAGEM

{implementacao}

6. EVOLUÇÃO DE ENFERMAGEM

{evolucao}


Responsável pelo Processo de Enfermagem

Enfermeiro(a): ______________________________________

COREN: ____________________________________________

Data: ____/____/______

Assinatura: ________________________________________
"""

    pdf_buffer = gerar_pdf_processo_enfermagem(texto_final)

    st.download_button(
        "📄 Baixar Processo de Enfermagem em PDF",
        data=pdf_buffer,
        file_name="processo_enfermagem_sape_ia.pdf",
        mime="application/pdf"
    )