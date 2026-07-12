# SAPE IA 2.0 — Regras clínicas de pré-natal
# Recuperadas e normalizadas a partir do acervo do projeto.

REGRAS = [{'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames laboratoriais',
  'achado_clinico': 'Hemoglobina baixa',
  'diagnostico': {'codigo': '10012606', 'termo': 'Processo do Sistema Circulatório, Prejudicado'},
  'resultado': {'codigo': '10028379', 'termo': 'Processo do Sistema Circulatório, Positivo'},
  'intervencao': {'codigo': '10024618', 'termo': 'Orientar sobre Nutrição'},
  'prioridade': 'Alta',
  'fundamentacao': 'Hemoglobina baixa no pré-natal sugere anemia gestacional, associada a maior risco de fadiga, '
                   'infecção, parto prematuro, baixo peso ao nascer e morbimortalidade materno-fetal. A conduta de '
                   'enfermagem inclui avaliação clínica, orientação alimentar rica em ferro, adesão à suplementação '
                   'prescrita, investigação de sinais de gravidade e encaminhamento conforme protocolo.',
  'transcultural': {'preservacao': ['Valorizar alimentos culturalmente aceitos e ricos em ferro disponíveis no '
                                    'território.'],
                    'acomodacao': ['Adaptar orientações alimentares à renda, acesso, hábitos familiares e crenças da '
                                   'gestante.'],
                    'repadronizacao': ['Reorientar práticas alimentares que reduzam absorção de ferro, como consumo de '
                                       'café junto às refeições.']},
  'referencias': ['Ministério da Saúde. Atenção ao pré-natal de baixo risco.',
                  'FEBRASGO. Recomendações para anemia na gestação.',
                  'COFEN Resolução nº 736/2024.',
                  'OMS. Recomendações de cuidado pré-natal.',
                  'Leininger. Teoria Transcultural.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames laboratoriais',
  'achado_clinico': 'Hematócrito baixo',
  'diagnostico': {'codigo': '10012606', 'termo': 'Processo do Sistema Circulatório, Prejudicado'},
  'resultado': {'codigo': '10028379', 'termo': 'Processo do Sistema Circulatório, Positivo'},
  'intervencao': {'codigo': '10019470', 'termo': 'Orientar sobre Medicação'},
  'prioridade': 'Alta',
  'fundamentacao': 'Hematócrito baixo pode indicar hemodiluição fisiológica ou anemia, devendo ser interpretado em '
                   'conjunto com hemoglobina, ferritina, sinais clínicos e idade gestacional. A enfermagem deve '
                   'orientar uso correto de sulfato ferroso quando prescrito, alimentação adequada e seguimento '
                   'laboratorial.',
  'transcultural': {'preservacao': ['Reconhecer práticas alimentares familiares protetoras.'],
                    'acomodacao': ['Negociar horários de suplementação conforme rotina da gestante.'],
                    'repadronizacao': ['Corrigir crenças que levem à suspensão do ferro por náuseas ou escurecimento '
                                       'das fezes.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'COFEN Resolução nº 736/2024.', 'OMS.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames laboratoriais',
  'achado_clinico': 'Ferritina baixa',
  'diagnostico': {'codigo': '10023009', 'termo': 'Ingestão Nutricional, Prejudicada'},
  'resultado': {'codigo': '10037572', 'termo': 'Ingestão Nutricional, nos Limites Normais'},
  'intervencao': {'codigo': '10024618', 'termo': 'Orientar sobre Nutrição'},
  'prioridade': 'Alta',
  'fundamentacao': 'Ferritina baixa indica redução das reservas de ferro, podendo anteceder ou acompanhar anemia '
                   'ferropriva. No pré-natal, exige orientação nutricional, avaliação de adesão à suplementação e '
                   'monitoramento para prevenção de repercussões maternas e fetais.',
  'transcultural': {'preservacao': ['Estimular alimentos regionais ricos em ferro.'],
                    'acomodacao': ['Adequar plano alimentar à disponibilidade local.'],
                    'repadronizacao': ['Orientar combinação com fontes de vitamina C e evitar inibidores de absorção '
                                       'junto às refeições.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'COFEN Resolução nº 736/2024.', 'OMS.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames laboratoriais',
  'achado_clinico': 'Vitamina B12 baixa',
  'diagnostico': {'codigo': '10023009', 'termo': 'Ingestão Nutricional, Prejudicada'},
  'resultado': {'codigo': '10037572', 'termo': 'Ingestão Nutricional, nos Limites Normais'},
  'intervencao': {'codigo': '10024618', 'termo': 'Orientar sobre Nutrição'},
  'prioridade': 'Média',
  'fundamentacao': 'Vitamina B12 baixa pode contribuir para anemia megaloblástica, sintomas neurológicos e alterações '
                   'no desenvolvimento fetal. A enfermagem deve orientar alimentação, investigar dietas restritivas e '
                   'encaminhar para avaliação e reposição conforme protocolo.',
  'transcultural': {'preservacao': ['Respeitar escolhas alimentares culturais ou religiosas.'],
                    'acomodacao': ['Adequar orientação para gestantes vegetarianas, veganas ou com baixa ingestão de '
                                   'alimentos de origem animal.'],
                    'repadronizacao': ['Reorientar restrições alimentares com risco nutricional sem acompanhamento '
                                       'profissional.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'COFEN Resolução nº 736/2024.', 'OMS.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames laboratoriais',
  'achado_clinico': 'Vitamina D baixa',
  'diagnostico': {'codigo': '10023009', 'termo': 'Ingestão Nutricional, Prejudicada'},
  'resultado': {'codigo': '10037572', 'termo': 'Ingestão Nutricional, nos Limites Normais'},
  'intervencao': {'codigo': '10024618', 'termo': 'Orientar sobre Nutrição'},
  'prioridade': 'Média',
  'fundamentacao': 'Vitamina D baixa pode relacionar-se a alterações ósseas, metabólicas e imunológicas. Na gestação, '
                   'deve ser avaliada conforme risco clínico, dieta, exposição solar e protocolo local, com orientação '
                   'segura e encaminhamento quando necessário.',
  'transcultural': {'preservacao': ['Considerar hábitos culturais de vestimenta e exposição solar.'],
                    'acomodacao': ['Orientar exposição solar segura conforme realidade territorial.'],
                    'repadronizacao': ['Evitar automedicação com doses elevadas sem prescrição.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'COFEN Resolução nº 736/2024.', 'OMS.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames laboratoriais',
  'achado_clinico': 'Glicemia alterada',
  'diagnostico': {'codigo': '10005876', 'termo': 'Diabetes'},
  'resultado': {'codigo': '10027532', 'termo': 'Processo do Sistema Regulatório, Eficaz'},
  'intervencao': {'codigo': '10024618', 'termo': 'Orientar sobre Nutrição'},
  'prioridade': 'Alta',
  'fundamentacao': 'Glicemia alterada no pré-natal pode indicar risco de diabetes mellitus gestacional ou diabetes '
                   'prévio não diagnosticado. Deve-se orientar alimentação adequada, atividade física quando não '
                   'contraindicada, controle glicêmico, avaliação médica e seguimento conforme protocolo.',
  'transcultural': {'preservacao': ['Valorizar alimentos tradicionais saudáveis e acessíveis.'],
                    'acomodacao': ['Adaptar plano alimentar à cultura, renda e rotina familiar.'],
                    'repadronizacao': ['Reduzir consumo frequente de açúcar, bebidas adoçadas e ultraprocessados.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'COFEN Resolução nº 736/2024.', 'OMS.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames laboratoriais',
  'achado_clinico': 'TOTG alterado',
  'diagnostico': {'codigo': '10005876', 'termo': 'Diabetes'},
  'resultado': {'codigo': '10027532', 'termo': 'Processo do Sistema Regulatório, Eficaz'},
  'intervencao': {'codigo': '10024625', 'termo': 'Orientar sobre Regime Terapêutico'},
  'prioridade': 'Alta',
  'fundamentacao': 'TOTG alterado confirma alteração do metabolismo glicêmico na gestação e exige acompanhamento para '
                   'prevenção de macrossomia, pré-eclâmpsia, parto traumático, hipoglicemia neonatal e complicações '
                   'maternas. A enfermagem deve orientar tratamento, autocuidado e seguimento multiprofissional.',
  'transcultural': {'preservacao': ['Manter alimentos culturais que sejam adequados ao controle glicêmico.'],
                    'acomodacao': ['Construir plano possível conforme acesso a alimentos e rotina da gestante.'],
                    'repadronizacao': ['Substituir padrões alimentares de alto índice glicêmico por alternativas '
                                       'locais mais saudáveis.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'COFEN Resolução nº 736/2024.', 'OMS.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames laboratoriais',
  'achado_clinico': 'Proteinúria',
  'diagnostico': {'codigo': '10001359', 'termo': 'Função do Sistema Urinário, Prejudicada'},
  'resultado': {'codigo': '10028615', 'termo': 'Função do Sistema Urinário, Eficaz'},
  'intervencao': {'codigo': '10044148', 'termo': 'Orientar sobre Medição de Pressão Arterial'},
  'prioridade': 'Alta',
  'fundamentacao': 'Proteinúria na gestação pode estar associada a infecção urinária, doença renal ou pré-eclâmpsia, '
                   'especialmente quando acompanhada de hipertensão, cefaleia, escotomas, dor epigástrica ou edema. '
                   'Exige avaliação imediata, controle pressórico e encaminhamento conforme gravidade.',
  'transcultural': {'preservacao': ['Acolher relatos de sintomas conforme linguagem e interpretação cultural da '
                                    'gestante.'],
                    'acomodacao': ['Orientar sinais de alerta de forma simples e objetiva.'],
                    'repadronizacao': ['Reforçar que edema importante, cefaleia ou alterações visuais não devem ser '
                                       'tratados apenas com medidas caseiras.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'COFEN Resolução nº 736/2024.', 'OMS.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames laboratoriais',
  'achado_clinico': 'Creatinina alterada',
  'diagnostico': {'codigo': '10012972', 'termo': 'Processo do Sistema Urinário, Prejudicado'},
  'resultado': {'codigo': '10028604', 'termo': 'Processo do Sistema Urinário, Eficaz'},
  'intervencao': {'codigo': '10024625', 'termo': 'Orientar sobre Regime Terapêutico'},
  'prioridade': 'Alta',
  'fundamentacao': 'Creatinina alterada na gestação pode indicar comprometimento renal, doença hipertensiva, infecção '
                   'ou condição clínica de maior risco. Deve-se avaliar sinais associados, pressão arterial, '
                   'proteinúria, hidratação, medicamentos em uso e necessidade de referência ao pré-natal de alto '
                   'risco.',
  'transcultural': {'preservacao': ['Considerar práticas locais de ingestão hídrica e uso de chás.'],
                    'acomodacao': ['Orientar hidratação segura e evitar automedicação.'],
                    'repadronizacao': ['Desestimular uso de plantas medicinais potencialmente nefrotóxicas sem '
                                       'avaliação profissional.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'COFEN Resolução nº 736/2024.', 'OMS.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames laboratoriais',
  'achado_clinico': 'Plaquetopenia',
  'diagnostico': {'codigo': '10012606', 'termo': 'Processo do Sistema Circulatório, Prejudicado'},
  'resultado': {'codigo': '10028379', 'termo': 'Processo do Sistema Circulatório, Positivo'},
  'intervencao': {'codigo': '10024625', 'termo': 'Orientar sobre Regime Terapêutico'},
  'prioridade': 'Alta',
  'fundamentacao': 'Plaquetopenia na gestação pode ser gestacional, imunológica ou associada a síndromes hipertensivas '
                   'graves, como pré-eclâmpsia e HELLP. A avaliação deve considerar valores seriados, sangramentos, '
                   'pressão arterial, enzimas hepáticas e sinais de gravidade.',
  'transcultural': {'preservacao': ['Acolher relatos de sangramentos e sinais percebidos pela gestante.'],
                    'acomodacao': ['Orientar procura imediata diante de sangramento, dor epigástrica, cefaleia intensa '
                                   'ou mal-estar.'],
                    'repadronizacao': ['Evitar banalização de manchas roxas, sangramento gengival ou epistaxe na '
                                       'gestação.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'COFEN Resolução nº 736/2024.', 'OMS.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames laboratoriais',
  'achado_clinico': 'Urocultura positiva',
  'diagnostico': {'codigo': '10029915', 'termo': 'Infecção do Trato Urinário'},
  'resultado': {'codigo': '10028945', 'termo': 'Infecção, Ausente'},
  'intervencao': {'codigo': '10051016', 'termo': 'Orientar sobre Infecção'},
  'prioridade': 'Alta',
  'fundamentacao': 'Urocultura positiva na gestação indica infecção urinária ou bacteriúria significativa, condições '
                   'associadas a pielonefrite, parto prematuro e baixo peso ao nascer. A enfermagem deve orientar '
                   'adesão ao tratamento, hidratação, sinais de alerta e controle após tratamento.',
  'transcultural': {'preservacao': ['Reconhecer práticas de cuidado íntimo culturalmente aceitas e seguras.'],
                    'acomodacao': ['Orientar higiene, hidratação e uso correto do antibiótico conforme prescrição.'],
                    'repadronizacao': ['Desestimular interrupção do tratamento quando sintomas melhorarem.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'COFEN Resolução nº 736/2024.', 'OMS.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames laboratoriais',
  'achado_clinico': 'Bacteriúria assintomática',
  'diagnostico': {'codigo': '10051950', 'termo': 'Risco de Infecção Urinária'},
  'resultado': {'codigo': '10028945', 'termo': 'Infecção, Ausente'},
  'intervencao': {'codigo': '10038112', 'termo': 'Orientar sobre Prevenção de Infecção Cruzada'},
  'prioridade': 'Alta',
  'fundamentacao': 'Bacteriúria assintomática no pré-natal deve ser tratada conforme protocolo por risco de evolução '
                   'para pielonefrite e complicações obstétricas. Mesmo sem sintomas, requer orientação, tratamento '
                   'prescrito, retorno e controle laboratorial.',
  'transcultural': {'preservacao': ['Acolher a percepção da gestante de estar saudável por não apresentar sintomas.'],
                    'acomodacao': ['Explicar que ausência de sintomas não exclui risco gestacional.'],
                    'repadronizacao': ['Reforçar necessidade de tratamento completo mesmo sem dor ou ardência '
                                       'urinária.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'COFEN Resolução nº 736/2024.', 'OMS.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames laboratoriais',
  'achado_clinico': 'VDRL reagente',
  'diagnostico': {'codigo': '10023032', 'termo': 'Infecção'},
  'resultado': {'codigo': '10028945', 'termo': 'Infecção, Ausente'},
  'intervencao': {'codigo': '10051016', 'termo': 'Orientar sobre Infecção'},
  'prioridade': 'Alta',
  'fundamentacao': 'VDRL reagente no pré-natal sugere sífilis e exige confirmação/avaliação conforme protocolo, '
                   'tratamento imediato com penicilina quando indicado, tratamento de parceria sexual, notificação e '
                   'seguimento sorológico para prevenção da sífilis congênita.',
  'transcultural': {'preservacao': ['Acolher a gestante sem julgamento moral.'],
                    'acomodacao': ['Incluir parceria sexual no cuidado quando autorizado e conforme protocolo.'],
                    'repadronizacao': ['Reduzir estigma e reforçar que tratamento adequado previne transmissão '
                                       'vertical.']},
  'referencias': ['Ministério da Saúde. Protocolo Clínico e Diretrizes Terapêuticas para IST.',
                  'FEBRASGO.',
                  'COFEN Resolução nº 736/2024.',
                  'OMS.',
                  'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames laboratoriais',
  'achado_clinico': 'HIV reagente',
  'diagnostico': {'codigo': '10023032', 'termo': 'Infecção'},
  'resultado': {'codigo': '10028945', 'termo': 'Infecção, Ausente'},
  'intervencao': {'codigo': '10024625', 'termo': 'Orientar sobre Regime Terapêutico'},
  'prioridade': 'Alta',
  'fundamentacao': 'HIV reagente na gestação requer acolhimento, confirmação diagnóstica conforme fluxo, início ou '
                   'continuidade imediata da terapia antirretroviral, avaliação da carga viral, prevenção da '
                   'transmissão vertical, orientação sobre parto, puerpério e alimentação infantil conforme protocolo.',
  'transcultural': {'preservacao': ['Garantir sigilo, acolhimento e respeito à identidade da gestante.'],
                    'acomodacao': ['Adaptar orientações à rede de apoio e ao contexto familiar.'],
                    'repadronizacao': ['Combater estigma, abandono do tratamento e crenças que dificultem adesão à '
                                       'TARV.']},
  'referencias': ['Ministério da Saúde. PCDT para manejo da infecção pelo HIV em gestantes.',
                  'FEBRASGO.',
                  'COFEN Resolução nº 736/2024.',
                  'OMS.',
                  'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames laboratoriais',
  'achado_clinico': 'HBsAg reagente',
  'diagnostico': {'codigo': '10023032', 'termo': 'Infecção'},
  'resultado': {'codigo': '10028945', 'termo': 'Infecção, Ausente'},
  'intervencao': {'codigo': '10051016', 'termo': 'Orientar sobre Infecção'},
  'prioridade': 'Alta',
  'fundamentacao': 'HBsAg reagente indica infecção pelo vírus da hepatite B e exige avaliação clínica, exames '
                   'complementares, seguimento especializado quando indicado e planejamento da profilaxia neonatal com '
                   'vacina e imunoglobulina conforme protocolo para prevenção da transmissão vertical.',
  'transcultural': {'preservacao': ['Acolher medos e crenças familiares sobre hepatites.'],
                    'acomodacao': ['Orientar prevenção de transmissão domiciliar e vacinação de contatos.'],
                    'repadronizacao': ['Reduzir estigma e reforçar medidas efetivas de prevenção neonatal.']},
  'referencias': ['Ministério da Saúde. Hepatites virais e pré-natal.',
                  'FEBRASGO.',
                  'COFEN Resolução nº 736/2024.',
                  'OMS.',
                  'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames laboratoriais',
  'achado_clinico': 'Hepatite C reagente',
  'diagnostico': {'codigo': '10023032', 'termo': 'Infecção'},
  'resultado': {'codigo': '10028945', 'termo': 'Infecção, Ausente'},
  'intervencao': {'codigo': '10051016', 'termo': 'Orientar sobre Infecção'},
  'prioridade': 'Alta',
  'fundamentacao': 'Hepatite C reagente na gestação requer confirmação diagnóstica, avaliação de coinfecções, função '
                   'hepática e encaminhamento para seguimento. A enfermagem deve orientar prevenção de transmissão, '
                   'evitar exposição sanguínea e garantir acompanhamento materno e neonatal.',
  'transcultural': {'preservacao': ['Acolher a gestante sem julgamento.'],
                    'acomodacao': ['Adequar orientações preventivas à realidade familiar e comunitária.'],
                    'repadronizacao': ['Corrigir crenças sobre transmissão por contato casual.']},
  'referencias': ['Ministério da Saúde. Hepatites virais.',
                  'FEBRASGO.',
                  'COFEN Resolução nº 736/2024.',
                  'OMS.',
                  'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames laboratoriais',
  'achado_clinico': 'Rubéola não imune',
  'diagnostico': {'codigo': '10041093', 'termo': 'Processo do Sistema Imunológico, Prejudicado'},
  'resultado': {'codigo': '10047463', 'termo': 'Processo do Sistema Imune, Eficaz'},
  'intervencao': {'codigo': '10045079', 'termo': 'Orientar sobre Gestação'},
  'prioridade': 'Média',
  'fundamentacao': 'Rubéola não imune indica suscetibilidade. Como a vacina tríplice viral é contraindicada durante a '
                   'gestação por ser vacina de vírus vivo atenuado, deve-se orientar prevenção de exposição e '
                   'vacinação no puerpério, conforme calendário vacinal.',
  'transcultural': {'preservacao': ['Valorizar redes familiares de proteção da gestante.'],
                    'acomodacao': ['Orientar evitar contato com pessoas com exantema ou suspeita de rubéola.'],
                    'repadronizacao': ['Explicar que a vacina deve ser realizada após o parto, não durante a '
                                       'gestação.']},
  'referencias': ['Ministério da Saúde. Calendário Nacional de Vacinação.',
                  'FEBRASGO.',
                  'COFEN Resolução nº 736/2024.',
                  'OMS.',
                  'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames laboratoriais',
  'achado_clinico': 'Toxoplasmose IgM positivo',
  'diagnostico': {'codigo': '10023032', 'termo': 'Infecção'},
  'resultado': {'codigo': '10028945', 'termo': 'Infecção, Ausente'},
  'intervencao': {'codigo': '10051016', 'termo': 'Orientar sobre Infecção'},
  'prioridade': 'Alta',
  'fundamentacao': 'Toxoplasmose IgM positivo pode indicar infecção recente e risco de transmissão fetal. Deve-se '
                   'confirmar diagnóstico com sorologia complementar, avididade quando aplicável, idade gestacional, '
                   'avaliação médica e início oportuno de tratamento conforme protocolo.',
  'transcultural': {'preservacao': ['Respeitar práticas alimentares locais seguras.'],
                    'acomodacao': ['Orientar higiene dos alimentos, cozimento adequado de carnes e cuidado com solo e '
                                   'fezes de gatos.'],
                    'repadronizacao': ['Modificar consumo de carnes cruas, malpassadas ou alimentos sem higienização '
                                       'adequada.']},
  'referencias': ['Ministério da Saúde. Pré-natal de baixo risco.',
                  'FEBRASGO.',
                  'COFEN Resolução nº 736/2024.',
                  'OMS.',
                  'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames laboratoriais',
  'achado_clinico': 'Toxoplasmose suscetível',
  'diagnostico': {'codigo': '10015133', 'termo': 'Risco de Infecção'},
  'resultado': {'codigo': '10028945', 'termo': 'Infecção, Ausente'},
  'intervencao': {'codigo': '10038112', 'termo': 'Orientar sobre Prevenção de Infecção Cruzada'},
  'prioridade': 'Média',
  'fundamentacao': 'Gestante suscetível à toxoplasmose não possui imunidade e deve receber orientações preventivas '
                   'durante toda a gestação, com repetição sorológica conforme protocolo local para detecção precoce '
                   'de soroconversão.',
  'transcultural': {'preservacao': ['Manter práticas culinárias regionais seguras.'],
                    'acomodacao': ['Adequar orientação ao acesso à água tratada, alimentos e condições de preparo.'],
                    'repadronizacao': ['Reforçar lavagem de frutas e verduras, uso de água segura e evitar carne crua '
                                       'ou malcozida.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'COFEN Resolução nº 736/2024.', 'OMS.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames laboratoriais',
  'achado_clinico': 'Coombs indireto positivo',
  'diagnostico': {'codigo': '10012606', 'termo': 'Processo do Sistema Circulatório, Prejudicado'},
  'resultado': {'codigo': '10028379', 'termo': 'Processo do Sistema Circulatório, Positivo'},
  'intervencao': {'codigo': '10024625', 'termo': 'Orientar sobre Regime Terapêutico'},
  'prioridade': 'Alta',
  'fundamentacao': 'Coombs indireto positivo em gestante pode indicar aloimunização materna, com risco de doença '
                   'hemolítica fetal e neonatal. Requer avaliação especializada, monitoramento de títulos, '
                   'investigação fetal quando indicada e seguimento em pré-natal de alto risco.',
  'transcultural': {'preservacao': ['Acolher dúvidas familiares sobre incompatibilidade sanguínea.'],
                    'acomodacao': ['Explicar de forma simples a necessidade de acompanhamento especializado.'],
                    'repadronizacao': ['Evitar abandono do seguimento por ausência de sintomas maternos.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'COFEN Resolução nº 736/2024.', 'OMS.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames laboratoriais',
  'achado_clinico': 'Tipagem Rh negativo',
  'diagnostico': {'codigo': '10015146', 'termo': 'Risco de Lesão'},
  'resultado': {'codigo': '10028379', 'termo': 'Processo do Sistema Circulatório, Positivo'},
  'intervencao': {'codigo': '10024625', 'termo': 'Orientar sobre Regime Terapêutico'},
  'prioridade': 'Alta',
  'fundamentacao': 'Gestante Rh negativo necessita avaliação do fator Rh do parceiro quando disponível, Coombs '
                   'indireto e acompanhamento para prevenção de aloimunização. Quando indicado, deve receber '
                   'imunoglobulina anti-D conforme protocolo, especialmente em situações de risco e no puerpério se '
                   'recém-nascido Rh positivo.',
  'transcultural': {'preservacao': ['Respeitar dúvidas da gestante e família sobre exames de sangue.'],
                    'acomodacao': ['Orientar a importância do cartão da gestante e registro da tipagem sanguínea.'],
                    'repadronizacao': ['Corrigir a ideia de que Rh negativo é doença, explicando o risco apenas em '
                                       'situações específicas.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'COFEN Resolução nº 736/2024.', 'OMS.', 'Leininger.']}]
