# SAPE IA 2.0 — Regras clínicas de pré-natal
# Recuperadas e normalizadas a partir do acervo do projeto.

REGRAS = [{'linha_cuidado': 'Pré-natal',
  'categoria': 'Vacinação',
  'achado_clinico': 'Situação vacinal desconhecida',
  'diagnostico': {'codigo': None, 'termo': 'Situação vacinal prejudicada'},
  'resultado': {'codigo': None, 'termo': 'Situação vacinal avaliada e atualizada'},
  'intervencao': {'codigo': None, 'termo': 'Avaliar situação vacinal da gestante'},
  'prioridade': 'Alta',
  'fundamentacao': 'Na primeira consulta de pré-natal, a situação vacinal deve ser verificada por meio do cartão de '
                   'vacina, registros disponíveis e relato da gestante. Quando não houver comprovação, deve-se '
                   'considerar esquema desconhecido e organizar a atualização vacinal conforme o Calendário Nacional '
                   'de Vacinação da Gestante, incluindo hepatite B, dT, influenza, COVID-19 e dTpa a partir da 20ª '
                   'semana gestacional.',
  'transcultural': {'preservacao': ['Valorizar práticas familiares de cuidado que favoreçam a proteção da gestante e '
                                    'do bebê.',
                                    'Manter diálogo respeitoso sobre experiências prévias com vacinação.'],
                    'acomodacao': ['Adequar a orientação ao grau de escolaridade, idioma, cultura e contexto '
                                   'territorial da gestante.',
                                   'Negociar datas de vacinação compatíveis com deslocamento, trabalho, transporte e '
                                   'rotina familiar.'],
                    'repadronizacao': ['Reformular crenças equivocadas sobre vacinas por meio de educação em saúde '
                                       'clara, respeitosa e baseada em evidências.',
                                       'Estimular a reconstrução do cuidado pré-natal com inclusão do cartão vacinal '
                                       'como documento essencial.']},
  'referencias': ['Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.',
                  'Programa Nacional de Imunizações - PNI.',
                  'COFEN Resolução nº 736/2024.',
                  'Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Vacinação',
  'achado_clinico': 'Vacina dT incompleta',
  'diagnostico': {'codigo': None, 'termo': 'Risco de imunização incompleta contra difteria e tétano'},
  'resultado': {'codigo': None, 'termo': 'Esquema vacinal contra difteria e tétano completado'},
  'intervencao': {'codigo': None, 'termo': 'Completar esquema vacinal com dT conforme histórico vacinal'},
  'prioridade': 'Alta',
  'fundamentacao': 'A vacina dT é indicada na gestação conforme histórico vacinal, com objetivo de proteger contra '
                   'difteria e tétano. Em esquema incompleto, não se reinicia o esquema; devem ser completadas as '
                   'doses necessárias, respeitando intervalos recomendados e articulando a administração da dTpa a '
                   'partir da 20ª semana gestacional.',
  'transcultural': {'preservacao': ['Reconhecer saberes familiares sobre prevenção de doenças e proteção '
                                    'materno-infantil.'],
                    'acomodacao': ['Explicar o esquema em linguagem simples, utilizando o cartão vacinal como '
                                   'ferramenta visual.',
                                   'Ajustar o agendamento das doses conforme disponibilidade da gestante e da sala de '
                                   'vacina.'],
                    'repadronizacao': ['Corrigir a ideia de que doses antigas tornam desnecessária a atualização '
                                       'vacinal.',
                                       'Fortalecer a adesão ao esquema completo como cuidado de proteção materna e '
                                       'neonatal.']},
  'referencias': ['Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.',
                  'Programa Nacional de Imunizações - PNI.',
                  'COFEN Resolução nº 736/2024.',
                  'Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Vacinação',
  'achado_clinico': 'Vacina dTpa indicada',
  'diagnostico': {'codigo': None, 'termo': 'Necessidade de imunização contra difteria, tétano e coqueluche'},
  'resultado': {'codigo': None, 'termo': 'Gestante imunizada com dTpa'},
  'intervencao': {'codigo': None,
                  'termo': 'Administrar ou encaminhar para vacina dTpa a partir da 20ª semana gestacional'},
  'prioridade': 'Alta',
  'fundamentacao': 'A vacina dTpa é indicada em cada gestação a partir da 20ª semana gestacional, independentemente de '
                   'vacinação prévia, com objetivo de reduzir o risco de tétano neonatal e coqueluche no recém-nascido '
                   'por transferência transplacentária de anticorpos.',
  'transcultural': {'preservacao': ['Valorizar o desejo materno e familiar de proteger o recém-nascido.'],
                    'acomodacao': ['Orientar que a vacina é recomendada em cada gestação, mesmo que tenha sido '
                                   'realizada em gestação anterior.',
                                   'Organizar busca ativa ou encaminhamento conforme idade gestacional.'],
                    'repadronizacao': ['Reformular crenças de que a dTpa seria desnecessária por vacinação anterior.',
                                       'Estimular compreensão da vacina como proteção direta ao bebê nos primeiros '
                                       'meses de vida.']},
  'referencias': ['Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.',
                  'Programa Nacional de Imunizações - PNI.',
                  'COFEN Resolução nº 736/2024.',
                  'Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Vacinação',
  'achado_clinico': 'Vacina dTpa não realizada',
  'diagnostico': {'codigo': None, 'termo': 'Imunização materna ausente contra coqueluche'},
  'resultado': {'codigo': None, 'termo': 'Vacinação dTpa realizada no período oportuno'},
  'intervencao': {'codigo': None, 'termo': 'Realizar busca ativa para vacinação dTpa'},
  'prioridade': 'Alta',
  'fundamentacao': 'A ausência da dTpa após a 20ª semana gestacional aumenta a vulnerabilidade do recém-nascido à '
                   'coqueluche e ao tétano neonatal. A equipe deve identificar a não realização, orientar a gestante, '
                   'registrar a pendência e encaminhar imediatamente para vacinação.',
  'transcultural': {'preservacao': ['Manter vínculo e escuta qualificada sem julgamento.'],
                    'acomodacao': ['Identificar motivo da não vacinação, como acesso, medo, esquecimento ou '
                                   'desinformação.',
                                   'Adequar o plano de cuidado ao contexto familiar, cultural e territorial.'],
                    'repadronizacao': ['Construir nova compreensão sobre a importância da dTpa para proteção neonatal.',
                                       'Estimular registro e acompanhamento ativo das pendências vacinais.']},
  'referencias': ['Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.',
                  'Programa Nacional de Imunizações - PNI.',
                  'COFEN Resolução nº 736/2024.',
                  'Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Vacinação',
  'achado_clinico': 'Vacina influenza indicada',
  'diagnostico': {'codigo': None, 'termo': 'Necessidade de imunização contra influenza'},
  'resultado': {'codigo': None, 'termo': 'Gestante imunizada contra influenza'},
  'intervencao': {'codigo': None, 'termo': 'Administrar ou encaminhar para vacina influenza sazonal'},
  'prioridade': 'Alta',
  'fundamentacao': 'Gestantes e puérperas pertencem a grupo prioritário para vacinação contra influenza, devido ao '
                   'maior risco de formas graves da doença. A vacina influenza é indicada em dose anual por temporada '
                   'durante a gestação.',
  'transcultural': {'preservacao': ['Respeitar práticas culturais seguras de prevenção de doenças respiratórias.'],
                    'acomodacao': ['Explicar diferença entre reação vacinal leve e influenza.',
                                   'Planejar vacinação conforme campanha vigente e disponibilidade local.'],
                    'repadronizacao': ['Corrigir crenças de que a vacina causa gripe.',
                                       'Fortalecer a vacinação como proteção da gestante e do bebê.']},
  'referencias': ['Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.',
                  'Programa Nacional de Imunizações - PNI.',
                  'COFEN Resolução nº 736/2024.',
                  'Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Vacinação',
  'achado_clinico': 'Vacina influenza não realizada',
  'diagnostico': {'codigo': None, 'termo': 'Imunização ausente contra influenza'},
  'resultado': {'codigo': None, 'termo': 'Vacinação contra influenza realizada'},
  'intervencao': {'codigo': None, 'termo': 'Orientar e encaminhar gestante para vacinação contra influenza'},
  'prioridade': 'Alta',
  'fundamentacao': 'A não realização da vacina influenza mantém a gestante suscetível a complicações respiratórias '
                   'evitáveis. A equipe deve verificar a disponibilidade da vacina, orientar sobre segurança e '
                   'benefício, registrar a pendência e realizar busca ativa.',
  'transcultural': {'preservacao': ['Valorizar medidas familiares seguras de cuidado respiratório.'],
                    'acomodacao': ['Investigar barreiras de acesso, medo de reação ou experiências negativas '
                                   'anteriores.',
                                   'Ajustar orientação conforme compreensão da gestante.'],
                    'repadronizacao': ['Reformular informações equivocadas sobre risco da vacina na gravidez.',
                                       'Estimular adesão anual à vacinação durante o pré-natal.']},
  'referencias': ['Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.',
                  'Programa Nacional de Imunizações - PNI.',
                  'COFEN Resolução nº 736/2024.',
                  'Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Vacinação',
  'achado_clinico': 'Vacina hepatite B incompleta',
  'diagnostico': {'codigo': None, 'termo': 'Risco de imunização incompleta contra hepatite B'},
  'resultado': {'codigo': None, 'termo': 'Esquema vacinal contra hepatite B completado'},
  'intervencao': {'codigo': None, 'termo': 'Completar esquema vacinal contra hepatite B'},
  'prioridade': 'Alta',
  'fundamentacao': 'A vacina hepatite B é indicada na gestação conforme histórico vacinal, em esquema de três doses '
                   'quando não houver comprovação. Em esquema incompleto, não se deve reiniciar; deve-se completar as '
                   'doses faltantes conforme intervalo recomendado.',
  'transcultural': {'preservacao': ['Valorizar a preocupação da gestante com proteção do bebê e prevenção de '
                                    'infecções.'],
                    'acomodacao': ['Explicar o esquema de três doses e a necessidade de completar o calendário.',
                                   'Agendar retorno de acordo com deslocamento e acesso da gestante.'],
                    'repadronizacao': ['Reformular a percepção de que uma ou duas doses garantem proteção completa.',
                                       'Fortalecer acompanhamento longitudinal até conclusão do esquema.']},
  'referencias': ['Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.',
                  'Programa Nacional de Imunizações - PNI.',
                  'COFEN Resolução nº 736/2024.',
                  'Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Vacinação',
  'achado_clinico': 'Vacina hepatite B não realizada',
  'diagnostico': {'codigo': None, 'termo': 'Imunização ausente contra hepatite B'},
  'resultado': {'codigo': None, 'termo': 'Esquema vacinal contra hepatite B iniciado'},
  'intervencao': {'codigo': None, 'termo': 'Iniciar vacinação contra hepatite B conforme calendário da gestante'},
  'prioridade': 'Alta',
  'fundamentacao': 'Gestantes sem comprovação de vacinação contra hepatite B devem iniciar esquema vacinal de três '
                   'doses, conforme o Calendário Nacional de Vacinação. A vacinação reduz risco de infecção materna e '
                   'contribui para prevenção de transmissão vertical associada ao cuidado pré-natal adequado.',
  'transcultural': {'preservacao': ['Respeitar valores familiares relacionados à proteção da gestação.'],
                    'acomodacao': ['Explicar a relação entre hepatite B, gestação e proteção do recém-nascido.',
                                   'Planejar as doses no calendário de consultas do pré-natal.'],
                    'repadronizacao': ['Superar desconhecimento sobre hepatite B e vacinação na gravidez.',
                                       'Estimular continuidade do esquema até conclusão.']},
  'referencias': ['Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.',
                  'Programa Nacional de Imunizações - PNI.',
                  'COFEN Resolução nº 736/2024.',
                  'Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Vacinação',
  'achado_clinico': 'Vacina COVID-19 indicada',
  'diagnostico': {'codigo': None, 'termo': 'Necessidade de imunização contra COVID-19'},
  'resultado': {'codigo': None, 'termo': 'Gestante imunizada contra COVID-19'},
  'intervencao': {'codigo': None, 'termo': 'Encaminhar gestante para vacinação contra COVID-19'},
  'prioridade': 'Alta',
  'fundamentacao': 'A vacinação contra COVID-19 é indicada para gestantes em cada gestação, conforme Calendário '
                   'Nacional de Vacinação, com objetivo de reduzir formas graves, hospitalizações e óbitos por '
                   'SARS-CoV-2.',
  'transcultural': {'preservacao': ['Manter escuta respeitosa sobre experiências pessoais e familiares durante a '
                                    'pandemia.'],
                    'acomodacao': ['Esclarecer dúvidas sobre segurança, indicação e benefício da vacina.',
                                   'Considerar medos, crenças religiosas, culturais e experiências anteriores.'],
                    'repadronizacao': ['Reformular informações falsas ou inseguras sobre vacinação contra COVID-19 na '
                                       'gestação.',
                                       'Promover decisão informada baseada em evidências e no cuidado materno-fetal.']},
  'referencias': ['Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.',
                  'Programa Nacional de Imunizações - PNI.',
                  'COFEN Resolução nº 736/2024.',
                  'Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Vacinação',
  'achado_clinico': 'Recusa vacinal',
  'diagnostico': {'codigo': None, 'termo': 'Adesão prejudicada à vacinação'},
  'resultado': {'codigo': None, 'termo': 'Gestante orientada e decisão vacinal reavaliada'},
  'intervencao': {'codigo': None, 'termo': 'Realizar aconselhamento sobre vacinação na gestação'},
  'prioridade': 'Alta',
  'fundamentacao': 'A recusa vacinal deve ser acolhida com escuta qualificada, identificação dos motivos, orientação '
                   'baseada em evidências e registro em prontuário. A abordagem deve respeitar autonomia, cultura e '
                   'crenças, sem deixar de informar riscos da não vacinação para gestante e recém-nascido.',
  'transcultural': {'preservacao': ['Preservar vínculo, autonomia e respeito às crenças da gestante.'],
                    'acomodacao': ['Negociar nova conversa, envolver pessoa de confiança quando autorizado e oferecer '
                                   'material educativo.',
                                   'Adequar linguagem e estratégia educativa à realidade sociocultural.'],
                    'repadronizacao': ['Reformular mitos e informações falsas sem confronto ou julgamento.',
                                       'Construir plano gradual de adesão vacinal com decisão compartilhada.']},
  'referencias': ['Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.',
                  'Programa Nacional de Imunizações - PNI.',
                  'COFEN Resolução nº 736/2024.',
                  'Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Vacinação',
  'achado_clinico': 'Medo de reação vacinal',
  'diagnostico': {'codigo': None, 'termo': 'Medo relacionado à vacinação'},
  'resultado': {'codigo': None, 'termo': 'Medo reduzido e vacinação aceita ou reavaliada'},
  'intervencao': {'codigo': None, 'termo': 'Orientar sobre eventos adversos esperados e sinais de alerta'},
  'prioridade': 'Média',
  'fundamentacao': 'O medo de reação vacinal é uma barreira comum à adesão. A equipe deve explicar possíveis eventos '
                   'leves, sinais de alerta, condutas após vacinação e benefícios da imunização durante a gestação, '
                   'fortalecendo segurança e autonomia da gestante.',
  'transcultural': {'preservacao': ['Acolher relatos de experiências anteriores da gestante ou familiares.'],
                    'acomodacao': ['Explicar reações esperadas em linguagem simples e oferecer suporte pós-vacinação.',
                                   'Permitir tempo para perguntas e tomada de decisão.'],
                    'repadronizacao': ['Diferenciar reação vacinal leve de doença grave evitável por vacina.',
                                       'Reduzir medo por meio de educação em saúde baseada em evidências.']},
  'referencias': ['Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.',
                  'Programa Nacional de Imunizações - PNI.',
                  'COFEN Resolução nº 736/2024.',
                  'Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Vacinação',
  'achado_clinico': 'Falta de acesso à sala de vacina',
  'diagnostico': {'codigo': None, 'termo': 'Acesso prejudicado à vacinação'},
  'resultado': {'codigo': None, 'termo': 'Acesso à vacinação garantido'},
  'intervencao': {'codigo': None, 'termo': 'Articular acesso da gestante à sala de vacina'},
  'prioridade': 'Alta',
  'fundamentacao': 'A falta de acesso à sala de vacina compromete a integralidade do pré-natal e aumenta risco de '
                   'atraso vacinal. A equipe deve articular agendamento, transporte sanitário quando disponível, '
                   'vacinação em ações extramuros, busca ativa e integração entre pré-natal e imunização.',
  'transcultural': {'preservacao': ['Reconhecer estratégias comunitárias de deslocamento e apoio familiar.'],
                    'acomodacao': ['Adequar o plano vacinal aos dias de atendimento, transporte e permanência da '
                                   'gestante no território urbano ou rural.',
                                   'Articular com ACS, equipe ribeirinha, unidade de referência ou sala de vacina.'],
                    'repadronizacao': ['Transformar o cuidado fragmentado em acompanhamento programado e '
                                       'territorializado.',
                                       'Estimular registro ativo das pendências vacinais pela equipe.']},
  'referencias': ['Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.',
                  'Programa Nacional de Imunizações - PNI.',
                  'COFEN Resolução nº 736/2024.',
                  'Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Vacinação',
  'achado_clinico': 'Barreiras culturais relacionadas à vacinação',
  'diagnostico': {'codigo': None, 'termo': 'Conflito cultural relacionado à vacinação'},
  'resultado': {'codigo': None, 'termo': 'Barreiras culturais identificadas e manejadas'},
  'intervencao': {'codigo': None, 'termo': 'Realizar cuidado culturalmente congruente sobre vacinação'},
  'prioridade': 'Média',
  'fundamentacao': 'Barreiras culturais podem envolver crenças familiares, religiosas, comunitárias, experiências '
                   'históricas de desconfiança, medo de dano fetal ou informações falsas. A abordagem deve seguir '
                   'cuidado culturalmente congruente, com preservação de práticas seguras, acomodação de valores e '
                   'repadronização de práticas prejudiciais.',
  'transcultural': {'preservacao': ['Preservar práticas culturais que não tragam risco à gestante ou ao bebê.',
                                    'Valorizar lideranças familiares e comunitárias quando favorecem o cuidado.'],
                    'acomodacao': ['Negociar estratégias educativas compatíveis com crenças e organização familiar.',
                                   'Usar linguagem respeitosa, exemplos locais e escuta ativa.'],
                    'repadronizacao': ['Reformular práticas ou crenças que impeçam vacinação segura.',
                                       'Construir novo significado da vacina como proteção materna, fetal e '
                                       'comunitária.']},
  'referencias': ['Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.',
                  'Programa Nacional de Imunizações - PNI.',
                  'COFEN Resolução nº 736/2024.',
                  'Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Vacinação',
  'achado_clinico': 'Gestante ribeirinha com dificuldade de acesso à vacina',
  'diagnostico': {'codigo': None, 'termo': 'Vulnerabilidade territorial para atraso vacinal'},
  'resultado': {'codigo': None, 'termo': 'Vacinação viabilizada conforme realidade territorial'},
  'intervencao': {'codigo': None, 'termo': 'Planejar vacinação conforme contexto ribeirinho'},
  'prioridade': 'Alta',
  'fundamentacao': 'Gestantes ribeirinhas podem apresentar atraso vacinal por distância geográfica, transporte '
                   'fluvial, sazonalidade dos rios, custos de deslocamento e ausência de sala de vacina próxima. A '
                   'equipe deve planejar cuidado territorial, busca ativa, vacinação em ações itinerantes e '
                   'articulação com rede de atenção.',
  'transcultural': {'preservacao': ['Valorizar modos de vida ribeirinhos, redes comunitárias e formas locais de '
                                    'organização do cuidado.'],
                    'acomodacao': ['Adequar datas de vacinação ao calendário das embarcações, cheia/vazante dos rios e '
                                   'consultas de pré-natal.',
                                   'Articular com ACS, equipe fluvial, UBS de referência e gestão local.'],
                    'repadronizacao': ['Substituir cuidado oportunístico por plano vacinal programado e acompanhado.',
                                       'Estimular registro, busca ativa e monitoramento das pendências vacinais em '
                                       'territórios de difícil acesso.']},
  'referencias': ['Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.',
                  'Programa Nacional de Imunizações - PNI.',
                  'COFEN Resolução nº 736/2024.',
                  'Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Vacinação',
  'achado_clinico': 'Gestante sem cartão vacinal',
  'diagnostico': {'codigo': None, 'termo': 'Registro vacinal ausente'},
  'resultado': {'codigo': None, 'termo': 'Registro vacinal recuperado ou atualizado'},
  'intervencao': {'codigo': None, 'termo': 'Solicitar, recuperar ou reconstruir registro vacinal'},
  'prioridade': 'Alta',
  'fundamentacao': 'A ausência do cartão vacinal dificulta a avaliação da situação imunológica da gestante. A equipe '
                   'deve buscar registros em sistemas disponíveis, orientar emissão ou segunda via quando possível e, '
                   'na ausência de comprovação, conduzir o esquema conforme situação vacinal desconhecida.',
  'transcultural': {'preservacao': ['Evitar culpabilização da gestante pela perda ou ausência do documento.'],
                    'acomodacao': ['Orientar sobre guarda do cartão junto aos documentos do pré-natal.',
                                   'Auxiliar na recuperação de registros conforme rede local.'],
                    'repadronizacao': ['Reorganizar o cuidado para que o cartão vacinal seja acompanhado em todas as '
                                       'consultas.',
                                       'Estimular corresponsabilização entre gestante, família e equipe.']},
  'referencias': ['Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.',
                  'Programa Nacional de Imunizações - PNI.',
                  'COFEN Resolução nº 736/2024.',
                  'Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural.']}]
