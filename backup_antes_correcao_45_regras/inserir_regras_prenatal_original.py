import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "banco_dados" / "cipe.db"

regras_prenatal = [
    ("Pré-natal", "Hipertensão arterial", "Pressão arterial alterada", "Pressão arterial controlada", "Monitorar pressão arterial", "Alta", "Gestante com pressão arterial elevada requer avaliação de risco gestacional."),
    ("Pré-natal", "Proteinúria", "Risco de condição hipertensiva na gestação", "Risco reduzido", "Avaliar sinais de gravidade", "Alta", "Proteinúria associada à hipertensão pode indicar risco de pré-eclâmpsia."),
    ("Pré-natal", "Cefaleia persistente", "Risco de condição hipertensiva na gestação", "Estado neurológico preservado", "Encaminhar conforme protocolo de risco gestacional", "Alta", "Cefaleia persistente em gestante exige avaliação clínica imediata."),
    ("Pré-natal", "Corrimento vaginal", "Corrimento vaginal", "Conforto melhorado", "Avaliar características do corrimento vaginal", "Média", "Corrimento vaginal deve ser avaliado conforme sinais associados e protocolo de IST/vulvovaginites."),
    ("Pré-natal", "Prurido vaginal", "Prurido genital", "Conforto melhorado", "Orientar higiene íntima", "Média", "Prurido associado a corrimento pode indicar vulvovaginite."),
    ("Pré-natal", "Área descoberta pela ESF", "Acesso ao serviço de saúde prejudicado", "Acesso ao cuidado melhorado", "Organizar seguimento do pré-natal", "Alta", "Dificuldade de acesso exige planejamento do cuidado e seguimento longitudinal."),
]

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("DELETE FROM regras_clinicas_cipe WHERE linha_cuidado = 'Pré-natal'")

