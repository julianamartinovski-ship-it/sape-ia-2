def _add(lista, titulo, regra, gravidade, achados, justificativa, cipe_diag, cipe_res, cipe_int, nanda, noc, nic, fundamentacao, grau):
    lista.append({"titulo": titulo, "regra": regra, "gravidade": gravidade, "achados": achados, "justificativa": justificativa, "cipe_diag": cipe_diag, "cipe_res": cipe_res, "cipe_int": cipe_int, "nanda": nanda, "noc": noc, "nic": nic, "fundamentacao": fundamentacao, "grau": grau})

def apoio_decisao_clinica(achados, bloco_b):
    sugestoes = []
    if "Hipertensão arterial" in achados and "Proteinúria" in achados:
        _add(sugestoes, "Risco para Síndrome Hipertensiva da Gestação", "R001", "Alerta", ["Hipertensão arterial", "Proteinúria"], "Os achados sugerem alteração hipertensiva na gestação, exigindo avaliação de gravidade, classificação de risco e conduta conforme protocolo vigente.", ["Pressão arterial alterada", "Risco materno aumentado", "Risco de complicação na gestação"], ["Pressão arterial controlada", "Gestante orientada sobre sinais de alerta", "Risco materno reduzido"], ["Monitorar pressão arterial", "Investigar cefaleia, escotomas e dor epigástrica", "Avaliar edema", "Orientar sinais de alerta", "Encaminhar conforme classificação de risco"], ["Risco de pressão arterial instável", "Risco de perfusão tissular ineficaz", "Conhecimento deficiente sobre sinais de alerta na gestação"], ["Controle da pressão arterial", "Conhecimento: gestação de risco", "Estado materno: estabilidade clínica"], ["Monitorização dos sinais vitais", "Controle da hipertensão", "Educação em saúde", "Monitorização materna", "Encaminhamento para cuidado especializado quando indicado"], "Protocolos de pré-natal do Ministério da Saúde; Processo de Enfermagem; CIPE®; NANDA-I; NOC; NIC.", "Alto apoio à decisão")
    if "Edema importante" in achados and "Hipertensão arterial" in achados:
        _add(sugestoes, "Sinal de alerta materno associado à hipertensão", "R002", "Atenção", ["Edema importante", "Hipertensão arterial"], "A associação de edema importante e hipertensão requer investigação de sinais de gravidade e acompanhamento clínico rigoroso.", ["Edema presente", "Risco materno aumentado"], ["Edema reduzido", "Sinais de agravamento ausentes"], ["Avaliar edema", "Monitorar sinais vitais", "Orientar sinais de alarme", "Registrar evolução clínica"], ["Excesso de volume de líquidos", "Risco de pressão arterial instável"], ["Equilíbrio hídrico", "Estado materno: estabilidade clínica"], ["Controle hídrico", "Monitorização dos sinais vitais", "Educação em saúde"], "Protocolos de pré-natal; avaliação clínica da gestante; julgamento clínico do enfermeiro.", "Apoio moderado")
    if "Corrimento vaginal" in achados and "Prurido genital" in achados:
        _add(sugestoes, "Alteração gineco-obstétrica: corrimento associado a prurido", "R003", "Atenção", ["Corrimento vaginal", "Prurido genital"], "Corrimento vaginal associado a prurido demanda avaliação das características do corrimento, sinais associados, orientação e manejo conforme protocolo assistencial.", ["Corrimento vaginal presente", "Prurido genital presente", "Risco de infecção"], ["Sintomas reduzidos", "Conforto genital melhorado", "Gestante orientada"], ["Avaliar características do corrimento", "Orientar higiene íntima", "Investigar sinais de infecção", "Encaminhar ou manejar conforme protocolo"], ["Conforto prejudicado", "Risco de infecção"], ["Conforto físico", "Conhecimento: cuidados na gestação"], ["Cuidados perineais", "Educação em saúde", "Controle de infecção"], "Protocolos de atenção ao pré-natal e saúde sexual/reprodutiva.", "Apoio moderado")
    if "Infecção urinária" in achados:
        _add(sugestoes, "Infecção urinária na gestação", "R004", "Atenção", ["Infecção urinária"], "Infecção urinária na gestação exige manejo oportuno e acompanhamento para prevenção de complicações maternas e fetais.", ["Infecção urinária presente", "Risco de complicação na gestação"], ["Sinais de infecção reduzidos", "Gestante orientada", "Adesão ao tratamento"], ["Orientar ingesta hídrica", "Orientar sinais de alerta", "Verificar tratamento prescrito", "Acompanhar resultado de exames"], ["Eliminação urinária prejudicada", "Risco de infecção"], ["Eliminação urinária", "Controle de risco"], ["Controle da infecção", "Cuidados na eliminação urinária", "Educação em saúde"], "Protocolos de pré-natal do Ministério da Saúde.", "Apoio moderado")
    if "Anemia" in achados:
        _add(sugestoes, "Anemia na gestação", "R005", "Atenção", ["Anemia"], "Anemia durante a gestação requer avaliação, suplementação conforme protocolo e acompanhamento da adesão ao tratamento.", ["Anemia presente", "Risco nutricional aumentado"], ["Estado nutricional melhorado", "Adesão à suplementação", "Gestante orientada"], ["Orientar suplementação prescrita", "Orientar alimentação rica em ferro", "Acompanhar hemoglobina", "Investigar sintomas associados"], ["Nutrição desequilibrada: menor que as necessidades corporais", "Fadiga"], ["Estado nutricional", "Conhecimento: dieta saudável"], ["Aconselhamento nutricional", "Controle da nutrição", "Educação em saúde"], "Protocolos de pré-natal; atenção nutricional na gestação.", "Apoio moderado")
    if "Comunidade ribeirinha" in bloco_b.get("contexto_territorial", []) or "Acesso exclusivamente fluvial" in bloco_b.get("acesso_servicos", []):
        _add(sugestoes, "Alerta territorial e transcultural: contexto ribeirinho", "T001", "Contextual", ["Território ribeirinho / acesso fluvial"], "O contexto ribeirinho pode influenciar acesso, continuidade do cuidado, retorno ao pré-natal e planejamento das ações de enfermagem.", ["Acesso aos serviços de saúde prejudicado", "Risco de cuidado pré-natal interrompido"], ["Acesso ao cuidado melhorado", "Plano de cuidado culturalmente congruente"], ["Planejar retorno considerando transporte fluvial", "Articular ACS e rede comunitária", "Considerar nível do rio", "Registrar barreiras territoriais"], ["Manutenção ineficaz da saúde", "Risco de vínculo prejudicado com o serviço de saúde"], ["Acesso ao cuidado", "Comportamento de busca de saúde"], ["Facilitação do acesso ao serviço de saúde", "Aconselhamento", "Coordenação do cuidado"], "Teoria Transcultural de Madeleine Leininger; PNAB; APS em territórios ribeirinhos.", "Apoio contextual")
    return sugestoes

