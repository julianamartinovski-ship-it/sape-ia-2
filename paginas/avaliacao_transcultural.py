import streamlit as st


def tela_avaliacao_transcultural():
    st.header("🌿 Avaliação Transcultural")
    st.caption(
        "Fundamentada na Teoria Transcultural de Madeleine Leininger (Modelo Sunrise)."
    )

    st.progress(60)

    with st.expander("1. Contexto ambiental e territorial", expanded=True):
        contexto_territorial = st.multiselect(
            "Selecione o contexto territorial",
            [
                "Urbano",
                "Rural",
                "Comunidade ribeirinha",
                "Ilha",
                "Várzea",
                "Terra firme",
                "Comunidade quilombola",
                "Comunidade indígena",
                "Comunidade tradicional",
                "Assentamento"
            ],
            placeholder="Selecione uma ou mais opções"
        )

    with st.expander("2. Organização comunitária e acesso aos serviços", expanded=False):
        acesso_servicos = st.multiselect(
            "Selecione características de acesso",
            [
                "UBS distante",
                "UBS Fluvial",
                "Acesso exclusivamente fluvial",
                "Transporte em rabeta",
                "Transporte em voadeira",
                "Embarcação comunitária",
                "Dependência do nível do rio",
                "Longo tempo de deslocamento",
                "Área descoberta pela ESF",
                "Dificuldade para retorno ao pré-natal"
            ],
            placeholder="Selecione uma ou mais opções"
        )

    with st.expander("3. Fatores tecnológicos", expanded=False):
        tecnologicos = st.multiselect(
            "Selecione os fatores tecnológicos",
            [
                "Sem sinal de celular",
                "Sinal de celular intermitente",
                "Sem acesso à internet",
                "Energia elétrica limitada",
                "Energia por gerador",
                "Energia solar",
                "Sem possibilidade de teleatendimento"
            ],
            placeholder="Selecione uma ou mais opções"
        )

    with st.expander("4. Fatores religiosos e filosóficos", expanded=False):
        religiosos = st.multiselect(
            "Selecione os fatores religiosos e filosóficos",
            [
                "Religião influencia o cuidado",
                "Crenças espirituais sobre a gestação",
                "Benzimento",
                "Oração como prática de cuidado",
                "Restrição religiosa a procedimentos",
                "Pajelança"
            ],
            placeholder="Selecione uma ou mais opções"
        )

    with st.expander("5. Fatores de parentesco e sociais", expanded=False):
        parentesco = st.multiselect(
            "Selecione os fatores de parentesco e sociais",
            [
                "Apoio do companheiro",
                "Apoio familiar",
                "Família extensa presente",
                "Rede social fragilizada",
                "Conflito familiar",
                "Situação de violência",
                "Gestante adolescente"
            ],
            placeholder="Selecione uma ou mais opções"
        )

    with st.expander("6. Valores culturais, crenças e modos de vida", expanded=False):
        valores_culturais = st.multiselect(
            "Selecione os valores culturais e modos de vida",
            [
                "Uso de chás tradicionais",
                "Uso de plantas medicinais",
                "Parteira tradicional",
                "Cuidados tradicionais na gestação",
                "Cuidados tradicionais no puerpério",
                "Restrições alimentares culturais",
                "Influência familiar nas decisões de saúde",
                "Automedicação",
                "Recusa de encaminhamento"
            ],
            placeholder="Selecione uma ou mais opções"
        )

    with st.expander("7. Fatores políticos e legais", expanded=False):
        politicos_legais = st.multiselect(
            "Selecione os fatores políticos e legais",
            [
                "Ausência de documentação",
                "Dificuldade de acesso a benefícios sociais",
                "Dificuldade de acesso a direitos sociais",
                "Vulnerabilidade social"
            ],
            placeholder="Selecione uma ou mais opções"
        )

    with st.expander("8. Fatores econômicos", expanded=False):
        economicos = st.multiselect(
            "Selecione os fatores econômicos",
            [
                "Baixa renda",
                "Insegurança alimentar",
                "Pesca artesanal",
                "Agricultura familiar",
                "Extrativismo",
                "Trabalho informal",
                "Renda sazonal",
                "Beneficiário de programa social"
            ],
            placeholder="Selecione uma ou mais opções"
        )

    with st.expander("9. Fatores educacionais", expanded=False):
        educacionais = st.multiselect(
            "Selecione os fatores educacionais",
            [
                "Baixa escolaridade",
                "Dificuldade de compreensão das orientações",
                "Alfabetização limitada em saúde",
                "Dificuldade de leitura"
            ],
            placeholder="Selecione uma ou mais opções"
        )

    with st.expander("10. Rede de apoio", expanded=False):
        rede_apoio = st.multiselect(
            "Selecione a rede de apoio identificada",
            [
                "Companheiro",
                "Família",
                "Família extensa",
                "Parteira tradicional",
                "Agente Comunitário de Saúde",
                "Liderança comunitária",
                "Líder religioso",
                "Vizinhos/comunidade",
                "Sem rede de apoio"
            ],
            placeholder="Selecione uma ou mais opções"
        )

    if st.button(
        "💾 Salvar avaliação transcultural",
        use_container_width=True
    ):
        st.session_state.dados["avaliacao_transcultural"] = {
            "contexto_territorial": contexto_territorial,
            "acesso_servicos": acesso_servicos,
            "tecnologicos": tecnologicos,
            "religiosos": religiosos,
            "parentesco": parentesco,
            "valores_culturais": valores_culturais,
            "politicos_legais": politicos_legais,
            "economicos": economicos,
            "educacionais": educacionais,
            "rede_apoio": rede_apoio
        }

        st.success("✅ Avaliação transcultural salva com sucesso.")