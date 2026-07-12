import streamlit as st


def tela_avaliacao_clinica():
    st.header("🩺 Avaliação Clínica de Enfermagem")
    st.caption("Coleta de dados clínicos relevantes para a consulta de pré-natal.")

    st.progress(40)

    with st.expander("1. Alterações obstétricas", expanded=True):
        obstetricas = st.multiselect(
            "Selecione as alterações obstétricas",
            [
                "Bradicardia fetal",
                "Taquicardia fetal",
                "Arritmia fetal",
                "Ausência de batimentos cardíacos fetais",
                "Movimentos fetais diminuídos",
                "Ausência de movimentos fetais",
                "Altura uterina incompatível com a idade gestacional",
                "Sangramento vaginal",
                "Perda de líquido amniótico",
                "Oligodrâmnio",
                "Polidrâmnio",
                "Placenta prévia",
                "Suspeita de descolamento prematuro de placenta",
                "Apresentação fetal anômala",
                "Trabalho de parto prematuro",
                "Edema importante",
                "Proteinúria",
                "Contrações uterinas"
            ],
            placeholder="Selecione uma ou mais opções"
        )

    with st.expander("2. Alterações dos sinais vitais", expanded=False):
        sinais_vitais = st.multiselect(
            "Selecione as alterações dos sinais vitais",
            [
                "Hipertensão arterial",
                "Hipotensão arterial",
                "Taquicardia",
                "Bradicardia",
                "Hipertermia",
                "Hipotermia",
                "Taquipneia",
                "Bradipneia",
                "Saturação de oxigênio reduzida"
            ],
            placeholder="Selecione uma ou mais opções"
        )

    with st.expander("3. Alterações no exame físico", expanded=False):
        exame_fisico = st.multiselect(
            "Selecione os achados do exame físico",
            [
                "Corrimento vaginal",
                "Prurido vaginal",
                "Hiperemia vaginal",
                "Dor pélvica",
                "Dor lombar",
                "Disúria",
                "Polaciúria",
                "Hematúria",
                "Cefaleia persistente",
                "Escotomas",
                "Dor epigástrica",
                "Náuseas",
                "Vômitos",
                "Palidez cutaneomucosa",
                "Icterícia",
                "Cianose"
            ],
            placeholder="Selecione uma ou mais opções"
        )

    with st.expander("4. Alterações laboratoriais", expanded=False):
        laboratoriais = st.multiselect(
            "Selecione os achados laboratoriais",
            [
                "Anemia",
                "Glicemia alterada",
                "Proteinúria",
                "Infecção urinária",
                "Sífilis",
                "HIV",
                "Hepatite B",
                "Hepatite C",
                "Toxoplasmose"
            ],
            placeholder="Selecione uma ou mais opções"
        )

    with st.expander("5. Fatores de risco clínico-obstétricos", expanded=False):
        fatores_risco = st.multiselect(
            "Selecione os fatores de risco identificados",
            [
                "Tabagismo",
                "Uso de álcool",
                "Uso de outras substâncias psicoativas",
                "Antecedente de parto prematuro",
                "Antecedente de aborto recorrente",
                "Intervalo intergestacional curto",
                "Idade materna menor que 15 anos",
                "Idade materna maior ou igual a 35 anos"
            ],
            placeholder="Selecione uma ou mais opções"
        )

    observacoes = st.text_area(
        "Observações clínicas do enfermeiro",
        placeholder="Registre informações complementares da avaliação clínica..."
    )

    if st.button(
        "💾 Salvar avaliação clínica",
        use_container_width=True
    ):
        st.session_state.dados["avaliacao_clinica"] = {
            "obstetricas": obstetricas,
            "sinais_vitais": sinais_vitais,
            "exame_fisico": exame_fisico,
            "laboratoriais": laboratoriais,
            "fatores_risco": fatores_risco,
            "observacoes": observacoes
        }

        st.success("✅ Avaliação clínica salva com sucesso.")