cur.executemany("""
    INSERT INTO regras_clinicas_cipe
    (linha_cuidado, achado_clinico, codigo_diagnostico, codigo_resultado, codigo_intervencao, prioridade, justificativa)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", regras_prenatal)

conn.commit()
conn.close()

print("Regras clínicas de pré-natal inseridas com sucesso.")
print("Total inserido:", len(regras_prenatal))"""
SAPE IA 2.0
Regras Clínicas - Pré-natal
Categoria: Captação e Vínculo
"""

REGRAS = [

    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Captação e vínculo",

        "achado_clinico": "Início tardio do pré-natal",

        "diagnostico": {
            "codigo": None,
            "termo": "Adesão ao cuidado prejudicada"
        },

        "resultado": {
            "codigo": None,
            "termo": "Adesão ao cuidado melhorada"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Organizar plano de seguimento do pré-natal"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "O início tardio do pré-natal dificulta o rastreamento oportuno de fatores de risco, o vínculo com a equipe e a prevenção de agravos maternos e fetais.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Adequar agenda conforme realidade territorial e familiar da gestante."
            ],

            "repadronizacao": [
                "Reorganizar plano de cuidado garantindo consultas mínimas e exames essenciais."
            ]
        },

        "referencias": [
            "Ministério da Saúde. Atenção ao Pré-Natal de Baixo Risco.",
            "COFEN Resolução nº 736/2024.",
            "Leininger. Teoria Transcultural do Cuidado."
        ]
    },

    {
        "linha_cuidado": "Pré-natal",

        "categoria": "Captação e vínculo",

        "achado_clinico": "Gestante faltosa",

        "diagnostico": {
            "codigo": None,
            "termo": "Continuidade do cuidado prejudicada"
        },

        "resultado": {
            "codigo": None,
            "termo": "Continuidade do cuidado melhorada"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Realizar busca ativa da gestante"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "A ausência nas consultas compromete a vigilância clínica materna e fetal e aumenta o risco de perda de oportunidades diagnósticas.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Investigar barreiras familiares, culturais, econômicas e territoriais."
            ],

            "repadronizacao": [
                "Planejar busca ativa juntamente com ACS e equipe multiprofissional."
            ]
        },

        "referencias": [
            "PNAB.",
            "COFEN Resolução nº 736/2024.",
            "Leininger."
        ]
    },

    {
        "linha_cuidado": "Pré-natal",

        "categoria": "Captação e vínculo",

        "achado_clinico": "Área descoberta pela ESF",

        "diagnostico": {
            "codigo": None,
            "termo": "Acesso ao serviço de saúde prejudicado"
        },

        "resultado": {
            "codigo": None,
            "termo": "Acesso ao cuidado melhorado"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Organizar seguimento do pré-natal"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "A ausência de cobertura regular da ESF compromete a longitudinalidade do cuidado.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Considerar lideranças comunitárias e formas locais de comunicação."
            ],

            "repadronizacao": [
                "Articular plano alternativo de acompanhamento pela UBS."
            ]
        },

        "referencias": [
            "PNAB.",
            "Leininger."
        ]
    },

    {
        "linha_cuidado": "Pré-natal",

        "categoria": "Captação e vínculo",

        "achado_clinico": "Longa distância até a UBS",

        "diagnostico": {
            "codigo": None,
            "termo": "Acesso ao serviço de saúde prejudicado"
        },

        "resultado": {
            "codigo": None,
            "termo": "Acesso ao cuidado melhorado"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Planejar retorno conforme possibilidade de deslocamento"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "Barreiras geográficas dificultam a continuidade do acompanhamento pré-natal.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Adequar cronograma conforme logística territorial."
            ],

            "repadronizacao": [
                "Concentrar exames e procedimentos na mesma consulta."
            ]
        },

        "referencias": [
            "PNAB.",
            "Leininger."
        ]
    },

    {
        "linha_cuidado": "Pré-natal",

        "categoria": "Captação e vínculo",

        "achado_clinico": "Transporte fluvial",

        "diagnostico": {
            "codigo": None,
            "termo": "Acesso ao serviço de saúde prejudicado"
        },

        "resultado": {
            "codigo": None,
            "termo": "Continuidade do cuidado melhorada"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Planejar consultas conforme logística fluvial"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "A logística fluvial interfere no acesso oportuno ao cuidado.",

        "transcultural": {

            "preservacao": [
                "Reconhecer o modo de vida ribeirinho."
            ],

            "acomodacao": [
                "Adequar consultas conforme disponibilidade das embarcações."
            ],

            "repadronizacao": [
                "Criar plano para situações de urgência obstétrica."
            ]
        },

        "referencias": [
            "Leininger.",
            "PNAB."
        ]
    }

]"""
SAPE IA 2.0
Regras Clínicas - Pré-natal
Categoria: Captação e Vínculo
"""

REGRAS = [

    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Captação e vínculo",

        "achado_clinico": "Início tardio do pré-natal",

        "diagnostico": {
            "codigo": None,
            "termo": "Adesão ao cuidado prejudicada"
        },

        "resultado": {
            "codigo": None,
            "termo": "Adesão ao cuidado melhorada"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Organizar plano de seguimento do pré-natal"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "O início tardio do pré-natal dificulta o rastreamento oportuno de fatores de risco, o vínculo com a equipe e a prevenção de agravos maternos e fetais.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Adequar agenda conforme realidade territorial e familiar da gestante."
            ],

            "repadronizacao": [
                "Reorganizar plano de cuidado garantindo consultas mínimas e exames essenciais."
            ]
        },

        "referencias": [
            "Ministério da Saúde. Atenção ao Pré-Natal de Baixo Risco.",
            "COFEN Resolução nº 736/2024.",
            "Leininger. Teoria Transcultural do Cuidado."
        ]
    },

    {
        "linha_cuidado": "Pré-natal",

        "categoria": "Captação e vínculo",

        "achado_clinico": "Gestante faltosa",

        "diagnostico": {
            "codigo": None,
            "termo": "Continuidade do cuidado prejudicada"
        },

        "resultado": {
            "codigo": None,
            "termo": "Continuidade do cuidado melhorada"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Realizar busca ativa da gestante"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "A ausência nas consultas compromete a vigilância clínica materna e fetal e aumenta o risco de perda de oportunidades diagnósticas.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Investigar barreiras familiares, culturais, econômicas e territoriais."
            ],

            "repadronizacao": [
                "Planejar busca ativa juntamente com ACS e equipe multiprofissional."
            ]
        },

        "referencias": [
            "PNAB.",
            "COFEN Resolução nº 736/2024.",
            "Leininger."
        ]
    },

    {
        "linha_cuidado": "Pré-natal",

        "categoria": "Captação e vínculo",

        "achado_clinico": "Área descoberta pela ESF",

        "diagnostico": {
            "codigo": None,
            "termo": "Acesso ao serviço de saúde prejudicado"
        },

        "resultado": {
            "codigo": None,
            "termo": "Acesso ao cuidado melhorado"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Organizar seguimento do pré-natal"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "A ausência de cobertura regular da ESF compromete a longitudinalidade do cuidado.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Considerar lideranças comunitárias e formas locais de comunicação."
            ],

            "repadronizacao": [
                "Articular plano alternativo de acompanhamento pela UBS."
            ]
        },

        "referencias": [
            "PNAB.",
            "Leininger."
        ]
    },

    {
        "linha_cuidado": "Pré-natal",

        "categoria": "Captação e vínculo",

        "achado_clinico": "Longa distância até a UBS",

        "diagnostico": {
            "codigo": None,
            "termo": "Acesso ao serviço de saúde prejudicado"
        },

        "resultado": {
            "codigo": None,
            "termo": "Acesso ao cuidado melhorado"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Planejar retorno conforme possibilidade de deslocamento"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "Barreiras geográficas dificultam a continuidade do acompanhamento pré-natal.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Adequar cronograma conforme logística territorial."
            ],

            "repadronizacao": [
                "Concentrar exames e procedimentos na mesma consulta."
            ]
        },

        "referencias": [
            "PNAB.",
            "Leininger."
        ]
    },

    {
        "linha_cuidado": "Pré-natal",

        "categoria": "Captação e vínculo",

        "achado_clinico": "Transporte fluvial",

        "diagnostico": {
            "codigo": None,
            "termo": "Acesso ao serviço de saúde prejudicado"
        },

        "resultado": {
            "codigo": None,
            "termo": "Continuidade do cuidado melhorada"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Planejar consultas conforme logística fluvial"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "A logística fluvial interfere no acesso oportuno ao cuidado.",

        "transcultural": {

            "preservacao": [
                "Reconhecer o modo de vida ribeirinho."
            ],

            "acomodacao": [
                "Adequar consultas conforme disponibilidade das embarcações."
            ],

            "repadronizacao": [
                "Criar plano para situações de urgência obstétrica."
            ]
        },

        "referencias": [
            "Leininger.",
            "PNAB."
        ]
    }

]"""
SAPE IA 2.0
Regras Clínicas - Pré-natal
Categoria: Captação e Vínculo
"""

REGRAS = [

    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Captação e vínculo",

        "achado_clinico": "Início tardio do pré-natal",

        "diagnostico": {
            "codigo": None,
            "termo": "Adesão ao cuidado prejudicada"
        },

        "resultado": {
            "codigo": None,
            "termo": "Adesão ao cuidado melhorada"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Organizar plano de seguimento do pré-natal"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "O início tardio do pré-natal dificulta o rastreamento oportuno de fatores de risco, o vínculo com a equipe e a prevenção de agravos maternos e fetais.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Adequar agenda conforme realidade territorial e familiar da gestante."
            ],

            "repadronizacao": [
                "Reorganizar plano de cuidado garantindo consultas mínimas e exames essenciais."
            ]
        },

        "referencias": [
            "Ministério da Saúde. Atenção ao Pré-Natal de Baixo Risco.",
            "COFEN Resolução nº 736/2024.",
            "Leininger. Teoria Transcultural do Cuidado."
        ]
    },

    {
        "linha_cuidado": "Pré-natal",

        "categoria": "Captação e vínculo",

        "achado_clinico": "Gestante faltosa",

        "diagnostico": {
            "codigo": None,
            "termo": "Continuidade do cuidado prejudicada"
        },

        "resultado": {
            "codigo": None,
            "termo": "Continuidade do cuidado melhorada"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Realizar busca ativa da gestante"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "A ausência nas consultas compromete a vigilância clínica materna e fetal e aumenta o risco de perda de oportunidades diagnósticas.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Investigar barreiras familiares, culturais, econômicas e territoriais."
            ],

            "repadronizacao": [
                "Planejar busca ativa juntamente com ACS e equipe multiprofissional."
            ]
        },

        "referencias": [
            "PNAB.",
            "COFEN Resolução nº 736/2024.",
            "Leininger."
        ]
    },

    {
        "linha_cuidado": "Pré-natal",

        "categoria": "Captação e vínculo",

        "achado_clinico": "Área descoberta pela ESF",

        "diagnostico": {
            "codigo": None,
            "termo": "Acesso ao serviço de saúde prejudicado"
        },

        "resultado": {
            "codigo": None,
            "termo": "Acesso ao cuidado melhorado"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Organizar seguimento do pré-natal"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "A ausência de cobertura regular da ESF compromete a longitudinalidade do cuidado.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Considerar lideranças comunitárias e formas locais de comunicação."
            ],

            "repadronizacao": [
                "Articular plano alternativo de acompanhamento pela UBS."
            ]
        },

        "referencias": [
            "PNAB.",
            "Leininger."
        ]
    },

    {
        "linha_cuidado": "Pré-natal",

        "categoria": "Captação e vínculo",

        "achado_clinico": "Longa distância até a UBS",

        "diagnostico": {
            "codigo": None,
            "termo": "Acesso ao serviço de saúde prejudicado"
        },

        "resultado": {
            "codigo": None,
            "termo": "Acesso ao cuidado melhorado"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Planejar retorno conforme possibilidade de deslocamento"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "Barreiras geográficas dificultam a continuidade do acompanhamento pré-natal.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Adequar cronograma conforme logística territorial."
            ],

            "repadronizacao": [
                "Concentrar exames e procedimentos na mesma consulta."
            ]
        },

        "referencias": [
            "PNAB.",
            "Leininger."
        ]
    },

    {
        "linha_cuidado": "Pré-natal",

        "categoria": "Captação e vínculo",

        "achado_clinico": "Transporte fluvial",

        "diagnostico": {
            "codigo": None,
            "termo": "Acesso ao serviço de saúde prejudicado"
        },

        "resultado": {
            "codigo": None,
            "termo": "Continuidade do cuidado melhorada"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Planejar consultas conforme logística fluvial"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "A logística fluvial interfere no acesso oportuno ao cuidado.",

        "transcultural": {

            "preservacao": [
                "Reconhecer o modo de vida ribeirinho."
            ],

            "acomodacao": [
                "Adequar consultas conforme disponibilidade das embarcações."
            ],

            "repadronizacao": [
                "Criar plano para situações de urgência obstétrica."
            ]
        },

        "referencias": [
            "Leininger.",
            "PNAB."
        ]
    }

]"""
SAPE IA 2.0
Regras Clínicas - Pré-natal
Categoria: Fatores de risco gestacional
"""

REGRAS = [
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Hipertensão arterial",
        "diagnostico": {"codigo": None, "termo": "Pressão arterial alterada"},
        "resultado": {"codigo": None, "termo": "Pressão arterial controlada"},
        "intervencao": {"codigo": None, "termo": "Monitorar pressão arterial"},
        "prioridade": "Alta",
        "fundamentacao": "Pressão arterial elevada na gestação exige avaliação de risco para síndromes hipertensivas.",
        "transcultural": {
            "preservacao": [],
            "acomodacao": ["Adequar monitoramento conforme acesso da gestante ao serviço."],
            "repadronizacao": ["Criar plano de urgência para sinais de pré-eclâmpsia."]
        },
        "referencias": ["Ministério da Saúde.", "Manual de Gestação de Alto Risco.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Proteinúria",
        "diagnostico": {"codigo": None, "termo": "Risco de condição hipertensiva na gestação"},
        "resultado": {"codigo": None, "termo": "Risco reduzido"},
        "intervencao": {"codigo": None, "termo": "Avaliar sinais de gravidade"},
        "prioridade": "Alta",
        "fundamentacao": "Proteinúria associada à hipertensão pode indicar pré-eclâmpsia.",
        "transcultural": {
            "preservacao": [],
            "acomodacao": ["Orientar sinais de alerta com linguagem adequada ao contexto cultural."],
            "repadronizacao": ["Encaminhar conforme risco e organizar transporte se necessário."]
        },
        "referencias": ["Ministério da Saúde.", "Manual de Gestação de Alto Risco.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Cefaleia persistente",
        "diagnostico": {"codigo": None, "termo": "Risco de condição hipertensiva na gestação"},
        "resultado": {"codigo": None, "termo": "Segurança materno-fetal preservada"},
        "intervencao": {"codigo": None, "termo": "Encaminhar para avaliação conforme protocolo de risco gestacional"},
        "prioridade": "Alta",
        "fundamentacao": "Cefaleia persistente pode ser sinal de gravidade em síndromes hipertensivas.",
        "transcultural": {
            "preservacao": [],
            "acomodacao": ["Verificar práticas locais de autocuidado já utilizadas."],
            "repadronizacao": ["Orientar procura imediata do serviço diante de piora ou sinais associados."]
        },
        "referencias": ["Ministério da Saúde.", "Manual de Gestação de Alto Risco.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Escotomas visuais",
        "diagnostico": {"codigo": None, "termo": "Risco de condição hipertensiva na gestação"},
        "resultado": {"codigo": None, "termo": "Segurança materno-fetal preservada"},
        "intervencao": {"codigo": None, "termo": "Encaminhar para avaliação imediata"},
        "prioridade": "Alta",
        "fundamentacao": "Alterações visuais na gestação são sinais de alerta para agravamento hipertensivo.",
        "transcultural": {
            "preservacao": [],
            "acomodacao": ["Explicar a gravidade usando linguagem simples."],
            "repadronizacao": ["Priorizar remoção/encaminhamento mesmo diante de barreiras territoriais."]
        },
        "referencias": ["Ministério da Saúde.", "Manual de Gestação de Alto Risco.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Edema importante",
        "diagnostico": {"codigo": None, "termo": "Risco de pré-eclâmpsia"},
        "resultado": {"codigo": None, "termo": "Risco reduzido"},
        "intervencao": {"codigo": None, "termo": "Avaliar pressão arterial e proteinúria"},
        "prioridade": "Alta",
        "fundamentacao": "Edema importante associado a outros sinais pode indicar agravamento clínico.",
        "transcultural": {
            "preservacao": [],
            "acomodacao": ["Investigar percepção cultural sobre edema na gestação."],
            "repadronizacao": ["Reforçar sinais de alerta e necessidade de avaliação imediata."]
        },
        "referencias": ["Ministério da Saúde.", "Manual de Gestação de Alto Risco.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Glicemia alterada",
        "diagnostico": {"codigo": None, "termo": "Risco de glicemia alterada"},
        "resultado": {"codigo": None, "termo": "Glicemia controlada"},
        "intervencao": {"codigo": None, "termo": "Orientar acompanhamento glicêmico conforme protocolo"},
        "prioridade": "Alta",
        "fundamentacao": "Alterações glicêmicas na gestação exigem rastreamento e acompanhamento de diabetes gestacional.",
        "transcultural": {
            "preservacao": ["Reconhecer hábitos alimentares regionais."],
            "acomodacao": ["Adaptar orientação alimentar à disponibilidade local de alimentos."],
            "repadronizacao": ["Reorganizar plano alimentar quando houver risco metabólico."]
        },
        "referencias": ["Ministério da Saúde.", "Manual de Gestação de Alto Risco.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Diabetes gestacional",
        "diagnostico": {"codigo": None, "termo": "Glicemia alterada"},
        "resultado": {"codigo": None, "termo": "Glicemia controlada"},
        "intervencao": {"codigo": None, "termo": "Acompanhar controle glicêmico"},
        "prioridade": "Alta",
        "fundamentacao": "Diabetes gestacional requer acompanhamento contínuo para redução de riscos materno-fetais.",
        "transcultural": {
            "preservacao": ["Valorizar práticas alimentares seguras da família."],
            "acomodacao": ["Negociar mudanças alimentares possíveis no contexto socioeconômico."],
            "repadronizacao": ["Encaminhar e intensificar acompanhamento conforme risco."]
        },
        "referencias": ["Ministério da Saúde.", "Manual de Gestação de Alto Risco.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Anemia",
        "diagnostico": {"codigo": None, "termo": "Hemoglobina diminuída"},
        "resultado": {"codigo": None, "termo": "Hemoglobina melhorada"},
        "intervencao": {"codigo": None, "termo": "Orientar suplementação de ferro"},
        "prioridade": "Média",
        "fundamentacao": "Anemia gestacional pode comprometer o bem-estar materno-fetal e deve ser acompanhada.",
        "transcultural": {
            "preservacao": ["Considerar alimentos regionais ricos em ferro."],
            "acomodacao": ["Orientar alimentação conforme disponibilidade local."],
            "repadronizacao": ["Reforçar adesão à suplementação quando houver risco."]
        },
        "referencias": ["Ministério da Saúde.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Obesidade",
        "diagnostico": {"codigo": None, "termo": "Peso corporal aumentado"},
        "resultado": {"codigo": None, "termo": "Peso corporal adequado"},
        "intervencao": {"codigo": None, "termo": "Orientar alimentação saudável"},
        "prioridade": "Média",
        "fundamentacao": "Obesidade na gestação aumenta risco de hipertensão, diabetes gestacional e complicações obstétricas.",
        "transcultural": {
            "preservacao": ["Reconhecer hábitos alimentares familiares."],
            "acomodacao": ["Negociar mudanças possíveis sem desconsiderar cultura alimentar."],
            "repadronizacao": ["Reorganizar plano alimentar e atividade física conforme risco."]
        },
        "referencias": ["Ministério da Saúde.", "Manual de Gestação de Alto Risco.", "Leininger."]
    },

    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Baixo peso",
        "diagnostico": {"codigo": None, "termo": "Peso corporal diminuído"},
        "resultado": {"codigo": None, "termo": "Estado nutricional melhorado"},
        "intervencao": {"codigo": None, "termo": "Orientar alimentação adequada"},
        "prioridade": "Média",
        "fundamentacao": "Baixo peso gestacional pode estar associado a vulnerabilidade nutricional e risco fetal.",
        "transcultural": {
            "preservacao": ["Considerar alimentos culturalmente aceitos."],
            "acomodacao": ["Ajustar plano alimentar à renda e disponibilidade local."],
            "repadronizacao": ["Articular apoio alimentar quando houver insegurança alimentar."]
        },
        "referencias": ["Ministério da Saúde.", "Leininger.", "PNAB."]
    },

    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Tabagismo",
        "diagnostico": {"codigo": None, "termo": "Comportamento de saúde prejudicado"},
        "resultado": {"codigo": None, "termo": "Comportamento de saúde melhorado"},
        "intervencao": {"codigo": None, "termo": "Orientar cessação do tabagismo"},
        "prioridade": "Alta",
        "fundamentacao": "Tabagismo na gestação aumenta risco de complicações maternas e fetais.",
        "transcultural": {
            "preservacao": [],
            "acomodacao": ["Investigar contexto familiar e social do uso de tabaco."],
            "repadronizacao": ["Construir plano gradual de redução e cessação."]
        },
        "referencias": ["Ministério da Saúde.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Uso de álcool",
        "diagnostico": {"codigo": None, "termo": "Comportamento de saúde prejudicado"},
        "resultado": {"codigo": None, "termo": "Comportamento de saúde melhorado"},
        "intervencao": {"codigo": None, "termo": "Orientar interrupção do uso de álcool"},
        "prioridade": "Alta",
        "fundamentacao": "O uso de álcool na gestação representa risco para o desenvolvimento fetal.",
        "transcultural": {
            "preservacao": [],
            "acomodacao": ["Avaliar contexto social e familiar relacionado ao uso."],
            "repadronizacao": ["Encaminhar para rede de apoio quando houver uso persistente."]
        },
        "referencias": ["Ministério da Saúde.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Uso de drogas",
        "diagnostico": {"codigo": None, "termo": "Comportamento de saúde prejudicado"},
        "resultado": {"codigo": None, "termo": "Comportamento de saúde melhorado"},
        "intervencao": {"codigo": None, "termo": "Encaminhar para cuidado compartilhado em saúde mental"},
        "prioridade": "Alta",
        "fundamentacao": "Uso de substâncias psicoativas na gestação exige cuidado multiprofissional e redução de danos.",
        "transcultural": {
            "preservacao": [],
            "acomodacao": ["Realizar escuta qualificada sem julgamento."],
            "repadronizacao": ["Articular rede de saúde mental, assistência social e pré-natal de alto risco."]
        },
        "referencias": ["Ministério da Saúde.", "Rede de Atenção Psicossocial.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Idade materna menor que 15 anos",
        "diagnostico": {"codigo": None, "termo": "Risco materno-fetal aumentado"},
        "resultado": {"codigo": None, "termo": "Risco materno-fetal reduzido"},
        "intervencao": {"codigo": None, "termo": "Encaminhar para acompanhamento de pré-natal de alto risco"},
        "prioridade": "Alta",
        "fundamentacao": "Gestação em adolescente muito jovem requer avaliação ampliada de risco clínico, social e familiar.",
        "transcultural": {
            "preservacao": [],
            "acomodacao": ["Avaliar apoio familiar, vínculo escolar e proteção social."],
            "repadronizacao": ["Acionar rede de proteção quando necessário."]
        },
        "referencias": ["Ministério da Saúde.", "ECA.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Idade materna maior ou igual a 35 anos",
        "diagnostico": {"codigo": None, "termo": "Risco materno-fetal aumentado"},
        "resultado": {"codigo": None, "termo": "Risco materno-fetal reduzido"},
        "intervencao": {"codigo": None, "termo": "Avaliar fatores de risco gestacional"},
        "prioridade": "Média",
        "fundamentacao": "Idade materna avançada pode estar associada a maior risco obstétrico e comorbidades.",
        "transcultural": {
            "preservacao": [],
            "acomodacao": ["Considerar história reprodutiva, rede de apoio e expectativas familiares."],
            "repadronizacao": ["Intensificar acompanhamento se houver comorbidades."]
        },
        "referencias": ["Ministério da Saúde.", "Manual de Gestação de Alto Risco.", "Leininger."]
    }
]REGRAS = [
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Vacinação",
        "achado_clinico": "Situação vacinal desconhecida",
        "diagnostico": {"codigo": None, "termo": "Situação vacinal prejudicada"},
        "resultado": {"codigo": None, "termo": "Situação vacinal avaliada e atualizada"},
        "intervencao": {"codigo": None, "termo": "Avaliar situação vacinal da gestante"},
        "prioridade": "Alta",
        "fundamentacao": "Na primeira consulta de pré-natal, a situação vacinal deve ser verificada por meio do cartão de vacina, registros disponíveis e relato da gestante. Quando não houver comprovação, deve-se considerar esquema desconhecido e organizar a atualização vacinal conforme o Calendário Nacional de Vacinação da Gestante, incluindo hepatite B, dT, influenza, COVID-19 e dTpa a partir da 20ª semana gestacional.",
        "transcultural": {
            "preservacao": [
                "Valorizar práticas familiares de cuidado que favoreçam a proteção da gestante e do bebê.",
                "Manter diálogo respeitoso sobre experiências prévias com vacinação."
            ],
            "acomodacao": [
                "Adequar a orientação ao grau de escolaridade, idioma, cultura e contexto territorial da gestante.",
                "Negociar datas de vacinação compatíveis com deslocamento, trabalho, transporte e rotina familiar."
            ],
            "repadronizacao": [
                "Reformular crenças equivocadas sobre vacinas por meio de educação em saúde clara, respeitosa e baseada em evidências.",
                "Estimular a reconstrução do cuidado pré-natal com inclusão do cartão vacinal como documento essencial."
            ]
        },
        "referencias": [
            "Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.",
            "Programa Nacional de Imunizações - PNI.",
            "COFEN Resolução nº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Vacinação",
        "achado_clinico": "Vacina dT incompleta",
        "diagnostico": {"codigo": None, "termo": "Risco de imunização incompleta contra difteria e tétano"},
        "resultado": {"codigo": None, "termo": "Esquema vacinal contra difteria e tétano completado"},
        "intervencao": {"codigo": None, "termo": "Completar esquema vacinal com dT conforme histórico vacinal"},
        "prioridade": "Alta",
        "fundamentacao": "A vacina dT é indicada na gestação conforme histórico vacinal, com objetivo de proteger contra difteria e tétano. Em esquema incompleto, não se reinicia o esquema; devem ser completadas as doses necessárias, respeitando intervalos recomendados e articulando a administração da dTpa a partir da 20ª semana gestacional.",
        "transcultural": {
            "preservacao": [
                "Reconhecer saberes familiares sobre prevenção de doenças e proteção materno-infantil."
            ],
            "acomodacao": [
                "Explicar o esquema em linguagem simples, utilizando o cartão vacinal como ferramenta visual.",
                "Ajustar o agendamento das doses conforme disponibilidade da gestante e da sala de vacina."
            ],
            "repadronizacao": [
                "Corrigir a ideia de que doses antigas tornam desnecessária a atualização vacinal.",
                "Fortalecer a adesão ao esquema completo como cuidado de proteção materna e neonatal."
            ]
        },
        "referencias": [
            "Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.",
            "Programa Nacional de Imunizações - PNI.",
            "COFEN Resolução nº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Vacinação",
        "achado_clinico": "Vacina dTpa indicada",
        "diagnostico": {"codigo": None, "termo": "Necessidade de imunização contra difteria, tétano e coqueluche"},
        "resultado": {"codigo": None, "termo": "Gestante imunizada com dTpa"},
        "intervencao": {"codigo": None, "termo": "Administrar ou encaminhar para vacina dTpa a partir da 20ª semana gestacional"},
        "prioridade": "Alta",
        "fundamentacao": "A vacina dTpa é indicada em cada gestação a partir da 20ª semana gestacional, independentemente de vacinação prévia, com objetivo de reduzir o risco de tétano neonatal e coqueluche no recém-nascido por transferência transplacentária de anticorpos.",
        "transcultural": {
            "preservacao": [
                "Valorizar o desejo materno e familiar de proteger o recém-nascido."
            ],
            "acomodacao": [
                "Orientar que a vacina é recomendada em cada gestação, mesmo que tenha sido realizada em gestação anterior.",
                "Organizar busca ativa ou encaminhamento conforme idade gestacional."
            ],
            "repadronizacao": [
                "Reformular crenças de que a dTpa seria desnecessária por vacinação anterior.",
                "Estimular compreensão da vacina como proteção direta ao bebê nos primeiros meses de vida."
            ]
        },
        "referencias": [
            "Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.",
            "Programa Nacional de Imunizações - PNI.",
            "COFEN Resolução nº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Vacinação",
        "achado_clinico": "Vacina dTpa não realizada",
        "diagnostico": {"codigo": None, "termo": "Imunização materna ausente contra coqueluche"},
        "resultado": {"codigo": None, "termo": "Vacinação dTpa realizada no período oportuno"},
        "intervencao": {"codigo": None, "termo": "Realizar busca ativa para vacinação dTpa"},
        "prioridade": "Alta",
        "fundamentacao": "A ausência da dTpa após a 20ª semana gestacional aumenta a vulnerabilidade do recém-nascido à coqueluche e ao tétano neonatal. A equipe deve identificar a não realização, orientar a gestante, registrar a pendência e encaminhar imediatamente para vacinação.",
        "transcultural": {
            "preservacao": [
                "Manter vínculo e escuta qualificada sem julgamento."
            ],
            "acomodacao": [
                "Identificar motivo da não vacinação, como acesso, medo, esquecimento ou desinformação.",
                "Adequar o plano de cuidado ao contexto familiar, cultural e territorial."
            ],
            "repadronizacao": [
                "Construir nova compreensão sobre a importância da dTpa para proteção neonatal.",
                "Estimular registro e acompanhamento ativo das pendências vacinais."
            ]
        },
        "referencias": [
            "Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.",
            "Programa Nacional de Imunizações - PNI.",
            "COFEN Resolução nº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Vacinação",
        "achado_clinico": "Vacina influenza indicada",
        "diagnostico": {"codigo": None, "termo": "Necessidade de imunização contra influenza"},
        "resultado": {"codigo": None, "termo": "Gestante imunizada contra influenza"},
        "intervencao": {"codigo": None, "termo": "Administrar ou encaminhar para vacina influenza sazonal"},
        "prioridade": "Alta",
        "fundamentacao": "Gestantes e puérperas pertencem a grupo prioritário para vacinação contra influenza, devido ao maior risco de formas graves da doença. A vacina influenza é indicada em dose anual por temporada durante a gestação.",
        "transcultural": {
            "preservacao": [
                "Respeitar práticas culturais seguras de prevenção de doenças respiratórias."
            ],
            "acomodacao": [
                "Explicar diferença entre reação vacinal leve e influenza.",
                "Planejar vacinação conforme campanha vigente e disponibilidade local."
            ],
            "repadronizacao": [
                "Corrigir crenças de que a vacina causa gripe.",
                "Fortalecer a vacinação como proteção da gestante e do bebê."
            ]
        },
        "referencias": [
            "Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.",
            "Programa Nacional de Imunizações - PNI.",
            "COFEN Resolução nº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Vacinação",
        "achado_clinico": "Vacina influenza não realizada",
        "diagnostico": {"codigo": None, "termo": "Imunização ausente contra influenza"},
        "resultado": {"codigo": None, "termo": "Vacinação contra influenza realizada"},
        "intervencao": {"codigo": None, "termo": "Orientar e encaminhar gestante para vacinação contra influenza"},
        "prioridade": "Alta",
        "fundamentacao": "A não realização da vacina influenza mantém a gestante suscetível a complicações respiratórias evitáveis. A equipe deve verificar a disponibilidade da vacina, orientar sobre segurança e benefício, registrar a pendência e realizar busca ativa.",
        "transcultural": {
            "preservacao": [
                "Valorizar medidas familiares seguras de cuidado respiratório."
            ],
            "acomodacao": [
                "Investigar barreiras de acesso, medo de reação ou experiências negativas anteriores.",
                "Ajustar orientação conforme compreensão da gestante."
            ],
            "repadronizacao": [
                "Reformular informações equivocadas sobre risco da vacina na gravidez.",
                "Estimular adesão anual à vacinação durante o pré-natal."
            ]
        },
        "referencias": [
            "Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.",
            "Programa Nacional de Imunizações - PNI.",
            "COFEN Resolução nº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Vacinação",
        "achado_clinico": "Vacina hepatite B incompleta",
        "diagnostico": {"codigo": None, "termo": "Risco de imunização incompleta contra hepatite B"},
        "resultado": {"codigo": None, "termo": "Esquema vacinal contra hepatite B completado"},
        "intervencao": {"codigo": None, "termo": "Completar esquema vacinal contra hepatite B"},
        "prioridade": "Alta",
        "fundamentacao": "A vacina hepatite B é indicada na gestação conforme histórico vacinal, em esquema de três doses quando não houver comprovação. Em esquema incompleto, não se deve reiniciar; deve-se completar as doses faltantes conforme intervalo recomendado.",
        "transcultural": {
            "preservacao": [
                "Valorizar a preocupação da gestante com proteção do bebê e prevenção de infecções."
            ],
            "acomodacao": [
                "Explicar o esquema de três doses e a necessidade de completar o calendário.",
                "Agendar retorno de acordo com deslocamento e acesso da gestante."
            ],
            "repadronizacao": [
                "Reformular a percepção de que uma ou duas doses garantem proteção completa.",
                "Fortalecer acompanhamento longitudinal até conclusão do esquema."
            ]
        },
        "referencias": [
            "Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.",
            "Programa Nacional de Imunizações - PNI.",
            "COFEN Resolução nº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Vacinação",
        "achado_clinico": "Vacina hepatite B não realizada",
        "diagnostico": {"codigo": None, "termo": "Imunização ausente contra hepatite B"},
        "resultado": {"codigo": None, "termo": "Esquema vacinal contra hepatite B iniciado"},
        "intervencao": {"codigo": None, "termo": "Iniciar vacinação contra hepatite B conforme calendário da gestante"},
        "prioridade": "Alta",
        "fundamentacao": "Gestantes sem comprovação de vacinação contra hepatite B devem iniciar esquema vacinal de três doses, conforme o Calendário Nacional de Vacinação. A vacinação reduz risco de infecção materna e contribui para prevenção de transmissão vertical associada ao cuidado pré-natal adequado.",
        "transcultural": {
            "preservacao": [
                "Respeitar valores familiares relacionados à proteção da gestação."
            ],
            "acomodacao": [
                "Explicar a relação entre hepatite B, gestação e proteção do recém-nascido.",
                "Planejar as doses no calendário de consultas do pré-natal."
            ],
            "repadronizacao": [
                "Superar desconhecimento sobre hepatite B e vacinação na gravidez.",
                "Estimular continuidade do esquema até conclusão."
            ]
        },
        "referencias": [
            "Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.",
            "Programa Nacional de Imunizações - PNI.",
            "COFEN Resolução nº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Vacinação",
        "achado_clinico": "Vacina COVID-19 indicada",
        "diagnostico": {"codigo": None, "termo": "Necessidade de imunização contra COVID-19"},
        "resultado": {"codigo": None, "termo": "Gestante imunizada contra COVID-19"},
        "intervencao": {"codigo": None, "termo": "Encaminhar gestante para vacinação contra COVID-19"},
        "prioridade": "Alta",
        "fundamentacao": "A vacinação contra COVID-19 é indicada para gestantes em cada gestação, conforme Calendário Nacional de Vacinação, com objetivo de reduzir formas graves, hospitalizações e óbitos por SARS-CoV-2.",
        "transcultural": {
            "preservacao": [
                "Manter escuta respeitosa sobre experiências pessoais e familiares durante a pandemia."
            ],
            "acomodacao": [
                "Esclarecer dúvidas sobre segurança, indicação e benefício da vacina.",
                "Considerar medos, crenças religiosas, culturais e experiências anteriores."
            ],
            "repadronizacao": [
                "Reformular informações falsas ou inseguras sobre vacinação contra COVID-19 na gestação.",
                "Promover decisão informada baseada em evidências e no cuidado materno-fetal."
            ]
        },
        "referencias": [
            "Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.",
            "Programa Nacional de Imunizações - PNI.",
            "COFEN Resolução nº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Vacinação",
        "achado_clinico": "Recusa vacinal",
        "diagnostico": {"codigo": None, "termo": "Adesão prejudicada à vacinação"},
        "resultado": {"codigo": None, "termo": "Gestante orientada e decisão vacinal reavaliada"},
        "intervencao": {"codigo": None, "termo": "Realizar aconselhamento sobre vacinação na gestação"},
        "prioridade": "Alta",
        "fundamentacao": "A recusa vacinal deve ser acolhida com escuta qualificada, identificação dos motivos, orientação baseada em evidências e registro em prontuário. A abordagem deve respeitar autonomia, cultura e crenças, sem deixar de informar riscos da não vacinação para gestante e recém-nascido.",
        "transcultural": {
            "preservacao": [
                "Preservar vínculo, autonomia e respeito às crenças da gestante."
            ],
            "acomodacao": [
                "Negociar nova conversa, envolver pessoa de confiança quando autorizado e oferecer material educativo.",
                "Adequar linguagem e estratégia educativa à realidade sociocultural."
            ],
            "repadronizacao": [
                "Reformular mitos e informações falsas sem confronto ou julgamento.",
                "Construir plano gradual de adesão vacinal com decisão compartilhada."
            ]
        },
        "referencias": [
            "Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.",
            "Programa Nacional de Imunizações - PNI.",
            "COFEN Resolução nº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Vacinação",
        "achado_clinico": "Medo de reação vacinal",
        "diagnostico": {"codigo": None, "termo": "Medo relacionado à vacinação"},
        "resultado": {"codigo": None, "termo": "Medo reduzido e vacinação aceita ou reavaliada"},
        "intervencao": {"codigo": None, "termo": "Orientar sobre eventos adversos esperados e sinais de alerta"},
        "prioridade": "Média",
        "fundamentacao": "O medo de reação vacinal é uma barreira comum à adesão. A equipe deve explicar possíveis eventos leves, sinais de alerta, condutas após vacinação e benefícios da imunização durante a gestação, fortalecendo segurança e autonomia da gestante.",
        "transcultural": {
            "preservacao": [
                "Acolher relatos de experiências anteriores da gestante ou familiares."
            ],
            "acomodacao": [
                "Explicar reações esperadas em linguagem simples e oferecer suporte pós-vacinação.",
                "Permitir tempo para perguntas e tomada de decisão."
            ],
            "repadronizacao": [
                "Diferenciar reação vacinal leve de doença grave evitável por vacina.",
                "Reduzir medo por meio de educação em saúde baseada em evidências."
            ]
        },
        "referencias": [
            "Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.",
            "Programa Nacional de Imunizações - PNI.",
            "COFEN Resolução nº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Vacinação",
        "achado_clinico": "Falta de acesso à sala de vacina",
        "diagnostico": {"codigo": None, "termo": "Acesso prejudicado à vacinação"},
        "resultado": {"codigo": None, "termo": "Acesso à vacinação garantido"},
        "intervencao": {"codigo": None, "termo": "Articular acesso da gestante à sala de vacina"},
        "prioridade": "Alta",
        "fundamentacao": "A falta de acesso à sala de vacina compromete a integralidade do pré-natal e aumenta risco de atraso vacinal. A equipe deve articular agendamento, transporte sanitário quando disponível, vacinação em ações extramuros, busca ativa e integração entre pré-natal e imunização.",
        "transcultural": {
            "preservacao": [
                "Reconhecer estratégias comunitárias de deslocamento e apoio familiar."
            ],
            "acomodacao": [
                "Adequar o plano vacinal aos dias de atendimento, transporte e permanência da gestante no território urbano ou rural.",
                "Articular com ACS, equipe ribeirinha, unidade de referência ou sala de vacina."
            ],
            "repadronizacao": [
                "Transformar o cuidado fragmentado em acompanhamento programado e territorializado.",
                "Estimular registro ativo das pendências vacinais pela equipe."
            ]
        },
        "referencias": [
            "Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.",
            "Programa Nacional de Imunizações - PNI.",
            "COFEN Resolução nº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Vacinação",
        "achado_clinico": "Barreiras culturais relacionadas à vacinação",
        "diagnostico": {"codigo": None, "termo": "Conflito cultural relacionado à vacinação"},
        "resultado": {"codigo": None, "termo": "Barreiras culturais identificadas e manejadas"},
        "intervencao": {"codigo": None, "termo": "Realizar cuidado culturalmente congruente sobre vacinação"},
        "prioridade": "Média",
        "fundamentacao": "Barreiras culturais podem envolver crenças familiares, religiosas, comunitárias, experiências históricas de desconfiança, medo de dano fetal ou informações falsas. A abordagem deve seguir cuidado culturalmente congruente, com preservação de práticas seguras, acomodação de valores e repadronização de práticas prejudiciais.",
        "transcultural": {
            "preservacao": [
                "Preservar práticas culturais que não tragam risco à gestante ou ao bebê.",
                "Valorizar lideranças familiares e comunitárias quando favorecem o cuidado."
            ],
            "acomodacao": [
                "Negociar estratégias educativas compatíveis com crenças e organização familiar.",
                "Usar linguagem respeitosa, exemplos locais e escuta ativa."
            ],
            "repadronizacao": [
                "Reformular práticas ou crenças que impeçam vacinação segura.",
                "Construir novo significado da vacina como proteção materna, fetal e comunitária."
            ]
        },
        "referencias": [
            "Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.",
            "Programa Nacional de Imunizações - PNI.",
            "COFEN Resolução nº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Vacinação",
        "achado_clinico": "Gestante ribeirinha com dificuldade de acesso à vacina",
        "diagnostico": {"codigo": None, "termo": "Vulnerabilidade territorial para atraso vacinal"},
        "resultado": {"codigo": None, "termo": "Vacinação viabilizada conforme realidade territorial"},
        "intervencao": {"codigo": None, "termo": "Planejar vacinação conforme contexto ribeirinho"},
        "prioridade": "Alta",
        "fundamentacao": "Gestantes ribeirinhas podem apresentar atraso vacinal por distância geográfica, transporte fluvial, sazonalidade dos rios, custos de deslocamento e ausência de sala de vacina próxima. A equipe deve planejar cuidado territorial, busca ativa, vacinação em ações itinerantes e articulação com rede de atenção.",
        "transcultural": {
            "preservacao": [
                "Valorizar modos de vida ribeirinhos, redes comunitárias e formas locais de organização do cuidado."
            ],
            "acomodacao": [
                "Adequar datas de vacinação ao calendário das embarcações, cheia/vazante dos rios e consultas de pré-natal.",
                "Articular com ACS, equipe fluvial, UBS de referência e gestão local."
            ],
            "repadronizacao": [
                "Substituir cuidado oportunístico por plano vacinal programado e acompanhado.",
                "Estimular registro, busca ativa e monitoramento das pendências vacinais em territórios de difícil acesso."
            ]
        },
        "referencias": [
            "Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.",
            "Programa Nacional de Imunizações - PNI.",
            "COFEN Resolução nº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Vacinação",
        "achado_clinico": "Gestante sem cartão vacinal",
        "diagnostico": {"codigo": None, "termo": "Registro vacinal ausente"},
        "resultado": {"codigo": None, "termo": "Registro vacinal recuperado ou atualizado"},
        "intervencao": {"codigo": None, "termo": "Solicitar, recuperar ou reconstruir registro vacinal"},
        "prioridade": "Alta",
        "fundamentacao": "A ausência do cartão vacinal dificulta a avaliação da situação imunológica da gestante. A equipe deve buscar registros em sistemas disponíveis, orientar emissão ou segunda via quando possível e, na ausência de comprovação, conduzir o esquema conforme situação vacinal desconhecida.",
        "transcultural": {
            "preservacao": [
                "Evitar culpabilização da gestante pela perda ou ausência do documento."
            ],
            "acomodacao": [
                "Orientar sobre guarda do cartão junto aos documentos do pré-natal.",
                "Auxiliar na recuperação de registros conforme rede local."
            ],
            "repadronizacao": [
                "Reorganizar o cuidado para que o cartão vacinal seja acompanhado em todas as consultas.",
                "Estimular corresponsabilização entre gestante, família e equipe."
            ]
        },
        "referencias": [
            "Ministério da Saúde. Calendário Nacional de Vacinação da Gestante, 2026.",
            "Programa Nacional de Imunizações - PNI.",
            "COFEN Resolução nº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    }
]REGRAS = [
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Hemoglobina baixa",
        "diagnostico": {"codigo": "10012606", "termo": "Processo do Sistema Circulatório, Prejudicado"},
        "resultado": {"codigo": "10028379", "termo": "Processo do Sistema Circulatório, Positivo"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre Nutrição"},
        "prioridade": "Alta",
        "fundamentacao": "Hemoglobina baixa no pré-natal sugere anemia gestacional, associada a maior risco de fadiga, infecção, parto prematuro, baixo peso ao nascer e morbimortalidade materno-fetal. A conduta de enfermagem inclui avaliação clínica, orientação alimentar rica em ferro, adesão à suplementação prescrita, investigação de sinais de gravidade e encaminhamento conforme protocolo.",
        "transcultural": {
            "preservacao": ["Valorizar alimentos culturalmente aceitos e ricos em ferro disponíveis no território."],
            "acomodacao": ["Adaptar orientações alimentares à renda, acesso, hábitos familiares e crenças da gestante."],
            "repadronizacao": ["Reorientar práticas alimentares que reduzam absorção de ferro, como consumo de café junto às refeições."]
        },
        "referencias": ["Ministério da Saúde. Atenção ao pré-natal de baixo risco.", "FEBRASGO. Recomendações para anemia na gestação.", "COFEN Resolução nº 736/2024.", "OMS. Recomendações de cuidado pré-natal.", "Leininger. Teoria Transcultural."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Hematócrito baixo",
        "diagnostico": {"codigo": "10012606", "termo": "Processo do Sistema Circulatório, Prejudicado"},
        "resultado": {"codigo": "10028379", "termo": "Processo do Sistema Circulatório, Positivo"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre Medicação"},
        "prioridade": "Alta",
        "fundamentacao": "Hematócrito baixo pode indicar hemodiluição fisiológica ou anemia, devendo ser interpretado em conjunto com hemoglobina, ferritina, sinais clínicos e idade gestacional. A enfermagem deve orientar uso correto de sulfato ferroso quando prescrito, alimentação adequada e seguimento laboratorial.",
        "transcultural": {
            "preservacao": ["Reconhecer práticas alimentares familiares protetoras."],
            "acomodacao": ["Negociar horários de suplementação conforme rotina da gestante."],
            "repadronizacao": ["Corrigir crenças que levem à suspensão do ferro por náuseas ou escurecimento das fezes."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Ferritina baixa",
        "diagnostico": {"codigo": "10023009", "termo": "Ingestão Nutricional, Prejudicada"},
        "resultado": {"codigo": "10037572", "termo": "Ingestão Nutricional, nos Limites Normais"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre Nutrição"},
        "prioridade": "Alta",
        "fundamentacao": "Ferritina baixa indica redução das reservas de ferro, podendo anteceder ou acompanhar anemia ferropriva. No pré-natal, exige orientação nutricional, avaliação de adesão à suplementação e monitoramento para prevenção de repercussões maternas e fetais.",
        "transcultural": {
            "preservacao": ["Estimular alimentos regionais ricos em ferro."],
            "acomodacao": ["Adequar plano alimentar à disponibilidade local."],
            "repadronizacao": ["Orientar combinação com fontes de vitamina C e evitar inibidores de absorção junto às refeições."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Vitamina B12 baixa",
        "diagnostico": {"codigo": "10023009", "termo": "Ingestão Nutricional, Prejudicada"},
        "resultado": {"codigo": "10037572", "termo": "Ingestão Nutricional, nos Limites Normais"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre Nutrição"},
        "prioridade": "Média",
        "fundamentacao": "Vitamina B12 baixa pode contribuir para anemia megaloblástica, sintomas neurológicos e alterações no desenvolvimento fetal. A enfermagem deve orientar alimentação, investigar dietas restritivas e encaminhar para avaliação e reposição conforme protocolo.",
        "transcultural": {
            "preservacao": ["Respeitar escolhas alimentares culturais ou religiosas."],
            "acomodacao": ["Adequar orientação para gestantes vegetarianas, veganas ou com baixa ingestão de alimentos de origem animal."],
            "repadronizacao": ["Reorientar restrições alimentares com risco nutricional sem acompanhamento profissional."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Vitamina D baixa",
        "diagnostico": {"codigo": "10023009", "termo": "Ingestão Nutricional, Prejudicada"},
        "resultado": {"codigo": "10037572", "termo": "Ingestão Nutricional, nos Limites Normais"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre Nutrição"},
        "prioridade": "Média",
        "fundamentacao": "Vitamina D baixa pode relacionar-se a alterações ósseas, metabólicas e imunológicas. Na gestação, deve ser avaliada conforme risco clínico, dieta, exposição solar e protocolo local, com orientação segura e encaminhamento quando necessário.",
        "transcultural": {
            "preservacao": ["Considerar hábitos culturais de vestimenta e exposição solar."],
            "acomodacao": ["Orientar exposição solar segura conforme realidade territorial."],
            "repadronizacao": ["Evitar automedicação com doses elevadas sem prescrição."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Glicemia alterada",
        "diagnostico": {"codigo": "10005876", "termo": "Diabetes"},
        "resultado": {"codigo": "10027532", "termo": "Processo do Sistema Regulatório, Eficaz"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre Nutrição"},
        "prioridade": "Alta",
        "fundamentacao": "Glicemia alterada no pré-natal pode indicar risco de diabetes mellitus gestacional ou diabetes prévio não diagnosticado. Deve-se orientar alimentação adequada, atividade física quando não contraindicada, controle glicêmico, avaliação médica e seguimento conforme protocolo.",
        "transcultural": {
            "preservacao": ["Valorizar alimentos tradicionais saudáveis e acessíveis."],
            "acomodacao": ["Adaptar plano alimentar à cultura, renda e rotina familiar."],
            "repadronizacao": ["Reduzir consumo frequente de açúcar, bebidas adoçadas e ultraprocessados."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "TOTG alterado",
        "diagnostico": {"codigo": "10005876", "termo": "Diabetes"},
        "resultado": {"codigo": "10027532", "termo": "Processo do Sistema Regulatório, Eficaz"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Alta",
        "fundamentacao": "TOTG alterado confirma alteração do metabolismo glicêmico na gestação e exige acompanhamento para prevenção de macrossomia, pré-eclâmpsia, parto traumático, hipoglicemia neonatal e complicações maternas. A enfermagem deve orientar tratamento, autocuidado e seguimento multiprofissional.",
        "transcultural": {
            "preservacao": ["Manter alimentos culturais que sejam adequados ao controle glicêmico."],
            "acomodacao": ["Construir plano possível conforme acesso a alimentos e rotina da gestante."],
            "repadronizacao": ["Substituir padrões alimentares de alto índice glicêmico por alternativas locais mais saudáveis."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Proteinúria",
        "diagnostico": {"codigo": "10001359", "termo": "Função do Sistema Urinário, Prejudicada"},
        "resultado": {"codigo": "10028615", "termo": "Função do Sistema Urinário, Eficaz"},
        "intervencao": {"codigo": "10044148", "termo": "Orientar sobre Medição de Pressão Arterial"},
        "prioridade": "Alta",
        "fundamentacao": "Proteinúria na gestação pode estar associada a infecção urinária, doença renal ou pré-eclâmpsia, especialmente quando acompanhada de hipertensão, cefaleia, escotomas, dor epigástrica ou edema. Exige avaliação imediata, controle pressórico e encaminhamento conforme gravidade.",
        "transcultural": {
            "preservacao": ["Acolher relatos de sintomas conforme linguagem e interpretação cultural da gestante."],
            "acomodacao": ["Orientar sinais de alerta de forma simples e objetiva."],
            "repadronizacao": ["Reforçar que edema importante, cefaleia ou alterações visuais não devem ser tratados apenas com medidas caseiras."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Creatinina alterada",
        "diagnostico": {"codigo": "10012972", "termo": "Processo do Sistema Urinário, Prejudicado"},
        "resultado": {"codigo": "10028604", "termo": "Processo do Sistema Urinário, Eficaz"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Alta",
        "fundamentacao": "Creatinina alterada na gestação pode indicar comprometimento renal, doença hipertensiva, infecção ou condição clínica de maior risco. Deve-se avaliar sinais associados, pressão arterial, proteinúria, hidratação, medicamentos em uso e necessidade de referência ao pré-natal de alto risco.",
        "transcultural": {
            "preservacao": ["Considerar práticas locais de ingestão hídrica e uso de chás."],
            "acomodacao": ["Orientar hidratação segura e evitar automedicação."],
            "repadronizacao": ["Desestimular uso de plantas medicinais potencialmente nefrotóxicas sem avaliação profissional."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Plaquetopenia",
        "diagnostico": {"codigo": "10012606", "termo": "Processo do Sistema Circulatório, Prejudicado"},
        "resultado": {"codigo": "10028379", "termo": "Processo do Sistema Circulatório, Positivo"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Alta",
        "fundamentacao": "Plaquetopenia na gestação pode ser gestacional, imunológica ou associada a síndromes hipertensivas graves, como pré-eclâmpsia e HELLP. A avaliação deve considerar valores seriados, sangramentos, pressão arterial, enzimas hepáticas e sinais de gravidade.",
        "transcultural": {
            "preservacao": ["Acolher relatos de sangramentos e sinais percebidos pela gestante."],
            "acomodacao": ["Orientar procura imediata diante de sangramento, dor epigástrica, cefaleia intensa ou mal-estar."],
            "repadronizacao": ["Evitar banalização de manchas roxas, sangramento gengival ou epistaxe na gestação."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Urocultura positiva",
        "diagnostico": {"codigo": "10029915", "termo": "Infecção do Trato Urinário"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre Infecção"},
        "prioridade": "Alta",
        "fundamentacao": "Urocultura positiva na gestação indica infecção urinária ou bacteriúria significativa, condições associadas a pielonefrite, parto prematuro e baixo peso ao nascer. A enfermagem deve orientar adesão ao tratamento, hidratação, sinais de alerta e controle após tratamento.",
        "transcultural": {
            "preservacao": ["Reconhecer práticas de cuidado íntimo culturalmente aceitas e seguras."],
            "acomodacao": ["Orientar higiene, hidratação e uso correto do antibiótico conforme prescrição."],
            "repadronizacao": ["Desestimular interrupção do tratamento quando sintomas melhorarem."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Bacteriúria assintomática",
        "diagnostico": {"codigo": "10051950", "termo": "Risco de Infecção Urinária"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10038112", "termo": "Orientar sobre Prevenção de Infecção Cruzada"},
        "prioridade": "Alta",
        "fundamentacao": "Bacteriúria assintomática no pré-natal deve ser tratada conforme protocolo por risco de evolução para pielonefrite e complicações obstétricas. Mesmo sem sintomas, requer orientação, tratamento prescrito, retorno e controle laboratorial.",
        "transcultural": {
            "preservacao": ["Acolher a percepção da gestante de estar saudável por não apresentar sintomas."],
            "acomodacao": ["Explicar que ausência de sintomas não exclui risco gestacional."],
            "repadronizacao": ["Reforçar necessidade de tratamento completo mesmo sem dor ou ardência urinária."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "VDRL reagente",
        "diagnostico": {"codigo": "10023032", "termo": "Infecção"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre Infecção"},
        "prioridade": "Alta",
        "fundamentacao": "VDRL reagente no pré-natal sugere sífilis e exige confirmação/avaliação conforme protocolo, tratamento imediato com penicilina quando indicado, tratamento de parceria sexual, notificação e seguimento sorológico para prevenção da sífilis congênita.",
        "transcultural": {
            "preservacao": ["Acolher a gestante sem julgamento moral."],
            "acomodacao": ["Incluir parceria sexual no cuidado quando autorizado e conforme protocolo."],
            "repadronizacao": ["Reduzir estigma e reforçar que tratamento adequado previne transmissão vertical."]
        },
        "referencias": ["Ministério da Saúde. Protocolo Clínico e Diretrizes Terapêuticas para IST.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "HIV reagente",
        "diagnostico": {"codigo": "10023032", "termo": "Infecção"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Alta",
        "fundamentacao": "HIV reagente na gestação requer acolhimento, confirmação diagnóstica conforme fluxo, início ou continuidade imediata da terapia antirretroviral, avaliação da carga viral, prevenção da transmissão vertical, orientação sobre parto, puerpério e alimentação infantil conforme protocolo.",
        "transcultural": {
            "preservacao": ["Garantir sigilo, acolhimento e respeito à identidade da gestante."],
            "acomodacao": ["Adaptar orientações à rede de apoio e ao contexto familiar."],
            "repadronizacao": ["Combater estigma, abandono do tratamento e crenças que dificultem adesão à TARV."]
        },
        "referencias": ["Ministério da Saúde. PCDT para manejo da infecção pelo HIV em gestantes.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "HBsAg reagente",
        "diagnostico": {"codigo": "10023032", "termo": "Infecção"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre Infecção"},
        "prioridade": "Alta",
        "fundamentacao": "HBsAg reagente indica infecção pelo vírus da hepatite B e exige avaliação clínica, exames complementares, seguimento especializado quando indicado e planejamento da profilaxia neonatal com vacina e imunoglobulina conforme protocolo para prevenção da transmissão vertical.",
        "transcultural": {
            "preservacao": ["Acolher medos e crenças familiares sobre hepatites."],
            "acomodacao": ["Orientar prevenção de transmissão domiciliar e vacinação de contatos."],
            "repadronizacao": ["Reduzir estigma e reforçar medidas efetivas de prevenção neonatal."]
        },
        "referencias": ["Ministério da Saúde. Hepatites virais e pré-natal.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Hepatite C reagente",
        "diagnostico": {"codigo": "10023032", "termo": "Infecção"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre Infecção"},
        "prioridade": "Alta",
        "fundamentacao": "Hepatite C reagente na gestação requer confirmação diagnóstica, avaliação de coinfecções, função hepática e encaminhamento para seguimento. A enfermagem deve orientar prevenção de transmissão, evitar exposição sanguínea e garantir acompanhamento materno e neonatal.",
        "transcultural": {
            "preservacao": ["Acolher a gestante sem julgamento."],
            "acomodacao": ["Adequar orientações preventivas à realidade familiar e comunitária."],
            "repadronizacao": ["Corrigir crenças sobre transmissão por contato casual."]
        },
        "referencias": ["Ministério da Saúde. Hepatites virais.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Rubéola não imune",
        "diagnostico": {"codigo": "10041093", "termo": "Processo do Sistema Imunológico, Prejudicado"},
        "resultado": {"codigo": "10047463", "termo": "Processo do Sistema Imune, Eficaz"},
        "intervencao": {"codigo": "10045079", "termo": "Orientar sobre Gestação"},
        "prioridade": "Média",
        "fundamentacao": "Rubéola não imune indica suscetibilidade. Como a vacina tríplice viral é contraindicada durante a gestação por ser vacina de vírus vivo atenuado, deve-se orientar prevenção de exposição e vacinação no puerpério, conforme calendário vacinal.",
        "transcultural": {
            "preservacao": ["Valorizar redes familiares de proteção da gestante."],
            "acomodacao": ["Orientar evitar contato com pessoas com exantema ou suspeita de rubéola."],
            "repadronizacao": ["Explicar que a vacina deve ser realizada após o parto, não durante a gestação."]
        },
        "referencias": ["Ministério da Saúde. Calendário Nacional de Vacinação.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Toxoplasmose IgM positivo",
        "diagnostico": {"codigo": "10023032", "termo": "Infecção"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre Infecção"},
        "prioridade": "Alta",
        "fundamentacao": "Toxoplasmose IgM positivo pode indicar infecção recente e risco de transmissão fetal. Deve-se confirmar diagnóstico com sorologia complementar, avididade quando aplicável, idade gestacional, avaliação médica e início oportuno de tratamento conforme protocolo.",
        "transcultural": {
            "preservacao": ["Respeitar práticas alimentares locais seguras."],
            "acomodacao": ["Orientar higiene dos alimentos, cozimento adequado de carnes e cuidado com solo e fezes de gatos."],
            "repadronizacao": ["Modificar consumo de carnes cruas, malpassadas ou alimentos sem higienização adequada."]
        },
        "referencias": ["Ministério da Saúde. Pré-natal de baixo risco.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Toxoplasmose suscetível",
        "diagnostico": {"codigo": "10015133", "termo": "Risco de Infecção"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10038112", "termo": "Orientar sobre Prevenção de Infecção Cruzada"},
        "prioridade": "Média",
        "fundamentacao": "Gestante suscetível à toxoplasmose não possui imunidade e deve receber orientações preventivas durante toda a gestação, com repetição sorológica conforme protocolo local para detecção precoce de soroconversão.",
        "transcultural": {
            "preservacao": ["Manter práticas culinárias regionais seguras."],
            "acomodacao": ["Adequar orientação ao acesso à água tratada, alimentos e condições de preparo."],
            "repadronizacao": ["Reforçar lavagem de frutas e verduras, uso de água segura e evitar carne crua ou malcozida."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Coombs indireto positivo",
        "diagnostico": {"codigo": "10012606", "termo": "Processo do Sistema Circulatório, Prejudicado"},
        "resultado": {"codigo": "10028379", "termo": "Processo do Sistema Circulatório, Positivo"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Alta",
        "fundamentacao": "Coombs indireto positivo em gestante pode indicar aloimunização materna, com risco de doença hemolítica fetal e neonatal. Requer avaliação especializada, monitoramento de títulos, investigação fetal quando indicada e seguimento em pré-natal de alto risco.",
        "transcultural": {
            "preservacao": ["Acolher dúvidas familiares sobre incompatibilidade sanguínea."],
            "acomodacao": ["Explicar de forma simples a necessidade de acompanhamento especializado."],
            "repadronizacao": ["Evitar abandono do seguimento por ausência de sintomas maternos."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Tipagem Rh negativo",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10028379", "termo": "Processo do Sistema Circulatório, Positivo"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Alta",
        "fundamentacao": "Gestante Rh negativo necessita avaliação do fator Rh do parceiro quando disponível, Coombs indireto e acompanhamento para prevenção de aloimunização. Quando indicado, deve receber imunoglobulina anti-D conforme protocolo, especialmente em situações de risco e no puerpério se recém-nascido Rh positivo.",
        "transcultural": {
            "preservacao": ["Respeitar dúvidas da gestante e família sobre exames de sangue."],
            "acomodacao": ["Orientar a importância do cartão da gestante e registro da tipagem sanguínea."],
            "repadronizacao": ["Corrigir a ideia de que Rh negativo é doença, explicando o risco apenas em situações específicas."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "OMS.", "Leininger."]
    }
]# modulos/regras_clinicas/prenatal/sinais_sintomas.py

REGRAS = [
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Náuseas",
        "diagnostico": {"codigo": "10012453", "termo": "Náusea"},
        "resultado": {"codigo": "10028992", "termo": "Náusea, Ausente"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre Nutrição"},
        "prioridade": "Baixa",
        "fundamentacao": "Náuseas são frequentes no primeiro trimestre, geralmente relacionadas a alterações hormonais. A avaliação deve identificar intensidade, hidratação, perda ponderal e impacto funcional, orientando fracionamento alimentar, hidratação e sinais de alerta.",
        "transcultural": {
            "preservacao": ["Valorizar práticas alimentares culturais seguras que aliviem náuseas."],
            "acomodacao": ["Adaptar horários e tipos de alimentos à rotina e tolerância da gestante."],
            "repadronizacao": ["Reorientar uso de chás, ervas ou medicamentos sem avaliação profissional."]
        },
        "referencias": ["Ministério da Saúde. Pré-natal de baixo risco.", "OMS. Recomendações sobre cuidados pré-natais.", "FEBRASGO. Assistência pré-natal.", "COFEN Resolução nº 736/2024.", "Leininger. Teoria Transcultural."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Vômitos",
        "diagnostico": {"codigo": "10020864", "termo": "Vômito"},
        "resultado": {"codigo": "10029134", "termo": "Vômito, Ausente"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre Nutrição"},
        "prioridade": "Média",
        "fundamentacao": "Vômitos persistentes podem causar desidratação, perda de peso e distúrbios hidroeletrolíticos. No pré-natal, deve-se avaliar frequência, aceitação oral, diurese, sinais de desidratação e necessidade de encaminhamento.",
        "transcultural": {
            "preservacao": ["Reconhecer alimentos culturalmente aceitos que melhorem a tolerância oral."],
            "acomodacao": ["Orientar pequenas refeições, líquidos em pequenos volumes e repouso após alimentação."],
            "repadronizacao": ["Desencorajar automedicação antiemética e práticas inseguras."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Hiperêmese gravídica",
        "diagnostico": {"codigo": "10020864", "termo": "Vômito"},
        "resultado": {"codigo": "10027617", "termo": "Equilíbrio Hídrico, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Hiperêmese gravídica caracteriza-se por vômitos intensos, perda de peso, desidratação, cetonúria e risco de desequilíbrio metabólico. Requer avaliação imediata, hidratação, suporte clínico e possível encaminhamento hospitalar.",
        "transcultural": {
            "preservacao": ["Acolher explicações culturais da gestante sobre o mal-estar."],
            "acomodacao": ["Explicar sinais de gravidade de forma simples para gestante e família."],
            "repadronizacao": ["Reforçar que vômitos intensos não devem ser tratados apenas com medidas caseiras."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Azia",
        "diagnostico": {"codigo": "10013950", "termo": "Dor"},
        "resultado": {"codigo": "10029008", "termo": "Dor, Ausente"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre Nutrição"},
        "prioridade": "Baixa",
        "fundamentacao": "Azia é comum na gestação por relaxamento do esfíncter esofágico e compressão uterina. Deve-se orientar refeições menores, evitar deitar após comer e observar sinais de alarme, como dor intensa ou vômitos persistentes.",
        "transcultural": {
            "preservacao": ["Manter alimentos tradicionais que não piorem sintomas."],
            "acomodacao": ["Ajustar orientação alimentar à rotina familiar."],
            "repadronizacao": ["Evitar automedicação com antiácidos ou bicarbonato sem orientação."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Pirose",
        "diagnostico": {"codigo": "10013950", "termo": "Dor"},
        "resultado": {"codigo": "10029008", "termo": "Dor, Ausente"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre Nutrição"},
        "prioridade": "Baixa",
        "fundamentacao": "Pirose gestacional geralmente decorre de refluxo gastroesofágico. A enfermagem deve orientar medidas posturais, fracionamento alimentar, redução de alimentos irritantes e avaliação se sintomas forem intensos ou persistentes.",
        "transcultural": {
            "preservacao": ["Preservar preparações alimentares locais bem toleradas."],
            "acomodacao": ["Negociar substituições alimentares possíveis."],
            "repadronizacao": ["Desestimular condutas caseiras de risco ou uso indiscriminado de medicamentos."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Constipação",
        "diagnostico": {"codigo": "10004999", "termo": "Constipação"},
        "resultado": {"codigo": "10027800", "termo": "Eliminação Intestinal, Eficaz"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre Nutrição"},
        "prioridade": "Baixa",
        "fundamentacao": "Constipação é frequente na gestação por alterações hormonais, redução da motilidade intestinal e suplementação de ferro. Orienta-se aumento de fibras, ingestão hídrica, atividade física se não contraindicada e evitar laxantes sem prescrição.",
        "transcultural": {
            "preservacao": ["Valorizar alimentos regionais ricos em fibras."],
            "acomodacao": ["Adequar consumo de água e fibras à disponibilidade local."],
            "repadronizacao": ["Evitar uso rotineiro de laxantes, chás purgativos ou automedicação."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Diarreia",
        "diagnostico": {"codigo": "10005933", "termo": "Diarreia"},
        "resultado": {"codigo": "10027800", "termo": "Eliminação Intestinal, Eficaz"},
        "intervencao": {"codigo": "10036112", "termo": "Orientar sobre Hidratação"},
        "prioridade": "Média",
        "fundamentacao": "Diarreia pode causar desidratação e indicar infecção gastrointestinal. A enfermagem deve avaliar duração, febre, sangue nas fezes, sinais de desidratação, orientar hidratação e encaminhar quando houver sinais de gravidade.",
        "transcultural": {
            "preservacao": ["Reconhecer alimentos tradicionais leves e seguros."],
            "acomodacao": ["Orientar preparo seguro de água e alimentos."],
            "repadronizacao": ["Desestimular uso de antidiarreicos ou antibióticos sem prescrição."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Dor lombar",
        "diagnostico": {"codigo": "10013950", "termo": "Dor"},
        "resultado": {"codigo": "10029008", "termo": "Dor, Ausente"},
        "intervencao": {"codigo": "10039276", "termo": "Ensinar Exercício"},
        "prioridade": "Baixa",
        "fundamentacao": "Dor lombar é comum por alterações posturais, ganho ponderal e frouxidão ligamentar. Deve-se orientar postura, alongamentos seguros, repouso relativo, uso de calçados adequados e investigar sinais urinários ou neurológicos.",
        "transcultural": {
            "preservacao": ["Valorizar práticas corporais seguras e aceitas pela gestante."],
            "acomodacao": ["Adaptar exercícios à rotina, trabalho e território."],
            "repadronizacao": ["Evitar massagens agressivas, automedicação e esforços excessivos."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Dor pélvica",
        "diagnostico": {"codigo": "10013950", "termo": "Dor"},
        "resultado": {"codigo": "10029008", "termo": "Dor, Ausente"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Média",
        "fundamentacao": "Dor pélvica pode estar associada a alterações musculoesqueléticas, crescimento uterino, infecção, contrações ou sinais obstétricos. Deve-se avaliar intensidade, sangramento, perda de líquido, febre e contrações.",
        "transcultural": {
            "preservacao": ["Acolher formas locais de descrever dor e desconforto."],
            "acomodacao": ["Orientar repouso, postura e sinais de alerta em linguagem acessível."],
            "repadronizacao": ["Reforçar busca imediata se houver sangramento, febre, perda de líquido ou contrações regulares."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Dor abdominal",
        "diagnostico": {"codigo": "10013950", "termo": "Dor"},
        "resultado": {"codigo": "10029008", "termo": "Dor, Ausente"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Dor abdominal na gestação pode indicar condições benignas ou urgências obstétricas, como ameaça de abortamento, trabalho de parto prematuro, descolamento placentário, infecção ou abdome agudo. Deve-se avaliar sinais associados e encaminhar se dor intensa, persistente ou acompanhada de sangramento, febre ou contrações.",
        "transcultural": {
            "preservacao": ["Acolher interpretações culturais da dor."],
            "acomodacao": ["Explicar sinais de risco para gestante e família."],
            "repadronizacao": ["Desencorajar atraso na busca de atendimento por uso exclusivo de remédios caseiros."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Cefaleia",
        "diagnostico": {"codigo": "10013950", "termo": "Dor"},
        "resultado": {"codigo": "10029008", "termo": "Dor, Ausente"},
        "intervencao": {"codigo": "10044148", "termo": "Orientar sobre Medição de Pressão Arterial"},
        "prioridade": "Alta",
        "fundamentacao": "Cefaleia na gestação exige avaliação da pressão arterial e sinais de pré-eclâmpsia, especialmente se intensa, persistente, associada a escotomas, dor epigástrica, edema ou proteinúria. A enfermagem deve classificar risco e encaminhar quando necessário.",
        "transcultural": {
            "preservacao": ["Acolher medidas culturais seguras de conforto."],
            "acomodacao": ["Orientar sinais de alerta com linguagem clara."],
            "repadronizacao": ["Evitar automedicação e atraso na avaliação pressórica."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Tontura",
        "diagnostico": {"codigo": "10006160", "termo": "Tontura"},
        "resultado": {"codigo": "10028992", "termo": "Sintoma, Ausente"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Média",
        "fundamentacao": "Tontura pode estar relacionada a hipotensão postural, hipoglicemia, anemia, desidratação ou alterações clínicas. Deve-se avaliar sinais vitais, alimentação, hidratação, hemoglobina e ocorrência de quedas ou síncope.",
        "transcultural": {
            "preservacao": ["Valorizar relatos da gestante sobre fatores desencadeantes."],
            "acomodacao": ["Orientar levantar lentamente, alimentar-se regularmente e hidratar-se."],
            "repadronizacao": ["Reforçar procura de atendimento se houver desmaio, palpitação, sangramento ou dor intensa."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Lipotímia",
        "diagnostico": {"codigo": "10006160", "termo": "Tontura"},
        "resultado": {"codigo": "10027617", "termo": "Equilíbrio Hídrico, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Lipotímia ou quase desmaio pode decorrer de hipotensão, hipoglicemia, anemia, arritmia, desidratação ou sangramento. Exige avaliação de sinais vitais, glicemia quando disponível, hidratação e encaminhamento se recorrente ou associada a sinais de risco.",
        "transcultural": {
            "preservacao": ["Acolher explicações familiares sobre o episódio."],
            "acomodacao": ["Orientar medidas imediatas de segurança para prevenir quedas."],
            "repadronizacao": ["Evitar normalizar desmaios recorrentes na gestação."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Dispneia",
        "diagnostico": {"codigo": "10006461", "termo": "Dispneia"},
        "resultado": {"codigo": "10029208", "termo": "Respiração, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Dispneia leve pode ocorrer por alterações fisiológicas da gestação, mas dispneia intensa, súbita, associada a dor torácica, cianose, febre, taquicardia ou saturação baixa exige avaliação urgente.",
        "transcultural": {
            "preservacao": ["Acolher percepções culturais sobre falta de ar."],
            "acomodacao": ["Orientar repouso, posição confortável e sinais de alerta."],
            "repadronizacao": ["Reforçar que falta de ar importante não deve ser atribuída apenas à gravidez."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Edema fisiológico",
        "diagnostico": {"codigo": "10041951", "termo": "Edema"},
        "resultado": {"codigo": "10029019", "termo": "Edema, Reduzido"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Baixa",
        "fundamentacao": "Edema leve em membros inferiores pode ser fisiológico no final da gestação. Deve-se avaliar pressão arterial, proteinúria e sinais de alarme. Orienta-se repouso com elevação de pernas, hidratação e evitar longos períodos em pé.",
        "transcultural": {
            "preservacao": ["Valorizar práticas seguras de repouso e cuidado corporal."],
            "acomodacao": ["Adequar orientações à rotina laboral e doméstica."],
            "repadronizacao": ["Evitar uso de diuréticos, chás ou restrição hídrica sem prescrição."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Edema patológico",
        "diagnostico": {"codigo": "10041951", "termo": "Edema"},
        "resultado": {"codigo": "10029019", "termo": "Edema, Reduzido"},
        "intervencao": {"codigo": "10044148", "termo": "Orientar sobre Medição de Pressão Arterial"},
        "prioridade": "Alta",
        "fundamentacao": "Edema súbito, generalizado ou associado a hipertensão, cefaleia, alterações visuais, dor epigástrica ou proteinúria pode indicar pré-eclâmpsia. Requer avaliação imediata e encaminhamento conforme protocolo.",
        "transcultural": {
            "preservacao": ["Acolher o relato da gestante sobre mudanças corporais."],
            "acomodacao": ["Explicar sinais de gravidade para gestante e família."],
            "repadronizacao": ["Reforçar que edema no rosto e mãos, quando associado a sintomas, exige atendimento imediato."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Câimbras",
        "diagnostico": {"codigo": "10040943", "termo": "Cãibra Muscular"},
        "resultado": {"codigo": "10028337", "termo": "Conforto, Melhorado"},
        "intervencao": {"codigo": "10039276", "termo": "Ensinar Exercício"},
        "prioridade": "Baixa",
        "fundamentacao": "Câimbras são comuns na gestação, especialmente em membros inferiores. Orienta-se alongamento suave, hidratação, atividade física segura e avaliação se houver dor unilateral, edema importante ou suspeita vascular.",
        "transcultural": {
            "preservacao": ["Manter práticas corporais seguras já utilizadas pela gestante."],
            "acomodacao": ["Adaptar alongamentos à capacidade física e idade gestacional."],
            "repadronizacao": ["Desencorajar uso de medicamentos ou suplementos sem avaliação."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Fadiga",
        "diagnostico": {"codigo": "10000695", "termo": "Fadiga"},
        "resultado": {"codigo": "10000707", "termo": "Fadiga, Reduzida"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Baixa",
        "fundamentacao": "Fadiga pode ser fisiológica, mas também se relaciona a anemia, sono inadequado, sobrecarga de trabalho, sofrimento emocional ou doença clínica. A enfermagem deve avaliar intensidade, rotina, exames e sinais associados.",
        "transcultural": {
            "preservacao": ["Reconhecer papéis familiares e atividades culturais da gestante."],
            "acomodacao": ["Negociar pausas, divisão de tarefas e repouso possível."],
            "repadronizacao": ["Evitar naturalizar fadiga incapacitante sem investigação."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Insônia",
        "diagnostico": {"codigo": "10010330", "termo": "Insônia"},
        "resultado": {"codigo": "10041399", "termo": "Sono, Melhorado"},
        "intervencao": {"codigo": "10024662", "termo": "Orientar sobre Sono"},
        "prioridade": "Baixa",
        "fundamentacao": "Insônia pode ocorrer por desconfortos físicos, ansiedade, noctúria e alterações hormonais. Deve-se orientar higiene do sono, posição confortável, rotina relaxante e avaliar sofrimento psíquico.",
        "transcultural": {
            "preservacao": ["Valorizar rituais culturais seguros de relaxamento."],
            "acomodacao": ["Adaptar medidas de sono à rotina familiar e ambiente domiciliar."],
            "repadronizacao": ["Evitar uso de sedativos, álcool ou fitoterápicos sem prescrição."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Sonolência",
        "diagnostico": {"codigo": "10041396", "termo": "Sono, Prejudicado"},
        "resultado": {"codigo": "10041399", "termo": "Sono, Melhorado"},
        "intervencao": {"codigo": "10024662", "termo": "Orientar sobre Sono"},
        "prioridade": "Baixa",
        "fundamentacao": "Sonolência pode ser fisiológica no início da gestação, mas deve ser avaliada quando excessiva, associada a anemia, depressão, privação de sono, uso de medicamentos ou prejuízo funcional.",
        "transcultural": {
            "preservacao": ["Respeitar hábitos familiares de descanso quando seguros."],
            "acomodacao": ["Orientar pausas programadas e rotina regular de sono."],
            "repadronizacao": ["Investigar sonolência incapacitante em vez de atribuí-la apenas à gestação."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Corrimento vaginal",
        "diagnostico": {"codigo": "10023032", "termo": "Infecção"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre Infecção"},
        "prioridade": "Média",
        "fundamentacao": "Corrimento vaginal pode ser fisiológico quando claro e sem odor, mas corrimento com odor, prurido, dor, ardor ou alteração de cor sugere infecção vaginal ou IST. Deve-se avaliar sintomas associados e encaminhar para diagnóstico e tratamento.",
        "transcultural": {
            "preservacao": ["Acolher crenças sobre higiene íntima sem julgamento."],
            "acomodacao": ["Orientar higiene adequada e uso de roupas confortáveis."],
            "repadronizacao": ["Desencorajar duchas vaginais, automedicação e uso de produtos irritantes."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Prurido vaginal",
        "diagnostico": {"codigo": "10023032", "termo": "Infecção"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre Infecção"},
        "prioridade": "Média",
        "fundamentacao": "Prurido vaginal pode indicar candidíase, vaginose, IST ou irritação local. A gestante deve ser avaliada para tratamento adequado, evitando automedicação e prevenindo complicações.",
        "transcultural": {
            "preservacao": ["Acolher pudor e formas culturais de relatar sintomas íntimos."],
            "acomodacao": ["Garantir privacidade e linguagem respeitosa."],
            "repadronizacao": ["Evitar uso de pomadas, duchas ou receitas caseiras sem avaliação."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Sangramento vaginal",
        "diagnostico": {"codigo": "10003303", "termo": "Sangramento"},
        "resultado": {"codigo": "10028120", "termo": "Sangramento, Ausente"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Sangramento vaginal na gestação é sinal de alerta e pode estar associado a abortamento, gravidez ectópica, placenta prévia, descolamento placentário ou trabalho de parto. Exige avaliação imediata, independentemente do volume.",
        "transcultural": {
            "preservacao": ["Acolher a gestante e reduzir medo e culpa."],
            "acomodacao": ["Orientar familiares sobre urgência do atendimento."],
            "repadronizacao": ["Reforçar que sangramento não deve ser observado em casa sem avaliação."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Perda de líquido",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10028120", "termo": "Risco, Reduzido"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Perda de líquido vaginal pode indicar ruptura de membranas, com risco de infecção, prematuridade e sofrimento fetal. Deve-se encaminhar imediatamente para avaliação obstétrica, evitando toque vaginal desnecessário.",
        "transcultural": {
            "preservacao": ["Acolher a descrição da gestante sobre o líquido e circunstâncias."],
            "acomodacao": ["Explicar que perda contínua, mesmo sem dor, exige avaliação."],
            "repadronizacao": ["Evitar espera domiciliar ou uso de absorventes internos."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Redução dos movimentos fetais",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Redução ou ausência de movimentos fetais após a percepção habitual é sinal de alerta e pode indicar comprometimento fetal. A gestante deve ser orientada a procurar avaliação imediata para ausculta fetal e conduta obstétrica.",
        "transcultural": {
            "preservacao": ["Valorizar a percepção materna sobre o padrão de movimentos do bebê."],
            "acomodacao": ["Orientar registro e observação dos movimentos fetais conforme idade gestacional."],
            "repadronizacao": ["Desestimular esperar muitos dias para procurar atendimento quando houver redução importante."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Febre",
        "diagnostico": {"codigo": "10007916", "termo": "Febre"},
        "resultado": {"codigo": "10033694", "termo": "Temperatura Corporal, nos Limites Normais"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Febre na gestação pode indicar infecção urinária, respiratória, gastrointestinal, arbovirose, infecção intra-amniótica ou outras condições de risco. Requer avaliação clínica, hidratação, investigação etiológica e encaminhamento conforme gravidade.",
        "transcultural": {
            "preservacao": ["Acolher práticas culturais seguras de conforto térmico."],
            "acomodacao": ["Orientar hidratação e monitoramento da temperatura."],
            "repadronizacao": ["Evitar uso de medicamentos, chás ou banhos extremos sem orientação."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Disúria",
        "diagnostico": {"codigo": "10029915", "termo": "Infecção do Trato Urinário"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre Infecção"},
        "prioridade": "Alta",
        "fundamentacao": "Disúria sugere infecção urinária, condição frequente na gestação e associada a pielonefrite, parto prematuro e baixo peso ao nascer. Deve-se solicitar/avaliar exames conforme protocolo, orientar hidratação e tratamento prescrito.",
        "transcultural": {
            "preservacao": ["Acolher práticas seguras de cuidado íntimo."],
            "acomodacao": ["Orientar ingestão hídrica e adesão ao tratamento."],
            "repadronizacao": ["Desestimular automedicação e interrupção precoce de antibiótico."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Polaciúria",
        "diagnostico": {"codigo": "10001359", "termo": "Função do Sistema Urinário, Prejudicada"},
        "resultado": {"codigo": "10028615", "termo": "Função do Sistema Urinário, Eficaz"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Média",
        "fundamentacao": "Polaciúria pode ser fisiológica pela compressão uterina, mas quando associada a disúria, urgência, febre ou dor lombar sugere infecção urinária. A enfermagem deve diferenciar sintomas fisiológicos de sinais de infecção.",
        "transcultural": {
            "preservacao": ["Acolher relatos sobre hábitos urinários."],
            "acomodacao": ["Orientar sinais de alerta e hidratação adequada."],
            "repadronizacao": ["Evitar reduzir ingestão hídrica de forma inadequada por medo de urinar."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Urgência urinária",
        "diagnostico": {"codigo": "10001359", "termo": "Função do Sistema Urinário, Prejudicada"},
        "resultado": {"codigo": "10028615", "termo": "Função do Sistema Urinário, Eficaz"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre Infecção"},
        "prioridade": "Média",
        "fundamentacao": "Urgência urinária pode ocorrer por alterações mecânicas da gestação ou infecção urinária. Deve-se investigar disúria, febre, dor lombar, hematúria e orientar coleta de exames e tratamento conforme protocolo.",
        "transcultural": {
            "preservacao": ["Respeitar formas de expressão de sintomas urinários."],
            "acomodacao": ["Garantir privacidade para abordagem do sintoma."],
            "repadronizacao": ["Reforçar que urgência com dor ou febre precisa de avaliação."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Incontinência urinária",
        "diagnostico": {"codigo": "10025686", "termo": "Incontinência Urinária"},
        "resultado": {"codigo": "10028615", "termo": "Função do Sistema Urinário, Eficaz"},
        "intervencao": {"codigo": "10039276", "termo": "Ensinar Exercício"},
        "prioridade": "Baixa",
        "fundamentacao": "Incontinência urinária pode ocorrer por sobrecarga do assoalho pélvico durante a gestação. A enfermagem deve orientar exercícios pélvicos quando indicados, higiene, prevenção de irritações e avaliação de infecção associada.",
        "transcultural": {
            "preservacao": ["Acolher o sintoma sem constrangimento."],
            "acomodacao": ["Orientar exercícios de forma respeitosa e adequada à compreensão da gestante."],
            "repadronizacao": ["Reduzir vergonha e estimular relato do sintoma nas consultas."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Hemorroidas",
        "diagnostico": {"codigo": "10009118", "termo": "Hemorroida"},
        "resultado": {"codigo": "10029008", "termo": "Dor, Ausente"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre Nutrição"},
        "prioridade": "Baixa",
        "fundamentacao": "Hemorroidas são favorecidas por constipação, aumento da pressão venosa e esforço evacuatório. Orienta-se dieta rica em fibras, hidratação, evitar esforço, higiene local e avaliação se sangramento intenso ou dor persistente.",
        "transcultural": {
            "preservacao": ["Respeitar pudor e formas culturais de relatar sintomas anorretais."],
            "acomodacao": ["Orientar medidas alimentares possíveis no território."],
            "repadronizacao": ["Evitar pomadas, supositórios ou chás sem orientação."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Varizes",
        "diagnostico": {"codigo": "10020882", "termo": "Veia Varicosa"},
        "resultado": {"codigo": "10028379", "termo": "Processo do Sistema Circulatório, Positivo"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Baixa",
        "fundamentacao": "Varizes podem surgir ou piorar na gestação por alterações hormonais, compressão venosa e aumento do volume circulante. Orienta-se evitar longos períodos em pé, elevar membros, atividade física segura e observar sinais de trombose.",
        "transcultural": {
            "preservacao": ["Valorizar práticas seguras de repouso e cuidado com pernas."],
            "acomodacao": ["Adaptar orientações às atividades domésticas e laborais."],
            "repadronizacao": ["Orientar busca imediata se dor unilateral, calor, vermelhidão ou edema assimétrico."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Prurido cutâneo",
        "diagnostico": {"codigo": "10010934", "termo": "Prurido"},
        "resultado": {"codigo": "10028337", "termo": "Conforto, Melhorado"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Média",
        "fundamentacao": "Prurido cutâneo pode estar relacionado ao estiramento da pele, alergias, dermatoses gestacionais ou colestase intra-hepática, especialmente quando intenso em palmas e plantas ou associado a icterícia. Deve-se avaliar sinais de gravidade e encaminhar quando indicado.",
        "transcultural": {
            "preservacao": ["Acolher práticas seguras de hidratação da pele."],
            "acomodacao": ["Orientar produtos suaves e evitar irritantes."],
            "repadronizacao": ["Evitar uso de plantas, pomadas ou medicamentos sem avaliação, principalmente em prurido intenso."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Alterações mamárias",
        "diagnostico": {"codigo": "10003595", "termo": "Processo Mamário, Prejudicado"},
        "resultado": {"codigo": "10033682", "termo": "Processo Mamário, Eficaz"},
        "intervencao": {"codigo": "10033017", "termo": "Orientar sobre Amamentação"},
        "prioridade": "Baixa",
        "fundamentacao": "Alterações mamárias como aumento de volume, sensibilidade, escurecimento areolar e colostro podem ser fisiológicas. A consulta deve orientar preparo para amamentação, sinais de alerta e evitar práticas prejudiciais às mamas.",
        "transcultural": {
            "preservacao": ["Valorizar experiências familiares positivas de amamentação."],
            "acomodacao": ["Adequar orientações às crenças e experiências da gestante."],
            "repadronizacao": ["Desencorajar preparo agressivo dos mamilos ou uso de produtos irritantes."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Mastalgia",
        "diagnostico": {"codigo": "10013950", "termo": "Dor"},
        "resultado": {"codigo": "10029008", "termo": "Dor, Ausente"},
        "intervencao": {"codigo": "10033017", "termo": "Orientar sobre Amamentação"},
        "prioridade": "Baixa",
        "fundamentacao": "Mastalgia é comum por alterações hormonais e crescimento mamário. Deve-se orientar sutiã adequado, medidas de conforto e avaliação se houver febre, vermelhidão, nódulo, secreção purulenta ou dor intensa.",
        "transcultural": {
            "preservacao": ["Acolher pudor e crenças sobre exposição das mamas."],
            "acomodacao": ["Garantir privacidade na avaliação e orientação."],
            "repadronizacao": ["Estimular procura de atendimento diante de sinais inflamatórios."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Contrações uterinas",
        "diagnostico": {"codigo": "10006364", "termo": "Contração Uterina"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Contrações uterinas devem ser avaliadas quanto à frequência, intensidade, dor, idade gestacional, perda de líquido, sangramento e alteração dos movimentos fetais. Contrações regulares antes de 37 semanas sugerem risco de trabalho de parto prematuro.",
        "transcultural": {
            "preservacao": ["Acolher a forma como a gestante diferencia dor, cólica e contração."],
            "acomodacao": ["Orientar observação da frequência e duração das contrações."],
            "repadronizacao": ["Reforçar que contrações regulares antes do termo exigem atendimento imediato."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Sinais de trabalho de parto prematuro",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Sinais de trabalho de parto prematuro incluem contrações regulares antes de 37 semanas, dor lombar persistente, pressão pélvica, cólicas, sangramento, alteração do corrimento ou perda de líquido. A condição exige encaminhamento imediato para avaliação obstétrica e prevenção de complicações neonatais.",
        "transcultural": {
            "preservacao": ["Valorizar a percepção da gestante sobre mudanças no corpo."],
            "acomodacao": ["Orientar plano de deslocamento rápido, considerando território e rede de apoio."],
            "repadronizacao": ["Evitar aguardar em casa quando houver sinais de prematuridade."]
        },
        "referencias": ["Ministério da Saúde.", "OMS.", "FEBRASGO.", "COFEN Resolução nº 736/2024.", "Leininger."]
    }
]# modulos/regras_clinicas/prenatal/intercorrencias.py

REGRAS = [
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Pré-eclâmpsia",
        "diagnostico": {"codigo": "10032017", "termo": "Pressão Arterial, Alterada"},
        "resultado": {"codigo": "10027647", "termo": "Pressão Arterial, nos Limites Normais"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "A pré-eclâmpsia é síndrome hipertensiva multissistêmica após 20 semanas de gestação, associada a proteinúria ou sinais de disfunção orgânica, com risco materno-fetal elevado.",
        "transcultural": {
            "preservacao": ["Acolher a compreensão cultural da gestante sobre pressão alta e gravidez."],
            "acomodacao": ["Explicar sinais de alerta em linguagem simples, incluindo cefaleia, escotomas, dor epigástrica e edema súbito."],
            "repadronizacao": ["Reforçar que sintomas graves não devem ser tratados apenas com chás, repouso ou medidas caseiras."]
        },
        "referencias": ["Ministério da Saúde. Manual de Gestação de Alto Risco.", "FEBRASGO. Síndromes hipertensivas na gestação.", "OMS. Recomendações de cuidado pré-natal.", "COFEN Resolução nº 736/2024.", "Leininger. Teoria Transcultural."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Eclâmpsia",
        "diagnostico": {"codigo": "10032017", "termo": "Pressão Arterial, Alterada"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Eclâmpsia corresponde à ocorrência de convulsões em gestante com síndrome hipertensiva, configurando emergência obstétrica com risco de morte materna e fetal.",
        "transcultural": {
            "preservacao": ["Acolher crenças familiares sobre convulsões sem julgamento."],
            "acomodacao": ["Orientar a família sobre necessidade de atendimento de urgência imediato."],
            "repadronizacao": ["Desencorajar práticas que atrasem o encaminhamento, como contenção inadequada ou terapias caseiras."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Síndrome HELLP",
        "diagnostico": {"codigo": "10012606", "termo": "Processo do Sistema Circulatório, Prejudicado"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "A síndrome HELLP é complicação grave da pré-eclâmpsia, caracterizada por hemólise, elevação de enzimas hepáticas e plaquetopenia, exigindo atendimento obstétrico urgente.",
        "transcultural": {
            "preservacao": ["Acolher sintomas referidos pela gestante, como dor epigástrica e mal-estar."],
            "acomodacao": ["Orientar que dor forte no estômago, náuseas intensas ou sangramentos podem indicar gravidade."],
            "repadronizacao": ["Evitar banalização de dor epigástrica como azia comum da gravidez."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Hipertensão gestacional grave",
        "diagnostico": {"codigo": "10032017", "termo": "Pressão Arterial, Alterada"},
        "resultado": {"codigo": "10027647", "termo": "Pressão Arterial, nos Limites Normais"},
        "intervencao": {"codigo": "10044148", "termo": "Orientar sobre Medição de Pressão Arterial"},
        "prioridade": "Alta",
        "fundamentacao": "Hipertensão gestacional grave aumenta risco de pré-eclâmpsia, eclâmpsia, AVC, descolamento placentário, restrição de crescimento fetal e prematuridade.",
        "transcultural": {
            "preservacao": ["Valorizar cuidados familiares de proteção à gestante."],
            "acomodacao": ["Orientar aferição regular da pressão arterial e retorno imediato em sinais de alerta."],
            "repadronizacao": ["Desestimular abandono do tratamento anti-hipertensivo por medo de prejudicar o bebê."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Crise hipertensiva",
        "diagnostico": {"codigo": "10032017", "termo": "Pressão Arterial, Alterada"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Crise hipertensiva na gestação é emergência clínica e obstétrica, especialmente quando associada a sintomas neurológicos, dor epigástrica, dispneia ou alterações fetais.",
        "transcultural": {
            "preservacao": ["Acolher preocupações da família sobre internação e medicação."],
            "acomodacao": ["Explicar risco de complicações maternas e fetais de forma objetiva."],
            "repadronizacao": ["Reforçar que pressão muito elevada exige atendimento imediato."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "ITU",
        "diagnostico": {"codigo": "10029915", "termo": "Infecção do Trato Urinário"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre Infecção"},
        "prioridade": "Alta",
        "fundamentacao": "Infecção do trato urinário na gestação aumenta risco de pielonefrite, trabalho de parto prematuro e baixo peso ao nascer, exigindo tratamento adequado e controle.",
        "transcultural": {
            "preservacao": ["Reconhecer práticas seguras de higiene íntima já utilizadas."],
            "acomodacao": ["Orientar hidratação, coleta adequada de urina e adesão ao antibiótico prescrito."],
            "repadronizacao": ["Evitar automedicação e interrupção do tratamento após melhora dos sintomas."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Pielonefrite",
        "diagnostico": {"codigo": "10029915", "termo": "Infecção do Trato Urinário"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Pielonefrite na gestação é infecção urinária alta, geralmente com febre, dor lombar e comprometimento sistêmico, podendo causar sepse, prematuridade e complicações maternas.",
        "transcultural": {
            "preservacao": ["Acolher relatos de dor lombar e febre conforme linguagem local."],
            "acomodacao": ["Orientar urgência de atendimento, mesmo que a gestante já use medidas caseiras."],
            "repadronizacao": ["Reforçar que febre com dor lombar na gestação não deve ser tratada apenas em casa."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Bacteriúria assintomática",
        "diagnostico": {"codigo": "10051950", "termo": "Risco de Infecção Urinária"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10038112", "termo": "Orientar sobre Prevenção de Infecção Cruzada"},
        "prioridade": "Alta",
        "fundamentacao": "Bacteriúria assintomática na gestação deve ser tratada conforme protocolo, pois pode evoluir para pielonefrite e aumentar risco de complicações obstétricas.",
        "transcultural": {
            "preservacao": ["Acolher a percepção de ausência de doença por não haver sintomas."],
            "acomodacao": ["Explicar que infecção pode existir mesmo sem dor ou ardência."],
            "repadronizacao": ["Reforçar necessidade de tratamento completo e controle laboratorial."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Candidíase",
        "diagnostico": {"codigo": "10023032", "termo": "Infecção"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre Infecção"},
        "prioridade": "Média",
        "fundamentacao": "Candidíase vulvovaginal é frequente na gestação e pode causar corrimento, prurido e desconforto, exigindo diagnóstico clínico e tratamento seguro para gestantes.",
        "transcultural": {
            "preservacao": ["Acolher pudor e crenças sobre sintomas íntimos."],
            "acomodacao": ["Garantir privacidade e orientar higiene íntima adequada."],
            "repadronizacao": ["Desencorajar duchas vaginais, pomadas sem prescrição e receitas caseiras intravaginais."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Vaginose bacteriana",
        "diagnostico": {"codigo": "10023032", "termo": "Infecção"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre Infecção"},
        "prioridade": "Média",
        "fundamentacao": "Vaginose bacteriana pode cursar com corrimento e odor vaginal, sendo associada a maior risco de complicações obstétricas quando sintomática.",
        "transcultural": {
            "preservacao": ["Respeitar formas culturais de cuidado íntimo que não causem dano."],
            "acomodacao": ["Orientar tratamento prescrito e evitar produtos irritantes."],
            "repadronizacao": ["Reorientar a crença de que odor vaginal deve ser tratado com duchas ou substâncias caseiras."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Tricomoníase",
        "diagnostico": {"codigo": "10023032", "termo": "Infecção"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre Infecção"},
        "prioridade": "Média",
        "fundamentacao": "Tricomoníase é infecção sexualmente transmissível que pode causar corrimento, prurido e desconforto, exigindo tratamento da gestante e avaliação da parceria sexual.",
        "transcultural": {
            "preservacao": ["Acolher a gestante sem julgamento moral."],
            "acomodacao": ["Orientar prevenção de reinfecção e necessidade de abordagem da parceria."],
            "repadronizacao": ["Reduzir estigma e reforçar tratamento adequado como proteção materno-fetal."]
        },
        "referencias": ["Ministério da Saúde. PCDT IST.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Sangramento vaginal no primeiro trimestre",
        "diagnostico": {"codigo": "10003303", "termo": "Sangramento"},
        "resultado": {"codigo": "10028120", "termo": "Sangramento, Ausente"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Sangramento no primeiro trimestre pode estar associado a ameaça de abortamento, abortamento em curso, gravidez ectópica ou doença trofoblástica, necessitando avaliação imediata.",
        "transcultural": {
            "preservacao": ["Acolher medos e crenças familiares sobre perda gestacional."],
            "acomodacao": ["Orientar sinais de gravidade e necessidade de avaliação mesmo com pequeno volume."],
            "repadronizacao": ["Evitar culpabilização da gestante e atraso na busca por cuidado."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Sangramento vaginal no segundo trimestre",
        "diagnostico": {"codigo": "10003303", "termo": "Sangramento"},
        "resultado": {"codigo": "10028120", "termo": "Sangramento, Ausente"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Sangramento no segundo trimestre pode indicar condições obstétricas relevantes, como alterações placentárias, abortamento tardio, insuficiência cervical ou trabalho de parto prematuro.",
        "transcultural": {
            "preservacao": ["Acolher a descrição da gestante sobre cor, volume e dor."],
            "acomodacao": ["Explicar que todo sangramento na gestação exige avaliação."],
            "repadronizacao": ["Evitar observação domiciliar prolongada sem avaliação profissional."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Sangramento vaginal no terceiro trimestre",
        "diagnostico": {"codigo": "10003303", "termo": "Sangramento"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Sangramento no terceiro trimestre pode estar associado a placenta prévia, descolamento prematuro de placenta ou início de trabalho de parto, exigindo avaliação obstétrica urgente.",
        "transcultural": {
            "preservacao": ["Acolher práticas familiares de apoio durante urgências."],
            "acomodacao": ["Orientar deslocamento imediato e evitar toque vaginal fora de ambiente adequado."],
            "repadronizacao": ["Reforçar que sangramento no fim da gestação pode ser emergência."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Ameaça de abortamento",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Ameaça de abortamento é caracterizada por sangramento vaginal no início da gestação com colo geralmente fechado, exigindo avaliação clínica e ultrassonográfica quando indicada.",
        "transcultural": {
            "preservacao": ["Acolher sofrimento emocional e crenças sobre perda gestacional."],
            "acomodacao": ["Orientar repouso relativo conforme avaliação e retorno se piora."],
            "repadronizacao": ["Evitar culpa, automedicação e práticas invasivas caseiras."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Abortamento",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10028379", "termo": "Processo do Sistema Circulatório, Positivo"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Abortamento pode apresentar sangramento, dor abdominal, eliminação de tecidos e risco de hemorragia, infecção e sofrimento psíquico, requerendo assistência imediata e humanizada.",
        "transcultural": {
            "preservacao": ["Respeitar luto, crenças espirituais e rituais familiares seguros."],
            "acomodacao": ["Oferecer acolhimento, privacidade e orientação sobre sinais de gravidade."],
            "repadronizacao": ["Combater julgamento, culpa e abandono do cuidado pós-evento."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Placenta prévia",
        "diagnostico": {"codigo": "10003303", "termo": "Sangramento"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Placenta prévia pode causar sangramento vaginal indolor no segundo ou terceiro trimestre e está associada a risco hemorrágico materno-fetal, exigindo acompanhamento especializado.",
        "transcultural": {
            "preservacao": ["Acolher medo da gestante diante do sangramento."],
            "acomodacao": ["Orientar repouso, sinais de alerta e comparecimento imediato se sangrar."],
            "repadronizacao": ["Evitar toque vaginal e práticas caseiras diante de sangramento."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Descolamento prematuro de placenta",
        "diagnostico": {"codigo": "10003303", "termo": "Sangramento"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Descolamento prematuro de placenta é emergência obstétrica, podendo causar dor abdominal intensa, hipertonia uterina, sangramento e sofrimento fetal.",
        "transcultural": {
            "preservacao": ["Acolher a percepção materna de dor intensa ou mudança súbita."],
            "acomodacao": ["Orientar que dor forte com sangramento ou mal-estar exige urgência."],
            "repadronizacao": ["Evitar espera domiciliar por melhora espontânea."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Rotura prematura de membranas",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Rotura prematura de membranas aumenta risco de infecção, prematuridade e sofrimento fetal, exigindo avaliação obstétrica imediata e conduta conforme idade gestacional.",
        "transcultural": {
            "preservacao": ["Valorizar o relato da gestante sobre perda de líquido."],
            "acomodacao": ["Orientar observar cor, odor e quantidade, sem retardar atendimento."],
            "repadronizacao": ["Evitar banho de imersão, relação sexual ou toque vaginal após perda de líquido."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Trabalho de parto prematuro",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Trabalho de parto antes de 37 semanas está associado a morbimortalidade neonatal, exigindo reconhecimento precoce de contrações regulares, dor lombar, pressão pélvica, sangramento ou perda de líquido.",
        "transcultural": {
            "preservacao": ["Valorizar a percepção da gestante sobre sinais corporais."],
            "acomodacao": ["Construir plano de deslocamento rápido, considerando território e transporte."],
            "repadronizacao": ["Reforçar que contrações antes do termo não devem ser aguardadas em casa."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Contrações uterinas prematuras",
        "diagnostico": {"codigo": "10006364", "termo": "Contração Uterina"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Contrações uterinas prematuras podem indicar ameaça de trabalho de parto prematuro, especialmente quando regulares, dolorosas ou associadas a perda de líquido e sangramento.",
        "transcultural": {
            "preservacao": ["Acolher a forma como a gestante descreve cólicas e endurecimento uterino."],
            "acomodacao": ["Orientar registro de frequência e duração das contrações."],
            "repadronizacao": ["Evitar normalizar contrações regulares antes de 37 semanas."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Restrição de crescimento fetal",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Restrição de crescimento fetal indica risco de insuficiência placentária, hipóxia, morbidade neonatal e óbito fetal, exigindo investigação, vigilância fetal e acompanhamento especializado.",
        "transcultural": {
            "preservacao": ["Valorizar práticas familiares de cuidado nutricional e repouso seguro."],
            "acomodacao": ["Orientar importância do acompanhamento e dos exames seriados."],
            "repadronizacao": ["Evitar atribuir baixo crescimento fetal apenas a característica familiar sem avaliação."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Oligodrâmnio",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Oligodrâmnio pode estar relacionado a rotura de membranas, insuficiência placentária, restrição de crescimento fetal ou malformações, exigindo avaliação obstétrica e vigilância fetal.",
        "transcultural": {
            "preservacao": ["Acolher preocupações familiares sobre o líquido amniótico."],
            "acomodacao": ["Orientar sinais de alerta, como perda de líquido e redução dos movimentos fetais."],
            "repadronizacao": ["Evitar interpretação de que hidratação isolada resolve todos os casos sem avaliação médica."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Polidrâmnio",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Polidrâmnio pode estar associado a diabetes gestacional, alterações fetais, infecções ou outras condições, aumentando risco de parto prematuro e complicações obstétricas.",
        "transcultural": {
            "preservacao": ["Acolher explicações culturais sobre aumento exagerado da barriga."],
            "acomodacao": ["Orientar necessidade de investigação e controle glicêmico quando indicado."],
            "repadronizacao": ["Evitar normalizar crescimento uterino excessivo sem avaliação."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Sofrimento fetal suspeito",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Sofrimento fetal suspeito pode ser indicado por alteração de batimentos cardíacos fetais, redução de movimentos fetais ou condições maternas graves, exigindo avaliação obstétrica imediata.",
        "transcultural": {
            "preservacao": ["Valorizar a percepção materna sobre o comportamento fetal."],
            "acomodacao": ["Orientar sinais que exigem procura imediata do serviço."],
            "repadronizacao": ["Evitar aguardar retorno programado quando há suspeita de alteração fetal."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Redução dos movimentos fetais",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Redução dos movimentos fetais pode indicar comprometimento fetal e deve ser valorizada, especialmente após a gestante reconhecer o padrão habitual de movimentação.",
        "transcultural": {
            "preservacao": ["Valorizar o conhecimento materno sobre o padrão do bebê."],
            "acomodacao": ["Orientar busca imediata se houver redução importante ou ausência de movimentos."],
            "repadronizacao": ["Desestimular esperar dias para avaliação por acreditar que o bebê está apenas dormindo."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Hiperêmese gravídica",
        "diagnostico": {"codigo": "10020864", "termo": "Vômito"},
        "resultado": {"codigo": "10027617", "termo": "Equilíbrio Hídrico, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Hiperêmese gravídica envolve vômitos intensos, perda ponderal, desidratação e possível distúrbio eletrolítico, podendo exigir hidratação venosa e suporte clínico.",
        "transcultural": {
            "preservacao": ["Acolher práticas alimentares seguras que melhorem náuseas."],
            "acomodacao": ["Orientar sinais de desidratação e necessidade de atendimento."],
            "repadronizacao": ["Evitar automedicação e uso de ervas sem segurança na gestação."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Desidratação",
        "diagnostico": {"codigo": "10041895", "termo": "Desidratação"},
        "resultado": {"codigo": "10027617", "termo": "Equilíbrio Hídrico, Eficaz"},
        "intervencao": {"codigo": "10036112", "termo": "Orientar sobre Hidratação"},
        "prioridade": "Alta",
        "fundamentacao": "Desidratação na gestação pode decorrer de vômitos, diarreia, febre ou baixa ingestão hídrica, aumentando risco de hipotensão, contrações e comprometimento materno-fetal.",
        "transcultural": {
            "preservacao": ["Valorizar bebidas e alimentos locais seguros que favoreçam hidratação."],
            "acomodacao": ["Orientar ingestão hídrica fracionada conforme tolerância."],
            "repadronizacao": ["Evitar restrição hídrica por medo de urinar com frequência."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Anemia grave",
        "diagnostico": {"codigo": "10012606", "termo": "Processo do Sistema Circulatório, Prejudicado"},
        "resultado": {"codigo": "10028379", "termo": "Processo do Sistema Circulatório, Positivo"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre Nutrição"},
        "prioridade": "Alta",
        "fundamentacao": "Anemia grave na gestação aumenta risco de fadiga intensa, infecção, parto prematuro, baixo peso ao nascer, hemorragia e desfechos materno-fetais adversos.",
        "transcultural": {
            "preservacao": ["Estimular alimentos regionais ricos em ferro e culturalmente aceitos."],
            "acomodacao": ["Adequar suplementação e alimentação à rotina e tolerância da gestante."],
            "repadronizacao": ["Orientar evitar café ou chá junto das refeições e não suspender ferro sem avaliação."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Diabetes gestacional descompensado",
        "diagnostico": {"codigo": "10005876", "termo": "Diabetes"},
        "resultado": {"codigo": "10027532", "termo": "Processo do Sistema Regulatório, Eficaz"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Alta",
        "fundamentacao": "Diabetes gestacional descompensado aumenta risco de macrossomia, pré-eclâmpsia, parto traumático, hipoglicemia neonatal e complicações metabólicas.",
        "transcultural": {
            "preservacao": ["Preservar alimentos culturais compatíveis com controle glicêmico."],
            "acomodacao": ["Adaptar plano alimentar à renda, acesso e rotina familiar."],
            "repadronizacao": ["Reduzir consumo de açúcar, bebidas adoçadas e ultraprocessados."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Febre na gestação",
        "diagnostico": {"codigo": "10007916", "termo": "Febre"},
        "resultado": {"codigo": "10033694", "termo": "Temperatura Corporal, nos Limites Normais"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Febre na gestação pode indicar infecção urinária, respiratória, intra-amniótica, arbovirose ou outras condições com risco materno-fetal, exigindo investigação.",
        "transcultural": {
            "preservacao": ["Acolher práticas seguras de conforto térmico."],
            "acomodacao": ["Orientar hidratação, monitoramento e sinais de gravidade."],
            "repadronizacao": ["Evitar automedicação e uso de chás sem segurança gestacional."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Dengue na gestação",
        "diagnostico": {"codigo": "10023032", "termo": "Infecção"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Dengue na gestação aumenta risco de desidratação, sangramentos, plaquetopenia, parto prematuro e complicações maternas, exigindo acompanhamento clínico rigoroso.",
        "transcultural": {
            "preservacao": ["Valorizar medidas comunitárias de eliminação de criadouros."],
            "acomodacao": ["Orientar hidratação, sinais de alarme e proteção contra mosquitos."],
            "repadronizacao": ["Evitar anti-inflamatórios e automedicação, especialmente diante de suspeita de dengue."]
        },
        "referencias": ["Ministério da Saúde. Arboviroses na gestação.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Zika na gestação",
        "diagnostico": {"codigo": "10023032", "termo": "Infecção"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Infecção por Zika na gestação está associada a risco de síndrome congênita, alterações neurológicas fetais e necessidade de vigilância ultrassonográfica e acompanhamento especializado.",
        "transcultural": {
            "preservacao": ["Valorizar estratégias comunitárias de prevenção ao mosquito."],
            "acomodacao": ["Orientar uso de repelente seguro, barreiras físicas e acompanhamento fetal."],
            "repadronizacao": ["Evitar minimizar exantema, febre baixa ou conjuntivite em área de transmissão."]
        },
        "referencias": ["Ministério da Saúde. Zika e gestação.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "Chikungunya na gestação",
        "diagnostico": {"codigo": "10023032", "termo": "Infecção"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Chikungunya na gestação pode causar febre, artralgia intensa e risco de transmissão perinatal quando ocorre próximo ao parto, exigindo vigilância clínica e obstétrica.",
        "transcultural": {
            "preservacao": ["Valorizar medidas locais de proteção contra mosquitos."],
            "acomodacao": ["Orientar repouso, hidratação e sinais de gravidade."],
            "repadronizacao": ["Evitar automedicação com anti-inflamatórios sem avaliação profissional."]
        },
        "referencias": ["Ministério da Saúde. Arboviroses.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Intercorrências obstétricas",
        "achado_clinico": "COVID-19 na gestação",
        "diagnostico": {"codigo": "10023032", "termo": "Infecção"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "COVID-19 na gestação pode aumentar risco de complicações respiratórias, internação, prematuridade e agravamento em gestantes com comorbidades, exigindo avaliação de gravidade, isolamento orientado e acompanhamento.",
        "transcultural": {
            "preservacao": ["Acolher crenças familiares sobre infecções respiratórias sem julgamento."],
            "acomodacao": ["Orientar sinais de alerta respiratório, vacinação e medidas preventivas."],
            "repadronizacao": ["Combater desinformação sobre COVID-19, vacinação e segurança materno-fetal."]
        },
        "referencias": ["Ministério da Saúde. COVID-19 e gestação.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    }
]# modulos/regras_clinicas/prenatal/medicacoes.py

REGRAS = [
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Ácido fólico não iniciado",
        "diagnostico": {"codigo": "10024625", "termo": "Regime Terapêutico, Prejudicado"},
        "resultado": {"codigo": "10030185", "termo": "Adesão ao Regime Terapêutico"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre Medicação"},
        "prioridade": "Alta",
        "fundamentacao": "O ácido fólico é recomendado no período periconcepcional e no início da gestação para reduzir o risco de defeitos do tubo neural. Quando não iniciado, a enfermagem deve orientar início conforme protocolo, verificar acesso ao suplemento, registrar conduta e reforçar adesão.",
        "transcultural": {
            "preservacao": ["Valorizar práticas alimentares seguras e alimentos regionais ricos em folato."],
            "acomodacao": ["Adequar a orientação ao acesso da gestante à farmácia da unidade e à rotina diária."],
            "repadronizacao": ["Reorientar a ideia de que suplemento só é necessário quando há sintomas."]
        },
        "referencias": ["Ministério da Saúde. Atenção ao pré-natal de baixo risco.", "FEBRASGO. Assistência pré-natal.", "OMS. Recomendações sobre cuidado pré-natal.", "COFEN Resolução nº 736/2024.", "Leininger. Teoria Transcultural."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Ácido fólico iniciado tardiamente",
        "diagnostico": {"codigo": "10024625", "termo": "Regime Terapêutico, Prejudicado"},
        "resultado": {"codigo": "10030185", "termo": "Adesão ao Regime Terapêutico"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre Medicação"},
        "prioridade": "Média",
        "fundamentacao": "O início tardio do ácido fólico reduz o benefício máximo esperado na prevenção de defeitos do tubo neural, especialmente quando iniciado após o período de fechamento do tubo neural. Ainda assim, deve-se orientar continuidade conforme protocolo e reforçar suplementação adequada.",
        "transcultural": {
            "preservacao": ["Acolher a história da gestante sem culpabilização."],
            "acomodacao": ["Explicar a finalidade do suplemento em linguagem simples."],
            "repadronizacao": ["Estimular início precoce em futuras gestações e planejamento reprodutivo."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Baixa adesão ao ácido fólico",
        "diagnostico": {"codigo": "10022155", "termo": "Adesão ao Regime Terapêutico, Prejudicada"},
        "resultado": {"codigo": "10030185", "termo": "Adesão ao Regime Terapêutico"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Média",
        "fundamentacao": "A baixa adesão ao ácido fólico compromete a efetividade da suplementação. A equipe deve investigar esquecimento, efeitos adversos, acesso, compreensão da prescrição e crenças sobre medicamentos na gestação.",
        "transcultural": {
            "preservacao": ["Respeitar valores da gestante sobre uso de medicamentos."],
            "acomodacao": ["Pactuar horário de uso associado a rotina já existente."],
            "repadronizacao": ["Reformular crenças de que vitaminas fazem mal ao bebê."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Sulfato ferroso não iniciado",
        "diagnostico": {"codigo": "10023009", "termo": "Ingestão Nutricional, Prejudicada"},
        "resultado": {"codigo": "10037572", "termo": "Ingestão Nutricional, nos Limites Normais"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre Medicação"},
        "prioridade": "Alta",
        "fundamentacao": "A suplementação de ferro no pré-natal é recomendada para prevenção e tratamento da anemia ferropriva, condição associada a fadiga, infecção, prematuridade e baixo peso ao nascer. Deve-se orientar início conforme protocolo e avaliar hemoglobina, ferritina e tolerância.",
        "transcultural": {
            "preservacao": ["Valorizar alimentos locais ricos em ferro."],
            "acomodacao": ["Adequar horário de uso para reduzir desconfortos gastrointestinais."],
            "repadronizacao": ["Orientar evitar café, chá preto ou leite junto ao ferro, pois podem reduzir absorção."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Baixa adesão ao sulfato ferroso",
        "diagnostico": {"codigo": "10022155", "termo": "Adesão ao Regime Terapêutico, Prejudicada"},
        "resultado": {"codigo": "10030185", "termo": "Adesão ao Regime Terapêutico"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Alta",
        "fundamentacao": "A baixa adesão ao sulfato ferroso mantém risco de anemia gestacional e suas complicações. A enfermagem deve investigar eventos adversos, esquecimento, acesso ao medicamento e orientar estratégias para melhorar a tolerância e continuidade.",
        "transcultural": {
            "preservacao": ["Acolher relatos sobre intolerância e experiências anteriores."],
            "acomodacao": ["Negociar horário de uso e estratégias alimentares possíveis."],
            "repadronizacao": ["Reforçar que escurecimento das fezes é esperado e não deve motivar suspensão isolada."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Náuseas associadas ao sulfato ferroso",
        "diagnostico": {"codigo": "10012453", "termo": "Náusea"},
        "resultado": {"codigo": "10028992", "termo": "Náusea, Ausente"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre Medicação"},
        "prioridade": "Média",
        "fundamentacao": "Náuseas podem ocorrer com uso de sulfato ferroso e reduzir adesão. Deve-se orientar forma correta de uso, avaliar possibilidade de tomada após alimento leve quando necessário, verificar gravidade e encaminhar para ajuste terapêutico se intolerância persistente.",
        "transcultural": {
            "preservacao": ["Valorizar alimentos culturalmente aceitos que reduzam enjoo."],
            "acomodacao": ["Ajustar horário de uso conforme maior tolerância da gestante."],
            "repadronizacao": ["Evitar suspensão sem comunicação à equipe de saúde."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Constipação associada ao sulfato ferroso",
        "diagnostico": {"codigo": "10004999", "termo": "Constipação"},
        "resultado": {"codigo": "10027800", "termo": "Eliminação Intestinal, Eficaz"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre Nutrição"},
        "prioridade": "Média",
        "fundamentacao": "O sulfato ferroso pode agravar constipação, sintoma já comum na gestação. A enfermagem deve orientar ingestão hídrica, fibras, atividade física segura e comunicar a equipe caso o efeito adverso comprometa a adesão.",
        "transcultural": {
            "preservacao": ["Estimular alimentos regionais ricos em fibras."],
            "acomodacao": ["Adequar hidratação à realidade de acesso à água segura."],
            "repadronizacao": ["Evitar laxantes, chás purgativos ou automedicação."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Cálcio indicado",
        "diagnostico": {"codigo": "10023009", "termo": "Ingestão Nutricional, Prejudicada"},
        "resultado": {"codigo": "10037572", "termo": "Ingestão Nutricional, nos Limites Normais"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre Medicação"},
        "prioridade": "Média",
        "fundamentacao": "A suplementação de cálcio pode ser indicada em gestantes com baixa ingestão dietética ou maior risco de pré-eclâmpsia, conforme avaliação clínica e protocolo. Deve-se orientar uso correto, intervalo em relação ao ferro e acompanhamento.",
        "transcultural": {
            "preservacao": ["Valorizar fontes alimentares culturais de cálcio."],
            "acomodacao": ["Adequar suplementação ao horário possível e à rotina alimentar."],
            "repadronizacao": ["Orientar não tomar cálcio junto ao ferro para não prejudicar absorção."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Baixa adesão ao cálcio",
        "diagnostico": {"codigo": "10022155", "termo": "Adesão ao Regime Terapêutico, Prejudicada"},
        "resultado": {"codigo": "10030185", "termo": "Adesão ao Regime Terapêutico"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Média",
        "fundamentacao": "A baixa adesão ao cálcio reduz o potencial benefício preventivo em gestantes com indicação. A enfermagem deve identificar esquecimento, efeitos gastrointestinais, dificuldade de acesso e orientar horários separados do sulfato ferroso.",
        "transcultural": {
            "preservacao": ["Considerar hábitos alimentares e crenças sobre leite e derivados."],
            "acomodacao": ["Pactuar horários simples para evitar esquecimento."],
            "repadronizacao": ["Reforçar finalidade preventiva da suplementação quando indicada."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Uso inadequado de medicamentos na gestação",
        "diagnostico": {"codigo": "10022155", "termo": "Adesão ao Regime Terapêutico, Prejudicada"},
        "resultado": {"codigo": "10030185", "termo": "Adesão ao Regime Terapêutico"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre Medicação"},
        "prioridade": "Alta",
        "fundamentacao": "O uso inadequado de medicamentos na gestação pode expor mãe e feto a riscos evitáveis, incluindo toxicidade, efeitos teratogênicos, interações e falha terapêutica. Deve-se revisar todos os medicamentos em uso e encaminhar para avaliação quando houver risco.",
        "transcultural": {
            "preservacao": ["Acolher práticas familiares de cuidado sem julgamento."],
            "acomodacao": ["Solicitar que a gestante leve medicamentos, receitas e produtos usados às consultas."],
            "repadronizacao": ["Reforçar que todo medicamento na gestação deve ser avaliado por profissional de saúde."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Automedicação",
        "diagnostico": {"codigo": "10025806", "termo": "Comportamento de Saúde, Prejudicado"},
        "resultado": {"codigo": "10028276", "termo": "Comportamento de Saúde, Positivo"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre Medicação"},
        "prioridade": "Alta",
        "fundamentacao": "A automedicação na gestação pode causar eventos adversos maternos e fetais, mascarar sinais de gravidade e retardar diagnóstico. A enfermagem deve investigar substâncias utilizadas, orientar riscos e fortalecer acesso à avaliação profissional.",
        "transcultural": {
            "preservacao": ["Reconhecer o papel da família na tomada de decisão sobre cuidados."],
            "acomodacao": ["Orientar alternativas seguras de procura do serviço de saúde."],
            "repadronizacao": ["Modificar a prática de usar medicamentos por indicação de terceiros."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Uso de anti-inflamatório sem orientação",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10028120", "termo": "Risco, Reduzido"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre Medicação"},
        "prioridade": "Alta",
        "fundamentacao": "Anti-inflamatórios não esteroidais podem apresentar riscos na gestação, especialmente em fases específicas, incluindo alterações fetais, renais, ducto arterioso e complicações maternas. O uso sem orientação deve ser interrompido e avaliado por profissional habilitado.",
        "transcultural": {
            "preservacao": ["Acolher a motivação da gestante para alívio da dor."],
            "acomodacao": ["Orientar busca de alternativas seguras prescritas pela equipe."],
            "repadronizacao": ["Evitar uso de anti-inflamatórios por conta própria durante a gestação."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Uso de fitoterápico sem avaliação",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10028120", "termo": "Risco, Reduzido"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre Medicação"},
        "prioridade": "Média",
        "fundamentacao": "Fitoterápicos podem conter substâncias com efeitos uterotônicos, hepatotóxicos, nefrotóxicos, anticoagulantes ou interações medicamentosas. Na gestação, seu uso deve ser avaliado quanto à segurança, dose, procedência e indicação.",
        "transcultural": {
            "preservacao": ["Respeitar o uso tradicional de plantas como parte da cultura familiar."],
            "acomodacao": ["Dialogar sobre quais produtos são usados, finalidade e frequência."],
            "repadronizacao": ["Substituir práticas de risco por alternativas seguras pactuadas com a equipe."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Uso de plantas medicinais com risco gestacional",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10028120", "termo": "Risco, Reduzido"},
        "intervencao": {"codigo": "10019502", "termo": "Orientar sobre Segurança"},
        "prioridade": "Alta",
        "fundamentacao": "Algumas plantas medicinais podem provocar contrações uterinas, sangramento, toxicidade, alterações hepáticas ou interação com medicamentos. A enfermagem deve identificar uso, orientar riscos e comunicar a equipe para avaliação segura.",
        "transcultural": {
            "preservacao": ["Valorizar saberes tradicionais que não coloquem a gestação em risco."],
            "acomodacao": ["Negociar suspensão ou substituição de plantas potencialmente perigosas."],
            "repadronizacao": ["Reorientar a crença de que todo produto natural é seguro na gravidez."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Anti-hipertensivo prescrito",
        "diagnostico": {"codigo": "10009394", "termo": "Hipertensão"},
        "resultado": {"codigo": "10027647", "termo": "Pressão Arterial, nos Limites Normais"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre Medicação"},
        "prioridade": "Alta",
        "fundamentacao": "O uso de anti-hipertensivo na gestação pode ser necessário para controle pressórico e prevenção de complicações como pré-eclâmpsia grave, AVC, restrição de crescimento fetal e desfechos maternos adversos. A enfermagem deve orientar uso correto, monitoramento da pressão e sinais de alerta.",
        "transcultural": {
            "preservacao": ["Acolher práticas seguras de autocuidado e apoio familiar."],
            "acomodacao": ["Pactuar horários de uso conforme rotina da gestante."],
            "repadronizacao": ["Reforçar que pressão controlada não significa suspender medicamento sem orientação."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Baixa adesão ao anti-hipertensivo",
        "diagnostico": {"codigo": "10022155", "termo": "Adesão ao Regime Terapêutico, Prejudicada"},
        "resultado": {"codigo": "10030185", "termo": "Adesão ao Regime Terapêutico"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Alta",
        "fundamentacao": "A baixa adesão ao anti-hipertensivo aumenta risco de crise hipertensiva, pré-eclâmpsia grave, eclâmpsia, descolamento placentário e complicações fetais. É necessário investigar barreiras, orientar sinais de alerta e reforçar acompanhamento.",
        "transcultural": {
            "preservacao": ["Reconhecer crenças familiares sobre pressão alta."],
            "acomodacao": ["Usar lembretes e rotina diária para melhorar adesão."],
            "repadronizacao": ["Desestimular suspensão por melhora dos sintomas ou ausência de sintomas."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Efeitos adversos do anti-hipertensivo",
        "diagnostico": {"codigo": "10033557", "termo": "Efeito Secundário da Medicação"},
        "resultado": {"codigo": "10030185", "termo": "Adesão ao Regime Terapêutico"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre Medicação"},
        "prioridade": "Alta",
        "fundamentacao": "Efeitos adversos podem comprometer adesão ao anti-hipertensivo e exigem avaliação clínica para ajuste seguro. Sintomas como tontura intensa, síncope, dispneia, edema importante ou piora clínica devem ser comunicados imediatamente.",
        "transcultural": {
            "preservacao": ["Acolher relatos da gestante sobre sensações após o medicamento."],
            "acomodacao": ["Orientar registro de sintomas, horários e pressão arterial quando possível."],
            "repadronizacao": ["Evitar interrupção espontânea do tratamento por efeitos adversos sem avaliação."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Insulina prescrita",
        "diagnostico": {"codigo": "10005876", "termo": "Diabetes"},
        "resultado": {"codigo": "10027532", "termo": "Processo do Sistema Regulatório, Eficaz"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre Medicação"},
        "prioridade": "Alta",
        "fundamentacao": "A insulina pode ser indicada no diabetes gestacional ou diabetes prévio quando medidas alimentares e atividade física não são suficientes ou conforme avaliação clínica. O uso correto reduz hiperglicemia materna e complicações fetais.",
        "transcultural": {
            "preservacao": ["Valorizar o cuidado familiar no apoio ao tratamento."],
            "acomodacao": ["Ensinar aplicação considerando rotina, escolaridade e acesso a insumos."],
            "repadronizacao": ["Reforçar que insulina não representa fracasso da gestante, mas proteção materno-fetal."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Dificuldade no uso de insulina",
        "diagnostico": {"codigo": "10022155", "termo": "Adesão ao Regime Terapêutico, Prejudicada"},
        "resultado": {"codigo": "10030185", "termo": "Adesão ao Regime Terapêutico"},
        "intervencao": {"codigo": "10019502", "termo": "Orientar sobre Segurança"},
        "prioridade": "Alta",
        "fundamentacao": "Dificuldade no preparo, dose, aplicação, rodízio de locais ou descarte de materiais pode gerar hiperglicemia, hipoglicemia ou lesões locais. A enfermagem deve demonstrar a técnica, observar retorno demonstrativo e reforçar armazenamento e descarte.",
        "transcultural": {
            "preservacao": ["Incluir pessoa de confiança quando a gestante desejar."],
            "acomodacao": ["Usar demonstração prática e linguagem simples."],
            "repadronizacao": ["Corrigir técnicas inseguras de aplicação ou reutilização inadequada de materiais."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Medo de aplicar insulina",
        "diagnostico": {"codigo": "10007738", "termo": "Medo"},
        "resultado": {"codigo": "10027858", "termo": "Medo, Reduzido"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Alta",
        "fundamentacao": "O medo da aplicação de insulina pode levar à omissão de doses e descontrole glicêmico. A enfermagem deve acolher, demonstrar técnica, permitir treino supervisionado e reforçar benefícios para mãe e feto.",
        "transcultural": {
            "preservacao": ["Acolher experiências familiares com injeções e diabetes."],
            "acomodacao": ["Permitir apoio de familiar ou cuidador escolhido pela gestante."],
            "repadronizacao": ["Reduzir crenças de que insulina causa dependência ou prejudica o bebê."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Falta de armazenamento adequado da insulina",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10028120", "termo": "Risco, Reduzido"},
        "intervencao": {"codigo": "10019502", "termo": "Orientar sobre Segurança"},
        "prioridade": "Alta",
        "fundamentacao": "Armazenamento inadequado pode comprometer a estabilidade da insulina e prejudicar o controle glicêmico. Deve-se orientar conservação conforme apresentação, proteção contra calor e congelamento, transporte seguro e descarte de insumos.",
        "transcultural": {
            "preservacao": ["Reconhecer limitações territoriais, como ausência de energia elétrica contínua."],
            "acomodacao": ["Construir estratégia viável de conservação com a família e a rede de saúde."],
            "repadronizacao": ["Evitar exposição da insulina ao sol, calor excessivo ou congelamento."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Antibiótico prescrito para ITU",
        "diagnostico": {"codigo": "10029915", "termo": "Infecção do Trato Urinário"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre Medicação"},
        "prioridade": "Alta",
        "fundamentacao": "ITU na gestação deve ser tratada adequadamente para prevenir pielonefrite, parto prematuro e baixo peso ao nascer. A enfermagem deve orientar uso correto do antibiótico, hidratação, sinais de alerta e retorno para controle quando indicado.",
        "transcultural": {
            "preservacao": ["Valorizar práticas seguras de higiene e hidratação."],
            "acomodacao": ["Ajustar orientação ao horário das doses e rotina da gestante."],
            "repadronizacao": ["Evitar suspensão do antibiótico após melhora dos sintomas."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Baixa adesão ao antibiótico",
        "diagnostico": {"codigo": "10022155", "termo": "Adesão ao Regime Terapêutico, Prejudicada"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Alta",
        "fundamentacao": "A baixa adesão ao antibiótico pode resultar em persistência da infecção urinária, pielonefrite, resistência bacteriana e complicações obstétricas. Deve-se reforçar conclusão do tratamento e reavaliação se sintomas persistirem.",
        "transcultural": {
            "preservacao": ["Acolher motivos de interrupção do tratamento."],
            "acomodacao": ["Criar plano de horários simples para completar o esquema."],
            "repadronizacao": ["Reforçar que melhora inicial não significa cura completa."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Tratamento de sífilis indicado",
        "diagnostico": {"codigo": "10023032", "termo": "Infecção"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre Medicação"},
        "prioridade": "Alta",
        "fundamentacao": "A sífilis na gestação requer tratamento oportuno com penicilina benzatina conforme estágio clínico, além de seguimento sorológico e abordagem da parceria sexual. O tratamento adequado previne sífilis congênita, abortamento, natimortalidade e prematuridade.",
        "transcultural": {
            "preservacao": ["Garantir acolhimento sem julgamento e preservação do sigilo."],
            "acomodacao": ["Orientar a gestante e parceria sobre tratamento e prevenção de reinfecção."],
            "repadronizacao": ["Reduzir estigma e reforçar que tratamento completo protege o bebê."]
        },
        "referencias": ["Ministério da Saúde. PCDT para IST.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Medo da penicilina benzatina",
        "diagnostico": {"codigo": "10007738", "termo": "Medo"},
        "resultado": {"codigo": "10027858", "termo": "Medo, Reduzido"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Alta",
        "fundamentacao": "O medo da penicilina benzatina pode atrasar o tratamento da sífilis e aumentar risco de transmissão vertical. A enfermagem deve acolher, explicar benefícios, possíveis reações, medidas de segurança e fluxo de atendimento para administração.",
        "transcultural": {
            "preservacao": ["Acolher experiências prévias dolorosas ou relatos familiares."],
            "acomodacao": ["Explicar o procedimento e estratégias de conforto."],
            "repadronizacao": ["Reforçar que adiar tratamento aumenta risco para o bebê."]
        },
        "referencias": ["Ministério da Saúde. PCDT para IST.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Tratamento do parceiro não realizado",
        "diagnostico": {"codigo": "10015133", "termo": "Risco de Infecção"},
        "resultado": {"codigo": "10028945", "termo": "Infecção, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre Infecção"},
        "prioridade": "Alta",
        "fundamentacao": "A ausência de tratamento da parceria sexual em casos de sífilis ou outras IST aumenta risco de reinfecção materna e transmissão vertical. A equipe deve orientar tratamento da parceria, uso de preservativo e seguimento conforme protocolo.",
        "transcultural": {
            "preservacao": ["Respeitar dinâmica familiar e segurança da gestante."],
            "acomodacao": ["Ofertar aconselhamento sigiloso e estratégias de convocação da parceria."],
            "repadronizacao": ["Reforçar que tratar somente a gestante pode não impedir reinfecção."]
        },
        "referencias": ["Ministério da Saúde. PCDT para IST.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Antirretroviral indicado",
        "diagnostico": {"codigo": "10023032", "termo": "Infecção"},
        "resultado": {"codigo": "10030185", "termo": "Adesão ao Regime Terapêutico"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre Medicação"},
        "prioridade": "Alta",
        "fundamentacao": "A terapia antirretroviral na gestação é fundamental para reduzir carga viral materna e prevenir transmissão vertical do HIV. A enfermagem deve orientar adesão diária, manejo de efeitos adversos, exames de seguimento e sigilo.",
        "transcultural": {
            "preservacao": ["Garantir acolhimento, sigilo e respeito à história da gestante."],
            "acomodacao": ["Adaptar estratégias de adesão à rotina e rede de apoio."],
            "repadronizacao": ["Combater estigma e crenças que levem à interrupção do tratamento."]
        },
        "referencias": ["Ministério da Saúde. PCDT HIV em gestantes.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Baixa adesão ao antirretroviral",
        "diagnostico": {"codigo": "10022155", "termo": "Adesão ao Regime Terapêutico, Prejudicada"},
        "resultado": {"codigo": "10030185", "termo": "Adesão ao Regime Terapêutico"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Alta",
        "fundamentacao": "A baixa adesão ao antirretroviral pode manter carga viral detectável e aumentar risco de transmissão vertical do HIV. A equipe deve identificar barreiras, efeitos adversos, estigma, acesso ao medicamento e organizar suporte intensivo.",
        "transcultural": {
            "preservacao": ["Proteger sigilo e autonomia da gestante."],
            "acomodacao": ["Planejar horários discretos e compatíveis com sua rotina."],
            "repadronizacao": ["Reduzir crenças de abandono terapêutico por medo de descoberta do diagnóstico."]
        },
        "referencias": ["Ministério da Saúde. PCDT HIV em gestantes.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Medicamento controlado em uso",
        "diagnostico": {"codigo": "10024625", "termo": "Regime Terapêutico, Prejudicado"},
        "resultado": {"codigo": "10030185", "termo": "Adesão ao Regime Terapêutico"},
        "intervencao": {"codigo": "10019502", "termo": "Orientar sobre Segurança"},
        "prioridade": "Alta",
        "fundamentacao": "Medicamentos controlados durante a gestação exigem avaliação de risco-benefício, dose, indicação, interação medicamentosa, dependência, abstinência e possíveis efeitos fetais. A suspensão abrupta também pode ser perigosa, devendo ocorrer apenas com orientação profissional.",
        "transcultural": {
            "preservacao": ["Acolher a necessidade clínica sem julgamento."],
            "acomodacao": ["Orientar acompanhamento compartilhado com pré-natal e saúde mental quando necessário."],
            "repadronizacao": ["Evitar suspensão abrupta ou aumento de dose por conta própria."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Uso de psicotrópico na gestação",
        "diagnostico": {"codigo": "10022402", "termo": "Processo Psicológico, Prejudicado"},
        "resultado": {"codigo": "10027649", "termo": "Processo Psicológico, Eficaz"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Alta",
        "fundamentacao": "O uso de psicotrópicos na gestação deve ser acompanhado com avaliação de risco-benefício, pois tanto a doença mental não tratada quanto o uso inadequado de medicamentos podem trazer riscos. A enfermagem deve orientar não interromper abruptamente e articular cuidado multiprofissional.",
        "transcultural": {
            "preservacao": ["Reduzir estigma e acolher sofrimento psíquico."],
            "acomodacao": ["Incluir rede de apoio quando autorizado pela gestante."],
            "repadronizacao": ["Reforçar que tratamento em saúde mental também faz parte do cuidado pré-natal."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Medicações e suplementação",
        "achado_clinico": "Necessidade de conciliação medicamentosa",
        "diagnostico": {"codigo": "10024625", "termo": "Regime Terapêutico, Prejudicado"},
        "resultado": {"codigo": "10030185", "termo": "Adesão ao Regime Terapêutico"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre Medicação"},
        "prioridade": "Alta",
        "fundamentacao": "A conciliação medicamentosa no pré-natal identifica medicamentos prescritos, automedicação, fitoterápicos, suplementos, duplicidades, interações e riscos gestacionais. É essencial para segurança materno-fetal e continuidade do cuidado.",
        "transcultural": {
            "preservacao": ["Acolher todos os produtos usados pela gestante sem julgamento."],
            "acomodacao": ["Solicitar que leve receitas, cartelas, frascos, chás e suplementos às consultas."],
            "repadronizacao": ["Organizar lista única e segura de medicamentos autorizados e contraindicações orientadas."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    }
]# modulos/regras_clinicas/prenatal/exames_imagem.py

REGRAS = [
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Ultrassonografia obstétrica não realizada",
        "diagnostico": {"codigo": "10022155", "termo": "Adesão ao Regime Terapêutico, Prejudicada"},
        "resultado": {"codigo": "10030185", "termo": "Adesão ao Regime Terapêutico"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Média",
        "fundamentacao": "A ultrassonografia obstétrica auxilia na confirmação da idade gestacional, vitalidade fetal, número de fetos, localização placentária, crescimento fetal e identificação de alterações. Quando não realizada, deve-se verificar barreiras de acesso, solicitar ou encaminhar conforme protocolo e registrar conduta.",
        "transcultural": {
            "preservacao": ["Valorizar a percepção da gestante sobre o desenvolvimento fetal e seus saberes familiares."],
            "acomodacao": ["Adequar o agendamento à disponibilidade de transporte, trabalho, território e rede de apoio."],
            "repadronizacao": ["Reorientar a ideia de que exame de imagem só é necessário quando há dor ou sangramento."]
        },
        "referencias": ["Ministério da Saúde. Atenção ao pré-natal de baixo risco.", "FEBRASGO. Assistência pré-natal.", "OMS. Recomendações sobre cuidados pré-natais.", "COFEN Resolução nº 736/2024.", "Leininger. Teoria Transcultural."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Ultrassonografia do primeiro trimestre não realizada",
        "diagnostico": {"codigo": "10022155", "termo": "Adesão ao Regime Terapêutico, Prejudicada"},
        "resultado": {"codigo": "10030185", "termo": "Adesão ao Regime Terapêutico"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Média",
        "fundamentacao": "A ultrassonografia do primeiro trimestre é útil para datação gestacional, confirmação de vitalidade, localização gestacional e identificação de gestação múltipla. A ausência desse exame pode dificultar o acompanhamento adequado do crescimento fetal e a definição da idade gestacional.",
        "transcultural": {
            "preservacao": ["Acolher experiências familiares sobre confirmação da gestação."],
            "acomodacao": ["Explicar a finalidade do exame em linguagem simples."],
            "repadronizacao": ["Estimular realização oportuna de exames mesmo quando a gestante se sente bem."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Idade gestacional incerta",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "A idade gestacional incerta compromete a interpretação do crescimento fetal, a programação de exames, a identificação de prematuridade ou pós-datismo e a tomada de decisões obstétricas. A ultrassonografia, especialmente quando realizada precocemente, contribui para melhor datação da gestação.",
        "transcultural": {
            "preservacao": ["Acolher formas culturais de marcar datas, ciclos menstruais e eventos familiares."],
            "acomodacao": ["Reconstruir a história gestacional com apoio de marcos familiares e registros disponíveis."],
            "repadronizacao": ["Estimular registro da DUM e início precoce do pré-natal em futuras gestações."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Divergência entre DUM e ultrassonografia",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Média",
        "fundamentacao": "Divergência entre data da última menstruação e ultrassonografia pode ocorrer por ciclos irregulares, lembrança imprecisa da DUM ou alteração no crescimento fetal. A conduta depende da idade gestacional, qualidade do exame e critérios obstétricos de datação.",
        "transcultural": {
            "preservacao": ["Respeitar a narrativa da gestante sobre seu ciclo e sinais corporais."],
            "acomodacao": ["Explicar que a datação pode ser ajustada por critérios clínicos e ultrassonográficos."],
            "repadronizacao": ["Evitar conclusões precipitadas sem avaliação da equipe e registro adequado."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Translucência nucal alterada",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Translucência nucal alterada pode indicar risco aumentado para aneuploidias, cardiopatias e outras alterações fetais. Requer encaminhamento para avaliação especializada, aconselhamento, exames complementares e seguimento conforme protocolo.",
        "transcultural": {
            "preservacao": ["Acolher crenças e sentimentos da família diante de possível alteração fetal."],
            "acomodacao": ["Garantir comunicação clara, respeitosa e sem julgamento."],
            "repadronizacao": ["Evitar interpretação definitiva do achado sem avaliação especializada."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Morfológica do primeiro trimestre alterada",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Alterações na ultrassonografia morfológica do primeiro trimestre podem indicar risco de anomalias estruturais, cromossômicas ou alterações do desenvolvimento fetal. A gestante deve ser encaminhada para avaliação especializada e acompanhamento multiprofissional.",
        "transcultural": {
            "preservacao": ["Acolher espiritualidade, valores familiares e necessidades emocionais."],
            "acomodacao": ["Explicar a necessidade de exames complementares e seguimento especializado."],
            "repadronizacao": ["Reforçar que um achado alterado exige investigação, não conclusão isolada."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Morfológica do segundo trimestre não realizada",
        "diagnostico": {"codigo": "10022155", "termo": "Adesão ao Regime Terapêutico, Prejudicada"},
        "resultado": {"codigo": "10030185", "termo": "Adesão ao Regime Terapêutico"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Média",
        "fundamentacao": "A ultrassonografia morfológica do segundo trimestre avalia anatomia fetal, placenta, líquido amniótico e crescimento. Quando não realizada no período recomendado, deve-se providenciar agendamento ou encaminhamento conforme disponibilidade e idade gestacional.",
        "transcultural": {
            "preservacao": ["Valorizar o interesse da família em conhecer o desenvolvimento do bebê."],
            "acomodacao": ["Planejar o exame conforme acesso ao serviço e transporte."],
            "repadronizacao": ["Reforçar que o exame possui finalidade clínica, não apenas identificação do sexo fetal."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Morfológica do segundo trimestre alterada",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Alteração na morfológica do segundo trimestre pode indicar malformações fetais, alterações placentárias, restrição de crescimento, alterações de líquido amniótico ou necessidade de investigação complementar. Exige encaminhamento para avaliação especializada.",
        "transcultural": {
            "preservacao": ["Acolher medo, ansiedade e valores familiares."],
            "acomodacao": ["Orientar próximos passos de forma clara e respeitosa."],
            "repadronizacao": ["Evitar abandono do pré-natal após notícia de alteração fetal."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Placenta prévia suspeita",
        "diagnostico": {"codigo": "10003303", "termo": "Sangramento"},
        "resultado": {"codigo": "10028120", "termo": "Sangramento, Ausente"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Placenta prévia suspeita aumenta risco de sangramento vaginal, parto prematuro e necessidade de planejamento obstétrico. A gestante deve ser encaminhada para avaliação, confirmação diagnóstica e orientação sobre sinais de alerta.",
        "transcultural": {
            "preservacao": ["Acolher a gestante e sua família diante do medo de sangramento."],
            "acomodacao": ["Orientar repouso relativo e procura imediata em caso de sangramento conforme prescrição e protocolo."],
            "repadronizacao": ["Evitar minimizar qualquer sangramento vaginal na gestação."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Descolamento placentário suspeito",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Suspeita de descolamento placentário é emergência obstétrica, principalmente quando há dor abdominal, hipertonia uterina, sangramento, sofrimento fetal ou instabilidade materna. Requer encaminhamento imediato para avaliação obstétrica.",
        "transcultural": {
            "preservacao": ["Acolher relatos da gestante sobre dor, sangramento e percepção fetal."],
            "acomodacao": ["Acionar rede de apoio e transporte de urgência conforme realidade local."],
            "repadronizacao": ["Reforçar que dor abdominal intensa com sangramento não deve aguardar consulta agendada."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Restrição de crescimento fetal suspeita",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Restrição de crescimento fetal suspeita pode estar relacionada a insuficiência placentária, hipertensão, infecções, tabagismo, desnutrição ou outras condições maternas e fetais. Exige avaliação especializada, acompanhamento seriado do crescimento e, quando indicado, Doppler obstétrico.",
        "transcultural": {
            "preservacao": ["Valorizar alimentos e práticas de cuidado seguros do território."],
            "acomodacao": ["Adequar orientações nutricionais e de retorno à realidade social da gestante."],
            "repadronizacao": ["Reforçar necessidade de acompanhamento seriado, mesmo sem sintomas maternos."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Macrossomia fetal suspeita",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Alta",
        "fundamentacao": "Macrossomia fetal suspeita pode estar associada a diabetes gestacional, ganho ponderal excessivo e risco de distocia de ombro, trauma obstétrico, cesariana e hipoglicemia neonatal. Deve-se avaliar controle glicêmico, crescimento fetal e plano de parto.",
        "transcultural": {
            "preservacao": ["Respeitar crenças familiares sobre bebê grande e saúde."],
            "acomodacao": ["Orientar relação entre alimentação, glicemia e crescimento fetal de forma simples."],
            "repadronizacao": ["Reorientar a ideia de que bebê muito grande sempre significa gestação saudável."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Oligodrâmnio",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Oligodrâmnio pode estar associado a ruptura de membranas, insuficiência placentária, restrição de crescimento fetal, malformações renais fetais ou pós-datismo. Exige avaliação obstétrica, investigação da causa e monitoramento fetal.",
        "transcultural": {
            "preservacao": ["Acolher preocupações da gestante sobre líquido e vitalidade fetal."],
            "acomodacao": ["Orientar sinais de alerta, como perda de líquido e redução de movimentos fetais."],
            "repadronizacao": ["Evitar atribuir o achado apenas à baixa ingestão de água sem avaliação clínica."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Polidrâmnio",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Polidrâmnio pode estar associado a diabetes gestacional, malformações fetais, infecções, gestação múltipla ou causas idiopáticas. A gestante deve ser avaliada quanto a sintomas respiratórios, contrações, crescimento uterino aumentado e necessidade de investigação complementar.",
        "transcultural": {
            "preservacao": ["Acolher a interpretação da gestante sobre aumento abdominal."],
            "acomodacao": ["Orientar sinais de trabalho de parto prematuro e desconforto respiratório."],
            "repadronizacao": ["Reforçar necessidade de investigação, mesmo quando a gestante atribui o aumento apenas ao bebê grande."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Gestação gemelar",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Gestação gemelar apresenta maior risco de prematuridade, restrição de crescimento, anemia, síndromes hipertensivas e complicações fetais. Requer definição de corionicidade, acompanhamento mais frequente e, quando indicado, pré-natal de alto risco.",
        "transcultural": {
            "preservacao": ["Valorizar redes familiares de apoio à gestante."],
            "acomodacao": ["Planejar consultas, exames e transporte considerando maior risco e maior frequência de acompanhamento."],
            "repadronizacao": ["Reforçar que gestação gemelar demanda vigilância ampliada mesmo sem sintomas."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Apresentação pélvica",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10045079", "termo": "Orientar sobre Gestação"},
        "prioridade": "Média",
        "fundamentacao": "A apresentação pélvica pode ser transitória antes do termo, mas quando persistente no final da gestação pode influenciar planejamento do parto. A gestante deve ser orientada e acompanhada conforme idade gestacional, vitalidade fetal e avaliação obstétrica.",
        "transcultural": {
            "preservacao": ["Acolher crenças sobre posição fetal e parto."],
            "acomodacao": ["Explicar que a posição fetal pode mudar conforme idade gestacional."],
            "repadronizacao": ["Evitar manobras caseiras ou práticas sem segurança para tentar mudar a posição fetal."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Apresentação transversa",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Apresentação transversa persistente, especialmente no final da gestação, está associada a maior risco no parto vaginal e requer avaliação obstétrica para planejamento seguro do parto e prevenção de complicações.",
        "transcultural": {
            "preservacao": ["Acolher conhecimentos familiares sobre posição do bebê."],
            "acomodacao": ["Orientar acompanhamento e avaliação obstétrica sem gerar culpa na gestante."],
            "repadronizacao": ["Evitar tentativas caseiras de mudança de posição fetal."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Doppler obstétrico alterado",
        "diagnostico": {"codigo": "10012606", "termo": "Processo do Sistema Circulatório, Prejudicado"},
        "resultado": {"codigo": "10028379", "termo": "Processo do Sistema Circulatório, Positivo"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Doppler obstétrico alterado pode indicar comprometimento da circulação uteroplacentária ou fetal, associado a restrição de crescimento, insuficiência placentária, pré-eclâmpsia e risco fetal. Exige avaliação especializada e vigilância materno-fetal.",
        "transcultural": {
            "preservacao": ["Acolher ansiedade da gestante diante de exame alterado."],
            "acomodacao": ["Explicar a importância do seguimento e dos retornos seriados."],
            "repadronizacao": ["Reforçar que ausência de sintomas maternos não exclui risco fetal."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "BCF ausente em exame",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Batimentos cardíacos fetais ausentes em exame é achado crítico e requer confirmação imediata por avaliação obstétrica e exame apropriado, considerando idade gestacional, qualidade técnica e condição materno-fetal.",
        "transcultural": {
            "preservacao": ["Acolher a gestante e família com comunicação humanizada."],
            "acomodacao": ["Garantir encaminhamento rápido e suporte emocional."],
            "repadronizacao": ["Evitar conclusões definitivas sem confirmação adequada, mas não retardar avaliação urgente."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Malformação fetal suspeita",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Suspeita de malformação fetal exige confirmação diagnóstica, avaliação especializada, aconselhamento, planejamento do parto e organização da rede de cuidado neonatal quando necessário.",
        "transcultural": {
            "preservacao": ["Respeitar valores, espiritualidade e decisões familiares."],
            "acomodacao": ["Oferecer informação clara, apoio emocional e encaminhamento especializado."],
            "repadronizacao": ["Evitar estigmatização ou culpabilização da gestante pela alteração fetal."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Colo uterino curto",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Colo uterino curto em exame de imagem está associado a maior risco de parto prematuro, especialmente em gestantes com história obstétrica compatível. Exige avaliação obstétrica, estratificação de risco e condutas preventivas conforme protocolo.",
        "transcultural": {
            "preservacao": ["Acolher preocupações da gestante sobre repouso e parto prematuro."],
            "acomodacao": ["Planejar acompanhamento considerando trabalho, deslocamento e rede de apoio."],
            "repadronizacao": ["Reforçar que ausência de dor não exclui risco de prematuridade."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Risco de parto prematuro por imagem",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Achados de imagem como colo curto, alterações placentárias, polidrâmnio, gestação múltipla ou sinais de insuficiência placentária podem aumentar risco de parto prematuro. A gestante deve ser encaminhada para avaliação, vigilância e orientações de sinais de alerta.",
        "transcultural": {
            "preservacao": ["Reconhecer estratégias familiares para proteção da gestante."],
            "acomodacao": ["Construir plano de deslocamento e busca de atendimento em caso de contrações, sangramento ou perda de líquido."],
            "repadronizacao": ["Reorientar a prática de aguardar melhora espontânea diante de sinais de prematuridade."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Crescimento fetal discordante",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Crescimento fetal discordante pode indicar restrição de crescimento, erro de datação, insuficiência placentária ou complicações em gestação múltipla. Requer avaliação seriada, revisão da idade gestacional e acompanhamento especializado.",
        "transcultural": {
            "preservacao": ["Valorizar a percepção materna sobre crescimento abdominal e movimentos fetais."],
            "acomodacao": ["Orientar necessidade de retornos e exames seriados."],
            "repadronizacao": ["Evitar considerar apenas o tamanho da barriga como indicador confiável de crescimento fetal."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Circular de cordão descrita",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10045079", "termo": "Orientar sobre Gestação"},
        "prioridade": "Baixa",
        "fundamentacao": "Circular de cordão é achado ultrassonográfico frequente e, isoladamente, geralmente não define via de parto nem indica sofrimento fetal. Deve-se orientar a gestante, reduzir ansiedade e reforçar observação dos movimentos fetais e acompanhamento habitual.",
        "transcultural": {
            "preservacao": ["Acolher crenças familiares sobre cordão umbilical e risco ao bebê."],
            "acomodacao": ["Explicar de forma simples quando o achado exige ou não preocupação adicional."],
            "repadronizacao": ["Reorientar a ideia de que circular de cordão isolada sempre exige cesariana."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Líquido amniótico alterado",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de Lesão"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "Alteração do líquido amniótico, seja por redução ou aumento, pode estar relacionada a ruptura de membranas, diabetes, malformações, restrição de crescimento, infecção ou alterações placentárias. Exige avaliação obstétrica e definição da causa.",
        "transcultural": {
            "preservacao": ["Acolher preocupações e interpretações culturais sobre líquido amniótico."],
            "acomodacao": ["Orientar sinais de alerta, como perda de líquido, contrações e redução de movimentos fetais."],
            "repadronizacao": ["Evitar condutas caseiras isoladas sem avaliação clínica."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Necessidade de repetir ultrassonografia",
        "diagnostico": {"codigo": "10024625", "termo": "Regime Terapêutico, Prejudicado"},
        "resultado": {"codigo": "10030185", "termo": "Adesão ao Regime Terapêutico"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Média",
        "fundamentacao": "A repetição da ultrassonografia pode ser necessária por exame inconclusivo, idade gestacional inadequada, dificuldade técnica, necessidade de acompanhar crescimento fetal, líquido amniótico, placenta ou achados suspeitos. Deve-se orientar a finalidade da repetição e garantir seguimento.",
        "transcultural": {
            "preservacao": ["Acolher dúvidas sobre por que repetir um exame já realizado."],
            "acomodacao": ["Planejar repetição conforme acesso, transporte e disponibilidade do serviço."],
            "repadronizacao": ["Reforçar que repetir o exame não significa necessariamente gravidade, mas necessidade de melhor avaliação."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Dificuldade de acesso ao exame de imagem",
        "diagnostico": {"codigo": "10025806", "termo": "Comportamento de Saúde, Prejudicado"},
        "resultado": {"codigo": "10028276", "termo": "Comportamento de Saúde, Positivo"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para Serviço de Saúde"},
        "prioridade": "Alta",
        "fundamentacao": "A dificuldade de acesso ao exame de imagem pode atrasar diagnóstico, estratificação de risco e planejamento obstétrico. A equipe deve articular regulação, transporte sanitário, busca ativa e priorização conforme risco gestacional.",
        "transcultural": {
            "preservacao": ["Reconhecer barreiras territoriais, econômicas, ribeirinhas, rurais ou familiares."],
            "acomodacao": ["Adequar agendamento aos dias de deslocamento, consulta e disponibilidade da rede."],
            "repadronizacao": ["Reorganizar o cuidado para reduzir iniquidades de acesso e perda de seguimento."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "Pré-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Exame de imagem atrasado",
        "diagnostico": {"codigo": "10022155", "termo": "Adesão ao Regime Terapêutico, Prejudicada"},
        "resultado": {"codigo": "10030185", "termo": "Adesão ao Regime Terapêutico"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime Terapêutico"},
        "prioridade": "Média",
        "fundamentacao": "Exame de imagem atrasado pode reduzir a utilidade clínica de avaliações dependentes da idade gestacional, como datação precoce, rastreamento morfológico e monitoramento do crescimento fetal. Deve-se reagendar, priorizar conforme risco e registrar justificativa.",
        "transcultural": {
            "preservacao": ["Acolher dificuldades reais que levaram ao atraso."],
            "acomodacao": ["Pactuar novo plano viável de realização do exame."],
            "repadronizacao": ["Reforçar a importância de realizar exames dentro da janela recomendada quando possível."]
        },
        "referencias": ["Ministério da Saúde.", "FEBRASGO.", "OMS.", "COFEN Resolução nº 736/2024.", "Leininger."]
    }
]