def gerar_planejamento_transcultural(bloco_b, sugestoes=None):
    preservacao, negociacao, reestruturacao = [], [], []

    for sugestao in sugestoes or []:
        plano = sugestao.get("transcultural", {}) or {}
        preservacao.extend(plano.get("preservacao", []))
        negociacao.extend(plano.get("acomodacao", plano.get("negociacao", [])))
        reestruturacao.extend(plano.get("repadronizacao", plano.get("reestruturacao", [])))

    acesso = bloco_b.get("acesso_servicos", [])
    valores = bloco_b.get("valores_culturais", [])
    rede = bloco_b.get("rede_apoio", [])
    tecnologia = bloco_b.get("tecnologicos", [])

    if "Apoio familiar" in rede or "Família extensa" in rede:
        preservacao.append("Manter e valorizar a participação da família no cuidado, quando desejado pela gestante.")
    if "Agente Comunitário de Saúde" in rede:
        preservacao.append("Manter articulação com o ACS para acompanhamento territorial e busca ativa.")
    if "Parteira tradicional" in rede or "Parteira tradicional" in valores:
        negociacao.append("Negociar a participação da parteira tradicional como apoio cultural, preservando a segurança clínica.")
    if "Uso de plantas medicinais" in valores or "Uso de chás tradicionais" in valores:
        negociacao.append("Investigar plantas e chás utilizados e negociar uso seguro na gestação.")
    if "Acesso exclusivamente fluvial" in acesso or "Dependência do nível do rio" in acesso:
        negociacao.append("Planejar retorno considerando transporte fluvial, nível do rio e tempo de deslocamento.")
    if "Sem acesso à internet" in tecnologia or "Sem sinal de celular" in tecnologia:
        negociacao.append("Adaptar orientações e seguimento para estratégias presenciais e apoio comunitário.")
    if "Recusa de encaminhamento" in valores:
        reestruturacao.append("Reestruturar o plano diante de recusa de encaminhamento em situação de risco, reforçando sinais de alerta.")
    if "Automedicação" in valores:
        reestruturacao.append("Orientar suspensão de automedicação e pactuar condutas seguras conforme avaliação clínica.")

    def unicos(itens):
        return list(dict.fromkeys(x for x in itens if x))

    preservacao = unicos(preservacao)
    negociacao = unicos(negociacao)
    reestruturacao = unicos(reestruturacao)

    if not preservacao:
        preservacao.append("Preservar práticas culturais e redes de apoio que não ofereçam risco à gestante ou ao feto.")
    if not negociacao:
        negociacao.append("Negociar o plano de cuidado considerando crenças, território, acesso e preferências da gestante.")
    if not reestruturacao:
        reestruturacao.append("Reestruturar práticas culturais apenas quando representarem risco à saúde materno-fetal.")

    return {"preservacao": preservacao, "negociacao": negociacao, "reestruturacao": reestruturacao}
