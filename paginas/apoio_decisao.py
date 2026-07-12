from modulos.regras import gerar_planejamento_transcultural
from modulos.inferencia import executar_inferencia
import streamlit as st
from modulos.estado import obter_achados_clinicos, obter_resumo_transcultural


def _rotulo_item(item):
    if isinstance(item, dict):
        codigo = item.get("codigo")
        termo = item.get("termo") or item.get("nome") or ""
        return f"{codigo} — {termo}" if codigo else f"{termo} — código CIPE 2019 não vinculado"
    return str(item)


def _mostrar_lista(titulo, itens, chave_base):
    st.markdown(f"**{titulo}**")
    selecionados = []
    if not itens:
        st.write("Nenhum item sugerido.")
        return selecionados
    for i, item in enumerate(itens):
        marcado = st.checkbox(_rotulo_item(item), value=True, key=f"{chave_base}_{i}")
        if marcado:
            selecionados.append(item)
    return selecionados


def tela_apoio_decisao():
    st.header("🧠 Apoio à Decisão Clínica de Enfermagem")
    st.caption("Revise as sugestões e desmarque aquilo que não deseja levar para o Processo de Enfermagem.")
    st.progress(80)

    dados = st.session_state.get("dados", {})
    achados = obter_achados_clinicos()
    bloco_b = dados.get("avaliacao_transcultural", {})
    transcultural = obter_resumo_transcultural()
    linguagem = dados.get("linguagem", "Comparativo")

    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Achados clínicos identificados")
        for item in achados: st.write(f"• {item}")
        if not achados: st.info("Nenhum achado clínico registrado.")
    with col_b:
        st.subheader("Resumo transcultural")
        for item in transcultural: st.write(f"• {item}")
        if not transcultural: st.info("Nenhum dado transcultural registrado.")

    sugestoes = executar_inferencia(achados, bloco_b, linguagem)
    dados["sugestoes"] = sugestoes
    st.session_state["dados"] = dados

    st.markdown("---")
    st.subheader("Síntese clínica automática")
    if sugestoes:
        st.write("Os achados selecionados foram cruzados com as regras clínicas de pré-natal. Revise as sugestões antes de salvá-las no Processo de Enfermagem.")
    else:
        st.info("Nenhuma regra clínica foi ativada pelos achados selecionados.")

    st.subheader("Diagnósticos, resultados e intervenções sugeridos")
    sugestoes_selecionadas = []

    for idx, s in enumerate(sugestoes):
        titulo = s.get("titulo") or s.get("achados", ["Regra clínica"])[0]
        prioridade = s.get("prioridade", "")
        if prioridade == "Alta": st.warning(f"⚠️ {titulo} — prioridade {prioridade}")
        else: st.info(f"🟡 {titulo}" + (f" — prioridade {prioridade}" if prioridade else ""))

        with st.expander(f"Revisar recomendação — {titulo}", expanded=True):
            st.markdown(f"**Achados considerados:** {', '.join(s.get('achados', []))}")
            st.markdown(f"**Justificativa:** {s.get('justificativa', '')}")
            nova = dict(s)
            if linguagem == "CIPE®":
                nova["cipe_diag"] = _mostrar_lista("Diagnósticos CIPE®", s.get("cipe_diag", []), f"cipe_diag_{idx}")
                nova["cipe_res"] = _mostrar_lista("Resultados CIPE®", s.get("cipe_res", []), f"cipe_res_{idx}")
                nova["cipe_int"] = _mostrar_lista("Intervenções CIPE®", s.get("cipe_int", []), f"cipe_int_{idx}")
            elif linguagem == "NANDA-I / NOC / NIC":
                nova["nanda"] = _mostrar_lista("Diagnósticos NANDA-I", s.get("nanda", []), f"nanda_{idx}")
                nova["noc"] = _mostrar_lista("Resultados NOC", s.get("noc", []), f"noc_{idx}")
                nova["nic"] = _mostrar_lista("Intervenções NIC", s.get("nic", []), f"nic_{idx}")
            else:
                nova["cipe_diag"] = _mostrar_lista("Diagnósticos CIPE®", s.get("cipe_diag", []), f"cipe_diag_{idx}")
                nova["nanda"] = _mostrar_lista("Diagnósticos NANDA-I", s.get("nanda", []), f"nanda_{idx}")
                nova["cipe_res"] = _mostrar_lista("Resultados CIPE®", s.get("cipe_res", []), f"cipe_res_{idx}")
                nova["noc"] = _mostrar_lista("Resultados NOC", s.get("noc", []), f"noc_{idx}")
                nova["cipe_int"] = _mostrar_lista("Intervenções CIPE®", s.get("cipe_int", []), f"cipe_int_{idx}")
                nova["nic"] = _mostrar_lista("Intervenções NIC", s.get("nic", []), f"nic_{idx}")
            st.markdown("**Fundamentação científica:**")
            st.info(s.get("fundamentacao", ""))
            sugestoes_selecionadas.append(nova)

    planejamento = gerar_planejamento_transcultural(bloco_b, sugestoes_selecionadas)
    st.subheader("Planejamento transcultural")
    colp, coln, colr = st.columns(3)
    with colp:
        st.markdown("### Preservação / Manutenção")
        for item in planejamento.get("preservacao", []): st.write(f"• {item}")
    with coln:
        st.markdown("### Acomodação / Negociação")
        for item in planejamento.get("negociacao", []): st.write(f"• {item}")
    with colr:
        st.markdown("### Repadronização / Reestruturação")
        for item in planejamento.get("reestruturacao", []): st.write(f"• {item}")

    if st.button("Salvar apoio à decisão revisado"):
        st.session_state.dados["sugestoes"] = sugestoes
        st.session_state.dados["sugestoes_selecionadas"] = sugestoes_selecionadas
        st.session_state.dados["planejamento_transcultural"] = planejamento
        st.success("Apoio à decisão revisado salvo. Vá para Processo de Enfermagem.")
