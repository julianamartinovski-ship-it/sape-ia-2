# SAPE IA 2.0 — Regras clínicas de pré-natal
# Recuperadas e normalizadas a partir do acervo do projeto.

REGRAS = [{'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Ultrassonografia obstétrica não realizada',
  'diagnostico': {'codigo': '10022155', 'termo': 'Adesão ao Regime Terapêutico, Prejudicada'},
  'resultado': {'codigo': '10030185', 'termo': 'Adesão ao Regime Terapêutico'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Média',
  'fundamentacao': 'A ultrassonografia obstétrica auxilia na confirmação da idade gestacional, vitalidade fetal, '
                   'número de fetos, localização placentária, crescimento fetal e identificação de alterações. Quando '
                   'não realizada, deve-se verificar barreiras de acesso, solicitar ou encaminhar conforme protocolo e '
                   'registrar conduta.',
  'transcultural': {'preservacao': ['Valorizar a percepção da gestante sobre o desenvolvimento fetal e seus saberes '
                                    'familiares.'],
                    'acomodacao': ['Adequar o agendamento à disponibilidade de transporte, trabalho, território e rede '
                                   'de apoio.'],
                    'repadronizacao': ['Reorientar a ideia de que exame de imagem só é necessário quando há dor ou '
                                       'sangramento.']},
  'referencias': ['Ministério da Saúde. Atenção ao pré-natal de baixo risco.',
                  'FEBRASGO. Assistência pré-natal.',
                  'OMS. Recomendações sobre cuidados pré-natais.',
                  'COFEN Resolução nº 736/2024.',
                  'Leininger. Teoria Transcultural.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Ultrassonografia do primeiro trimestre não realizada',
  'diagnostico': {'codigo': '10022155', 'termo': 'Adesão ao Regime Terapêutico, Prejudicada'},
  'resultado': {'codigo': '10030185', 'termo': 'Adesão ao Regime Terapêutico'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Média',
  'fundamentacao': 'A ultrassonografia do primeiro trimestre é útil para datação gestacional, confirmação de '
                   'vitalidade, localização gestacional e identificação de gestação múltipla. A ausência desse exame '
                   'pode dificultar o acompanhamento adequado do crescimento fetal e a definição da idade gestacional.',
  'transcultural': {'preservacao': ['Acolher experiências familiares sobre confirmação da gestação.'],
                    'acomodacao': ['Explicar a finalidade do exame em linguagem simples.'],
                    'repadronizacao': ['Estimular realização oportuna de exames mesmo quando a gestante se sente '
                                       'bem.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Idade gestacional incerta',
  'diagnostico': {'codigo': '10015146', 'termo': 'Risco de Lesão'},
  'resultado': {'codigo': '10033682', 'termo': 'Estado Materno-Fetal, Eficaz'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Alta',
  'fundamentacao': 'A idade gestacional incerta compromete a interpretação do crescimento fetal, a programação de '
                   'exames, a identificação de prematuridade ou pós-datismo e a tomada de decisões obstétricas. A '
                   'ultrassonografia, especialmente quando realizada precocemente, contribui para melhor datação da '
                   'gestação.',
  'transcultural': {'preservacao': ['Acolher formas culturais de marcar datas, ciclos menstruais e eventos '
                                    'familiares.'],
                    'acomodacao': ['Reconstruir a história gestacional com apoio de marcos familiares e registros '
                                   'disponíveis.'],
                    'repadronizacao': ['Estimular registro da DUM e início precoce do pré-natal em futuras '
                                       'gestações.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Divergência entre DUM e ultrassonografia',
  'diagnostico': {'codigo': '10015146', 'termo': 'Risco de Lesão'},
  'resultado': {'codigo': '10033682', 'termo': 'Estado Materno-Fetal, Eficaz'},
  'intervencao': {'codigo': '10024625', 'termo': 'Orientar sobre Regime Terapêutico'},
  'prioridade': 'Média',
  'fundamentacao': 'Divergência entre data da última menstruação e ultrassonografia pode ocorrer por ciclos '
                   'irregulares, lembrança imprecisa da DUM ou alteração no crescimento fetal. A conduta depende da '
                   'idade gestacional, qualidade do exame e critérios obstétricos de datação.',
  'transcultural': {'preservacao': ['Respeitar a narrativa da gestante sobre seu ciclo e sinais corporais.'],
                    'acomodacao': ['Explicar que a datação pode ser ajustada por critérios clínicos e '
                                   'ultrassonográficos.'],
                    'repadronizacao': ['Evitar conclusões precipitadas sem avaliação da equipe e registro adequado.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Translucência nucal alterada',
  'diagnostico': {'codigo': '10015146', 'termo': 'Risco de Lesão'},
  'resultado': {'codigo': '10033682', 'termo': 'Estado Fetal, Eficaz'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Alta',
  'fundamentacao': 'Translucência nucal alterada pode indicar risco aumentado para aneuploidias, cardiopatias e outras '
                   'alterações fetais. Requer encaminhamento para avaliação especializada, aconselhamento, exames '
                   'complementares e seguimento conforme protocolo.',
  'transcultural': {'preservacao': ['Acolher crenças e sentimentos da família diante de possível alteração fetal.'],
                    'acomodacao': ['Garantir comunicação clara, respeitosa e sem julgamento.'],
                    'repadronizacao': ['Evitar interpretação definitiva do achado sem avaliação especializada.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Morfológica do primeiro trimestre alterada',
  'diagnostico': {'codigo': '10015146', 'termo': 'Risco de Lesão'},
  'resultado': {'codigo': '10033682', 'termo': 'Estado Fetal, Eficaz'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Alta',
  'fundamentacao': 'Alterações na ultrassonografia morfológica do primeiro trimestre podem indicar risco de anomalias '
                   'estruturais, cromossômicas ou alterações do desenvolvimento fetal. A gestante deve ser encaminhada '
                   'para avaliação especializada e acompanhamento multiprofissional.',
  'transcultural': {'preservacao': ['Acolher espiritualidade, valores familiares e necessidades emocionais.'],
                    'acomodacao': ['Explicar a necessidade de exames complementares e seguimento especializado.'],
                    'repadronizacao': ['Reforçar que um achado alterado exige investigação, não conclusão isolada.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Morfológica do segundo trimestre não realizada',
  'diagnostico': {'codigo': '10022155', 'termo': 'Adesão ao Regime Terapêutico, Prejudicada'},
  'resultado': {'codigo': '10030185', 'termo': 'Adesão ao Regime Terapêutico'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Média',
  'fundamentacao': 'A ultrassonografia morfológica do segundo trimestre avalia anatomia fetal, placenta, líquido '
                   'amniótico e crescimento. Quando não realizada no período recomendado, deve-se providenciar '
                   'agendamento ou encaminhamento conforme disponibilidade e idade gestacional.',
  'transcultural': {'preservacao': ['Valorizar o interesse da família em conhecer o desenvolvimento do bebê.'],
                    'acomodacao': ['Planejar o exame conforme acesso ao serviço e transporte.'],
                    'repadronizacao': ['Reforçar que o exame possui finalidade clínica, não apenas identificação do '
                                       'sexo fetal.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Morfológica do segundo trimestre alterada',
  'diagnostico': {'codigo': '10015146', 'termo': 'Risco de Lesão'},
  'resultado': {'codigo': '10033682', 'termo': 'Estado Fetal, Eficaz'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Alta',
  'fundamentacao': 'Alteração na morfológica do segundo trimestre pode indicar malformações fetais, alterações '
                   'placentárias, restrição de crescimento, alterações de líquido amniótico ou necessidade de '
                   'investigação complementar. Exige encaminhamento para avaliação especializada.',
  'transcultural': {'preservacao': ['Acolher medo, ansiedade e valores familiares.'],
                    'acomodacao': ['Orientar próximos passos de forma clara e respeitosa.'],
                    'repadronizacao': ['Evitar abandono do pré-natal após notícia de alteração fetal.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Placenta prévia suspeita',
  'diagnostico': {'codigo': '10003303', 'termo': 'Sangramento'},
  'resultado': {'codigo': '10028120', 'termo': 'Sangramento, Ausente'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Alta',
  'fundamentacao': 'Placenta prévia suspeita aumenta risco de sangramento vaginal, parto prematuro e necessidade de '
                   'planejamento obstétrico. A gestante deve ser encaminhada para avaliação, confirmação diagnóstica e '
                   'orientação sobre sinais de alerta.',
  'transcultural': {'preservacao': ['Acolher a gestante e sua família diante do medo de sangramento.'],
                    'acomodacao': ['Orientar repouso relativo e procura imediata em caso de sangramento conforme '
                                   'prescrição e protocolo.'],
                    'repadronizacao': ['Evitar minimizar qualquer sangramento vaginal na gestação.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Descolamento placentário suspeito',
  'diagnostico': {'codigo': '10015146', 'termo': 'Risco de Lesão'},
  'resultado': {'codigo': '10033682', 'termo': 'Estado Materno-Fetal, Eficaz'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Alta',
  'fundamentacao': 'Suspeita de descolamento placentário é emergência obstétrica, principalmente quando há dor '
                   'abdominal, hipertonia uterina, sangramento, sofrimento fetal ou instabilidade materna. Requer '
                   'encaminhamento imediato para avaliação obstétrica.',
  'transcultural': {'preservacao': ['Acolher relatos da gestante sobre dor, sangramento e percepção fetal.'],
                    'acomodacao': ['Acionar rede de apoio e transporte de urgência conforme realidade local.'],
                    'repadronizacao': ['Reforçar que dor abdominal intensa com sangramento não deve aguardar consulta '
                                       'agendada.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Restrição de crescimento fetal suspeita',
  'diagnostico': {'codigo': '10015146', 'termo': 'Risco de Lesão'},
  'resultado': {'codigo': '10033682', 'termo': 'Estado Fetal, Eficaz'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Alta',
  'fundamentacao': 'Restrição de crescimento fetal suspeita pode estar relacionada a insuficiência placentária, '
                   'hipertensão, infecções, tabagismo, desnutrição ou outras condições maternas e fetais. Exige '
                   'avaliação especializada, acompanhamento seriado do crescimento e, quando indicado, Doppler '
                   'obstétrico.',
  'transcultural': {'preservacao': ['Valorizar alimentos e práticas de cuidado seguros do território.'],
                    'acomodacao': ['Adequar orientações nutricionais e de retorno à realidade social da gestante.'],
                    'repadronizacao': ['Reforçar necessidade de acompanhamento seriado, mesmo sem sintomas maternos.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Macrossomia fetal suspeita',
  'diagnostico': {'codigo': '10015146', 'termo': 'Risco de Lesão'},
  'resultado': {'codigo': '10033682', 'termo': 'Estado Fetal, Eficaz'},
  'intervencao': {'codigo': '10024625', 'termo': 'Orientar sobre Regime Terapêutico'},
  'prioridade': 'Alta',
  'fundamentacao': 'Macrossomia fetal suspeita pode estar associada a diabetes gestacional, ganho ponderal excessivo e '
                   'risco de distocia de ombro, trauma obstétrico, cesariana e hipoglicemia neonatal. Deve-se avaliar '
                   'controle glicêmico, crescimento fetal e plano de parto.',
  'transcultural': {'preservacao': ['Respeitar crenças familiares sobre bebê grande e saúde.'],
                    'acomodacao': ['Orientar relação entre alimentação, glicemia e crescimento fetal de forma '
                                   'simples.'],
                    'repadronizacao': ['Reorientar a ideia de que bebê muito grande sempre significa gestação '
                                       'saudável.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Oligodrâmnio',
  'diagnostico': {'codigo': '10015146', 'termo': 'Risco de Lesão'},
  'resultado': {'codigo': '10033682', 'termo': 'Estado Fetal, Eficaz'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Alta',
  'fundamentacao': 'Oligodrâmnio pode estar associado a ruptura de membranas, insuficiência placentária, restrição de '
                   'crescimento fetal, malformações renais fetais ou pós-datismo. Exige avaliação obstétrica, '
                   'investigação da causa e monitoramento fetal.',
  'transcultural': {'preservacao': ['Acolher preocupações da gestante sobre líquido e vitalidade fetal.'],
                    'acomodacao': ['Orientar sinais de alerta, como perda de líquido e redução de movimentos fetais.'],
                    'repadronizacao': ['Evitar atribuir o achado apenas à baixa ingestão de água sem avaliação '
                                       'clínica.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Polidrâmnio',
  'diagnostico': {'codigo': '10015146', 'termo': 'Risco de Lesão'},
  'resultado': {'codigo': '10033682', 'termo': 'Estado Fetal, Eficaz'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Alta',
  'fundamentacao': 'Polidrâmnio pode estar associado a diabetes gestacional, malformações fetais, infecções, gestação '
                   'múltipla ou causas idiopáticas. A gestante deve ser avaliada quanto a sintomas respiratórios, '
                   'contrações, crescimento uterino aumentado e necessidade de investigação complementar.',
  'transcultural': {'preservacao': ['Acolher a interpretação da gestante sobre aumento abdominal.'],
                    'acomodacao': ['Orientar sinais de trabalho de parto prematuro e desconforto respiratório.'],
                    'repadronizacao': ['Reforçar necessidade de investigação, mesmo quando a gestante atribui o '
                                       'aumento apenas ao bebê grande.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Gestação gemelar',
  'diagnostico': {'codigo': '10015146', 'termo': 'Risco de Lesão'},
  'resultado': {'codigo': '10033682', 'termo': 'Estado Materno-Fetal, Eficaz'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Alta',
  'fundamentacao': 'Gestação gemelar apresenta maior risco de prematuridade, restrição de crescimento, anemia, '
                   'síndromes hipertensivas e complicações fetais. Requer definição de corionicidade, acompanhamento '
                   'mais frequente e, quando indicado, pré-natal de alto risco.',
  'transcultural': {'preservacao': ['Valorizar redes familiares de apoio à gestante.'],
                    'acomodacao': ['Planejar consultas, exames e transporte considerando maior risco e maior '
                                   'frequência de acompanhamento.'],
                    'repadronizacao': ['Reforçar que gestação gemelar demanda vigilância ampliada mesmo sem '
                                       'sintomas.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Apresentação pélvica',
  'diagnostico': {'codigo': '10015146', 'termo': 'Risco de Lesão'},
  'resultado': {'codigo': '10033682', 'termo': 'Estado Materno-Fetal, Eficaz'},
  'intervencao': {'codigo': '10045079', 'termo': 'Orientar sobre Gestação'},
  'prioridade': 'Média',
  'fundamentacao': 'A apresentação pélvica pode ser transitória antes do termo, mas quando persistente no final da '
                   'gestação pode influenciar planejamento do parto. A gestante deve ser orientada e acompanhada '
                   'conforme idade gestacional, vitalidade fetal e avaliação obstétrica.',
  'transcultural': {'preservacao': ['Acolher crenças sobre posição fetal e parto.'],
                    'acomodacao': ['Explicar que a posição fetal pode mudar conforme idade gestacional.'],
                    'repadronizacao': ['Evitar manobras caseiras ou práticas sem segurança para tentar mudar a posição '
                                       'fetal.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Apresentação transversa',
  'diagnostico': {'codigo': '10015146', 'termo': 'Risco de Lesão'},
  'resultado': {'codigo': '10033682', 'termo': 'Estado Materno-Fetal, Eficaz'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Alta',
  'fundamentacao': 'Apresentação transversa persistente, especialmente no final da gestação, está associada a maior '
                   'risco no parto vaginal e requer avaliação obstétrica para planejamento seguro do parto e prevenção '
                   'de complicações.',
  'transcultural': {'preservacao': ['Acolher conhecimentos familiares sobre posição do bebê.'],
                    'acomodacao': ['Orientar acompanhamento e avaliação obstétrica sem gerar culpa na gestante.'],
                    'repadronizacao': ['Evitar tentativas caseiras de mudança de posição fetal.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Doppler obstétrico alterado',
  'diagnostico': {'codigo': '10012606', 'termo': 'Processo do Sistema Circulatório, Prejudicado'},
  'resultado': {'codigo': '10028379', 'termo': 'Processo do Sistema Circulatório, Positivo'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Alta',
  'fundamentacao': 'Doppler obstétrico alterado pode indicar comprometimento da circulação uteroplacentária ou fetal, '
                   'associado a restrição de crescimento, insuficiência placentária, pré-eclâmpsia e risco fetal. '
                   'Exige avaliação especializada e vigilância materno-fetal.',
  'transcultural': {'preservacao': ['Acolher ansiedade da gestante diante de exame alterado.'],
                    'acomodacao': ['Explicar a importância do seguimento e dos retornos seriados.'],
                    'repadronizacao': ['Reforçar que ausência de sintomas maternos não exclui risco fetal.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'BCF ausente em exame',
  'diagnostico': {'codigo': '10015146', 'termo': 'Risco de Lesão'},
  'resultado': {'codigo': '10033682', 'termo': 'Estado Fetal, Eficaz'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Alta',
  'fundamentacao': 'Batimentos cardíacos fetais ausentes em exame é achado crítico e requer confirmação imediata por '
                   'avaliação obstétrica e exame apropriado, considerando idade gestacional, qualidade técnica e '
                   'condição materno-fetal.',
  'transcultural': {'preservacao': ['Acolher a gestante e família com comunicação humanizada.'],
                    'acomodacao': ['Garantir encaminhamento rápido e suporte emocional.'],
                    'repadronizacao': ['Evitar conclusões definitivas sem confirmação adequada, mas não retardar '
                                       'avaliação urgente.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Malformação fetal suspeita',
  'diagnostico': {'codigo': '10015146', 'termo': 'Risco de Lesão'},
  'resultado': {'codigo': '10033682', 'termo': 'Estado Fetal, Eficaz'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Alta',
  'fundamentacao': 'Suspeita de malformação fetal exige confirmação diagnóstica, avaliação especializada, '
                   'aconselhamento, planejamento do parto e organização da rede de cuidado neonatal quando necessário.',
  'transcultural': {'preservacao': ['Respeitar valores, espiritualidade e decisões familiares.'],
                    'acomodacao': ['Oferecer informação clara, apoio emocional e encaminhamento especializado.'],
                    'repadronizacao': ['Evitar estigmatização ou culpabilização da gestante pela alteração fetal.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Colo uterino curto',
  'diagnostico': {'codigo': '10015146', 'termo': 'Risco de Lesão'},
  'resultado': {'codigo': '10033682', 'termo': 'Estado Materno-Fetal, Eficaz'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Alta',
  'fundamentacao': 'Colo uterino curto em exame de imagem está associado a maior risco de parto prematuro, '
                   'especialmente em gestantes com história obstétrica compatível. Exige avaliação obstétrica, '
                   'estratificação de risco e condutas preventivas conforme protocolo.',
  'transcultural': {'preservacao': ['Acolher preocupações da gestante sobre repouso e parto prematuro.'],
                    'acomodacao': ['Planejar acompanhamento considerando trabalho, deslocamento e rede de apoio.'],
                    'repadronizacao': ['Reforçar que ausência de dor não exclui risco de prematuridade.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Risco de parto prematuro por imagem',
  'diagnostico': {'codigo': '10015146', 'termo': 'Risco de Lesão'},
  'resultado': {'codigo': '10033682', 'termo': 'Estado Materno-Fetal, Eficaz'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Alta',
  'fundamentacao': 'Achados de imagem como colo curto, alterações placentárias, polidrâmnio, gestação múltipla ou '
                   'sinais de insuficiência placentária podem aumentar risco de parto prematuro. A gestante deve ser '
                   'encaminhada para avaliação, vigilância e orientações de sinais de alerta.',
  'transcultural': {'preservacao': ['Reconhecer estratégias familiares para proteção da gestante.'],
                    'acomodacao': ['Construir plano de deslocamento e busca de atendimento em caso de contrações, '
                                   'sangramento ou perda de líquido.'],
                    'repadronizacao': ['Reorientar a prática de aguardar melhora espontânea diante de sinais de '
                                       'prematuridade.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Crescimento fetal discordante',
  'diagnostico': {'codigo': '10015146', 'termo': 'Risco de Lesão'},
  'resultado': {'codigo': '10033682', 'termo': 'Estado Fetal, Eficaz'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Alta',
  'fundamentacao': 'Crescimento fetal discordante pode indicar restrição de crescimento, erro de datação, '
                   'insuficiência placentária ou complicações em gestação múltipla. Requer avaliação seriada, revisão '
                   'da idade gestacional e acompanhamento especializado.',
  'transcultural': {'preservacao': ['Valorizar a percepção materna sobre crescimento abdominal e movimentos fetais.'],
                    'acomodacao': ['Orientar necessidade de retornos e exames seriados.'],
                    'repadronizacao': ['Evitar considerar apenas o tamanho da barriga como indicador confiável de '
                                       'crescimento fetal.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Circular de cordão descrita',
  'diagnostico': {'codigo': '10015146', 'termo': 'Risco de Lesão'},
  'resultado': {'codigo': '10033682', 'termo': 'Estado Fetal, Eficaz'},
  'intervencao': {'codigo': '10045079', 'termo': 'Orientar sobre Gestação'},
  'prioridade': 'Baixa',
  'fundamentacao': 'Circular de cordão é achado ultrassonográfico frequente e, isoladamente, geralmente não define via '
                   'de parto nem indica sofrimento fetal. Deve-se orientar a gestante, reduzir ansiedade e reforçar '
                   'observação dos movimentos fetais e acompanhamento habitual.',
  'transcultural': {'preservacao': ['Acolher crenças familiares sobre cordão umbilical e risco ao bebê.'],
                    'acomodacao': ['Explicar de forma simples quando o achado exige ou não preocupação adicional.'],
                    'repadronizacao': ['Reorientar a ideia de que circular de cordão isolada sempre exige cesariana.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Líquido amniótico alterado',
  'diagnostico': {'codigo': '10015146', 'termo': 'Risco de Lesão'},
  'resultado': {'codigo': '10033682', 'termo': 'Estado Fetal, Eficaz'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Alta',
  'fundamentacao': 'Alteração do líquido amniótico, seja por redução ou aumento, pode estar relacionada a ruptura de '
                   'membranas, diabetes, malformações, restrição de crescimento, infecção ou alterações placentárias. '
                   'Exige avaliação obstétrica e definição da causa.',
  'transcultural': {'preservacao': ['Acolher preocupações e interpretações culturais sobre líquido amniótico.'],
                    'acomodacao': ['Orientar sinais de alerta, como perda de líquido, contrações e redução de '
                                   'movimentos fetais.'],
                    'repadronizacao': ['Evitar condutas caseiras isoladas sem avaliação clínica.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Necessidade de repetir ultrassonografia',
  'diagnostico': {'codigo': '10024625', 'termo': 'Regime Terapêutico, Prejudicado'},
  'resultado': {'codigo': '10030185', 'termo': 'Adesão ao Regime Terapêutico'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Média',
  'fundamentacao': 'A repetição da ultrassonografia pode ser necessária por exame inconclusivo, idade gestacional '
                   'inadequada, dificuldade técnica, necessidade de acompanhar crescimento fetal, líquido amniótico, '
                   'placenta ou achados suspeitos. Deve-se orientar a finalidade da repetição e garantir seguimento.',
  'transcultural': {'preservacao': ['Acolher dúvidas sobre por que repetir um exame já realizado.'],
                    'acomodacao': ['Planejar repetição conforme acesso, transporte e disponibilidade do serviço.'],
                    'repadronizacao': ['Reforçar que repetir o exame não significa necessariamente gravidade, mas '
                                       'necessidade de melhor avaliação.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Dificuldade de acesso ao exame de imagem',
  'diagnostico': {'codigo': '10025806', 'termo': 'Comportamento de Saúde, Prejudicado'},
  'resultado': {'codigo': '10028276', 'termo': 'Comportamento de Saúde, Positivo'},
  'intervencao': {'codigo': '10035331', 'termo': 'Encaminhar para Serviço de Saúde'},
  'prioridade': 'Alta',
  'fundamentacao': 'A dificuldade de acesso ao exame de imagem pode atrasar diagnóstico, estratificação de risco e '
                   'planejamento obstétrico. A equipe deve articular regulação, transporte sanitário, busca ativa e '
                   'priorização conforme risco gestacional.',
  'transcultural': {'preservacao': ['Reconhecer barreiras territoriais, econômicas, ribeirinhas, rurais ou '
                                    'familiares.'],
                    'acomodacao': ['Adequar agendamento aos dias de deslocamento, consulta e disponibilidade da rede.'],
                    'repadronizacao': ['Reorganizar o cuidado para reduzir iniquidades de acesso e perda de '
                                       'seguimento.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']},
 {'linha_cuidado': 'Pré-natal',
  'categoria': 'Exames de imagem',
  'achado_clinico': 'Exame de imagem atrasado',
  'diagnostico': {'codigo': '10022155', 'termo': 'Adesão ao Regime Terapêutico, Prejudicada'},
  'resultado': {'codigo': '10030185', 'termo': 'Adesão ao Regime Terapêutico'},
  'intervencao': {'codigo': '10024625', 'termo': 'Orientar sobre Regime Terapêutico'},
  'prioridade': 'Média',
  'fundamentacao': 'Exame de imagem atrasado pode reduzir a utilidade clínica de avaliações dependentes da idade '
                   'gestacional, como datação precoce, rastreamento morfológico e monitoramento do crescimento fetal. '
                   'Deve-se reagendar, priorizar conforme risco e registrar justificativa.',
  'transcultural': {'preservacao': ['Acolher dificuldades reais que levaram ao atraso.'],
                    'acomodacao': ['Pactuar novo plano viável de realização do exame.'],
                    'repadronizacao': ['Reforçar a importância de realizar exames dentro da janela recomendada quando '
                                       'possível.']},
  'referencias': ['Ministério da Saúde.', 'FEBRASGO.', 'OMS.', 'COFEN Resolução nº 736/2024.', 'Leininger.']}]
