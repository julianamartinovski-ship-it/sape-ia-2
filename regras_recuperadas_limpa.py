import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "banco_dados" / "cipe.db"

regras_prenatal = [
    ("PrÃ©-natal", "HipertensÃ£o arterial", "PressÃ£o arterial alterada", "PressÃ£o arterial controlada", "Monitorar pressÃ£o arterial", "Alta", "Gestante com pressÃ£o arterial elevada requer avaliaÃ§Ã£o de risco gestacional."),
    ("PrÃ©-natal", "ProteinÃºria", "Risco de condiÃ§Ã£o hipertensiva na gestaÃ§Ã£o", "Risco reduzido", "Avaliar sinais de gravidade", "Alta", "ProteinÃºria associada Ã  hipertensÃ£o pode indicar risco de prÃ©-eclÃ¢mpsia."),
    ("PrÃ©-natal", "Cefaleia persistente", "Risco de condiÃ§Ã£o hipertensiva na gestaÃ§Ã£o", "Estado neurolÃ³gico preservado", "Encaminhar conforme protocolo de risco gestacional", "Alta", "Cefaleia persistente em gestante exige avaliaÃ§Ã£o clÃ­nica imediata."),
    ("PrÃ©-natal", "Corrimento vaginal", "Corrimento vaginal", "Conforto melhorado", "Avaliar caracterÃ­sticas do corrimento vaginal", "MÃ©dia", "Corrimento vaginal deve ser avaliado conforme sinais associados e protocolo de IST/vulvovaginites."),
    ("PrÃ©-natal", "Prurido vaginal", "Prurido genital", "Conforto melhorado", "Orientar higiene Ã­ntima", "MÃ©dia", "Prurido associado a corrimento pode indicar vulvovaginite."),
    ("PrÃ©-natal", "Ãrea descoberta pela ESF", "Acesso ao serviÃ§o de saÃºde prejudicado", "Acesso ao cuidado melhorado", "Organizar seguimento do prÃ©-natal", "Alta", "Dificuldade de acesso exige planejamento do cuidado e seguimento longitudinal."),
]

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("DELETE FROM regras_clinicas_cipe WHERE linha_cuidado = 'PrÃ©-natal'")

cur.executemany("""
    INSERT INTO regras_clinicas_cipe
    (linha_cuidado, achado_clinico, codigo_diagnostico, codigo_resultado, codigo_intervencao, prioridade, justificativa)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", regras_prenatal)

conn.commit()
conn.close()

print("Regras clÃ­nicas de prÃ©-natal inseridas com sucesso.")
print("Total inserido:", len(regras_prenatal))"""
SAPE IA 2.0
Regras ClÃ­nicas - PrÃ©-natal
Categoria: CaptaÃ§Ã£o e VÃ­nculo
"""

REGRAS = [

    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "CaptaÃ§Ã£o e vÃ­nculo",

        "achado_clinico": "InÃ­cio tardio do prÃ©-natal",

        "diagnostico": {
            "codigo": None,
            "termo": "AdesÃ£o ao cuidado prejudicada"
        },

        "resultado": {
            "codigo": None,
            "termo": "AdesÃ£o ao cuidado melhorada"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Organizar plano de seguimento do prÃ©-natal"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "O inÃ­cio tardio do prÃ©-natal dificulta o rastreamento oportuno de fatores de risco, o vÃ­nculo com a equipe e a prevenÃ§Ã£o de agravos maternos e fetais.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Adequar agenda conforme realidade territorial e familiar da gestante."
            ],

            "repadronizacao": [
                "Reorganizar plano de cuidado garantindo consultas mÃ­nimas e exames essenciais."
            ]
        },

        "referencias": [
            "MinistÃ©rio da SaÃºde. AtenÃ§Ã£o ao PrÃ©-Natal de Baixo Risco.",
            "COFEN ResoluÃ§Ã£o nÂº 736/2024.",
            "Leininger. Teoria Transcultural do Cuidado."
        ]
    },

    {
        "linha_cuidado": "PrÃ©-natal",

        "categoria": "CaptaÃ§Ã£o e vÃ­nculo",

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
        "A ausÃªncia nas consultas compromete a vigilÃ¢ncia clÃ­nica materna e fetal e aumenta o risco de perda de oportunidades diagnÃ³sticas.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Investigar barreiras familiares, culturais, econÃ´micas e territoriais."
            ],

            "repadronizacao": [
                "Planejar busca ativa juntamente com ACS e equipe multiprofissional."
            ]
        },

        "referencias": [
            "PNAB.",
            "COFEN ResoluÃ§Ã£o nÂº 736/2024.",
            "Leininger."
        ]
    },

    {
        "linha_cuidado": "PrÃ©-natal",

        "categoria": "CaptaÃ§Ã£o e vÃ­nculo",

        "achado_clinico": "Ãrea descoberta pela ESF",

        "diagnostico": {
            "codigo": None,
            "termo": "Acesso ao serviÃ§o de saÃºde prejudicado"
        },

        "resultado": {
            "codigo": None,
            "termo": "Acesso ao cuidado melhorado"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Organizar seguimento do prÃ©-natal"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "A ausÃªncia de cobertura regular da ESF compromete a longitudinalidade do cuidado.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Considerar lideranÃ§as comunitÃ¡rias e formas locais de comunicaÃ§Ã£o."
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
        "linha_cuidado": "PrÃ©-natal",

        "categoria": "CaptaÃ§Ã£o e vÃ­nculo",

        "achado_clinico": "Longa distÃ¢ncia atÃ© a UBS",

        "diagnostico": {
            "codigo": None,
            "termo": "Acesso ao serviÃ§o de saÃºde prejudicado"
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
        "Barreiras geogrÃ¡ficas dificultam a continuidade do acompanhamento prÃ©-natal.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Adequar cronograma conforme logÃ­stica territorial."
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
        "linha_cuidado": "PrÃ©-natal",

        "categoria": "CaptaÃ§Ã£o e vÃ­nculo",

        "achado_clinico": "Transporte fluvial",

        "diagnostico": {
            "codigo": None,
            "termo": "Acesso ao serviÃ§o de saÃºde prejudicado"
        },

        "resultado": {
            "codigo": None,
            "termo": "Continuidade do cuidado melhorada"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Planejar consultas conforme logÃ­stica fluvial"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "A logÃ­stica fluvial interfere no acesso oportuno ao cuidado.",

        "transcultural": {

            "preservacao": [
                "Reconhecer o modo de vida ribeirinho."
            ],

            "acomodacao": [
                "Adequar consultas conforme disponibilidade das embarcaÃ§Ãµes."
            ],

            "repadronizacao": [
                "Criar plano para situaÃ§Ãµes de urgÃªncia obstÃ©trica."
            ]
        },

        "referencias": [
            "Leininger.",
            "PNAB."
        ]
    }

]"""
SAPE IA 2.0
Regras ClÃ­nicas - PrÃ©-natal
Categoria: CaptaÃ§Ã£o e VÃ­nculo
"""

REGRAS = [

    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "CaptaÃ§Ã£o e vÃ­nculo",

        "achado_clinico": "InÃ­cio tardio do prÃ©-natal",

        "diagnostico": {
            "codigo": None,
            "termo": "AdesÃ£o ao cuidado prejudicada"
        },

        "resultado": {
            "codigo": None,
            "termo": "AdesÃ£o ao cuidado melhorada"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Organizar plano de seguimento do prÃ©-natal"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "O inÃ­cio tardio do prÃ©-natal dificulta o rastreamento oportuno de fatores de risco, o vÃ­nculo com a equipe e a prevenÃ§Ã£o de agravos maternos e fetais.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Adequar agenda conforme realidade territorial e familiar da gestante."
            ],

            "repadronizacao": [
                "Reorganizar plano de cuidado garantindo consultas mÃ­nimas e exames essenciais."
            ]
        },

        "referencias": [
            "MinistÃ©rio da SaÃºde. AtenÃ§Ã£o ao PrÃ©-Natal de Baixo Risco.",
            "COFEN ResoluÃ§Ã£o nÂº 736/2024.",
            "Leininger. Teoria Transcultural do Cuidado."
        ]
    },

    {
        "linha_cuidado": "PrÃ©-natal",

        "categoria": "CaptaÃ§Ã£o e vÃ­nculo",

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
        "A ausÃªncia nas consultas compromete a vigilÃ¢ncia clÃ­nica materna e fetal e aumenta o risco de perda de oportunidades diagnÃ³sticas.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Investigar barreiras familiares, culturais, econÃ´micas e territoriais."
            ],

            "repadronizacao": [
                "Planejar busca ativa juntamente com ACS e equipe multiprofissional."
            ]
        },

        "referencias": [
            "PNAB.",
            "COFEN ResoluÃ§Ã£o nÂº 736/2024.",
            "Leininger."
        ]
    },

    {
        "linha_cuidado": "PrÃ©-natal",

        "categoria": "CaptaÃ§Ã£o e vÃ­nculo",

        "achado_clinico": "Ãrea descoberta pela ESF",

        "diagnostico": {
            "codigo": None,
            "termo": "Acesso ao serviÃ§o de saÃºde prejudicado"
        },

        "resultado": {
            "codigo": None,
            "termo": "Acesso ao cuidado melhorado"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Organizar seguimento do prÃ©-natal"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "A ausÃªncia de cobertura regular da ESF compromete a longitudinalidade do cuidado.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Considerar lideranÃ§as comunitÃ¡rias e formas locais de comunicaÃ§Ã£o."
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
        "linha_cuidado": "PrÃ©-natal",

        "categoria": "CaptaÃ§Ã£o e vÃ­nculo",

        "achado_clinico": "Longa distÃ¢ncia atÃ© a UBS",

        "diagnostico": {
            "codigo": None,
            "termo": "Acesso ao serviÃ§o de saÃºde prejudicado"
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
        "Barreiras geogrÃ¡ficas dificultam a continuidade do acompanhamento prÃ©-natal.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Adequar cronograma conforme logÃ­stica territorial."
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
        "linha_cuidado": "PrÃ©-natal",

        "categoria": "CaptaÃ§Ã£o e vÃ­nculo",

        "achado_clinico": "Transporte fluvial",

        "diagnostico": {
            "codigo": None,
            "termo": "Acesso ao serviÃ§o de saÃºde prejudicado"
        },

        "resultado": {
            "codigo": None,
            "termo": "Continuidade do cuidado melhorada"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Planejar consultas conforme logÃ­stica fluvial"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "A logÃ­stica fluvial interfere no acesso oportuno ao cuidado.",

        "transcultural": {

            "preservacao": [
                "Reconhecer o modo de vida ribeirinho."
            ],

            "acomodacao": [
                "Adequar consultas conforme disponibilidade das embarcaÃ§Ãµes."
            ],

            "repadronizacao": [
                "Criar plano para situaÃ§Ãµes de urgÃªncia obstÃ©trica."
            ]
        },

        "referencias": [
            "Leininger.",
            "PNAB."
        ]
    }

]"""
SAPE IA 2.0
Regras ClÃ­nicas - PrÃ©-natal
Categoria: CaptaÃ§Ã£o e VÃ­nculo
"""

REGRAS = [

    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "CaptaÃ§Ã£o e vÃ­nculo",

        "achado_clinico": "InÃ­cio tardio do prÃ©-natal",

        "diagnostico": {
            "codigo": None,
            "termo": "AdesÃ£o ao cuidado prejudicada"
        },

        "resultado": {
            "codigo": None,
            "termo": "AdesÃ£o ao cuidado melhorada"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Organizar plano de seguimento do prÃ©-natal"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "O inÃ­cio tardio do prÃ©-natal dificulta o rastreamento oportuno de fatores de risco, o vÃ­nculo com a equipe e a prevenÃ§Ã£o de agravos maternos e fetais.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Adequar agenda conforme realidade territorial e familiar da gestante."
            ],

            "repadronizacao": [
                "Reorganizar plano de cuidado garantindo consultas mÃ­nimas e exames essenciais."
            ]
        },

        "referencias": [
            "MinistÃ©rio da SaÃºde. AtenÃ§Ã£o ao PrÃ©-Natal de Baixo Risco.",
            "COFEN ResoluÃ§Ã£o nÂº 736/2024.",
            "Leininger. Teoria Transcultural do Cuidado."
        ]
    },

    {
        "linha_cuidado": "PrÃ©-natal",

        "categoria": "CaptaÃ§Ã£o e vÃ­nculo",

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
        "A ausÃªncia nas consultas compromete a vigilÃ¢ncia clÃ­nica materna e fetal e aumenta o risco de perda de oportunidades diagnÃ³sticas.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Investigar barreiras familiares, culturais, econÃ´micas e territoriais."
            ],

            "repadronizacao": [
                "Planejar busca ativa juntamente com ACS e equipe multiprofissional."
            ]
        },

        "referencias": [
            "PNAB.",
            "COFEN ResoluÃ§Ã£o nÂº 736/2024.",
            "Leininger."
        ]
    },

    {
        "linha_cuidado": "PrÃ©-natal",

        "categoria": "CaptaÃ§Ã£o e vÃ­nculo",

        "achado_clinico": "Ãrea descoberta pela ESF",

        "diagnostico": {
            "codigo": None,
            "termo": "Acesso ao serviÃ§o de saÃºde prejudicado"
        },

        "resultado": {
            "codigo": None,
            "termo": "Acesso ao cuidado melhorado"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Organizar seguimento do prÃ©-natal"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "A ausÃªncia de cobertura regular da ESF compromete a longitudinalidade do cuidado.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Considerar lideranÃ§as comunitÃ¡rias e formas locais de comunicaÃ§Ã£o."
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
        "linha_cuidado": "PrÃ©-natal",

        "categoria": "CaptaÃ§Ã£o e vÃ­nculo",

        "achado_clinico": "Longa distÃ¢ncia atÃ© a UBS",

        "diagnostico": {
            "codigo": None,
            "termo": "Acesso ao serviÃ§o de saÃºde prejudicado"
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
        "Barreiras geogrÃ¡ficas dificultam a continuidade do acompanhamento prÃ©-natal.",

        "transcultural": {

            "preservacao": [],

            "acomodacao": [
                "Adequar cronograma conforme logÃ­stica territorial."
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
        "linha_cuidado": "PrÃ©-natal",

        "categoria": "CaptaÃ§Ã£o e vÃ­nculo",

        "achado_clinico": "Transporte fluvial",

        "diagnostico": {
            "codigo": None,
            "termo": "Acesso ao serviÃ§o de saÃºde prejudicado"
        },

        "resultado": {
            "codigo": None,
            "termo": "Continuidade do cuidado melhorada"
        },

        "intervencao": {
            "codigo": None,
            "termo": "Planejar consultas conforme logÃ­stica fluvial"
        },

        "prioridade": "Alta",

        "fundamentacao":
        "A logÃ­stica fluvial interfere no acesso oportuno ao cuidado.",

        "transcultural": {

            "preservacao": [
                "Reconhecer o modo de vida ribeirinho."
            ],

            "acomodacao": [
                "Adequar consultas conforme disponibilidade das embarcaÃ§Ãµes."
            ],

            "repadronizacao": [
                "Criar plano para situaÃ§Ãµes de urgÃªncia obstÃ©trica."
            ]
        },

        "referencias": [
            "Leininger.",
            "PNAB."
        ]
    }

]"""
SAPE IA 2.0
Regras ClÃ­nicas - PrÃ©-natal
Categoria: Fatores de risco gestacional
"""

REGRAS = [
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "HipertensÃ£o arterial",
        "diagnostico": {"codigo": None, "termo": "PressÃ£o arterial alterada"},
        "resultado": {"codigo": None, "termo": "PressÃ£o arterial controlada"},
        "intervencao": {"codigo": None, "termo": "Monitorar pressÃ£o arterial"},
        "prioridade": "Alta",
        "fundamentacao": "PressÃ£o arterial elevada na gestaÃ§Ã£o exige avaliaÃ§Ã£o de risco para sÃ­ndromes hipertensivas.",
        "transcultural": {
            "preservacao": [],
            "acomodacao": ["Adequar monitoramento conforme acesso da gestante ao serviÃ§o."],
            "repadronizacao": ["Criar plano de urgÃªncia para sinais de prÃ©-eclÃ¢mpsia."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "Manual de GestaÃ§Ã£o de Alto Risco.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "ProteinÃºria",
        "diagnostico": {"codigo": None, "termo": "Risco de condiÃ§Ã£o hipertensiva na gestaÃ§Ã£o"},
        "resultado": {"codigo": None, "termo": "Risco reduzido"},
        "intervencao": {"codigo": None, "termo": "Avaliar sinais de gravidade"},
        "prioridade": "Alta",
        "fundamentacao": "ProteinÃºria associada Ã  hipertensÃ£o pode indicar prÃ©-eclÃ¢mpsia.",
        "transcultural": {
            "preservacao": [],
            "acomodacao": ["Orientar sinais de alerta com linguagem adequada ao contexto cultural."],
            "repadronizacao": ["Encaminhar conforme risco e organizar transporte se necessÃ¡rio."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "Manual de GestaÃ§Ã£o de Alto Risco.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Cefaleia persistente",
        "diagnostico": {"codigo": None, "termo": "Risco de condiÃ§Ã£o hipertensiva na gestaÃ§Ã£o"},
        "resultado": {"codigo": None, "termo": "SeguranÃ§a materno-fetal preservada"},
        "intervencao": {"codigo": None, "termo": "Encaminhar para avaliaÃ§Ã£o conforme protocolo de risco gestacional"},
        "prioridade": "Alta",
        "fundamentacao": "Cefaleia persistente pode ser sinal de gravidade em sÃ­ndromes hipertensivas.",
        "transcultural": {
            "preservacao": [],
            "acomodacao": ["Verificar prÃ¡ticas locais de autocuidado jÃ¡ utilizadas."],
            "repadronizacao": ["Orientar procura imediata do serviÃ§o diante de piora ou sinais associados."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "Manual de GestaÃ§Ã£o de Alto Risco.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Escotomas visuais",
        "diagnostico": {"codigo": None, "termo": "Risco de condiÃ§Ã£o hipertensiva na gestaÃ§Ã£o"},
        "resultado": {"codigo": None, "termo": "SeguranÃ§a materno-fetal preservada"},
        "intervencao": {"codigo": None, "termo": "Encaminhar para avaliaÃ§Ã£o imediata"},
        "prioridade": "Alta",
        "fundamentacao": "AlteraÃ§Ãµes visuais na gestaÃ§Ã£o sÃ£o sinais de alerta para agravamento hipertensivo.",
        "transcultural": {
            "preservacao": [],
            "acomodacao": ["Explicar a gravidade usando linguagem simples."],
            "repadronizacao": ["Priorizar remoÃ§Ã£o/encaminhamento mesmo diante de barreiras territoriais."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "Manual de GestaÃ§Ã£o de Alto Risco.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Edema importante",
        "diagnostico": {"codigo": None, "termo": "Risco de prÃ©-eclÃ¢mpsia"},
        "resultado": {"codigo": None, "termo": "Risco reduzido"},
        "intervencao": {"codigo": None, "termo": "Avaliar pressÃ£o arterial e proteinÃºria"},
        "prioridade": "Alta",
        "fundamentacao": "Edema importante associado a outros sinais pode indicar agravamento clÃ­nico.",
        "transcultural": {
            "preservacao": [],
            "acomodacao": ["Investigar percepÃ§Ã£o cultural sobre edema na gestaÃ§Ã£o."],
            "repadronizacao": ["ReforÃ§ar sinais de alerta e necessidade de avaliaÃ§Ã£o imediata."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "Manual de GestaÃ§Ã£o de Alto Risco.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Glicemia alterada",
        "diagnostico": {"codigo": None, "termo": "Risco de glicemia alterada"},
        "resultado": {"codigo": None, "termo": "Glicemia controlada"},
        "intervencao": {"codigo": None, "termo": "Orientar acompanhamento glicÃªmico conforme protocolo"},
        "prioridade": "Alta",
        "fundamentacao": "AlteraÃ§Ãµes glicÃªmicas na gestaÃ§Ã£o exigem rastreamento e acompanhamento de diabetes gestacional.",
        "transcultural": {
            "preservacao": ["Reconhecer hÃ¡bitos alimentares regionais."],
            "acomodacao": ["Adaptar orientaÃ§Ã£o alimentar Ã  disponibilidade local de alimentos."],
            "repadronizacao": ["Reorganizar plano alimentar quando houver risco metabÃ³lico."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "Manual de GestaÃ§Ã£o de Alto Risco.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Diabetes gestacional",
        "diagnostico": {"codigo": None, "termo": "Glicemia alterada"},
        "resultado": {"codigo": None, "termo": "Glicemia controlada"},
        "intervencao": {"codigo": None, "termo": "Acompanhar controle glicÃªmico"},
        "prioridade": "Alta",
        "fundamentacao": "Diabetes gestacional requer acompanhamento contÃ­nuo para reduÃ§Ã£o de riscos materno-fetais.",
        "transcultural": {
            "preservacao": ["Valorizar prÃ¡ticas alimentares seguras da famÃ­lia."],
            "acomodacao": ["Negociar mudanÃ§as alimentares possÃ­veis no contexto socioeconÃ´mico."],
            "repadronizacao": ["Encaminhar e intensificar acompanhamento conforme risco."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "Manual de GestaÃ§Ã£o de Alto Risco.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Anemia",
        "diagnostico": {"codigo": None, "termo": "Hemoglobina diminuÃ­da"},
        "resultado": {"codigo": None, "termo": "Hemoglobina melhorada"},
        "intervencao": {"codigo": None, "termo": "Orientar suplementaÃ§Ã£o de ferro"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "Anemia gestacional pode comprometer o bem-estar materno-fetal e deve ser acompanhada.",
        "transcultural": {
            "preservacao": ["Considerar alimentos regionais ricos em ferro."],
            "acomodacao": ["Orientar alimentaÃ§Ã£o conforme disponibilidade local."],
            "repadronizacao": ["ReforÃ§ar adesÃ£o Ã  suplementaÃ§Ã£o quando houver risco."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Obesidade",
        "diagnostico": {"codigo": None, "termo": "Peso corporal aumentado"},
        "resultado": {"codigo": None, "termo": "Peso corporal adequado"},
        "intervencao": {"codigo": None, "termo": "Orientar alimentaÃ§Ã£o saudÃ¡vel"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "Obesidade na gestaÃ§Ã£o aumenta risco de hipertensÃ£o, diabetes gestacional e complicaÃ§Ãµes obstÃ©tricas.",
        "transcultural": {
            "preservacao": ["Reconhecer hÃ¡bitos alimentares familiares."],
            "acomodacao": ["Negociar mudanÃ§as possÃ­veis sem desconsiderar cultura alimentar."],
            "repadronizacao": ["Reorganizar plano alimentar e atividade fÃ­sica conforme risco."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "Manual de GestaÃ§Ã£o de Alto Risco.", "Leininger."]
    },

    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Baixo peso",
        "diagnostico": {"codigo": None, "termo": "Peso corporal diminuÃ­do"},
        "resultado": {"codigo": None, "termo": "Estado nutricional melhorado"},
        "intervencao": {"codigo": None, "termo": "Orientar alimentaÃ§Ã£o adequada"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "Baixo peso gestacional pode estar associado a vulnerabilidade nutricional e risco fetal.",
        "transcultural": {
            "preservacao": ["Considerar alimentos culturalmente aceitos."],
            "acomodacao": ["Ajustar plano alimentar Ã  renda e disponibilidade local."],
            "repadronizacao": ["Articular apoio alimentar quando houver inseguranÃ§a alimentar."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "Leininger.", "PNAB."]
    },

    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Tabagismo",
        "diagnostico": {"codigo": None, "termo": "Comportamento de saÃºde prejudicado"},
        "resultado": {"codigo": None, "termo": "Comportamento de saÃºde melhorado"},
        "intervencao": {"codigo": None, "termo": "Orientar cessaÃ§Ã£o do tabagismo"},
        "prioridade": "Alta",
        "fundamentacao": "Tabagismo na gestaÃ§Ã£o aumenta risco de complicaÃ§Ãµes maternas e fetais.",
        "transcultural": {
            "preservacao": [],
            "acomodacao": ["Investigar contexto familiar e social do uso de tabaco."],
            "repadronizacao": ["Construir plano gradual de reduÃ§Ã£o e cessaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Uso de Ã¡lcool",
        "diagnostico": {"codigo": None, "termo": "Comportamento de saÃºde prejudicado"},
        "resultado": {"codigo": None, "termo": "Comportamento de saÃºde melhorado"},
        "intervencao": {"codigo": None, "termo": "Orientar interrupÃ§Ã£o do uso de Ã¡lcool"},
        "prioridade": "Alta",
        "fundamentacao": "O uso de Ã¡lcool na gestaÃ§Ã£o representa risco para o desenvolvimento fetal.",
        "transcultural": {
            "preservacao": [],
            "acomodacao": ["Avaliar contexto social e familiar relacionado ao uso."],
            "repadronizacao": ["Encaminhar para rede de apoio quando houver uso persistente."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Uso de drogas",
        "diagnostico": {"codigo": None, "termo": "Comportamento de saÃºde prejudicado"},
        "resultado": {"codigo": None, "termo": "Comportamento de saÃºde melhorado"},
        "intervencao": {"codigo": None, "termo": "Encaminhar para cuidado compartilhado em saÃºde mental"},
        "prioridade": "Alta",
        "fundamentacao": "Uso de substÃ¢ncias psicoativas na gestaÃ§Ã£o exige cuidado multiprofissional e reduÃ§Ã£o de danos.",
        "transcultural": {
            "preservacao": [],
            "acomodacao": ["Realizar escuta qualificada sem julgamento."],
            "repadronizacao": ["Articular rede de saÃºde mental, assistÃªncia social e prÃ©-natal de alto risco."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "Rede de AtenÃ§Ã£o Psicossocial.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Idade materna menor que 15 anos",
        "diagnostico": {"codigo": None, "termo": "Risco materno-fetal aumentado"},
        "resultado": {"codigo": None, "termo": "Risco materno-fetal reduzido"},
        "intervencao": {"codigo": None, "termo": "Encaminhar para acompanhamento de prÃ©-natal de alto risco"},
        "prioridade": "Alta",
        "fundamentacao": "GestaÃ§Ã£o em adolescente muito jovem requer avaliaÃ§Ã£o ampliada de risco clÃ­nico, social e familiar.",
        "transcultural": {
            "preservacao": [],
            "acomodacao": ["Avaliar apoio familiar, vÃ­nculo escolar e proteÃ§Ã£o social."],
            "repadronizacao": ["Acionar rede de proteÃ§Ã£o quando necessÃ¡rio."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "ECA.", "COFEN 736/2024.", "Leininger."]
    },

    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Fatores de risco",
        "achado_clinico": "Idade materna maior ou igual a 35 anos",
        "diagnostico": {"codigo": None, "termo": "Risco materno-fetal aumentado"},
        "resultado": {"codigo": None, "termo": "Risco materno-fetal reduzido"},
        "intervencao": {"codigo": None, "termo": "Avaliar fatores de risco gestacional"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "Idade materna avanÃ§ada pode estar associada a maior risco obstÃ©trico e comorbidades.",
        "transcultural": {
            "preservacao": [],
            "acomodacao": ["Considerar histÃ³ria reprodutiva, rede de apoio e expectativas familiares."],
            "repadronizacao": ["Intensificar acompanhamento se houver comorbidades."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "Manual de GestaÃ§Ã£o de Alto Risco.", "Leininger."]
    }
]REGRAS = [
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "VacinaÃ§Ã£o",
        "achado_clinico": "SituaÃ§Ã£o vacinal desconhecida",
        "diagnostico": {"codigo": None, "termo": "SituaÃ§Ã£o vacinal prejudicada"},
        "resultado": {"codigo": None, "termo": "SituaÃ§Ã£o vacinal avaliada e atualizada"},
        "intervencao": {"codigo": None, "termo": "Avaliar situaÃ§Ã£o vacinal da gestante"},
        "prioridade": "Alta",
        "fundamentacao": "Na primeira consulta de prÃ©-natal, a situaÃ§Ã£o vacinal deve ser verificada por meio do cartÃ£o de vacina, registros disponÃ­veis e relato da gestante. Quando nÃ£o houver comprovaÃ§Ã£o, deve-se considerar esquema desconhecido e organizar a atualizaÃ§Ã£o vacinal conforme o CalendÃ¡rio Nacional de VacinaÃ§Ã£o da Gestante, incluindo hepatite B, dT, influenza, COVID-19 e dTpa a partir da 20Âª semana gestacional.",
        "transcultural": {
            "preservacao": [
                "Valorizar prÃ¡ticas familiares de cuidado que favoreÃ§am a proteÃ§Ã£o da gestante e do bebÃª.",
                "Manter diÃ¡logo respeitoso sobre experiÃªncias prÃ©vias com vacinaÃ§Ã£o."
            ],
            "acomodacao": [
                "Adequar a orientaÃ§Ã£o ao grau de escolaridade, idioma, cultura e contexto territorial da gestante.",
                "Negociar datas de vacinaÃ§Ã£o compatÃ­veis com deslocamento, trabalho, transporte e rotina familiar."
            ],
            "repadronizacao": [
                "Reformular crenÃ§as equivocadas sobre vacinas por meio de educaÃ§Ã£o em saÃºde clara, respeitosa e baseada em evidÃªncias.",
                "Estimular a reconstruÃ§Ã£o do cuidado prÃ©-natal com inclusÃ£o do cartÃ£o vacinal como documento essencial."
            ]
        },
        "referencias": [
            "MinistÃ©rio da SaÃºde. CalendÃ¡rio Nacional de VacinaÃ§Ã£o da Gestante, 2026.",
            "Programa Nacional de ImunizaÃ§Ãµes - PNI.",
            "COFEN ResoluÃ§Ã£o nÂº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "VacinaÃ§Ã£o",
        "achado_clinico": "Vacina dT incompleta",
        "diagnostico": {"codigo": None, "termo": "Risco de imunizaÃ§Ã£o incompleta contra difteria e tÃ©tano"},
        "resultado": {"codigo": None, "termo": "Esquema vacinal contra difteria e tÃ©tano completado"},
        "intervencao": {"codigo": None, "termo": "Completar esquema vacinal com dT conforme histÃ³rico vacinal"},
        "prioridade": "Alta",
        "fundamentacao": "A vacina dT Ã© indicada na gestaÃ§Ã£o conforme histÃ³rico vacinal, com objetivo de proteger contra difteria e tÃ©tano. Em esquema incompleto, nÃ£o se reinicia o esquema; devem ser completadas as doses necessÃ¡rias, respeitando intervalos recomendados e articulando a administraÃ§Ã£o da dTpa a partir da 20Âª semana gestacional.",
        "transcultural": {
            "preservacao": [
                "Reconhecer saberes familiares sobre prevenÃ§Ã£o de doenÃ§as e proteÃ§Ã£o materno-infantil."
            ],
            "acomodacao": [
                "Explicar o esquema em linguagem simples, utilizando o cartÃ£o vacinal como ferramenta visual.",
                "Ajustar o agendamento das doses conforme disponibilidade da gestante e da sala de vacina."
            ],
            "repadronizacao": [
                "Corrigir a ideia de que doses antigas tornam desnecessÃ¡ria a atualizaÃ§Ã£o vacinal.",
                "Fortalecer a adesÃ£o ao esquema completo como cuidado de proteÃ§Ã£o materna e neonatal."
            ]
        },
        "referencias": [
            "MinistÃ©rio da SaÃºde. CalendÃ¡rio Nacional de VacinaÃ§Ã£o da Gestante, 2026.",
            "Programa Nacional de ImunizaÃ§Ãµes - PNI.",
            "COFEN ResoluÃ§Ã£o nÂº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "VacinaÃ§Ã£o",
        "achado_clinico": "Vacina dTpa indicada",
        "diagnostico": {"codigo": None, "termo": "Necessidade de imunizaÃ§Ã£o contra difteria, tÃ©tano e coqueluche"},
        "resultado": {"codigo": None, "termo": "Gestante imunizada com dTpa"},
        "intervencao": {"codigo": None, "termo": "Administrar ou encaminhar para vacina dTpa a partir da 20Âª semana gestacional"},
        "prioridade": "Alta",
        "fundamentacao": "A vacina dTpa Ã© indicada em cada gestaÃ§Ã£o a partir da 20Âª semana gestacional, independentemente de vacinaÃ§Ã£o prÃ©via, com objetivo de reduzir o risco de tÃ©tano neonatal e coqueluche no recÃ©m-nascido por transferÃªncia transplacentÃ¡ria de anticorpos.",
        "transcultural": {
            "preservacao": [
                "Valorizar o desejo materno e familiar de proteger o recÃ©m-nascido."
            ],
            "acomodacao": [
                "Orientar que a vacina Ã© recomendada em cada gestaÃ§Ã£o, mesmo que tenha sido realizada em gestaÃ§Ã£o anterior.",
                "Organizar busca ativa ou encaminhamento conforme idade gestacional."
            ],
            "repadronizacao": [
                "Reformular crenÃ§as de que a dTpa seria desnecessÃ¡ria por vacinaÃ§Ã£o anterior.",
                "Estimular compreensÃ£o da vacina como proteÃ§Ã£o direta ao bebÃª nos primeiros meses de vida."
            ]
        },
        "referencias": [
            "MinistÃ©rio da SaÃºde. CalendÃ¡rio Nacional de VacinaÃ§Ã£o da Gestante, 2026.",
            "Programa Nacional de ImunizaÃ§Ãµes - PNI.",
            "COFEN ResoluÃ§Ã£o nÂº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "VacinaÃ§Ã£o",
        "achado_clinico": "Vacina dTpa nÃ£o realizada",
        "diagnostico": {"codigo": None, "termo": "ImunizaÃ§Ã£o materna ausente contra coqueluche"},
        "resultado": {"codigo": None, "termo": "VacinaÃ§Ã£o dTpa realizada no perÃ­odo oportuno"},
        "intervencao": {"codigo": None, "termo": "Realizar busca ativa para vacinaÃ§Ã£o dTpa"},
        "prioridade": "Alta",
        "fundamentacao": "A ausÃªncia da dTpa apÃ³s a 20Âª semana gestacional aumenta a vulnerabilidade do recÃ©m-nascido Ã  coqueluche e ao tÃ©tano neonatal. A equipe deve identificar a nÃ£o realizaÃ§Ã£o, orientar a gestante, registrar a pendÃªncia e encaminhar imediatamente para vacinaÃ§Ã£o.",
        "transcultural": {
            "preservacao": [
                "Manter vÃ­nculo e escuta qualificada sem julgamento."
            ],
            "acomodacao": [
                "Identificar motivo da nÃ£o vacinaÃ§Ã£o, como acesso, medo, esquecimento ou desinformaÃ§Ã£o.",
                "Adequar o plano de cuidado ao contexto familiar, cultural e territorial."
            ],
            "repadronizacao": [
                "Construir nova compreensÃ£o sobre a importÃ¢ncia da dTpa para proteÃ§Ã£o neonatal.",
                "Estimular registro e acompanhamento ativo das pendÃªncias vacinais."
            ]
        },
        "referencias": [
            "MinistÃ©rio da SaÃºde. CalendÃ¡rio Nacional de VacinaÃ§Ã£o da Gestante, 2026.",
            "Programa Nacional de ImunizaÃ§Ãµes - PNI.",
            "COFEN ResoluÃ§Ã£o nÂº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "VacinaÃ§Ã£o",
        "achado_clinico": "Vacina influenza indicada",
        "diagnostico": {"codigo": None, "termo": "Necessidade de imunizaÃ§Ã£o contra influenza"},
        "resultado": {"codigo": None, "termo": "Gestante imunizada contra influenza"},
        "intervencao": {"codigo": None, "termo": "Administrar ou encaminhar para vacina influenza sazonal"},
        "prioridade": "Alta",
        "fundamentacao": "Gestantes e puÃ©rperas pertencem a grupo prioritÃ¡rio para vacinaÃ§Ã£o contra influenza, devido ao maior risco de formas graves da doenÃ§a. A vacina influenza Ã© indicada em dose anual por temporada durante a gestaÃ§Ã£o.",
        "transcultural": {
            "preservacao": [
                "Respeitar prÃ¡ticas culturais seguras de prevenÃ§Ã£o de doenÃ§as respiratÃ³rias."
            ],
            "acomodacao": [
                "Explicar diferenÃ§a entre reaÃ§Ã£o vacinal leve e influenza.",
                "Planejar vacinaÃ§Ã£o conforme campanha vigente e disponibilidade local."
            ],
            "repadronizacao": [
                "Corrigir crenÃ§as de que a vacina causa gripe.",
                "Fortalecer a vacinaÃ§Ã£o como proteÃ§Ã£o da gestante e do bebÃª."
            ]
        },
        "referencias": [
            "MinistÃ©rio da SaÃºde. CalendÃ¡rio Nacional de VacinaÃ§Ã£o da Gestante, 2026.",
            "Programa Nacional de ImunizaÃ§Ãµes - PNI.",
            "COFEN ResoluÃ§Ã£o nÂº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "VacinaÃ§Ã£o",
        "achado_clinico": "Vacina influenza nÃ£o realizada",
        "diagnostico": {"codigo": None, "termo": "ImunizaÃ§Ã£o ausente contra influenza"},
        "resultado": {"codigo": None, "termo": "VacinaÃ§Ã£o contra influenza realizada"},
        "intervencao": {"codigo": None, "termo": "Orientar e encaminhar gestante para vacinaÃ§Ã£o contra influenza"},
        "prioridade": "Alta",
        "fundamentacao": "A nÃ£o realizaÃ§Ã£o da vacina influenza mantÃ©m a gestante suscetÃ­vel a complicaÃ§Ãµes respiratÃ³rias evitÃ¡veis. A equipe deve verificar a disponibilidade da vacina, orientar sobre seguranÃ§a e benefÃ­cio, registrar a pendÃªncia e realizar busca ativa.",
        "transcultural": {
            "preservacao": [
                "Valorizar medidas familiares seguras de cuidado respiratÃ³rio."
            ],
            "acomodacao": [
                "Investigar barreiras de acesso, medo de reaÃ§Ã£o ou experiÃªncias negativas anteriores.",
                "Ajustar orientaÃ§Ã£o conforme compreensÃ£o da gestante."
            ],
            "repadronizacao": [
                "Reformular informaÃ§Ãµes equivocadas sobre risco da vacina na gravidez.",
                "Estimular adesÃ£o anual Ã  vacinaÃ§Ã£o durante o prÃ©-natal."
            ]
        },
        "referencias": [
            "MinistÃ©rio da SaÃºde. CalendÃ¡rio Nacional de VacinaÃ§Ã£o da Gestante, 2026.",
            "Programa Nacional de ImunizaÃ§Ãµes - PNI.",
            "COFEN ResoluÃ§Ã£o nÂº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "VacinaÃ§Ã£o",
        "achado_clinico": "Vacina hepatite B incompleta",
        "diagnostico": {"codigo": None, "termo": "Risco de imunizaÃ§Ã£o incompleta contra hepatite B"},
        "resultado": {"codigo": None, "termo": "Esquema vacinal contra hepatite B completado"},
        "intervencao": {"codigo": None, "termo": "Completar esquema vacinal contra hepatite B"},
        "prioridade": "Alta",
        "fundamentacao": "A vacina hepatite B Ã© indicada na gestaÃ§Ã£o conforme histÃ³rico vacinal, em esquema de trÃªs doses quando nÃ£o houver comprovaÃ§Ã£o. Em esquema incompleto, nÃ£o se deve reiniciar; deve-se completar as doses faltantes conforme intervalo recomendado.",
        "transcultural": {
            "preservacao": [
                "Valorizar a preocupaÃ§Ã£o da gestante com proteÃ§Ã£o do bebÃª e prevenÃ§Ã£o de infecÃ§Ãµes."
            ],
            "acomodacao": [
                "Explicar o esquema de trÃªs doses e a necessidade de completar o calendÃ¡rio.",
                "Agendar retorno de acordo com deslocamento e acesso da gestante."
            ],
            "repadronizacao": [
                "Reformular a percepÃ§Ã£o de que uma ou duas doses garantem proteÃ§Ã£o completa.",
                "Fortalecer acompanhamento longitudinal atÃ© conclusÃ£o do esquema."
            ]
        },
        "referencias": [
            "MinistÃ©rio da SaÃºde. CalendÃ¡rio Nacional de VacinaÃ§Ã£o da Gestante, 2026.",
            "Programa Nacional de ImunizaÃ§Ãµes - PNI.",
            "COFEN ResoluÃ§Ã£o nÂº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "VacinaÃ§Ã£o",
        "achado_clinico": "Vacina hepatite B nÃ£o realizada",
        "diagnostico": {"codigo": None, "termo": "ImunizaÃ§Ã£o ausente contra hepatite B"},
        "resultado": {"codigo": None, "termo": "Esquema vacinal contra hepatite B iniciado"},
        "intervencao": {"codigo": None, "termo": "Iniciar vacinaÃ§Ã£o contra hepatite B conforme calendÃ¡rio da gestante"},
        "prioridade": "Alta",
        "fundamentacao": "Gestantes sem comprovaÃ§Ã£o de vacinaÃ§Ã£o contra hepatite B devem iniciar esquema vacinal de trÃªs doses, conforme o CalendÃ¡rio Nacional de VacinaÃ§Ã£o. A vacinaÃ§Ã£o reduz risco de infecÃ§Ã£o materna e contribui para prevenÃ§Ã£o de transmissÃ£o vertical associada ao cuidado prÃ©-natal adequado.",
        "transcultural": {
            "preservacao": [
                "Respeitar valores familiares relacionados Ã  proteÃ§Ã£o da gestaÃ§Ã£o."
            ],
            "acomodacao": [
                "Explicar a relaÃ§Ã£o entre hepatite B, gestaÃ§Ã£o e proteÃ§Ã£o do recÃ©m-nascido.",
                "Planejar as doses no calendÃ¡rio de consultas do prÃ©-natal."
            ],
            "repadronizacao": [
                "Superar desconhecimento sobre hepatite B e vacinaÃ§Ã£o na gravidez.",
                "Estimular continuidade do esquema atÃ© conclusÃ£o."
            ]
        },
        "referencias": [
            "MinistÃ©rio da SaÃºde. CalendÃ¡rio Nacional de VacinaÃ§Ã£o da Gestante, 2026.",
            "Programa Nacional de ImunizaÃ§Ãµes - PNI.",
            "COFEN ResoluÃ§Ã£o nÂº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "VacinaÃ§Ã£o",
        "achado_clinico": "Vacina COVID-19 indicada",
        "diagnostico": {"codigo": None, "termo": "Necessidade de imunizaÃ§Ã£o contra COVID-19"},
        "resultado": {"codigo": None, "termo": "Gestante imunizada contra COVID-19"},
        "intervencao": {"codigo": None, "termo": "Encaminhar gestante para vacinaÃ§Ã£o contra COVID-19"},
        "prioridade": "Alta",
        "fundamentacao": "A vacinaÃ§Ã£o contra COVID-19 Ã© indicada para gestantes em cada gestaÃ§Ã£o, conforme CalendÃ¡rio Nacional de VacinaÃ§Ã£o, com objetivo de reduzir formas graves, hospitalizaÃ§Ãµes e Ã³bitos por SARS-CoV-2.",
        "transcultural": {
            "preservacao": [
                "Manter escuta respeitosa sobre experiÃªncias pessoais e familiares durante a pandemia."
            ],
            "acomodacao": [
                "Esclarecer dÃºvidas sobre seguranÃ§a, indicaÃ§Ã£o e benefÃ­cio da vacina.",
                "Considerar medos, crenÃ§as religiosas, culturais e experiÃªncias anteriores."
            ],
            "repadronizacao": [
                "Reformular informaÃ§Ãµes falsas ou inseguras sobre vacinaÃ§Ã£o contra COVID-19 na gestaÃ§Ã£o.",
                "Promover decisÃ£o informada baseada em evidÃªncias e no cuidado materno-fetal."
            ]
        },
        "referencias": [
            "MinistÃ©rio da SaÃºde. CalendÃ¡rio Nacional de VacinaÃ§Ã£o da Gestante, 2026.",
            "Programa Nacional de ImunizaÃ§Ãµes - PNI.",
            "COFEN ResoluÃ§Ã£o nÂº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "VacinaÃ§Ã£o",
        "achado_clinico": "Recusa vacinal",
        "diagnostico": {"codigo": None, "termo": "AdesÃ£o prejudicada Ã  vacinaÃ§Ã£o"},
        "resultado": {"codigo": None, "termo": "Gestante orientada e decisÃ£o vacinal reavaliada"},
        "intervencao": {"codigo": None, "termo": "Realizar aconselhamento sobre vacinaÃ§Ã£o na gestaÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "A recusa vacinal deve ser acolhida com escuta qualificada, identificaÃ§Ã£o dos motivos, orientaÃ§Ã£o baseada em evidÃªncias e registro em prontuÃ¡rio. A abordagem deve respeitar autonomia, cultura e crenÃ§as, sem deixar de informar riscos da nÃ£o vacinaÃ§Ã£o para gestante e recÃ©m-nascido.",
        "transcultural": {
            "preservacao": [
                "Preservar vÃ­nculo, autonomia e respeito Ã s crenÃ§as da gestante."
            ],
            "acomodacao": [
                "Negociar nova conversa, envolver pessoa de confianÃ§a quando autorizado e oferecer material educativo.",
                "Adequar linguagem e estratÃ©gia educativa Ã  realidade sociocultural."
            ],
            "repadronizacao": [
                "Reformular mitos e informaÃ§Ãµes falsas sem confronto ou julgamento.",
                "Construir plano gradual de adesÃ£o vacinal com decisÃ£o compartilhada."
            ]
        },
        "referencias": [
            "MinistÃ©rio da SaÃºde. CalendÃ¡rio Nacional de VacinaÃ§Ã£o da Gestante, 2026.",
            "Programa Nacional de ImunizaÃ§Ãµes - PNI.",
            "COFEN ResoluÃ§Ã£o nÂº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "VacinaÃ§Ã£o",
        "achado_clinico": "Medo de reaÃ§Ã£o vacinal",
        "diagnostico": {"codigo": None, "termo": "Medo relacionado Ã  vacinaÃ§Ã£o"},
        "resultado": {"codigo": None, "termo": "Medo reduzido e vacinaÃ§Ã£o aceita ou reavaliada"},
        "intervencao": {"codigo": None, "termo": "Orientar sobre eventos adversos esperados e sinais de alerta"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "O medo de reaÃ§Ã£o vacinal Ã© uma barreira comum Ã  adesÃ£o. A equipe deve explicar possÃ­veis eventos leves, sinais de alerta, condutas apÃ³s vacinaÃ§Ã£o e benefÃ­cios da imunizaÃ§Ã£o durante a gestaÃ§Ã£o, fortalecendo seguranÃ§a e autonomia da gestante.",
        "transcultural": {
            "preservacao": [
                "Acolher relatos de experiÃªncias anteriores da gestante ou familiares."
            ],
            "acomodacao": [
                "Explicar reaÃ§Ãµes esperadas em linguagem simples e oferecer suporte pÃ³s-vacinaÃ§Ã£o.",
                "Permitir tempo para perguntas e tomada de decisÃ£o."
            ],
            "repadronizacao": [
                "Diferenciar reaÃ§Ã£o vacinal leve de doenÃ§a grave evitÃ¡vel por vacina.",
                "Reduzir medo por meio de educaÃ§Ã£o em saÃºde baseada em evidÃªncias."
            ]
        },
        "referencias": [
            "MinistÃ©rio da SaÃºde. CalendÃ¡rio Nacional de VacinaÃ§Ã£o da Gestante, 2026.",
            "Programa Nacional de ImunizaÃ§Ãµes - PNI.",
            "COFEN ResoluÃ§Ã£o nÂº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "VacinaÃ§Ã£o",
        "achado_clinico": "Falta de acesso Ã  sala de vacina",
        "diagnostico": {"codigo": None, "termo": "Acesso prejudicado Ã  vacinaÃ§Ã£o"},
        "resultado": {"codigo": None, "termo": "Acesso Ã  vacinaÃ§Ã£o garantido"},
        "intervencao": {"codigo": None, "termo": "Articular acesso da gestante Ã  sala de vacina"},
        "prioridade": "Alta",
        "fundamentacao": "A falta de acesso Ã  sala de vacina compromete a integralidade do prÃ©-natal e aumenta risco de atraso vacinal. A equipe deve articular agendamento, transporte sanitÃ¡rio quando disponÃ­vel, vacinaÃ§Ã£o em aÃ§Ãµes extramuros, busca ativa e integraÃ§Ã£o entre prÃ©-natal e imunizaÃ§Ã£o.",
        "transcultural": {
            "preservacao": [
                "Reconhecer estratÃ©gias comunitÃ¡rias de deslocamento e apoio familiar."
            ],
            "acomodacao": [
                "Adequar o plano vacinal aos dias de atendimento, transporte e permanÃªncia da gestante no territÃ³rio urbano ou rural.",
                "Articular com ACS, equipe ribeirinha, unidade de referÃªncia ou sala de vacina."
            ],
            "repadronizacao": [
                "Transformar o cuidado fragmentado em acompanhamento programado e territorializado.",
                "Estimular registro ativo das pendÃªncias vacinais pela equipe."
            ]
        },
        "referencias": [
            "MinistÃ©rio da SaÃºde. CalendÃ¡rio Nacional de VacinaÃ§Ã£o da Gestante, 2026.",
            "Programa Nacional de ImunizaÃ§Ãµes - PNI.",
            "COFEN ResoluÃ§Ã£o nÂº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "VacinaÃ§Ã£o",
        "achado_clinico": "Barreiras culturais relacionadas Ã  vacinaÃ§Ã£o",
        "diagnostico": {"codigo": None, "termo": "Conflito cultural relacionado Ã  vacinaÃ§Ã£o"},
        "resultado": {"codigo": None, "termo": "Barreiras culturais identificadas e manejadas"},
        "intervencao": {"codigo": None, "termo": "Realizar cuidado culturalmente congruente sobre vacinaÃ§Ã£o"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "Barreiras culturais podem envolver crenÃ§as familiares, religiosas, comunitÃ¡rias, experiÃªncias histÃ³ricas de desconfianÃ§a, medo de dano fetal ou informaÃ§Ãµes falsas. A abordagem deve seguir cuidado culturalmente congruente, com preservaÃ§Ã£o de prÃ¡ticas seguras, acomodaÃ§Ã£o de valores e repadronizaÃ§Ã£o de prÃ¡ticas prejudiciais.",
        "transcultural": {
            "preservacao": [
                "Preservar prÃ¡ticas culturais que nÃ£o tragam risco Ã  gestante ou ao bebÃª.",
                "Valorizar lideranÃ§as familiares e comunitÃ¡rias quando favorecem o cuidado."
            ],
            "acomodacao": [
                "Negociar estratÃ©gias educativas compatÃ­veis com crenÃ§as e organizaÃ§Ã£o familiar.",
                "Usar linguagem respeitosa, exemplos locais e escuta ativa."
            ],
            "repadronizacao": [
                "Reformular prÃ¡ticas ou crenÃ§as que impeÃ§am vacinaÃ§Ã£o segura.",
                "Construir novo significado da vacina como proteÃ§Ã£o materna, fetal e comunitÃ¡ria."
            ]
        },
        "referencias": [
            "MinistÃ©rio da SaÃºde. CalendÃ¡rio Nacional de VacinaÃ§Ã£o da Gestante, 2026.",
            "Programa Nacional de ImunizaÃ§Ãµes - PNI.",
            "COFEN ResoluÃ§Ã£o nÂº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "VacinaÃ§Ã£o",
        "achado_clinico": "Gestante ribeirinha com dificuldade de acesso Ã  vacina",
        "diagnostico": {"codigo": None, "termo": "Vulnerabilidade territorial para atraso vacinal"},
        "resultado": {"codigo": None, "termo": "VacinaÃ§Ã£o viabilizada conforme realidade territorial"},
        "intervencao": {"codigo": None, "termo": "Planejar vacinaÃ§Ã£o conforme contexto ribeirinho"},
        "prioridade": "Alta",
        "fundamentacao": "Gestantes ribeirinhas podem apresentar atraso vacinal por distÃ¢ncia geogrÃ¡fica, transporte fluvial, sazonalidade dos rios, custos de deslocamento e ausÃªncia de sala de vacina prÃ³xima. A equipe deve planejar cuidado territorial, busca ativa, vacinaÃ§Ã£o em aÃ§Ãµes itinerantes e articulaÃ§Ã£o com rede de atenÃ§Ã£o.",
        "transcultural": {
            "preservacao": [
                "Valorizar modos de vida ribeirinhos, redes comunitÃ¡rias e formas locais de organizaÃ§Ã£o do cuidado."
            ],
            "acomodacao": [
                "Adequar datas de vacinaÃ§Ã£o ao calendÃ¡rio das embarcaÃ§Ãµes, cheia/vazante dos rios e consultas de prÃ©-natal.",
                "Articular com ACS, equipe fluvial, UBS de referÃªncia e gestÃ£o local."
            ],
            "repadronizacao": [
                "Substituir cuidado oportunÃ­stico por plano vacinal programado e acompanhado.",
                "Estimular registro, busca ativa e monitoramento das pendÃªncias vacinais em territÃ³rios de difÃ­cil acesso."
            ]
        },
        "referencias": [
            "MinistÃ©rio da SaÃºde. CalendÃ¡rio Nacional de VacinaÃ§Ã£o da Gestante, 2026.",
            "Programa Nacional de ImunizaÃ§Ãµes - PNI.",
            "COFEN ResoluÃ§Ã£o nÂº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "VacinaÃ§Ã£o",
        "achado_clinico": "Gestante sem cartÃ£o vacinal",
        "diagnostico": {"codigo": None, "termo": "Registro vacinal ausente"},
        "resultado": {"codigo": None, "termo": "Registro vacinal recuperado ou atualizado"},
        "intervencao": {"codigo": None, "termo": "Solicitar, recuperar ou reconstruir registro vacinal"},
        "prioridade": "Alta",
        "fundamentacao": "A ausÃªncia do cartÃ£o vacinal dificulta a avaliaÃ§Ã£o da situaÃ§Ã£o imunolÃ³gica da gestante. A equipe deve buscar registros em sistemas disponÃ­veis, orientar emissÃ£o ou segunda via quando possÃ­vel e, na ausÃªncia de comprovaÃ§Ã£o, conduzir o esquema conforme situaÃ§Ã£o vacinal desconhecida.",
        "transcultural": {
            "preservacao": [
                "Evitar culpabilizaÃ§Ã£o da gestante pela perda ou ausÃªncia do documento."
            ],
            "acomodacao": [
                "Orientar sobre guarda do cartÃ£o junto aos documentos do prÃ©-natal.",
                "Auxiliar na recuperaÃ§Ã£o de registros conforme rede local."
            ],
            "repadronizacao": [
                "Reorganizar o cuidado para que o cartÃ£o vacinal seja acompanhado em todas as consultas.",
                "Estimular corresponsabilizaÃ§Ã£o entre gestante, famÃ­lia e equipe."
            ]
        },
        "referencias": [
            "MinistÃ©rio da SaÃºde. CalendÃ¡rio Nacional de VacinaÃ§Ã£o da Gestante, 2026.",
            "Programa Nacional de ImunizaÃ§Ãµes - PNI.",
            "COFEN ResoluÃ§Ã£o nÂº 736/2024.",
            "Leininger M. Teoria da Diversidade e Universalidade do Cuidado Cultural."
        ]
    }
]REGRAS = [
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Hemoglobina baixa",
        "diagnostico": {"codigo": "10012606", "termo": "Processo do Sistema CirculatÃ³rio, Prejudicado"},
        "resultado": {"codigo": "10028379", "termo": "Processo do Sistema CirculatÃ³rio, Positivo"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre NutriÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "Hemoglobina baixa no prÃ©-natal sugere anemia gestacional, associada a maior risco de fadiga, infecÃ§Ã£o, parto prematuro, baixo peso ao nascer e morbimortalidade materno-fetal. A conduta de enfermagem inclui avaliaÃ§Ã£o clÃ­nica, orientaÃ§Ã£o alimentar rica em ferro, adesÃ£o Ã  suplementaÃ§Ã£o prescrita, investigaÃ§Ã£o de sinais de gravidade e encaminhamento conforme protocolo.",
        "transcultural": {
            "preservacao": ["Valorizar alimentos culturalmente aceitos e ricos em ferro disponÃ­veis no territÃ³rio."],
            "acomodacao": ["Adaptar orientaÃ§Ãµes alimentares Ã  renda, acesso, hÃ¡bitos familiares e crenÃ§as da gestante."],
            "repadronizacao": ["Reorientar prÃ¡ticas alimentares que reduzam absorÃ§Ã£o de ferro, como consumo de cafÃ© junto Ã s refeiÃ§Ãµes."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde. AtenÃ§Ã£o ao prÃ©-natal de baixo risco.", "FEBRASGO. RecomendaÃ§Ãµes para anemia na gestaÃ§Ã£o.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "OMS. RecomendaÃ§Ãµes de cuidado prÃ©-natal.", "Leininger. Teoria Transcultural."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "HematÃ³crito baixo",
        "diagnostico": {"codigo": "10012606", "termo": "Processo do Sistema CirculatÃ³rio, Prejudicado"},
        "resultado": {"codigo": "10028379", "termo": "Processo do Sistema CirculatÃ³rio, Positivo"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre MedicaÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "HematÃ³crito baixo pode indicar hemodiluiÃ§Ã£o fisiolÃ³gica ou anemia, devendo ser interpretado em conjunto com hemoglobina, ferritina, sinais clÃ­nicos e idade gestacional. A enfermagem deve orientar uso correto de sulfato ferroso quando prescrito, alimentaÃ§Ã£o adequada e seguimento laboratorial.",
        "transcultural": {
            "preservacao": ["Reconhecer prÃ¡ticas alimentares familiares protetoras."],
            "acomodacao": ["Negociar horÃ¡rios de suplementaÃ§Ã£o conforme rotina da gestante."],
            "repadronizacao": ["Corrigir crenÃ§as que levem Ã  suspensÃ£o do ferro por nÃ¡useas ou escurecimento das fezes."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Ferritina baixa",
        "diagnostico": {"codigo": "10023009", "termo": "IngestÃ£o Nutricional, Prejudicada"},
        "resultado": {"codigo": "10037572", "termo": "IngestÃ£o Nutricional, nos Limites Normais"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre NutriÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "Ferritina baixa indica reduÃ§Ã£o das reservas de ferro, podendo anteceder ou acompanhar anemia ferropriva. No prÃ©-natal, exige orientaÃ§Ã£o nutricional, avaliaÃ§Ã£o de adesÃ£o Ã  suplementaÃ§Ã£o e monitoramento para prevenÃ§Ã£o de repercussÃµes maternas e fetais.",
        "transcultural": {
            "preservacao": ["Estimular alimentos regionais ricos em ferro."],
            "acomodacao": ["Adequar plano alimentar Ã  disponibilidade local."],
            "repadronizacao": ["Orientar combinaÃ§Ã£o com fontes de vitamina C e evitar inibidores de absorÃ§Ã£o junto Ã s refeiÃ§Ãµes."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Vitamina B12 baixa",
        "diagnostico": {"codigo": "10023009", "termo": "IngestÃ£o Nutricional, Prejudicada"},
        "resultado": {"codigo": "10037572", "termo": "IngestÃ£o Nutricional, nos Limites Normais"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre NutriÃ§Ã£o"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "Vitamina B12 baixa pode contribuir para anemia megaloblÃ¡stica, sintomas neurolÃ³gicos e alteraÃ§Ãµes no desenvolvimento fetal. A enfermagem deve orientar alimentaÃ§Ã£o, investigar dietas restritivas e encaminhar para avaliaÃ§Ã£o e reposiÃ§Ã£o conforme protocolo.",
        "transcultural": {
            "preservacao": ["Respeitar escolhas alimentares culturais ou religiosas."],
            "acomodacao": ["Adequar orientaÃ§Ã£o para gestantes vegetarianas, veganas ou com baixa ingestÃ£o de alimentos de origem animal."],
            "repadronizacao": ["Reorientar restriÃ§Ãµes alimentares com risco nutricional sem acompanhamento profissional."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Vitamina D baixa",
        "diagnostico": {"codigo": "10023009", "termo": "IngestÃ£o Nutricional, Prejudicada"},
        "resultado": {"codigo": "10037572", "termo": "IngestÃ£o Nutricional, nos Limites Normais"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre NutriÃ§Ã£o"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "Vitamina D baixa pode relacionar-se a alteraÃ§Ãµes Ã³sseas, metabÃ³licas e imunolÃ³gicas. Na gestaÃ§Ã£o, deve ser avaliada conforme risco clÃ­nico, dieta, exposiÃ§Ã£o solar e protocolo local, com orientaÃ§Ã£o segura e encaminhamento quando necessÃ¡rio.",
        "transcultural": {
            "preservacao": ["Considerar hÃ¡bitos culturais de vestimenta e exposiÃ§Ã£o solar."],
            "acomodacao": ["Orientar exposiÃ§Ã£o solar segura conforme realidade territorial."],
            "repadronizacao": ["Evitar automedicaÃ§Ã£o com doses elevadas sem prescriÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Glicemia alterada",
        "diagnostico": {"codigo": "10005876", "termo": "Diabetes"},
        "resultado": {"codigo": "10027532", "termo": "Processo do Sistema RegulatÃ³rio, Eficaz"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre NutriÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "Glicemia alterada no prÃ©-natal pode indicar risco de diabetes mellitus gestacional ou diabetes prÃ©vio nÃ£o diagnosticado. Deve-se orientar alimentaÃ§Ã£o adequada, atividade fÃ­sica quando nÃ£o contraindicada, controle glicÃªmico, avaliaÃ§Ã£o mÃ©dica e seguimento conforme protocolo.",
        "transcultural": {
            "preservacao": ["Valorizar alimentos tradicionais saudÃ¡veis e acessÃ­veis."],
            "acomodacao": ["Adaptar plano alimentar Ã  cultura, renda e rotina familiar."],
            "repadronizacao": ["Reduzir consumo frequente de aÃ§Ãºcar, bebidas adoÃ§adas e ultraprocessados."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "TOTG alterado",
        "diagnostico": {"codigo": "10005876", "termo": "Diabetes"},
        "resultado": {"codigo": "10027532", "termo": "Processo do Sistema RegulatÃ³rio, Eficaz"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "Alta",
        "fundamentacao": "TOTG alterado confirma alteraÃ§Ã£o do metabolismo glicÃªmico na gestaÃ§Ã£o e exige acompanhamento para prevenÃ§Ã£o de macrossomia, prÃ©-eclÃ¢mpsia, parto traumÃ¡tico, hipoglicemia neonatal e complicaÃ§Ãµes maternas. A enfermagem deve orientar tratamento, autocuidado e seguimento multiprofissional.",
        "transcultural": {
            "preservacao": ["Manter alimentos culturais que sejam adequados ao controle glicÃªmico."],
            "acomodacao": ["Construir plano possÃ­vel conforme acesso a alimentos e rotina da gestante."],
            "repadronizacao": ["Substituir padrÃµes alimentares de alto Ã­ndice glicÃªmico por alternativas locais mais saudÃ¡veis."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "ProteinÃºria",
        "diagnostico": {"codigo": "10001359", "termo": "FunÃ§Ã£o do Sistema UrinÃ¡rio, Prejudicada"},
        "resultado": {"codigo": "10028615", "termo": "FunÃ§Ã£o do Sistema UrinÃ¡rio, Eficaz"},
        "intervencao": {"codigo": "10044148", "termo": "Orientar sobre MediÃ§Ã£o de PressÃ£o Arterial"},
        "prioridade": "Alta",
        "fundamentacao": "ProteinÃºria na gestaÃ§Ã£o pode estar associada a infecÃ§Ã£o urinÃ¡ria, doenÃ§a renal ou prÃ©-eclÃ¢mpsia, especialmente quando acompanhada de hipertensÃ£o, cefaleia, escotomas, dor epigÃ¡strica ou edema. Exige avaliaÃ§Ã£o imediata, controle pressÃ³rico e encaminhamento conforme gravidade.",
        "transcultural": {
            "preservacao": ["Acolher relatos de sintomas conforme linguagem e interpretaÃ§Ã£o cultural da gestante."],
            "acomodacao": ["Orientar sinais de alerta de forma simples e objetiva."],
            "repadronizacao": ["ReforÃ§ar que edema importante, cefaleia ou alteraÃ§Ãµes visuais nÃ£o devem ser tratados apenas com medidas caseiras."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Creatinina alterada",
        "diagnostico": {"codigo": "10012972", "termo": "Processo do Sistema UrinÃ¡rio, Prejudicado"},
        "resultado": {"codigo": "10028604", "termo": "Processo do Sistema UrinÃ¡rio, Eficaz"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "Alta",
        "fundamentacao": "Creatinina alterada na gestaÃ§Ã£o pode indicar comprometimento renal, doenÃ§a hipertensiva, infecÃ§Ã£o ou condiÃ§Ã£o clÃ­nica de maior risco. Deve-se avaliar sinais associados, pressÃ£o arterial, proteinÃºria, hidrataÃ§Ã£o, medicamentos em uso e necessidade de referÃªncia ao prÃ©-natal de alto risco.",
        "transcultural": {
            "preservacao": ["Considerar prÃ¡ticas locais de ingestÃ£o hÃ­drica e uso de chÃ¡s."],
            "acomodacao": ["Orientar hidrataÃ§Ã£o segura e evitar automedicaÃ§Ã£o."],
            "repadronizacao": ["Desestimular uso de plantas medicinais potencialmente nefrotÃ³xicas sem avaliaÃ§Ã£o profissional."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Plaquetopenia",
        "diagnostico": {"codigo": "10012606", "termo": "Processo do Sistema CirculatÃ³rio, Prejudicado"},
        "resultado": {"codigo": "10028379", "termo": "Processo do Sistema CirculatÃ³rio, Positivo"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "Alta",
        "fundamentacao": "Plaquetopenia na gestaÃ§Ã£o pode ser gestacional, imunolÃ³gica ou associada a sÃ­ndromes hipertensivas graves, como prÃ©-eclÃ¢mpsia e HELLP. A avaliaÃ§Ã£o deve considerar valores seriados, sangramentos, pressÃ£o arterial, enzimas hepÃ¡ticas e sinais de gravidade.",
        "transcultural": {
            "preservacao": ["Acolher relatos de sangramentos e sinais percebidos pela gestante."],
            "acomodacao": ["Orientar procura imediata diante de sangramento, dor epigÃ¡strica, cefaleia intensa ou mal-estar."],
            "repadronizacao": ["Evitar banalizaÃ§Ã£o de manchas roxas, sangramento gengival ou epistaxe na gestaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Urocultura positiva",
        "diagnostico": {"codigo": "10029915", "termo": "InfecÃ§Ã£o do Trato UrinÃ¡rio"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre InfecÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "Urocultura positiva na gestaÃ§Ã£o indica infecÃ§Ã£o urinÃ¡ria ou bacteriÃºria significativa, condiÃ§Ãµes associadas a pielonefrite, parto prematuro e baixo peso ao nascer. A enfermagem deve orientar adesÃ£o ao tratamento, hidrataÃ§Ã£o, sinais de alerta e controle apÃ³s tratamento.",
        "transcultural": {
            "preservacao": ["Reconhecer prÃ¡ticas de cuidado Ã­ntimo culturalmente aceitas e seguras."],
            "acomodacao": ["Orientar higiene, hidrataÃ§Ã£o e uso correto do antibiÃ³tico conforme prescriÃ§Ã£o."],
            "repadronizacao": ["Desestimular interrupÃ§Ã£o do tratamento quando sintomas melhorarem."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "BacteriÃºria assintomÃ¡tica",
        "diagnostico": {"codigo": "10051950", "termo": "Risco de InfecÃ§Ã£o UrinÃ¡ria"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10038112", "termo": "Orientar sobre PrevenÃ§Ã£o de InfecÃ§Ã£o Cruzada"},
        "prioridade": "Alta",
        "fundamentacao": "BacteriÃºria assintomÃ¡tica no prÃ©-natal deve ser tratada conforme protocolo por risco de evoluÃ§Ã£o para pielonefrite e complicaÃ§Ãµes obstÃ©tricas. Mesmo sem sintomas, requer orientaÃ§Ã£o, tratamento prescrito, retorno e controle laboratorial.",
        "transcultural": {
            "preservacao": ["Acolher a percepÃ§Ã£o da gestante de estar saudÃ¡vel por nÃ£o apresentar sintomas."],
            "acomodacao": ["Explicar que ausÃªncia de sintomas nÃ£o exclui risco gestacional."],
            "repadronizacao": ["ReforÃ§ar necessidade de tratamento completo mesmo sem dor ou ardÃªncia urinÃ¡ria."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "VDRL reagente",
        "diagnostico": {"codigo": "10023032", "termo": "InfecÃ§Ã£o"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre InfecÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "VDRL reagente no prÃ©-natal sugere sÃ­filis e exige confirmaÃ§Ã£o/avaliaÃ§Ã£o conforme protocolo, tratamento imediato com penicilina quando indicado, tratamento de parceria sexual, notificaÃ§Ã£o e seguimento sorolÃ³gico para prevenÃ§Ã£o da sÃ­filis congÃªnita.",
        "transcultural": {
            "preservacao": ["Acolher a gestante sem julgamento moral."],
            "acomodacao": ["Incluir parceria sexual no cuidado quando autorizado e conforme protocolo."],
            "repadronizacao": ["Reduzir estigma e reforÃ§ar que tratamento adequado previne transmissÃ£o vertical."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde. Protocolo ClÃ­nico e Diretrizes TerapÃªuticas para IST.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "HIV reagente",
        "diagnostico": {"codigo": "10023032", "termo": "InfecÃ§Ã£o"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "Alta",
        "fundamentacao": "HIV reagente na gestaÃ§Ã£o requer acolhimento, confirmaÃ§Ã£o diagnÃ³stica conforme fluxo, inÃ­cio ou continuidade imediata da terapia antirretroviral, avaliaÃ§Ã£o da carga viral, prevenÃ§Ã£o da transmissÃ£o vertical, orientaÃ§Ã£o sobre parto, puerpÃ©rio e alimentaÃ§Ã£o infantil conforme protocolo.",
        "transcultural": {
            "preservacao": ["Garantir sigilo, acolhimento e respeito Ã  identidade da gestante."],
            "acomodacao": ["Adaptar orientaÃ§Ãµes Ã  rede de apoio e ao contexto familiar."],
            "repadronizacao": ["Combater estigma, abandono do tratamento e crenÃ§as que dificultem adesÃ£o Ã  TARV."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde. PCDT para manejo da infecÃ§Ã£o pelo HIV em gestantes.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "HBsAg reagente",
        "diagnostico": {"codigo": "10023032", "termo": "InfecÃ§Ã£o"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre InfecÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "HBsAg reagente indica infecÃ§Ã£o pelo vÃ­rus da hepatite B e exige avaliaÃ§Ã£o clÃ­nica, exames complementares, seguimento especializado quando indicado e planejamento da profilaxia neonatal com vacina e imunoglobulina conforme protocolo para prevenÃ§Ã£o da transmissÃ£o vertical.",
        "transcultural": {
            "preservacao": ["Acolher medos e crenÃ§as familiares sobre hepatites."],
            "acomodacao": ["Orientar prevenÃ§Ã£o de transmissÃ£o domiciliar e vacinaÃ§Ã£o de contatos."],
            "repadronizacao": ["Reduzir estigma e reforÃ§ar medidas efetivas de prevenÃ§Ã£o neonatal."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde. Hepatites virais e prÃ©-natal.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Hepatite C reagente",
        "diagnostico": {"codigo": "10023032", "termo": "InfecÃ§Ã£o"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre InfecÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "Hepatite C reagente na gestaÃ§Ã£o requer confirmaÃ§Ã£o diagnÃ³stica, avaliaÃ§Ã£o de coinfecÃ§Ãµes, funÃ§Ã£o hepÃ¡tica e encaminhamento para seguimento. A enfermagem deve orientar prevenÃ§Ã£o de transmissÃ£o, evitar exposiÃ§Ã£o sanguÃ­nea e garantir acompanhamento materno e neonatal.",
        "transcultural": {
            "preservacao": ["Acolher a gestante sem julgamento."],
            "acomodacao": ["Adequar orientaÃ§Ãµes preventivas Ã  realidade familiar e comunitÃ¡ria."],
            "repadronizacao": ["Corrigir crenÃ§as sobre transmissÃ£o por contato casual."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde. Hepatites virais.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "RubÃ©ola nÃ£o imune",
        "diagnostico": {"codigo": "10041093", "termo": "Processo do Sistema ImunolÃ³gico, Prejudicado"},
        "resultado": {"codigo": "10047463", "termo": "Processo do Sistema Imune, Eficaz"},
        "intervencao": {"codigo": "10045079", "termo": "Orientar sobre GestaÃ§Ã£o"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "RubÃ©ola nÃ£o imune indica suscetibilidade. Como a vacina trÃ­plice viral Ã© contraindicada durante a gestaÃ§Ã£o por ser vacina de vÃ­rus vivo atenuado, deve-se orientar prevenÃ§Ã£o de exposiÃ§Ã£o e vacinaÃ§Ã£o no puerpÃ©rio, conforme calendÃ¡rio vacinal.",
        "transcultural": {
            "preservacao": ["Valorizar redes familiares de proteÃ§Ã£o da gestante."],
            "acomodacao": ["Orientar evitar contato com pessoas com exantema ou suspeita de rubÃ©ola."],
            "repadronizacao": ["Explicar que a vacina deve ser realizada apÃ³s o parto, nÃ£o durante a gestaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde. CalendÃ¡rio Nacional de VacinaÃ§Ã£o.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Toxoplasmose IgM positivo",
        "diagnostico": {"codigo": "10023032", "termo": "InfecÃ§Ã£o"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre InfecÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "Toxoplasmose IgM positivo pode indicar infecÃ§Ã£o recente e risco de transmissÃ£o fetal. Deve-se confirmar diagnÃ³stico com sorologia complementar, avididade quando aplicÃ¡vel, idade gestacional, avaliaÃ§Ã£o mÃ©dica e inÃ­cio oportuno de tratamento conforme protocolo.",
        "transcultural": {
            "preservacao": ["Respeitar prÃ¡ticas alimentares locais seguras."],
            "acomodacao": ["Orientar higiene dos alimentos, cozimento adequado de carnes e cuidado com solo e fezes de gatos."],
            "repadronizacao": ["Modificar consumo de carnes cruas, malpassadas ou alimentos sem higienizaÃ§Ã£o adequada."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde. PrÃ©-natal de baixo risco.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Toxoplasmose suscetÃ­vel",
        "diagnostico": {"codigo": "10015133", "termo": "Risco de InfecÃ§Ã£o"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10038112", "termo": "Orientar sobre PrevenÃ§Ã£o de InfecÃ§Ã£o Cruzada"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "Gestante suscetÃ­vel Ã  toxoplasmose nÃ£o possui imunidade e deve receber orientaÃ§Ãµes preventivas durante toda a gestaÃ§Ã£o, com repetiÃ§Ã£o sorolÃ³gica conforme protocolo local para detecÃ§Ã£o precoce de soroconversÃ£o.",
        "transcultural": {
            "preservacao": ["Manter prÃ¡ticas culinÃ¡rias regionais seguras."],
            "acomodacao": ["Adequar orientaÃ§Ã£o ao acesso Ã  Ã¡gua tratada, alimentos e condiÃ§Ãµes de preparo."],
            "repadronizacao": ["ReforÃ§ar lavagem de frutas e verduras, uso de Ã¡gua segura e evitar carne crua ou malcozida."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Coombs indireto positivo",
        "diagnostico": {"codigo": "10012606", "termo": "Processo do Sistema CirculatÃ³rio, Prejudicado"},
        "resultado": {"codigo": "10028379", "termo": "Processo do Sistema CirculatÃ³rio, Positivo"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "Alta",
        "fundamentacao": "Coombs indireto positivo em gestante pode indicar aloimunizaÃ§Ã£o materna, com risco de doenÃ§a hemolÃ­tica fetal e neonatal. Requer avaliaÃ§Ã£o especializada, monitoramento de tÃ­tulos, investigaÃ§Ã£o fetal quando indicada e seguimento em prÃ©-natal de alto risco.",
        "transcultural": {
            "preservacao": ["Acolher dÃºvidas familiares sobre incompatibilidade sanguÃ­nea."],
            "acomodacao": ["Explicar de forma simples a necessidade de acompanhamento especializado."],
            "repadronizacao": ["Evitar abandono do seguimento por ausÃªncia de sintomas maternos."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "OMS.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames laboratoriais",
        "achado_clinico": "Tipagem Rh negativo",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10028379", "termo": "Processo do Sistema CirculatÃ³rio, Positivo"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "Alta",
        "fundamentacao": "Gestante Rh negativo necessita avaliaÃ§Ã£o do fator Rh do parceiro quando disponÃ­vel, Coombs indireto e acompanhamento para prevenÃ§Ã£o de aloimunizaÃ§Ã£o. Quando indicado, deve receber imunoglobulina anti-D conforme protocolo, especialmente em situaÃ§Ãµes de risco e no puerpÃ©rio se recÃ©m-nascido Rh positivo.",
        "transcultural": {
            "preservacao": ["Respeitar dÃºvidas da gestante e famÃ­lia sobre exames de sangue."],
            "acomodacao": ["Orientar a importÃ¢ncia do cartÃ£o da gestante e registro da tipagem sanguÃ­nea."],
            "repadronizacao": ["Corrigir a ideia de que Rh negativo Ã© doenÃ§a, explicando o risco apenas em situaÃ§Ãµes especÃ­ficas."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "OMS.", "Leininger."]
    }
]# modulos/regras_clinicas/prenatal/sinais_sintomas.py

REGRAS = [
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "NÃ¡useas",
        "diagnostico": {"codigo": "10012453", "termo": "NÃ¡usea"},
        "resultado": {"codigo": "10028992", "termo": "NÃ¡usea, Ausente"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre NutriÃ§Ã£o"},
        "prioridade": "Baixa",
        "fundamentacao": "NÃ¡useas sÃ£o frequentes no primeiro trimestre, geralmente relacionadas a alteraÃ§Ãµes hormonais. A avaliaÃ§Ã£o deve identificar intensidade, hidrataÃ§Ã£o, perda ponderal e impacto funcional, orientando fracionamento alimentar, hidrataÃ§Ã£o e sinais de alerta.",
        "transcultural": {
            "preservacao": ["Valorizar prÃ¡ticas alimentares culturais seguras que aliviem nÃ¡useas."],
            "acomodacao": ["Adaptar horÃ¡rios e tipos de alimentos Ã  rotina e tolerÃ¢ncia da gestante."],
            "repadronizacao": ["Reorientar uso de chÃ¡s, ervas ou medicamentos sem avaliaÃ§Ã£o profissional."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde. PrÃ©-natal de baixo risco.", "OMS. RecomendaÃ§Ãµes sobre cuidados prÃ©-natais.", "FEBRASGO. AssistÃªncia prÃ©-natal.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger. Teoria Transcultural."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "VÃ´mitos",
        "diagnostico": {"codigo": "10020864", "termo": "VÃ´mito"},
        "resultado": {"codigo": "10029134", "termo": "VÃ´mito, Ausente"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre NutriÃ§Ã£o"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "VÃ´mitos persistentes podem causar desidrataÃ§Ã£o, perda de peso e distÃºrbios hidroeletrolÃ­ticos. No prÃ©-natal, deve-se avaliar frequÃªncia, aceitaÃ§Ã£o oral, diurese, sinais de desidrataÃ§Ã£o e necessidade de encaminhamento.",
        "transcultural": {
            "preservacao": ["Reconhecer alimentos culturalmente aceitos que melhorem a tolerÃ¢ncia oral."],
            "acomodacao": ["Orientar pequenas refeiÃ§Ãµes, lÃ­quidos em pequenos volumes e repouso apÃ³s alimentaÃ§Ã£o."],
            "repadronizacao": ["Desencorajar automedicaÃ§Ã£o antiemÃ©tica e prÃ¡ticas inseguras."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "HiperÃªmese gravÃ­dica",
        "diagnostico": {"codigo": "10020864", "termo": "VÃ´mito"},
        "resultado": {"codigo": "10027617", "termo": "EquilÃ­brio HÃ­drico, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "HiperÃªmese gravÃ­dica caracteriza-se por vÃ´mitos intensos, perda de peso, desidrataÃ§Ã£o, cetonÃºria e risco de desequilÃ­brio metabÃ³lico. Requer avaliaÃ§Ã£o imediata, hidrataÃ§Ã£o, suporte clÃ­nico e possÃ­vel encaminhamento hospitalar.",
        "transcultural": {
            "preservacao": ["Acolher explicaÃ§Ãµes culturais da gestante sobre o mal-estar."],
            "acomodacao": ["Explicar sinais de gravidade de forma simples para gestante e famÃ­lia."],
            "repadronizacao": ["ReforÃ§ar que vÃ´mitos intensos nÃ£o devem ser tratados apenas com medidas caseiras."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Azia",
        "diagnostico": {"codigo": "10013950", "termo": "Dor"},
        "resultado": {"codigo": "10029008", "termo": "Dor, Ausente"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre NutriÃ§Ã£o"},
        "prioridade": "Baixa",
        "fundamentacao": "Azia Ã© comum na gestaÃ§Ã£o por relaxamento do esfÃ­ncter esofÃ¡gico e compressÃ£o uterina. Deve-se orientar refeiÃ§Ãµes menores, evitar deitar apÃ³s comer e observar sinais de alarme, como dor intensa ou vÃ´mitos persistentes.",
        "transcultural": {
            "preservacao": ["Manter alimentos tradicionais que nÃ£o piorem sintomas."],
            "acomodacao": ["Ajustar orientaÃ§Ã£o alimentar Ã  rotina familiar."],
            "repadronizacao": ["Evitar automedicaÃ§Ã£o com antiÃ¡cidos ou bicarbonato sem orientaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Pirose",
        "diagnostico": {"codigo": "10013950", "termo": "Dor"},
        "resultado": {"codigo": "10029008", "termo": "Dor, Ausente"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre NutriÃ§Ã£o"},
        "prioridade": "Baixa",
        "fundamentacao": "Pirose gestacional geralmente decorre de refluxo gastroesofÃ¡gico. A enfermagem deve orientar medidas posturais, fracionamento alimentar, reduÃ§Ã£o de alimentos irritantes e avaliaÃ§Ã£o se sintomas forem intensos ou persistentes.",
        "transcultural": {
            "preservacao": ["Preservar preparaÃ§Ãµes alimentares locais bem toleradas."],
            "acomodacao": ["Negociar substituiÃ§Ãµes alimentares possÃ­veis."],
            "repadronizacao": ["Desestimular condutas caseiras de risco ou uso indiscriminado de medicamentos."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "ConstipaÃ§Ã£o",
        "diagnostico": {"codigo": "10004999", "termo": "ConstipaÃ§Ã£o"},
        "resultado": {"codigo": "10027800", "termo": "EliminaÃ§Ã£o Intestinal, Eficaz"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre NutriÃ§Ã£o"},
        "prioridade": "Baixa",
        "fundamentacao": "ConstipaÃ§Ã£o Ã© frequente na gestaÃ§Ã£o por alteraÃ§Ãµes hormonais, reduÃ§Ã£o da motilidade intestinal e suplementaÃ§Ã£o de ferro. Orienta-se aumento de fibras, ingestÃ£o hÃ­drica, atividade fÃ­sica se nÃ£o contraindicada e evitar laxantes sem prescriÃ§Ã£o.",
        "transcultural": {
            "preservacao": ["Valorizar alimentos regionais ricos em fibras."],
            "acomodacao": ["Adequar consumo de Ã¡gua e fibras Ã  disponibilidade local."],
            "repadronizacao": ["Evitar uso rotineiro de laxantes, chÃ¡s purgativos ou automedicaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Diarreia",
        "diagnostico": {"codigo": "10005933", "termo": "Diarreia"},
        "resultado": {"codigo": "10027800", "termo": "EliminaÃ§Ã£o Intestinal, Eficaz"},
        "intervencao": {"codigo": "10036112", "termo": "Orientar sobre HidrataÃ§Ã£o"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "Diarreia pode causar desidrataÃ§Ã£o e indicar infecÃ§Ã£o gastrointestinal. A enfermagem deve avaliar duraÃ§Ã£o, febre, sangue nas fezes, sinais de desidrataÃ§Ã£o, orientar hidrataÃ§Ã£o e encaminhar quando houver sinais de gravidade.",
        "transcultural": {
            "preservacao": ["Reconhecer alimentos tradicionais leves e seguros."],
            "acomodacao": ["Orientar preparo seguro de Ã¡gua e alimentos."],
            "repadronizacao": ["Desestimular uso de antidiarreicos ou antibiÃ³ticos sem prescriÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Dor lombar",
        "diagnostico": {"codigo": "10013950", "termo": "Dor"},
        "resultado": {"codigo": "10029008", "termo": "Dor, Ausente"},
        "intervencao": {"codigo": "10039276", "termo": "Ensinar ExercÃ­cio"},
        "prioridade": "Baixa",
        "fundamentacao": "Dor lombar Ã© comum por alteraÃ§Ãµes posturais, ganho ponderal e frouxidÃ£o ligamentar. Deve-se orientar postura, alongamentos seguros, repouso relativo, uso de calÃ§ados adequados e investigar sinais urinÃ¡rios ou neurolÃ³gicos.",
        "transcultural": {
            "preservacao": ["Valorizar prÃ¡ticas corporais seguras e aceitas pela gestante."],
            "acomodacao": ["Adaptar exercÃ­cios Ã  rotina, trabalho e territÃ³rio."],
            "repadronizacao": ["Evitar massagens agressivas, automedicaÃ§Ã£o e esforÃ§os excessivos."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Dor pÃ©lvica",
        "diagnostico": {"codigo": "10013950", "termo": "Dor"},
        "resultado": {"codigo": "10029008", "termo": "Dor, Ausente"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "Dor pÃ©lvica pode estar associada a alteraÃ§Ãµes musculoesquelÃ©ticas, crescimento uterino, infecÃ§Ã£o, contraÃ§Ãµes ou sinais obstÃ©tricos. Deve-se avaliar intensidade, sangramento, perda de lÃ­quido, febre e contraÃ§Ãµes.",
        "transcultural": {
            "preservacao": ["Acolher formas locais de descrever dor e desconforto."],
            "acomodacao": ["Orientar repouso, postura e sinais de alerta em linguagem acessÃ­vel."],
            "repadronizacao": ["ReforÃ§ar busca imediata se houver sangramento, febre, perda de lÃ­quido ou contraÃ§Ãµes regulares."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Dor abdominal",
        "diagnostico": {"codigo": "10013950", "termo": "Dor"},
        "resultado": {"codigo": "10029008", "termo": "Dor, Ausente"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Dor abdominal na gestaÃ§Ã£o pode indicar condiÃ§Ãµes benignas ou urgÃªncias obstÃ©tricas, como ameaÃ§a de abortamento, trabalho de parto prematuro, descolamento placentÃ¡rio, infecÃ§Ã£o ou abdome agudo. Deve-se avaliar sinais associados e encaminhar se dor intensa, persistente ou acompanhada de sangramento, febre ou contraÃ§Ãµes.",
        "transcultural": {
            "preservacao": ["Acolher interpretaÃ§Ãµes culturais da dor."],
            "acomodacao": ["Explicar sinais de risco para gestante e famÃ­lia."],
            "repadronizacao": ["Desencorajar atraso na busca de atendimento por uso exclusivo de remÃ©dios caseiros."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Cefaleia",
        "diagnostico": {"codigo": "10013950", "termo": "Dor"},
        "resultado": {"codigo": "10029008", "termo": "Dor, Ausente"},
        "intervencao": {"codigo": "10044148", "termo": "Orientar sobre MediÃ§Ã£o de PressÃ£o Arterial"},
        "prioridade": "Alta",
        "fundamentacao": "Cefaleia na gestaÃ§Ã£o exige avaliaÃ§Ã£o da pressÃ£o arterial e sinais de prÃ©-eclÃ¢mpsia, especialmente se intensa, persistente, associada a escotomas, dor epigÃ¡strica, edema ou proteinÃºria. A enfermagem deve classificar risco e encaminhar quando necessÃ¡rio.",
        "transcultural": {
            "preservacao": ["Acolher medidas culturais seguras de conforto."],
            "acomodacao": ["Orientar sinais de alerta com linguagem clara."],
            "repadronizacao": ["Evitar automedicaÃ§Ã£o e atraso na avaliaÃ§Ã£o pressÃ³rica."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Tontura",
        "diagnostico": {"codigo": "10006160", "termo": "Tontura"},
        "resultado": {"codigo": "10028992", "termo": "Sintoma, Ausente"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "Tontura pode estar relacionada a hipotensÃ£o postural, hipoglicemia, anemia, desidrataÃ§Ã£o ou alteraÃ§Ãµes clÃ­nicas. Deve-se avaliar sinais vitais, alimentaÃ§Ã£o, hidrataÃ§Ã£o, hemoglobina e ocorrÃªncia de quedas ou sÃ­ncope.",
        "transcultural": {
            "preservacao": ["Valorizar relatos da gestante sobre fatores desencadeantes."],
            "acomodacao": ["Orientar levantar lentamente, alimentar-se regularmente e hidratar-se."],
            "repadronizacao": ["ReforÃ§ar procura de atendimento se houver desmaio, palpitaÃ§Ã£o, sangramento ou dor intensa."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "LipotÃ­mia",
        "diagnostico": {"codigo": "10006160", "termo": "Tontura"},
        "resultado": {"codigo": "10027617", "termo": "EquilÃ­brio HÃ­drico, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "LipotÃ­mia ou quase desmaio pode decorrer de hipotensÃ£o, hipoglicemia, anemia, arritmia, desidrataÃ§Ã£o ou sangramento. Exige avaliaÃ§Ã£o de sinais vitais, glicemia quando disponÃ­vel, hidrataÃ§Ã£o e encaminhamento se recorrente ou associada a sinais de risco.",
        "transcultural": {
            "preservacao": ["Acolher explicaÃ§Ãµes familiares sobre o episÃ³dio."],
            "acomodacao": ["Orientar medidas imediatas de seguranÃ§a para prevenir quedas."],
            "repadronizacao": ["Evitar normalizar desmaios recorrentes na gestaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Dispneia",
        "diagnostico": {"codigo": "10006461", "termo": "Dispneia"},
        "resultado": {"codigo": "10029208", "termo": "RespiraÃ§Ã£o, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Dispneia leve pode ocorrer por alteraÃ§Ãµes fisiolÃ³gicas da gestaÃ§Ã£o, mas dispneia intensa, sÃºbita, associada a dor torÃ¡cica, cianose, febre, taquicardia ou saturaÃ§Ã£o baixa exige avaliaÃ§Ã£o urgente.",
        "transcultural": {
            "preservacao": ["Acolher percepÃ§Ãµes culturais sobre falta de ar."],
            "acomodacao": ["Orientar repouso, posiÃ§Ã£o confortÃ¡vel e sinais de alerta."],
            "repadronizacao": ["ReforÃ§ar que falta de ar importante nÃ£o deve ser atribuÃ­da apenas Ã  gravidez."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Edema fisiolÃ³gico",
        "diagnostico": {"codigo": "10041951", "termo": "Edema"},
        "resultado": {"codigo": "10029019", "termo": "Edema, Reduzido"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "Baixa",
        "fundamentacao": "Edema leve em membros inferiores pode ser fisiolÃ³gico no final da gestaÃ§Ã£o. Deve-se avaliar pressÃ£o arterial, proteinÃºria e sinais de alarme. Orienta-se repouso com elevaÃ§Ã£o de pernas, hidrataÃ§Ã£o e evitar longos perÃ­odos em pÃ©.",
        "transcultural": {
            "preservacao": ["Valorizar prÃ¡ticas seguras de repouso e cuidado corporal."],
            "acomodacao": ["Adequar orientaÃ§Ãµes Ã  rotina laboral e domÃ©stica."],
            "repadronizacao": ["Evitar uso de diurÃ©ticos, chÃ¡s ou restriÃ§Ã£o hÃ­drica sem prescriÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Edema patolÃ³gico",
        "diagnostico": {"codigo": "10041951", "termo": "Edema"},
        "resultado": {"codigo": "10029019", "termo": "Edema, Reduzido"},
        "intervencao": {"codigo": "10044148", "termo": "Orientar sobre MediÃ§Ã£o de PressÃ£o Arterial"},
        "prioridade": "Alta",
        "fundamentacao": "Edema sÃºbito, generalizado ou associado a hipertensÃ£o, cefaleia, alteraÃ§Ãµes visuais, dor epigÃ¡strica ou proteinÃºria pode indicar prÃ©-eclÃ¢mpsia. Requer avaliaÃ§Ã£o imediata e encaminhamento conforme protocolo.",
        "transcultural": {
            "preservacao": ["Acolher o relato da gestante sobre mudanÃ§as corporais."],
            "acomodacao": ["Explicar sinais de gravidade para gestante e famÃ­lia."],
            "repadronizacao": ["ReforÃ§ar que edema no rosto e mÃ£os, quando associado a sintomas, exige atendimento imediato."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "CÃ¢imbras",
        "diagnostico": {"codigo": "10040943", "termo": "CÃ£ibra Muscular"},
        "resultado": {"codigo": "10028337", "termo": "Conforto, Melhorado"},
        "intervencao": {"codigo": "10039276", "termo": "Ensinar ExercÃ­cio"},
        "prioridade": "Baixa",
        "fundamentacao": "CÃ¢imbras sÃ£o comuns na gestaÃ§Ã£o, especialmente em membros inferiores. Orienta-se alongamento suave, hidrataÃ§Ã£o, atividade fÃ­sica segura e avaliaÃ§Ã£o se houver dor unilateral, edema importante ou suspeita vascular.",
        "transcultural": {
            "preservacao": ["Manter prÃ¡ticas corporais seguras jÃ¡ utilizadas pela gestante."],
            "acomodacao": ["Adaptar alongamentos Ã  capacidade fÃ­sica e idade gestacional."],
            "repadronizacao": ["Desencorajar uso de medicamentos ou suplementos sem avaliaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Fadiga",
        "diagnostico": {"codigo": "10000695", "termo": "Fadiga"},
        "resultado": {"codigo": "10000707", "termo": "Fadiga, Reduzida"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "Baixa",
        "fundamentacao": "Fadiga pode ser fisiolÃ³gica, mas tambÃ©m se relaciona a anemia, sono inadequado, sobrecarga de trabalho, sofrimento emocional ou doenÃ§a clÃ­nica. A enfermagem deve avaliar intensidade, rotina, exames e sinais associados.",
        "transcultural": {
            "preservacao": ["Reconhecer papÃ©is familiares e atividades culturais da gestante."],
            "acomodacao": ["Negociar pausas, divisÃ£o de tarefas e repouso possÃ­vel."],
            "repadronizacao": ["Evitar naturalizar fadiga incapacitante sem investigaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "InsÃ´nia",
        "diagnostico": {"codigo": "10010330", "termo": "InsÃ´nia"},
        "resultado": {"codigo": "10041399", "termo": "Sono, Melhorado"},
        "intervencao": {"codigo": "10024662", "termo": "Orientar sobre Sono"},
        "prioridade": "Baixa",
        "fundamentacao": "InsÃ´nia pode ocorrer por desconfortos fÃ­sicos, ansiedade, noctÃºria e alteraÃ§Ãµes hormonais. Deve-se orientar higiene do sono, posiÃ§Ã£o confortÃ¡vel, rotina relaxante e avaliar sofrimento psÃ­quico.",
        "transcultural": {
            "preservacao": ["Valorizar rituais culturais seguros de relaxamento."],
            "acomodacao": ["Adaptar medidas de sono Ã  rotina familiar e ambiente domiciliar."],
            "repadronizacao": ["Evitar uso de sedativos, Ã¡lcool ou fitoterÃ¡picos sem prescriÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "SonolÃªncia",
        "diagnostico": {"codigo": "10041396", "termo": "Sono, Prejudicado"},
        "resultado": {"codigo": "10041399", "termo": "Sono, Melhorado"},
        "intervencao": {"codigo": "10024662", "termo": "Orientar sobre Sono"},
        "prioridade": "Baixa",
        "fundamentacao": "SonolÃªncia pode ser fisiolÃ³gica no inÃ­cio da gestaÃ§Ã£o, mas deve ser avaliada quando excessiva, associada a anemia, depressÃ£o, privaÃ§Ã£o de sono, uso de medicamentos ou prejuÃ­zo funcional.",
        "transcultural": {
            "preservacao": ["Respeitar hÃ¡bitos familiares de descanso quando seguros."],
            "acomodacao": ["Orientar pausas programadas e rotina regular de sono."],
            "repadronizacao": ["Investigar sonolÃªncia incapacitante em vez de atribuÃ­-la apenas Ã  gestaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Corrimento vaginal",
        "diagnostico": {"codigo": "10023032", "termo": "InfecÃ§Ã£o"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre InfecÃ§Ã£o"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "Corrimento vaginal pode ser fisiolÃ³gico quando claro e sem odor, mas corrimento com odor, prurido, dor, ardor ou alteraÃ§Ã£o de cor sugere infecÃ§Ã£o vaginal ou IST. Deve-se avaliar sintomas associados e encaminhar para diagnÃ³stico e tratamento.",
        "transcultural": {
            "preservacao": ["Acolher crenÃ§as sobre higiene Ã­ntima sem julgamento."],
            "acomodacao": ["Orientar higiene adequada e uso de roupas confortÃ¡veis."],
            "repadronizacao": ["Desencorajar duchas vaginais, automedicaÃ§Ã£o e uso de produtos irritantes."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Prurido vaginal",
        "diagnostico": {"codigo": "10023032", "termo": "InfecÃ§Ã£o"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre InfecÃ§Ã£o"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "Prurido vaginal pode indicar candidÃ­ase, vaginose, IST ou irritaÃ§Ã£o local. A gestante deve ser avaliada para tratamento adequado, evitando automedicaÃ§Ã£o e prevenindo complicaÃ§Ãµes.",
        "transcultural": {
            "preservacao": ["Acolher pudor e formas culturais de relatar sintomas Ã­ntimos."],
            "acomodacao": ["Garantir privacidade e linguagem respeitosa."],
            "repadronizacao": ["Evitar uso de pomadas, duchas ou receitas caseiras sem avaliaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Sangramento vaginal",
        "diagnostico": {"codigo": "10003303", "termo": "Sangramento"},
        "resultado": {"codigo": "10028120", "termo": "Sangramento, Ausente"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Sangramento vaginal na gestaÃ§Ã£o Ã© sinal de alerta e pode estar associado a abortamento, gravidez ectÃ³pica, placenta prÃ©via, descolamento placentÃ¡rio ou trabalho de parto. Exige avaliaÃ§Ã£o imediata, independentemente do volume.",
        "transcultural": {
            "preservacao": ["Acolher a gestante e reduzir medo e culpa."],
            "acomodacao": ["Orientar familiares sobre urgÃªncia do atendimento."],
            "repadronizacao": ["ReforÃ§ar que sangramento nÃ£o deve ser observado em casa sem avaliaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Perda de lÃ­quido",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10028120", "termo": "Risco, Reduzido"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Perda de lÃ­quido vaginal pode indicar ruptura de membranas, com risco de infecÃ§Ã£o, prematuridade e sofrimento fetal. Deve-se encaminhar imediatamente para avaliaÃ§Ã£o obstÃ©trica, evitando toque vaginal desnecessÃ¡rio.",
        "transcultural": {
            "preservacao": ["Acolher a descriÃ§Ã£o da gestante sobre o lÃ­quido e circunstÃ¢ncias."],
            "acomodacao": ["Explicar que perda contÃ­nua, mesmo sem dor, exige avaliaÃ§Ã£o."],
            "repadronizacao": ["Evitar espera domiciliar ou uso de absorventes internos."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "ReduÃ§Ã£o dos movimentos fetais",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "ReduÃ§Ã£o ou ausÃªncia de movimentos fetais apÃ³s a percepÃ§Ã£o habitual Ã© sinal de alerta e pode indicar comprometimento fetal. A gestante deve ser orientada a procurar avaliaÃ§Ã£o imediata para ausculta fetal e conduta obstÃ©trica.",
        "transcultural": {
            "preservacao": ["Valorizar a percepÃ§Ã£o materna sobre o padrÃ£o de movimentos do bebÃª."],
            "acomodacao": ["Orientar registro e observaÃ§Ã£o dos movimentos fetais conforme idade gestacional."],
            "repadronizacao": ["Desestimular esperar muitos dias para procurar atendimento quando houver reduÃ§Ã£o importante."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Febre",
        "diagnostico": {"codigo": "10007916", "termo": "Febre"},
        "resultado": {"codigo": "10033694", "termo": "Temperatura Corporal, nos Limites Normais"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Febre na gestaÃ§Ã£o pode indicar infecÃ§Ã£o urinÃ¡ria, respiratÃ³ria, gastrointestinal, arbovirose, infecÃ§Ã£o intra-amniÃ³tica ou outras condiÃ§Ãµes de risco. Requer avaliaÃ§Ã£o clÃ­nica, hidrataÃ§Ã£o, investigaÃ§Ã£o etiolÃ³gica e encaminhamento conforme gravidade.",
        "transcultural": {
            "preservacao": ["Acolher prÃ¡ticas culturais seguras de conforto tÃ©rmico."],
            "acomodacao": ["Orientar hidrataÃ§Ã£o e monitoramento da temperatura."],
            "repadronizacao": ["Evitar uso de medicamentos, chÃ¡s ou banhos extremos sem orientaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "DisÃºria",
        "diagnostico": {"codigo": "10029915", "termo": "InfecÃ§Ã£o do Trato UrinÃ¡rio"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre InfecÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "DisÃºria sugere infecÃ§Ã£o urinÃ¡ria, condiÃ§Ã£o frequente na gestaÃ§Ã£o e associada a pielonefrite, parto prematuro e baixo peso ao nascer. Deve-se solicitar/avaliar exames conforme protocolo, orientar hidrataÃ§Ã£o e tratamento prescrito.",
        "transcultural": {
            "preservacao": ["Acolher prÃ¡ticas seguras de cuidado Ã­ntimo."],
            "acomodacao": ["Orientar ingestÃ£o hÃ­drica e adesÃ£o ao tratamento."],
            "repadronizacao": ["Desestimular automedicaÃ§Ã£o e interrupÃ§Ã£o precoce de antibiÃ³tico."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "PolaciÃºria",
        "diagnostico": {"codigo": "10001359", "termo": "FunÃ§Ã£o do Sistema UrinÃ¡rio, Prejudicada"},
        "resultado": {"codigo": "10028615", "termo": "FunÃ§Ã£o do Sistema UrinÃ¡rio, Eficaz"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "PolaciÃºria pode ser fisiolÃ³gica pela compressÃ£o uterina, mas quando associada a disÃºria, urgÃªncia, febre ou dor lombar sugere infecÃ§Ã£o urinÃ¡ria. A enfermagem deve diferenciar sintomas fisiolÃ³gicos de sinais de infecÃ§Ã£o.",
        "transcultural": {
            "preservacao": ["Acolher relatos sobre hÃ¡bitos urinÃ¡rios."],
            "acomodacao": ["Orientar sinais de alerta e hidrataÃ§Ã£o adequada."],
            "repadronizacao": ["Evitar reduzir ingestÃ£o hÃ­drica de forma inadequada por medo de urinar."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "UrgÃªncia urinÃ¡ria",
        "diagnostico": {"codigo": "10001359", "termo": "FunÃ§Ã£o do Sistema UrinÃ¡rio, Prejudicada"},
        "resultado": {"codigo": "10028615", "termo": "FunÃ§Ã£o do Sistema UrinÃ¡rio, Eficaz"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre InfecÃ§Ã£o"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "UrgÃªncia urinÃ¡ria pode ocorrer por alteraÃ§Ãµes mecÃ¢nicas da gestaÃ§Ã£o ou infecÃ§Ã£o urinÃ¡ria. Deve-se investigar disÃºria, febre, dor lombar, hematÃºria e orientar coleta de exames e tratamento conforme protocolo.",
        "transcultural": {
            "preservacao": ["Respeitar formas de expressÃ£o de sintomas urinÃ¡rios."],
            "acomodacao": ["Garantir privacidade para abordagem do sintoma."],
            "repadronizacao": ["ReforÃ§ar que urgÃªncia com dor ou febre precisa de avaliaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "IncontinÃªncia urinÃ¡ria",
        "diagnostico": {"codigo": "10025686", "termo": "IncontinÃªncia UrinÃ¡ria"},
        "resultado": {"codigo": "10028615", "termo": "FunÃ§Ã£o do Sistema UrinÃ¡rio, Eficaz"},
        "intervencao": {"codigo": "10039276", "termo": "Ensinar ExercÃ­cio"},
        "prioridade": "Baixa",
        "fundamentacao": "IncontinÃªncia urinÃ¡ria pode ocorrer por sobrecarga do assoalho pÃ©lvico durante a gestaÃ§Ã£o. A enfermagem deve orientar exercÃ­cios pÃ©lvicos quando indicados, higiene, prevenÃ§Ã£o de irritaÃ§Ãµes e avaliaÃ§Ã£o de infecÃ§Ã£o associada.",
        "transcultural": {
            "preservacao": ["Acolher o sintoma sem constrangimento."],
            "acomodacao": ["Orientar exercÃ­cios de forma respeitosa e adequada Ã  compreensÃ£o da gestante."],
            "repadronizacao": ["Reduzir vergonha e estimular relato do sintoma nas consultas."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Hemorroidas",
        "diagnostico": {"codigo": "10009118", "termo": "Hemorroida"},
        "resultado": {"codigo": "10029008", "termo": "Dor, Ausente"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre NutriÃ§Ã£o"},
        "prioridade": "Baixa",
        "fundamentacao": "Hemorroidas sÃ£o favorecidas por constipaÃ§Ã£o, aumento da pressÃ£o venosa e esforÃ§o evacuatÃ³rio. Orienta-se dieta rica em fibras, hidrataÃ§Ã£o, evitar esforÃ§o, higiene local e avaliaÃ§Ã£o se sangramento intenso ou dor persistente.",
        "transcultural": {
            "preservacao": ["Respeitar pudor e formas culturais de relatar sintomas anorretais."],
            "acomodacao": ["Orientar medidas alimentares possÃ­veis no territÃ³rio."],
            "repadronizacao": ["Evitar pomadas, supositÃ³rios ou chÃ¡s sem orientaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Varizes",
        "diagnostico": {"codigo": "10020882", "termo": "Veia Varicosa"},
        "resultado": {"codigo": "10028379", "termo": "Processo do Sistema CirculatÃ³rio, Positivo"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "Baixa",
        "fundamentacao": "Varizes podem surgir ou piorar na gestaÃ§Ã£o por alteraÃ§Ãµes hormonais, compressÃ£o venosa e aumento do volume circulante. Orienta-se evitar longos perÃ­odos em pÃ©, elevar membros, atividade fÃ­sica segura e observar sinais de trombose.",
        "transcultural": {
            "preservacao": ["Valorizar prÃ¡ticas seguras de repouso e cuidado com pernas."],
            "acomodacao": ["Adaptar orientaÃ§Ãµes Ã s atividades domÃ©sticas e laborais."],
            "repadronizacao": ["Orientar busca imediata se dor unilateral, calor, vermelhidÃ£o ou edema assimÃ©trico."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Prurido cutÃ¢neo",
        "diagnostico": {"codigo": "10010934", "termo": "Prurido"},
        "resultado": {"codigo": "10028337", "termo": "Conforto, Melhorado"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "Prurido cutÃ¢neo pode estar relacionado ao estiramento da pele, alergias, dermatoses gestacionais ou colestase intra-hepÃ¡tica, especialmente quando intenso em palmas e plantas ou associado a icterÃ­cia. Deve-se avaliar sinais de gravidade e encaminhar quando indicado.",
        "transcultural": {
            "preservacao": ["Acolher prÃ¡ticas seguras de hidrataÃ§Ã£o da pele."],
            "acomodacao": ["Orientar produtos suaves e evitar irritantes."],
            "repadronizacao": ["Evitar uso de plantas, pomadas ou medicamentos sem avaliaÃ§Ã£o, principalmente em prurido intenso."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "AlteraÃ§Ãµes mamÃ¡rias",
        "diagnostico": {"codigo": "10003595", "termo": "Processo MamÃ¡rio, Prejudicado"},
        "resultado": {"codigo": "10033682", "termo": "Processo MamÃ¡rio, Eficaz"},
        "intervencao": {"codigo": "10033017", "termo": "Orientar sobre AmamentaÃ§Ã£o"},
        "prioridade": "Baixa",
        "fundamentacao": "AlteraÃ§Ãµes mamÃ¡rias como aumento de volume, sensibilidade, escurecimento areolar e colostro podem ser fisiolÃ³gicas. A consulta deve orientar preparo para amamentaÃ§Ã£o, sinais de alerta e evitar prÃ¡ticas prejudiciais Ã s mamas.",
        "transcultural": {
            "preservacao": ["Valorizar experiÃªncias familiares positivas de amamentaÃ§Ã£o."],
            "acomodacao": ["Adequar orientaÃ§Ãµes Ã s crenÃ§as e experiÃªncias da gestante."],
            "repadronizacao": ["Desencorajar preparo agressivo dos mamilos ou uso de produtos irritantes."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Mastalgia",
        "diagnostico": {"codigo": "10013950", "termo": "Dor"},
        "resultado": {"codigo": "10029008", "termo": "Dor, Ausente"},
        "intervencao": {"codigo": "10033017", "termo": "Orientar sobre AmamentaÃ§Ã£o"},
        "prioridade": "Baixa",
        "fundamentacao": "Mastalgia Ã© comum por alteraÃ§Ãµes hormonais e crescimento mamÃ¡rio. Deve-se orientar sutiÃ£ adequado, medidas de conforto e avaliaÃ§Ã£o se houver febre, vermelhidÃ£o, nÃ³dulo, secreÃ§Ã£o purulenta ou dor intensa.",
        "transcultural": {
            "preservacao": ["Acolher pudor e crenÃ§as sobre exposiÃ§Ã£o das mamas."],
            "acomodacao": ["Garantir privacidade na avaliaÃ§Ã£o e orientaÃ§Ã£o."],
            "repadronizacao": ["Estimular procura de atendimento diante de sinais inflamatÃ³rios."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "ContraÃ§Ãµes uterinas",
        "diagnostico": {"codigo": "10006364", "termo": "ContraÃ§Ã£o Uterina"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "ContraÃ§Ãµes uterinas devem ser avaliadas quanto Ã  frequÃªncia, intensidade, dor, idade gestacional, perda de lÃ­quido, sangramento e alteraÃ§Ã£o dos movimentos fetais. ContraÃ§Ãµes regulares antes de 37 semanas sugerem risco de trabalho de parto prematuro.",
        "transcultural": {
            "preservacao": ["Acolher a forma como a gestante diferencia dor, cÃ³lica e contraÃ§Ã£o."],
            "acomodacao": ["Orientar observaÃ§Ã£o da frequÃªncia e duraÃ§Ã£o das contraÃ§Ãµes."],
            "repadronizacao": ["ReforÃ§ar que contraÃ§Ãµes regulares antes do termo exigem atendimento imediato."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Sinais e sintomas",
        "achado_clinico": "Sinais de trabalho de parto prematuro",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Sinais de trabalho de parto prematuro incluem contraÃ§Ãµes regulares antes de 37 semanas, dor lombar persistente, pressÃ£o pÃ©lvica, cÃ³licas, sangramento, alteraÃ§Ã£o do corrimento ou perda de lÃ­quido. A condiÃ§Ã£o exige encaminhamento imediato para avaliaÃ§Ã£o obstÃ©trica e prevenÃ§Ã£o de complicaÃ§Ãµes neonatais.",
        "transcultural": {
            "preservacao": ["Valorizar a percepÃ§Ã£o da gestante sobre mudanÃ§as no corpo."],
            "acomodacao": ["Orientar plano de deslocamento rÃ¡pido, considerando territÃ³rio e rede de apoio."],
            "repadronizacao": ["Evitar aguardar em casa quando houver sinais de prematuridade."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "OMS.", "FEBRASGO.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    }
]# modulos/regras_clinicas/prenatal/intercorrencias.py

REGRAS = [
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "PrÃ©-eclÃ¢mpsia",
        "diagnostico": {"codigo": "10032017", "termo": "PressÃ£o Arterial, Alterada"},
        "resultado": {"codigo": "10027647", "termo": "PressÃ£o Arterial, nos Limites Normais"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "A prÃ©-eclÃ¢mpsia Ã© sÃ­ndrome hipertensiva multissistÃªmica apÃ³s 20 semanas de gestaÃ§Ã£o, associada a proteinÃºria ou sinais de disfunÃ§Ã£o orgÃ¢nica, com risco materno-fetal elevado.",
        "transcultural": {
            "preservacao": ["Acolher a compreensÃ£o cultural da gestante sobre pressÃ£o alta e gravidez."],
            "acomodacao": ["Explicar sinais de alerta em linguagem simples, incluindo cefaleia, escotomas, dor epigÃ¡strica e edema sÃºbito."],
            "repadronizacao": ["ReforÃ§ar que sintomas graves nÃ£o devem ser tratados apenas com chÃ¡s, repouso ou medidas caseiras."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde. Manual de GestaÃ§Ã£o de Alto Risco.", "FEBRASGO. SÃ­ndromes hipertensivas na gestaÃ§Ã£o.", "OMS. RecomendaÃ§Ãµes de cuidado prÃ©-natal.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger. Teoria Transcultural."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "EclÃ¢mpsia",
        "diagnostico": {"codigo": "10032017", "termo": "PressÃ£o Arterial, Alterada"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "EclÃ¢mpsia corresponde Ã  ocorrÃªncia de convulsÃµes em gestante com sÃ­ndrome hipertensiva, configurando emergÃªncia obstÃ©trica com risco de morte materna e fetal.",
        "transcultural": {
            "preservacao": ["Acolher crenÃ§as familiares sobre convulsÃµes sem julgamento."],
            "acomodacao": ["Orientar a famÃ­lia sobre necessidade de atendimento de urgÃªncia imediato."],
            "repadronizacao": ["Desencorajar prÃ¡ticas que atrasem o encaminhamento, como contenÃ§Ã£o inadequada ou terapias caseiras."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "SÃ­ndrome HELLP",
        "diagnostico": {"codigo": "10012606", "termo": "Processo do Sistema CirculatÃ³rio, Prejudicado"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "A sÃ­ndrome HELLP Ã© complicaÃ§Ã£o grave da prÃ©-eclÃ¢mpsia, caracterizada por hemÃ³lise, elevaÃ§Ã£o de enzimas hepÃ¡ticas e plaquetopenia, exigindo atendimento obstÃ©trico urgente.",
        "transcultural": {
            "preservacao": ["Acolher sintomas referidos pela gestante, como dor epigÃ¡strica e mal-estar."],
            "acomodacao": ["Orientar que dor forte no estÃ´mago, nÃ¡useas intensas ou sangramentos podem indicar gravidade."],
            "repadronizacao": ["Evitar banalizaÃ§Ã£o de dor epigÃ¡strica como azia comum da gravidez."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "HipertensÃ£o gestacional grave",
        "diagnostico": {"codigo": "10032017", "termo": "PressÃ£o Arterial, Alterada"},
        "resultado": {"codigo": "10027647", "termo": "PressÃ£o Arterial, nos Limites Normais"},
        "intervencao": {"codigo": "10044148", "termo": "Orientar sobre MediÃ§Ã£o de PressÃ£o Arterial"},
        "prioridade": "Alta",
        "fundamentacao": "HipertensÃ£o gestacional grave aumenta risco de prÃ©-eclÃ¢mpsia, eclÃ¢mpsia, AVC, descolamento placentÃ¡rio, restriÃ§Ã£o de crescimento fetal e prematuridade.",
        "transcultural": {
            "preservacao": ["Valorizar cuidados familiares de proteÃ§Ã£o Ã  gestante."],
            "acomodacao": ["Orientar aferiÃ§Ã£o regular da pressÃ£o arterial e retorno imediato em sinais de alerta."],
            "repadronizacao": ["Desestimular abandono do tratamento anti-hipertensivo por medo de prejudicar o bebÃª."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "Crise hipertensiva",
        "diagnostico": {"codigo": "10032017", "termo": "PressÃ£o Arterial, Alterada"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Crise hipertensiva na gestaÃ§Ã£o Ã© emergÃªncia clÃ­nica e obstÃ©trica, especialmente quando associada a sintomas neurolÃ³gicos, dor epigÃ¡strica, dispneia ou alteraÃ§Ãµes fetais.",
        "transcultural": {
            "preservacao": ["Acolher preocupaÃ§Ãµes da famÃ­lia sobre internaÃ§Ã£o e medicaÃ§Ã£o."],
            "acomodacao": ["Explicar risco de complicaÃ§Ãµes maternas e fetais de forma objetiva."],
            "repadronizacao": ["ReforÃ§ar que pressÃ£o muito elevada exige atendimento imediato."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "ITU",
        "diagnostico": {"codigo": "10029915", "termo": "InfecÃ§Ã£o do Trato UrinÃ¡rio"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre InfecÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "InfecÃ§Ã£o do trato urinÃ¡rio na gestaÃ§Ã£o aumenta risco de pielonefrite, trabalho de parto prematuro e baixo peso ao nascer, exigindo tratamento adequado e controle.",
        "transcultural": {
            "preservacao": ["Reconhecer prÃ¡ticas seguras de higiene Ã­ntima jÃ¡ utilizadas."],
            "acomodacao": ["Orientar hidrataÃ§Ã£o, coleta adequada de urina e adesÃ£o ao antibiÃ³tico prescrito."],
            "repadronizacao": ["Evitar automedicaÃ§Ã£o e interrupÃ§Ã£o do tratamento apÃ³s melhora dos sintomas."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "Pielonefrite",
        "diagnostico": {"codigo": "10029915", "termo": "InfecÃ§Ã£o do Trato UrinÃ¡rio"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Pielonefrite na gestaÃ§Ã£o Ã© infecÃ§Ã£o urinÃ¡ria alta, geralmente com febre, dor lombar e comprometimento sistÃªmico, podendo causar sepse, prematuridade e complicaÃ§Ãµes maternas.",
        "transcultural": {
            "preservacao": ["Acolher relatos de dor lombar e febre conforme linguagem local."],
            "acomodacao": ["Orientar urgÃªncia de atendimento, mesmo que a gestante jÃ¡ use medidas caseiras."],
            "repadronizacao": ["ReforÃ§ar que febre com dor lombar na gestaÃ§Ã£o nÃ£o deve ser tratada apenas em casa."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "BacteriÃºria assintomÃ¡tica",
        "diagnostico": {"codigo": "10051950", "termo": "Risco de InfecÃ§Ã£o UrinÃ¡ria"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10038112", "termo": "Orientar sobre PrevenÃ§Ã£o de InfecÃ§Ã£o Cruzada"},
        "prioridade": "Alta",
        "fundamentacao": "BacteriÃºria assintomÃ¡tica na gestaÃ§Ã£o deve ser tratada conforme protocolo, pois pode evoluir para pielonefrite e aumentar risco de complicaÃ§Ãµes obstÃ©tricas.",
        "transcultural": {
            "preservacao": ["Acolher a percepÃ§Ã£o de ausÃªncia de doenÃ§a por nÃ£o haver sintomas."],
            "acomodacao": ["Explicar que infecÃ§Ã£o pode existir mesmo sem dor ou ardÃªncia."],
            "repadronizacao": ["ReforÃ§ar necessidade de tratamento completo e controle laboratorial."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "CandidÃ­ase",
        "diagnostico": {"codigo": "10023032", "termo": "InfecÃ§Ã£o"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre InfecÃ§Ã£o"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "CandidÃ­ase vulvovaginal Ã© frequente na gestaÃ§Ã£o e pode causar corrimento, prurido e desconforto, exigindo diagnÃ³stico clÃ­nico e tratamento seguro para gestantes.",
        "transcultural": {
            "preservacao": ["Acolher pudor e crenÃ§as sobre sintomas Ã­ntimos."],
            "acomodacao": ["Garantir privacidade e orientar higiene Ã­ntima adequada."],
            "repadronizacao": ["Desencorajar duchas vaginais, pomadas sem prescriÃ§Ã£o e receitas caseiras intravaginais."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "Vaginose bacteriana",
        "diagnostico": {"codigo": "10023032", "termo": "InfecÃ§Ã£o"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre InfecÃ§Ã£o"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "Vaginose bacteriana pode cursar com corrimento e odor vaginal, sendo associada a maior risco de complicaÃ§Ãµes obstÃ©tricas quando sintomÃ¡tica.",
        "transcultural": {
            "preservacao": ["Respeitar formas culturais de cuidado Ã­ntimo que nÃ£o causem dano."],
            "acomodacao": ["Orientar tratamento prescrito e evitar produtos irritantes."],
            "repadronizacao": ["Reorientar a crenÃ§a de que odor vaginal deve ser tratado com duchas ou substÃ¢ncias caseiras."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "TricomonÃ­ase",
        "diagnostico": {"codigo": "10023032", "termo": "InfecÃ§Ã£o"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre InfecÃ§Ã£o"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "TricomonÃ­ase Ã© infecÃ§Ã£o sexualmente transmissÃ­vel que pode causar corrimento, prurido e desconforto, exigindo tratamento da gestante e avaliaÃ§Ã£o da parceria sexual.",
        "transcultural": {
            "preservacao": ["Acolher a gestante sem julgamento moral."],
            "acomodacao": ["Orientar prevenÃ§Ã£o de reinfecÃ§Ã£o e necessidade de abordagem da parceria."],
            "repadronizacao": ["Reduzir estigma e reforÃ§ar tratamento adequado como proteÃ§Ã£o materno-fetal."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde. PCDT IST.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "Sangramento vaginal no primeiro trimestre",
        "diagnostico": {"codigo": "10003303", "termo": "Sangramento"},
        "resultado": {"codigo": "10028120", "termo": "Sangramento, Ausente"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Sangramento no primeiro trimestre pode estar associado a ameaÃ§a de abortamento, abortamento em curso, gravidez ectÃ³pica ou doenÃ§a trofoblÃ¡stica, necessitando avaliaÃ§Ã£o imediata.",
        "transcultural": {
            "preservacao": ["Acolher medos e crenÃ§as familiares sobre perda gestacional."],
            "acomodacao": ["Orientar sinais de gravidade e necessidade de avaliaÃ§Ã£o mesmo com pequeno volume."],
            "repadronizacao": ["Evitar culpabilizaÃ§Ã£o da gestante e atraso na busca por cuidado."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "Sangramento vaginal no segundo trimestre",
        "diagnostico": {"codigo": "10003303", "termo": "Sangramento"},
        "resultado": {"codigo": "10028120", "termo": "Sangramento, Ausente"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Sangramento no segundo trimestre pode indicar condiÃ§Ãµes obstÃ©tricas relevantes, como alteraÃ§Ãµes placentÃ¡rias, abortamento tardio, insuficiÃªncia cervical ou trabalho de parto prematuro.",
        "transcultural": {
            "preservacao": ["Acolher a descriÃ§Ã£o da gestante sobre cor, volume e dor."],
            "acomodacao": ["Explicar que todo sangramento na gestaÃ§Ã£o exige avaliaÃ§Ã£o."],
            "repadronizacao": ["Evitar observaÃ§Ã£o domiciliar prolongada sem avaliaÃ§Ã£o profissional."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "Sangramento vaginal no terceiro trimestre",
        "diagnostico": {"codigo": "10003303", "termo": "Sangramento"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Sangramento no terceiro trimestre pode estar associado a placenta prÃ©via, descolamento prematuro de placenta ou inÃ­cio de trabalho de parto, exigindo avaliaÃ§Ã£o obstÃ©trica urgente.",
        "transcultural": {
            "preservacao": ["Acolher prÃ¡ticas familiares de apoio durante urgÃªncias."],
            "acomodacao": ["Orientar deslocamento imediato e evitar toque vaginal fora de ambiente adequado."],
            "repadronizacao": ["ReforÃ§ar que sangramento no fim da gestaÃ§Ã£o pode ser emergÃªncia."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "AmeaÃ§a de abortamento",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "AmeaÃ§a de abortamento Ã© caracterizada por sangramento vaginal no inÃ­cio da gestaÃ§Ã£o com colo geralmente fechado, exigindo avaliaÃ§Ã£o clÃ­nica e ultrassonogrÃ¡fica quando indicada.",
        "transcultural": {
            "preservacao": ["Acolher sofrimento emocional e crenÃ§as sobre perda gestacional."],
            "acomodacao": ["Orientar repouso relativo conforme avaliaÃ§Ã£o e retorno se piora."],
            "repadronizacao": ["Evitar culpa, automedicaÃ§Ã£o e prÃ¡ticas invasivas caseiras."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "Abortamento",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10028379", "termo": "Processo do Sistema CirculatÃ³rio, Positivo"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Abortamento pode apresentar sangramento, dor abdominal, eliminaÃ§Ã£o de tecidos e risco de hemorragia, infecÃ§Ã£o e sofrimento psÃ­quico, requerendo assistÃªncia imediata e humanizada.",
        "transcultural": {
            "preservacao": ["Respeitar luto, crenÃ§as espirituais e rituais familiares seguros."],
            "acomodacao": ["Oferecer acolhimento, privacidade e orientaÃ§Ã£o sobre sinais de gravidade."],
            "repadronizacao": ["Combater julgamento, culpa e abandono do cuidado pÃ³s-evento."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "Placenta prÃ©via",
        "diagnostico": {"codigo": "10003303", "termo": "Sangramento"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Placenta prÃ©via pode causar sangramento vaginal indolor no segundo ou terceiro trimestre e estÃ¡ associada a risco hemorrÃ¡gico materno-fetal, exigindo acompanhamento especializado.",
        "transcultural": {
            "preservacao": ["Acolher medo da gestante diante do sangramento."],
            "acomodacao": ["Orientar repouso, sinais de alerta e comparecimento imediato se sangrar."],
            "repadronizacao": ["Evitar toque vaginal e prÃ¡ticas caseiras diante de sangramento."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "Descolamento prematuro de placenta",
        "diagnostico": {"codigo": "10003303", "termo": "Sangramento"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Descolamento prematuro de placenta Ã© emergÃªncia obstÃ©trica, podendo causar dor abdominal intensa, hipertonia uterina, sangramento e sofrimento fetal.",
        "transcultural": {
            "preservacao": ["Acolher a percepÃ§Ã£o materna de dor intensa ou mudanÃ§a sÃºbita."],
            "acomodacao": ["Orientar que dor forte com sangramento ou mal-estar exige urgÃªncia."],
            "repadronizacao": ["Evitar espera domiciliar por melhora espontÃ¢nea."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "Rotura prematura de membranas",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Rotura prematura de membranas aumenta risco de infecÃ§Ã£o, prematuridade e sofrimento fetal, exigindo avaliaÃ§Ã£o obstÃ©trica imediata e conduta conforme idade gestacional.",
        "transcultural": {
            "preservacao": ["Valorizar o relato da gestante sobre perda de lÃ­quido."],
            "acomodacao": ["Orientar observar cor, odor e quantidade, sem retardar atendimento."],
            "repadronizacao": ["Evitar banho de imersÃ£o, relaÃ§Ã£o sexual ou toque vaginal apÃ³s perda de lÃ­quido."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "Trabalho de parto prematuro",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Trabalho de parto antes de 37 semanas estÃ¡ associado a morbimortalidade neonatal, exigindo reconhecimento precoce de contraÃ§Ãµes regulares, dor lombar, pressÃ£o pÃ©lvica, sangramento ou perda de lÃ­quido.",
        "transcultural": {
            "preservacao": ["Valorizar a percepÃ§Ã£o da gestante sobre sinais corporais."],
            "acomodacao": ["Construir plano de deslocamento rÃ¡pido, considerando territÃ³rio e transporte."],
            "repadronizacao": ["ReforÃ§ar que contraÃ§Ãµes antes do termo nÃ£o devem ser aguardadas em casa."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "ContraÃ§Ãµes uterinas prematuras",
        "diagnostico": {"codigo": "10006364", "termo": "ContraÃ§Ã£o Uterina"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "ContraÃ§Ãµes uterinas prematuras podem indicar ameaÃ§a de trabalho de parto prematuro, especialmente quando regulares, dolorosas ou associadas a perda de lÃ­quido e sangramento.",
        "transcultural": {
            "preservacao": ["Acolher a forma como a gestante descreve cÃ³licas e endurecimento uterino."],
            "acomodacao": ["Orientar registro de frequÃªncia e duraÃ§Ã£o das contraÃ§Ãµes."],
            "repadronizacao": ["Evitar normalizar contraÃ§Ãµes regulares antes de 37 semanas."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "RestriÃ§Ã£o de crescimento fetal",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "RestriÃ§Ã£o de crescimento fetal indica risco de insuficiÃªncia placentÃ¡ria, hipÃ³xia, morbidade neonatal e Ã³bito fetal, exigindo investigaÃ§Ã£o, vigilÃ¢ncia fetal e acompanhamento especializado.",
        "transcultural": {
            "preservacao": ["Valorizar prÃ¡ticas familiares de cuidado nutricional e repouso seguro."],
            "acomodacao": ["Orientar importÃ¢ncia do acompanhamento e dos exames seriados."],
            "repadronizacao": ["Evitar atribuir baixo crescimento fetal apenas a caracterÃ­stica familiar sem avaliaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "OligodrÃ¢mnio",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "OligodrÃ¢mnio pode estar relacionado a rotura de membranas, insuficiÃªncia placentÃ¡ria, restriÃ§Ã£o de crescimento fetal ou malformaÃ§Ãµes, exigindo avaliaÃ§Ã£o obstÃ©trica e vigilÃ¢ncia fetal.",
        "transcultural": {
            "preservacao": ["Acolher preocupaÃ§Ãµes familiares sobre o lÃ­quido amniÃ³tico."],
            "acomodacao": ["Orientar sinais de alerta, como perda de lÃ­quido e reduÃ§Ã£o dos movimentos fetais."],
            "repadronizacao": ["Evitar interpretaÃ§Ã£o de que hidrataÃ§Ã£o isolada resolve todos os casos sem avaliaÃ§Ã£o mÃ©dica."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "PolidrÃ¢mnio",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "PolidrÃ¢mnio pode estar associado a diabetes gestacional, alteraÃ§Ãµes fetais, infecÃ§Ãµes ou outras condiÃ§Ãµes, aumentando risco de parto prematuro e complicaÃ§Ãµes obstÃ©tricas.",
        "transcultural": {
            "preservacao": ["Acolher explicaÃ§Ãµes culturais sobre aumento exagerado da barriga."],
            "acomodacao": ["Orientar necessidade de investigaÃ§Ã£o e controle glicÃªmico quando indicado."],
            "repadronizacao": ["Evitar normalizar crescimento uterino excessivo sem avaliaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "Sofrimento fetal suspeito",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Sofrimento fetal suspeito pode ser indicado por alteraÃ§Ã£o de batimentos cardÃ­acos fetais, reduÃ§Ã£o de movimentos fetais ou condiÃ§Ãµes maternas graves, exigindo avaliaÃ§Ã£o obstÃ©trica imediata.",
        "transcultural": {
            "preservacao": ["Valorizar a percepÃ§Ã£o materna sobre o comportamento fetal."],
            "acomodacao": ["Orientar sinais que exigem procura imediata do serviÃ§o."],
            "repadronizacao": ["Evitar aguardar retorno programado quando hÃ¡ suspeita de alteraÃ§Ã£o fetal."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "ReduÃ§Ã£o dos movimentos fetais",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "ReduÃ§Ã£o dos movimentos fetais pode indicar comprometimento fetal e deve ser valorizada, especialmente apÃ³s a gestante reconhecer o padrÃ£o habitual de movimentaÃ§Ã£o.",
        "transcultural": {
            "preservacao": ["Valorizar o conhecimento materno sobre o padrÃ£o do bebÃª."],
            "acomodacao": ["Orientar busca imediata se houver reduÃ§Ã£o importante ou ausÃªncia de movimentos."],
            "repadronizacao": ["Desestimular esperar dias para avaliaÃ§Ã£o por acreditar que o bebÃª estÃ¡ apenas dormindo."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "HiperÃªmese gravÃ­dica",
        "diagnostico": {"codigo": "10020864", "termo": "VÃ´mito"},
        "resultado": {"codigo": "10027617", "termo": "EquilÃ­brio HÃ­drico, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "HiperÃªmese gravÃ­dica envolve vÃ´mitos intensos, perda ponderal, desidrataÃ§Ã£o e possÃ­vel distÃºrbio eletrolÃ­tico, podendo exigir hidrataÃ§Ã£o venosa e suporte clÃ­nico.",
        "transcultural": {
            "preservacao": ["Acolher prÃ¡ticas alimentares seguras que melhorem nÃ¡useas."],
            "acomodacao": ["Orientar sinais de desidrataÃ§Ã£o e necessidade de atendimento."],
            "repadronizacao": ["Evitar automedicaÃ§Ã£o e uso de ervas sem seguranÃ§a na gestaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "DesidrataÃ§Ã£o",
        "diagnostico": {"codigo": "10041895", "termo": "DesidrataÃ§Ã£o"},
        "resultado": {"codigo": "10027617", "termo": "EquilÃ­brio HÃ­drico, Eficaz"},
        "intervencao": {"codigo": "10036112", "termo": "Orientar sobre HidrataÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "DesidrataÃ§Ã£o na gestaÃ§Ã£o pode decorrer de vÃ´mitos, diarreia, febre ou baixa ingestÃ£o hÃ­drica, aumentando risco de hipotensÃ£o, contraÃ§Ãµes e comprometimento materno-fetal.",
        "transcultural": {
            "preservacao": ["Valorizar bebidas e alimentos locais seguros que favoreÃ§am hidrataÃ§Ã£o."],
            "acomodacao": ["Orientar ingestÃ£o hÃ­drica fracionada conforme tolerÃ¢ncia."],
            "repadronizacao": ["Evitar restriÃ§Ã£o hÃ­drica por medo de urinar com frequÃªncia."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "Anemia grave",
        "diagnostico": {"codigo": "10012606", "termo": "Processo do Sistema CirculatÃ³rio, Prejudicado"},
        "resultado": {"codigo": "10028379", "termo": "Processo do Sistema CirculatÃ³rio, Positivo"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre NutriÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "Anemia grave na gestaÃ§Ã£o aumenta risco de fadiga intensa, infecÃ§Ã£o, parto prematuro, baixo peso ao nascer, hemorragia e desfechos materno-fetais adversos.",
        "transcultural": {
            "preservacao": ["Estimular alimentos regionais ricos em ferro e culturalmente aceitos."],
            "acomodacao": ["Adequar suplementaÃ§Ã£o e alimentaÃ§Ã£o Ã  rotina e tolerÃ¢ncia da gestante."],
            "repadronizacao": ["Orientar evitar cafÃ© ou chÃ¡ junto das refeiÃ§Ãµes e nÃ£o suspender ferro sem avaliaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "Diabetes gestacional descompensado",
        "diagnostico": {"codigo": "10005876", "termo": "Diabetes"},
        "resultado": {"codigo": "10027532", "termo": "Processo do Sistema RegulatÃ³rio, Eficaz"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "Alta",
        "fundamentacao": "Diabetes gestacional descompensado aumenta risco de macrossomia, prÃ©-eclÃ¢mpsia, parto traumÃ¡tico, hipoglicemia neonatal e complicaÃ§Ãµes metabÃ³licas.",
        "transcultural": {
            "preservacao": ["Preservar alimentos culturais compatÃ­veis com controle glicÃªmico."],
            "acomodacao": ["Adaptar plano alimentar Ã  renda, acesso e rotina familiar."],
            "repadronizacao": ["Reduzir consumo de aÃ§Ãºcar, bebidas adoÃ§adas e ultraprocessados."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "Febre na gestaÃ§Ã£o",
        "diagnostico": {"codigo": "10007916", "termo": "Febre"},
        "resultado": {"codigo": "10033694", "termo": "Temperatura Corporal, nos Limites Normais"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Febre na gestaÃ§Ã£o pode indicar infecÃ§Ã£o urinÃ¡ria, respiratÃ³ria, intra-amniÃ³tica, arbovirose ou outras condiÃ§Ãµes com risco materno-fetal, exigindo investigaÃ§Ã£o.",
        "transcultural": {
            "preservacao": ["Acolher prÃ¡ticas seguras de conforto tÃ©rmico."],
            "acomodacao": ["Orientar hidrataÃ§Ã£o, monitoramento e sinais de gravidade."],
            "repadronizacao": ["Evitar automedicaÃ§Ã£o e uso de chÃ¡s sem seguranÃ§a gestacional."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "Dengue na gestaÃ§Ã£o",
        "diagnostico": {"codigo": "10023032", "termo": "InfecÃ§Ã£o"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Dengue na gestaÃ§Ã£o aumenta risco de desidrataÃ§Ã£o, sangramentos, plaquetopenia, parto prematuro e complicaÃ§Ãµes maternas, exigindo acompanhamento clÃ­nico rigoroso.",
        "transcultural": {
            "preservacao": ["Valorizar medidas comunitÃ¡rias de eliminaÃ§Ã£o de criadouros."],
            "acomodacao": ["Orientar hidrataÃ§Ã£o, sinais de alarme e proteÃ§Ã£o contra mosquitos."],
            "repadronizacao": ["Evitar anti-inflamatÃ³rios e automedicaÃ§Ã£o, especialmente diante de suspeita de dengue."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde. Arboviroses na gestaÃ§Ã£o.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "Zika na gestaÃ§Ã£o",
        "diagnostico": {"codigo": "10023032", "termo": "InfecÃ§Ã£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "InfecÃ§Ã£o por Zika na gestaÃ§Ã£o estÃ¡ associada a risco de sÃ­ndrome congÃªnita, alteraÃ§Ãµes neurolÃ³gicas fetais e necessidade de vigilÃ¢ncia ultrassonogrÃ¡fica e acompanhamento especializado.",
        "transcultural": {
            "preservacao": ["Valorizar estratÃ©gias comunitÃ¡rias de prevenÃ§Ã£o ao mosquito."],
            "acomodacao": ["Orientar uso de repelente seguro, barreiras fÃ­sicas e acompanhamento fetal."],
            "repadronizacao": ["Evitar minimizar exantema, febre baixa ou conjuntivite em Ã¡rea de transmissÃ£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde. Zika e gestaÃ§Ã£o.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "Chikungunya na gestaÃ§Ã£o",
        "diagnostico": {"codigo": "10023032", "termo": "InfecÃ§Ã£o"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Chikungunya na gestaÃ§Ã£o pode causar febre, artralgia intensa e risco de transmissÃ£o perinatal quando ocorre prÃ³ximo ao parto, exigindo vigilÃ¢ncia clÃ­nica e obstÃ©trica.",
        "transcultural": {
            "preservacao": ["Valorizar medidas locais de proteÃ§Ã£o contra mosquitos."],
            "acomodacao": ["Orientar repouso, hidrataÃ§Ã£o e sinais de gravidade."],
            "repadronizacao": ["Evitar automedicaÃ§Ã£o com anti-inflamatÃ³rios sem avaliaÃ§Ã£o profissional."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde. Arboviroses.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "IntercorrÃªncias obstÃ©tricas",
        "achado_clinico": "COVID-19 na gestaÃ§Ã£o",
        "diagnostico": {"codigo": "10023032", "termo": "InfecÃ§Ã£o"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "COVID-19 na gestaÃ§Ã£o pode aumentar risco de complicaÃ§Ãµes respiratÃ³rias, internaÃ§Ã£o, prematuridade e agravamento em gestantes com comorbidades, exigindo avaliaÃ§Ã£o de gravidade, isolamento orientado e acompanhamento.",
        "transcultural": {
            "preservacao": ["Acolher crenÃ§as familiares sobre infecÃ§Ãµes respiratÃ³rias sem julgamento."],
            "acomodacao": ["Orientar sinais de alerta respiratÃ³rio, vacinaÃ§Ã£o e medidas preventivas."],
            "repadronizacao": ["Combater desinformaÃ§Ã£o sobre COVID-19, vacinaÃ§Ã£o e seguranÃ§a materno-fetal."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde. COVID-19 e gestaÃ§Ã£o.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    }
]# modulos/regras_clinicas/prenatal/medicacoes.py

REGRAS = [
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Ãcido fÃ³lico nÃ£o iniciado",
        "diagnostico": {"codigo": "10024625", "termo": "Regime TerapÃªutico, Prejudicado"},
        "resultado": {"codigo": "10030185", "termo": "AdesÃ£o ao Regime TerapÃªutico"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre MedicaÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "O Ã¡cido fÃ³lico Ã© recomendado no perÃ­odo periconcepcional e no inÃ­cio da gestaÃ§Ã£o para reduzir o risco de defeitos do tubo neural. Quando nÃ£o iniciado, a enfermagem deve orientar inÃ­cio conforme protocolo, verificar acesso ao suplemento, registrar conduta e reforÃ§ar adesÃ£o.",
        "transcultural": {
            "preservacao": ["Valorizar prÃ¡ticas alimentares seguras e alimentos regionais ricos em folato."],
            "acomodacao": ["Adequar a orientaÃ§Ã£o ao acesso da gestante Ã  farmÃ¡cia da unidade e Ã  rotina diÃ¡ria."],
            "repadronizacao": ["Reorientar a ideia de que suplemento sÃ³ Ã© necessÃ¡rio quando hÃ¡ sintomas."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde. AtenÃ§Ã£o ao prÃ©-natal de baixo risco.", "FEBRASGO. AssistÃªncia prÃ©-natal.", "OMS. RecomendaÃ§Ãµes sobre cuidado prÃ©-natal.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger. Teoria Transcultural."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Ãcido fÃ³lico iniciado tardiamente",
        "diagnostico": {"codigo": "10024625", "termo": "Regime TerapÃªutico, Prejudicado"},
        "resultado": {"codigo": "10030185", "termo": "AdesÃ£o ao Regime TerapÃªutico"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre MedicaÃ§Ã£o"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "O inÃ­cio tardio do Ã¡cido fÃ³lico reduz o benefÃ­cio mÃ¡ximo esperado na prevenÃ§Ã£o de defeitos do tubo neural, especialmente quando iniciado apÃ³s o perÃ­odo de fechamento do tubo neural. Ainda assim, deve-se orientar continuidade conforme protocolo e reforÃ§ar suplementaÃ§Ã£o adequada.",
        "transcultural": {
            "preservacao": ["Acolher a histÃ³ria da gestante sem culpabilizaÃ§Ã£o."],
            "acomodacao": ["Explicar a finalidade do suplemento em linguagem simples."],
            "repadronizacao": ["Estimular inÃ­cio precoce em futuras gestaÃ§Ãµes e planejamento reprodutivo."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Baixa adesÃ£o ao Ã¡cido fÃ³lico",
        "diagnostico": {"codigo": "10022155", "termo": "AdesÃ£o ao Regime TerapÃªutico, Prejudicada"},
        "resultado": {"codigo": "10030185", "termo": "AdesÃ£o ao Regime TerapÃªutico"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "A baixa adesÃ£o ao Ã¡cido fÃ³lico compromete a efetividade da suplementaÃ§Ã£o. A equipe deve investigar esquecimento, efeitos adversos, acesso, compreensÃ£o da prescriÃ§Ã£o e crenÃ§as sobre medicamentos na gestaÃ§Ã£o.",
        "transcultural": {
            "preservacao": ["Respeitar valores da gestante sobre uso de medicamentos."],
            "acomodacao": ["Pactuar horÃ¡rio de uso associado a rotina jÃ¡ existente."],
            "repadronizacao": ["Reformular crenÃ§as de que vitaminas fazem mal ao bebÃª."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Sulfato ferroso nÃ£o iniciado",
        "diagnostico": {"codigo": "10023009", "termo": "IngestÃ£o Nutricional, Prejudicada"},
        "resultado": {"codigo": "10037572", "termo": "IngestÃ£o Nutricional, nos Limites Normais"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre MedicaÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "A suplementaÃ§Ã£o de ferro no prÃ©-natal Ã© recomendada para prevenÃ§Ã£o e tratamento da anemia ferropriva, condiÃ§Ã£o associada a fadiga, infecÃ§Ã£o, prematuridade e baixo peso ao nascer. Deve-se orientar inÃ­cio conforme protocolo e avaliar hemoglobina, ferritina e tolerÃ¢ncia.",
        "transcultural": {
            "preservacao": ["Valorizar alimentos locais ricos em ferro."],
            "acomodacao": ["Adequar horÃ¡rio de uso para reduzir desconfortos gastrointestinais."],
            "repadronizacao": ["Orientar evitar cafÃ©, chÃ¡ preto ou leite junto ao ferro, pois podem reduzir absorÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Baixa adesÃ£o ao sulfato ferroso",
        "diagnostico": {"codigo": "10022155", "termo": "AdesÃ£o ao Regime TerapÃªutico, Prejudicada"},
        "resultado": {"codigo": "10030185", "termo": "AdesÃ£o ao Regime TerapÃªutico"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "Alta",
        "fundamentacao": "A baixa adesÃ£o ao sulfato ferroso mantÃ©m risco de anemia gestacional e suas complicaÃ§Ãµes. A enfermagem deve investigar eventos adversos, esquecimento, acesso ao medicamento e orientar estratÃ©gias para melhorar a tolerÃ¢ncia e continuidade.",
        "transcultural": {
            "preservacao": ["Acolher relatos sobre intolerÃ¢ncia e experiÃªncias anteriores."],
            "acomodacao": ["Negociar horÃ¡rio de uso e estratÃ©gias alimentares possÃ­veis."],
            "repadronizacao": ["ReforÃ§ar que escurecimento das fezes Ã© esperado e nÃ£o deve motivar suspensÃ£o isolada."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "NÃ¡useas associadas ao sulfato ferroso",
        "diagnostico": {"codigo": "10012453", "termo": "NÃ¡usea"},
        "resultado": {"codigo": "10028992", "termo": "NÃ¡usea, Ausente"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre MedicaÃ§Ã£o"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "NÃ¡useas podem ocorrer com uso de sulfato ferroso e reduzir adesÃ£o. Deve-se orientar forma correta de uso, avaliar possibilidade de tomada apÃ³s alimento leve quando necessÃ¡rio, verificar gravidade e encaminhar para ajuste terapÃªutico se intolerÃ¢ncia persistente.",
        "transcultural": {
            "preservacao": ["Valorizar alimentos culturalmente aceitos que reduzam enjoo."],
            "acomodacao": ["Ajustar horÃ¡rio de uso conforme maior tolerÃ¢ncia da gestante."],
            "repadronizacao": ["Evitar suspensÃ£o sem comunicaÃ§Ã£o Ã  equipe de saÃºde."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "ConstipaÃ§Ã£o associada ao sulfato ferroso",
        "diagnostico": {"codigo": "10004999", "termo": "ConstipaÃ§Ã£o"},
        "resultado": {"codigo": "10027800", "termo": "EliminaÃ§Ã£o Intestinal, Eficaz"},
        "intervencao": {"codigo": "10024618", "termo": "Orientar sobre NutriÃ§Ã£o"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "O sulfato ferroso pode agravar constipaÃ§Ã£o, sintoma jÃ¡ comum na gestaÃ§Ã£o. A enfermagem deve orientar ingestÃ£o hÃ­drica, fibras, atividade fÃ­sica segura e comunicar a equipe caso o efeito adverso comprometa a adesÃ£o.",
        "transcultural": {
            "preservacao": ["Estimular alimentos regionais ricos em fibras."],
            "acomodacao": ["Adequar hidrataÃ§Ã£o Ã  realidade de acesso Ã  Ã¡gua segura."],
            "repadronizacao": ["Evitar laxantes, chÃ¡s purgativos ou automedicaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "CÃ¡lcio indicado",
        "diagnostico": {"codigo": "10023009", "termo": "IngestÃ£o Nutricional, Prejudicada"},
        "resultado": {"codigo": "10037572", "termo": "IngestÃ£o Nutricional, nos Limites Normais"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre MedicaÃ§Ã£o"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "A suplementaÃ§Ã£o de cÃ¡lcio pode ser indicada em gestantes com baixa ingestÃ£o dietÃ©tica ou maior risco de prÃ©-eclÃ¢mpsia, conforme avaliaÃ§Ã£o clÃ­nica e protocolo. Deve-se orientar uso correto, intervalo em relaÃ§Ã£o ao ferro e acompanhamento.",
        "transcultural": {
            "preservacao": ["Valorizar fontes alimentares culturais de cÃ¡lcio."],
            "acomodacao": ["Adequar suplementaÃ§Ã£o ao horÃ¡rio possÃ­vel e Ã  rotina alimentar."],
            "repadronizacao": ["Orientar nÃ£o tomar cÃ¡lcio junto ao ferro para nÃ£o prejudicar absorÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Baixa adesÃ£o ao cÃ¡lcio",
        "diagnostico": {"codigo": "10022155", "termo": "AdesÃ£o ao Regime TerapÃªutico, Prejudicada"},
        "resultado": {"codigo": "10030185", "termo": "AdesÃ£o ao Regime TerapÃªutico"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "A baixa adesÃ£o ao cÃ¡lcio reduz o potencial benefÃ­cio preventivo em gestantes com indicaÃ§Ã£o. A enfermagem deve identificar esquecimento, efeitos gastrointestinais, dificuldade de acesso e orientar horÃ¡rios separados do sulfato ferroso.",
        "transcultural": {
            "preservacao": ["Considerar hÃ¡bitos alimentares e crenÃ§as sobre leite e derivados."],
            "acomodacao": ["Pactuar horÃ¡rios simples para evitar esquecimento."],
            "repadronizacao": ["ReforÃ§ar finalidade preventiva da suplementaÃ§Ã£o quando indicada."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Uso inadequado de medicamentos na gestaÃ§Ã£o",
        "diagnostico": {"codigo": "10022155", "termo": "AdesÃ£o ao Regime TerapÃªutico, Prejudicada"},
        "resultado": {"codigo": "10030185", "termo": "AdesÃ£o ao Regime TerapÃªutico"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre MedicaÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "O uso inadequado de medicamentos na gestaÃ§Ã£o pode expor mÃ£e e feto a riscos evitÃ¡veis, incluindo toxicidade, efeitos teratogÃªnicos, interaÃ§Ãµes e falha terapÃªutica. Deve-se revisar todos os medicamentos em uso e encaminhar para avaliaÃ§Ã£o quando houver risco.",
        "transcultural": {
            "preservacao": ["Acolher prÃ¡ticas familiares de cuidado sem julgamento."],
            "acomodacao": ["Solicitar que a gestante leve medicamentos, receitas e produtos usados Ã s consultas."],
            "repadronizacao": ["ReforÃ§ar que todo medicamento na gestaÃ§Ã£o deve ser avaliado por profissional de saÃºde."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "AutomedicaÃ§Ã£o",
        "diagnostico": {"codigo": "10025806", "termo": "Comportamento de SaÃºde, Prejudicado"},
        "resultado": {"codigo": "10028276", "termo": "Comportamento de SaÃºde, Positivo"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre MedicaÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "A automedicaÃ§Ã£o na gestaÃ§Ã£o pode causar eventos adversos maternos e fetais, mascarar sinais de gravidade e retardar diagnÃ³stico. A enfermagem deve investigar substÃ¢ncias utilizadas, orientar riscos e fortalecer acesso Ã  avaliaÃ§Ã£o profissional.",
        "transcultural": {
            "preservacao": ["Reconhecer o papel da famÃ­lia na tomada de decisÃ£o sobre cuidados."],
            "acomodacao": ["Orientar alternativas seguras de procura do serviÃ§o de saÃºde."],
            "repadronizacao": ["Modificar a prÃ¡tica de usar medicamentos por indicaÃ§Ã£o de terceiros."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Uso de anti-inflamatÃ³rio sem orientaÃ§Ã£o",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10028120", "termo": "Risco, Reduzido"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre MedicaÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "Anti-inflamatÃ³rios nÃ£o esteroidais podem apresentar riscos na gestaÃ§Ã£o, especialmente em fases especÃ­ficas, incluindo alteraÃ§Ãµes fetais, renais, ducto arterioso e complicaÃ§Ãµes maternas. O uso sem orientaÃ§Ã£o deve ser interrompido e avaliado por profissional habilitado.",
        "transcultural": {
            "preservacao": ["Acolher a motivaÃ§Ã£o da gestante para alÃ­vio da dor."],
            "acomodacao": ["Orientar busca de alternativas seguras prescritas pela equipe."],
            "repadronizacao": ["Evitar uso de anti-inflamatÃ³rios por conta prÃ³pria durante a gestaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Uso de fitoterÃ¡pico sem avaliaÃ§Ã£o",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10028120", "termo": "Risco, Reduzido"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre MedicaÃ§Ã£o"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "FitoterÃ¡picos podem conter substÃ¢ncias com efeitos uterotÃ´nicos, hepatotÃ³xicos, nefrotÃ³xicos, anticoagulantes ou interaÃ§Ãµes medicamentosas. Na gestaÃ§Ã£o, seu uso deve ser avaliado quanto Ã  seguranÃ§a, dose, procedÃªncia e indicaÃ§Ã£o.",
        "transcultural": {
            "preservacao": ["Respeitar o uso tradicional de plantas como parte da cultura familiar."],
            "acomodacao": ["Dialogar sobre quais produtos sÃ£o usados, finalidade e frequÃªncia."],
            "repadronizacao": ["Substituir prÃ¡ticas de risco por alternativas seguras pactuadas com a equipe."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Uso de plantas medicinais com risco gestacional",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10028120", "termo": "Risco, Reduzido"},
        "intervencao": {"codigo": "10019502", "termo": "Orientar sobre SeguranÃ§a"},
        "prioridade": "Alta",
        "fundamentacao": "Algumas plantas medicinais podem provocar contraÃ§Ãµes uterinas, sangramento, toxicidade, alteraÃ§Ãµes hepÃ¡ticas ou interaÃ§Ã£o com medicamentos. A enfermagem deve identificar uso, orientar riscos e comunicar a equipe para avaliaÃ§Ã£o segura.",
        "transcultural": {
            "preservacao": ["Valorizar saberes tradicionais que nÃ£o coloquem a gestaÃ§Ã£o em risco."],
            "acomodacao": ["Negociar suspensÃ£o ou substituiÃ§Ã£o de plantas potencialmente perigosas."],
            "repadronizacao": ["Reorientar a crenÃ§a de que todo produto natural Ã© seguro na gravidez."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Anti-hipertensivo prescrito",
        "diagnostico": {"codigo": "10009394", "termo": "HipertensÃ£o"},
        "resultado": {"codigo": "10027647", "termo": "PressÃ£o Arterial, nos Limites Normais"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre MedicaÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "O uso de anti-hipertensivo na gestaÃ§Ã£o pode ser necessÃ¡rio para controle pressÃ³rico e prevenÃ§Ã£o de complicaÃ§Ãµes como prÃ©-eclÃ¢mpsia grave, AVC, restriÃ§Ã£o de crescimento fetal e desfechos maternos adversos. A enfermagem deve orientar uso correto, monitoramento da pressÃ£o e sinais de alerta.",
        "transcultural": {
            "preservacao": ["Acolher prÃ¡ticas seguras de autocuidado e apoio familiar."],
            "acomodacao": ["Pactuar horÃ¡rios de uso conforme rotina da gestante."],
            "repadronizacao": ["ReforÃ§ar que pressÃ£o controlada nÃ£o significa suspender medicamento sem orientaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Baixa adesÃ£o ao anti-hipertensivo",
        "diagnostico": {"codigo": "10022155", "termo": "AdesÃ£o ao Regime TerapÃªutico, Prejudicada"},
        "resultado": {"codigo": "10030185", "termo": "AdesÃ£o ao Regime TerapÃªutico"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "Alta",
        "fundamentacao": "A baixa adesÃ£o ao anti-hipertensivo aumenta risco de crise hipertensiva, prÃ©-eclÃ¢mpsia grave, eclÃ¢mpsia, descolamento placentÃ¡rio e complicaÃ§Ãµes fetais. Ã‰ necessÃ¡rio investigar barreiras, orientar sinais de alerta e reforÃ§ar acompanhamento.",
        "transcultural": {
            "preservacao": ["Reconhecer crenÃ§as familiares sobre pressÃ£o alta."],
            "acomodacao": ["Usar lembretes e rotina diÃ¡ria para melhorar adesÃ£o."],
            "repadronizacao": ["Desestimular suspensÃ£o por melhora dos sintomas ou ausÃªncia de sintomas."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Efeitos adversos do anti-hipertensivo",
        "diagnostico": {"codigo": "10033557", "termo": "Efeito SecundÃ¡rio da MedicaÃ§Ã£o"},
        "resultado": {"codigo": "10030185", "termo": "AdesÃ£o ao Regime TerapÃªutico"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre MedicaÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "Efeitos adversos podem comprometer adesÃ£o ao anti-hipertensivo e exigem avaliaÃ§Ã£o clÃ­nica para ajuste seguro. Sintomas como tontura intensa, sÃ­ncope, dispneia, edema importante ou piora clÃ­nica devem ser comunicados imediatamente.",
        "transcultural": {
            "preservacao": ["Acolher relatos da gestante sobre sensaÃ§Ãµes apÃ³s o medicamento."],
            "acomodacao": ["Orientar registro de sintomas, horÃ¡rios e pressÃ£o arterial quando possÃ­vel."],
            "repadronizacao": ["Evitar interrupÃ§Ã£o espontÃ¢nea do tratamento por efeitos adversos sem avaliaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Insulina prescrita",
        "diagnostico": {"codigo": "10005876", "termo": "Diabetes"},
        "resultado": {"codigo": "10027532", "termo": "Processo do Sistema RegulatÃ³rio, Eficaz"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre MedicaÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "A insulina pode ser indicada no diabetes gestacional ou diabetes prÃ©vio quando medidas alimentares e atividade fÃ­sica nÃ£o sÃ£o suficientes ou conforme avaliaÃ§Ã£o clÃ­nica. O uso correto reduz hiperglicemia materna e complicaÃ§Ãµes fetais.",
        "transcultural": {
            "preservacao": ["Valorizar o cuidado familiar no apoio ao tratamento."],
            "acomodacao": ["Ensinar aplicaÃ§Ã£o considerando rotina, escolaridade e acesso a insumos."],
            "repadronizacao": ["ReforÃ§ar que insulina nÃ£o representa fracasso da gestante, mas proteÃ§Ã£o materno-fetal."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Dificuldade no uso de insulina",
        "diagnostico": {"codigo": "10022155", "termo": "AdesÃ£o ao Regime TerapÃªutico, Prejudicada"},
        "resultado": {"codigo": "10030185", "termo": "AdesÃ£o ao Regime TerapÃªutico"},
        "intervencao": {"codigo": "10019502", "termo": "Orientar sobre SeguranÃ§a"},
        "prioridade": "Alta",
        "fundamentacao": "Dificuldade no preparo, dose, aplicaÃ§Ã£o, rodÃ­zio de locais ou descarte de materiais pode gerar hiperglicemia, hipoglicemia ou lesÃµes locais. A enfermagem deve demonstrar a tÃ©cnica, observar retorno demonstrativo e reforÃ§ar armazenamento e descarte.",
        "transcultural": {
            "preservacao": ["Incluir pessoa de confianÃ§a quando a gestante desejar."],
            "acomodacao": ["Usar demonstraÃ§Ã£o prÃ¡tica e linguagem simples."],
            "repadronizacao": ["Corrigir tÃ©cnicas inseguras de aplicaÃ§Ã£o ou reutilizaÃ§Ã£o inadequada de materiais."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Medo de aplicar insulina",
        "diagnostico": {"codigo": "10007738", "termo": "Medo"},
        "resultado": {"codigo": "10027858", "termo": "Medo, Reduzido"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "Alta",
        "fundamentacao": "O medo da aplicaÃ§Ã£o de insulina pode levar Ã  omissÃ£o de doses e descontrole glicÃªmico. A enfermagem deve acolher, demonstrar tÃ©cnica, permitir treino supervisionado e reforÃ§ar benefÃ­cios para mÃ£e e feto.",
        "transcultural": {
            "preservacao": ["Acolher experiÃªncias familiares com injeÃ§Ãµes e diabetes."],
            "acomodacao": ["Permitir apoio de familiar ou cuidador escolhido pela gestante."],
            "repadronizacao": ["Reduzir crenÃ§as de que insulina causa dependÃªncia ou prejudica o bebÃª."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Falta de armazenamento adequado da insulina",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10028120", "termo": "Risco, Reduzido"},
        "intervencao": {"codigo": "10019502", "termo": "Orientar sobre SeguranÃ§a"},
        "prioridade": "Alta",
        "fundamentacao": "Armazenamento inadequado pode comprometer a estabilidade da insulina e prejudicar o controle glicÃªmico. Deve-se orientar conservaÃ§Ã£o conforme apresentaÃ§Ã£o, proteÃ§Ã£o contra calor e congelamento, transporte seguro e descarte de insumos.",
        "transcultural": {
            "preservacao": ["Reconhecer limitaÃ§Ãµes territoriais, como ausÃªncia de energia elÃ©trica contÃ­nua."],
            "acomodacao": ["Construir estratÃ©gia viÃ¡vel de conservaÃ§Ã£o com a famÃ­lia e a rede de saÃºde."],
            "repadronizacao": ["Evitar exposiÃ§Ã£o da insulina ao sol, calor excessivo ou congelamento."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "AntibiÃ³tico prescrito para ITU",
        "diagnostico": {"codigo": "10029915", "termo": "InfecÃ§Ã£o do Trato UrinÃ¡rio"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre MedicaÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "ITU na gestaÃ§Ã£o deve ser tratada adequadamente para prevenir pielonefrite, parto prematuro e baixo peso ao nascer. A enfermagem deve orientar uso correto do antibiÃ³tico, hidrataÃ§Ã£o, sinais de alerta e retorno para controle quando indicado.",
        "transcultural": {
            "preservacao": ["Valorizar prÃ¡ticas seguras de higiene e hidrataÃ§Ã£o."],
            "acomodacao": ["Ajustar orientaÃ§Ã£o ao horÃ¡rio das doses e rotina da gestante."],
            "repadronizacao": ["Evitar suspensÃ£o do antibiÃ³tico apÃ³s melhora dos sintomas."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Baixa adesÃ£o ao antibiÃ³tico",
        "diagnostico": {"codigo": "10022155", "termo": "AdesÃ£o ao Regime TerapÃªutico, Prejudicada"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "Alta",
        "fundamentacao": "A baixa adesÃ£o ao antibiÃ³tico pode resultar em persistÃªncia da infecÃ§Ã£o urinÃ¡ria, pielonefrite, resistÃªncia bacteriana e complicaÃ§Ãµes obstÃ©tricas. Deve-se reforÃ§ar conclusÃ£o do tratamento e reavaliaÃ§Ã£o se sintomas persistirem.",
        "transcultural": {
            "preservacao": ["Acolher motivos de interrupÃ§Ã£o do tratamento."],
            "acomodacao": ["Criar plano de horÃ¡rios simples para completar o esquema."],
            "repadronizacao": ["ReforÃ§ar que melhora inicial nÃ£o significa cura completa."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Tratamento de sÃ­filis indicado",
        "diagnostico": {"codigo": "10023032", "termo": "InfecÃ§Ã£o"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre MedicaÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "A sÃ­filis na gestaÃ§Ã£o requer tratamento oportuno com penicilina benzatina conforme estÃ¡gio clÃ­nico, alÃ©m de seguimento sorolÃ³gico e abordagem da parceria sexual. O tratamento adequado previne sÃ­filis congÃªnita, abortamento, natimortalidade e prematuridade.",
        "transcultural": {
            "preservacao": ["Garantir acolhimento sem julgamento e preservaÃ§Ã£o do sigilo."],
            "acomodacao": ["Orientar a gestante e parceria sobre tratamento e prevenÃ§Ã£o de reinfecÃ§Ã£o."],
            "repadronizacao": ["Reduzir estigma e reforÃ§ar que tratamento completo protege o bebÃª."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde. PCDT para IST.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Medo da penicilina benzatina",
        "diagnostico": {"codigo": "10007738", "termo": "Medo"},
        "resultado": {"codigo": "10027858", "termo": "Medo, Reduzido"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "Alta",
        "fundamentacao": "O medo da penicilina benzatina pode atrasar o tratamento da sÃ­filis e aumentar risco de transmissÃ£o vertical. A enfermagem deve acolher, explicar benefÃ­cios, possÃ­veis reaÃ§Ãµes, medidas de seguranÃ§a e fluxo de atendimento para administraÃ§Ã£o.",
        "transcultural": {
            "preservacao": ["Acolher experiÃªncias prÃ©vias dolorosas ou relatos familiares."],
            "acomodacao": ["Explicar o procedimento e estratÃ©gias de conforto."],
            "repadronizacao": ["ReforÃ§ar que adiar tratamento aumenta risco para o bebÃª."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde. PCDT para IST.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Tratamento do parceiro nÃ£o realizado",
        "diagnostico": {"codigo": "10015133", "termo": "Risco de InfecÃ§Ã£o"},
        "resultado": {"codigo": "10028945", "termo": "InfecÃ§Ã£o, Ausente"},
        "intervencao": {"codigo": "10051016", "termo": "Orientar sobre InfecÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "A ausÃªncia de tratamento da parceria sexual em casos de sÃ­filis ou outras IST aumenta risco de reinfecÃ§Ã£o materna e transmissÃ£o vertical. A equipe deve orientar tratamento da parceria, uso de preservativo e seguimento conforme protocolo.",
        "transcultural": {
            "preservacao": ["Respeitar dinÃ¢mica familiar e seguranÃ§a da gestante."],
            "acomodacao": ["Ofertar aconselhamento sigiloso e estratÃ©gias de convocaÃ§Ã£o da parceria."],
            "repadronizacao": ["ReforÃ§ar que tratar somente a gestante pode nÃ£o impedir reinfecÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde. PCDT para IST.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Antirretroviral indicado",
        "diagnostico": {"codigo": "10023032", "termo": "InfecÃ§Ã£o"},
        "resultado": {"codigo": "10030185", "termo": "AdesÃ£o ao Regime TerapÃªutico"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre MedicaÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "A terapia antirretroviral na gestaÃ§Ã£o Ã© fundamental para reduzir carga viral materna e prevenir transmissÃ£o vertical do HIV. A enfermagem deve orientar adesÃ£o diÃ¡ria, manejo de efeitos adversos, exames de seguimento e sigilo.",
        "transcultural": {
            "preservacao": ["Garantir acolhimento, sigilo e respeito Ã  histÃ³ria da gestante."],
            "acomodacao": ["Adaptar estratÃ©gias de adesÃ£o Ã  rotina e rede de apoio."],
            "repadronizacao": ["Combater estigma e crenÃ§as que levem Ã  interrupÃ§Ã£o do tratamento."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde. PCDT HIV em gestantes.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Baixa adesÃ£o ao antirretroviral",
        "diagnostico": {"codigo": "10022155", "termo": "AdesÃ£o ao Regime TerapÃªutico, Prejudicada"},
        "resultado": {"codigo": "10030185", "termo": "AdesÃ£o ao Regime TerapÃªutico"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "Alta",
        "fundamentacao": "A baixa adesÃ£o ao antirretroviral pode manter carga viral detectÃ¡vel e aumentar risco de transmissÃ£o vertical do HIV. A equipe deve identificar barreiras, efeitos adversos, estigma, acesso ao medicamento e organizar suporte intensivo.",
        "transcultural": {
            "preservacao": ["Proteger sigilo e autonomia da gestante."],
            "acomodacao": ["Planejar horÃ¡rios discretos e compatÃ­veis com sua rotina."],
            "repadronizacao": ["Reduzir crenÃ§as de abandono terapÃªutico por medo de descoberta do diagnÃ³stico."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde. PCDT HIV em gestantes.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Medicamento controlado em uso",
        "diagnostico": {"codigo": "10024625", "termo": "Regime TerapÃªutico, Prejudicado"},
        "resultado": {"codigo": "10030185", "termo": "AdesÃ£o ao Regime TerapÃªutico"},
        "intervencao": {"codigo": "10019502", "termo": "Orientar sobre SeguranÃ§a"},
        "prioridade": "Alta",
        "fundamentacao": "Medicamentos controlados durante a gestaÃ§Ã£o exigem avaliaÃ§Ã£o de risco-benefÃ­cio, dose, indicaÃ§Ã£o, interaÃ§Ã£o medicamentosa, dependÃªncia, abstinÃªncia e possÃ­veis efeitos fetais. A suspensÃ£o abrupta tambÃ©m pode ser perigosa, devendo ocorrer apenas com orientaÃ§Ã£o profissional.",
        "transcultural": {
            "preservacao": ["Acolher a necessidade clÃ­nica sem julgamento."],
            "acomodacao": ["Orientar acompanhamento compartilhado com prÃ©-natal e saÃºde mental quando necessÃ¡rio."],
            "repadronizacao": ["Evitar suspensÃ£o abrupta ou aumento de dose por conta prÃ³pria."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Uso de psicotrÃ³pico na gestaÃ§Ã£o",
        "diagnostico": {"codigo": "10022402", "termo": "Processo PsicolÃ³gico, Prejudicado"},
        "resultado": {"codigo": "10027649", "termo": "Processo PsicolÃ³gico, Eficaz"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "Alta",
        "fundamentacao": "O uso de psicotrÃ³picos na gestaÃ§Ã£o deve ser acompanhado com avaliaÃ§Ã£o de risco-benefÃ­cio, pois tanto a doenÃ§a mental nÃ£o tratada quanto o uso inadequado de medicamentos podem trazer riscos. A enfermagem deve orientar nÃ£o interromper abruptamente e articular cuidado multiprofissional.",
        "transcultural": {
            "preservacao": ["Reduzir estigma e acolher sofrimento psÃ­quico."],
            "acomodacao": ["Incluir rede de apoio quando autorizado pela gestante."],
            "repadronizacao": ["ReforÃ§ar que tratamento em saÃºde mental tambÃ©m faz parte do cuidado prÃ©-natal."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "MedicaÃ§Ãµes e suplementaÃ§Ã£o",
        "achado_clinico": "Necessidade de conciliaÃ§Ã£o medicamentosa",
        "diagnostico": {"codigo": "10024625", "termo": "Regime TerapÃªutico, Prejudicado"},
        "resultado": {"codigo": "10030185", "termo": "AdesÃ£o ao Regime TerapÃªutico"},
        "intervencao": {"codigo": "10019470", "termo": "Orientar sobre MedicaÃ§Ã£o"},
        "prioridade": "Alta",
        "fundamentacao": "A conciliaÃ§Ã£o medicamentosa no prÃ©-natal identifica medicamentos prescritos, automedicaÃ§Ã£o, fitoterÃ¡picos, suplementos, duplicidades, interaÃ§Ãµes e riscos gestacionais. Ã‰ essencial para seguranÃ§a materno-fetal e continuidade do cuidado.",
        "transcultural": {
            "preservacao": ["Acolher todos os produtos usados pela gestante sem julgamento."],
            "acomodacao": ["Solicitar que leve receitas, cartelas, frascos, chÃ¡s e suplementos Ã s consultas."],
            "repadronizacao": ["Organizar lista Ãºnica e segura de medicamentos autorizados e contraindicaÃ§Ãµes orientadas."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    }
]# modulos/regras_clinicas/prenatal/exames_imagem.py

REGRAS = [
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Ultrassonografia obstÃ©trica nÃ£o realizada",
        "diagnostico": {"codigo": "10022155", "termo": "AdesÃ£o ao Regime TerapÃªutico, Prejudicada"},
        "resultado": {"codigo": "10030185", "termo": "AdesÃ£o ao Regime TerapÃªutico"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "A ultrassonografia obstÃ©trica auxilia na confirmaÃ§Ã£o da idade gestacional, vitalidade fetal, nÃºmero de fetos, localizaÃ§Ã£o placentÃ¡ria, crescimento fetal e identificaÃ§Ã£o de alteraÃ§Ãµes. Quando nÃ£o realizada, deve-se verificar barreiras de acesso, solicitar ou encaminhar conforme protocolo e registrar conduta.",
        "transcultural": {
            "preservacao": ["Valorizar a percepÃ§Ã£o da gestante sobre o desenvolvimento fetal e seus saberes familiares."],
            "acomodacao": ["Adequar o agendamento Ã  disponibilidade de transporte, trabalho, territÃ³rio e rede de apoio."],
            "repadronizacao": ["Reorientar a ideia de que exame de imagem sÃ³ Ã© necessÃ¡rio quando hÃ¡ dor ou sangramento."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde. AtenÃ§Ã£o ao prÃ©-natal de baixo risco.", "FEBRASGO. AssistÃªncia prÃ©-natal.", "OMS. RecomendaÃ§Ãµes sobre cuidados prÃ©-natais.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger. Teoria Transcultural."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Ultrassonografia do primeiro trimestre nÃ£o realizada",
        "diagnostico": {"codigo": "10022155", "termo": "AdesÃ£o ao Regime TerapÃªutico, Prejudicada"},
        "resultado": {"codigo": "10030185", "termo": "AdesÃ£o ao Regime TerapÃªutico"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "A ultrassonografia do primeiro trimestre Ã© Ãºtil para dataÃ§Ã£o gestacional, confirmaÃ§Ã£o de vitalidade, localizaÃ§Ã£o gestacional e identificaÃ§Ã£o de gestaÃ§Ã£o mÃºltipla. A ausÃªncia desse exame pode dificultar o acompanhamento adequado do crescimento fetal e a definiÃ§Ã£o da idade gestacional.",
        "transcultural": {
            "preservacao": ["Acolher experiÃªncias familiares sobre confirmaÃ§Ã£o da gestaÃ§Ã£o."],
            "acomodacao": ["Explicar a finalidade do exame em linguagem simples."],
            "repadronizacao": ["Estimular realizaÃ§Ã£o oportuna de exames mesmo quando a gestante se sente bem."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Idade gestacional incerta",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "A idade gestacional incerta compromete a interpretaÃ§Ã£o do crescimento fetal, a programaÃ§Ã£o de exames, a identificaÃ§Ã£o de prematuridade ou pÃ³s-datismo e a tomada de decisÃµes obstÃ©tricas. A ultrassonografia, especialmente quando realizada precocemente, contribui para melhor dataÃ§Ã£o da gestaÃ§Ã£o.",
        "transcultural": {
            "preservacao": ["Acolher formas culturais de marcar datas, ciclos menstruais e eventos familiares."],
            "acomodacao": ["Reconstruir a histÃ³ria gestacional com apoio de marcos familiares e registros disponÃ­veis."],
            "repadronizacao": ["Estimular registro da DUM e inÃ­cio precoce do prÃ©-natal em futuras gestaÃ§Ãµes."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "DivergÃªncia entre DUM e ultrassonografia",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "DivergÃªncia entre data da Ãºltima menstruaÃ§Ã£o e ultrassonografia pode ocorrer por ciclos irregulares, lembranÃ§a imprecisa da DUM ou alteraÃ§Ã£o no crescimento fetal. A conduta depende da idade gestacional, qualidade do exame e critÃ©rios obstÃ©tricos de dataÃ§Ã£o.",
        "transcultural": {
            "preservacao": ["Respeitar a narrativa da gestante sobre seu ciclo e sinais corporais."],
            "acomodacao": ["Explicar que a dataÃ§Ã£o pode ser ajustada por critÃ©rios clÃ­nicos e ultrassonogrÃ¡ficos."],
            "repadronizacao": ["Evitar conclusÃµes precipitadas sem avaliaÃ§Ã£o da equipe e registro adequado."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "TranslucÃªncia nucal alterada",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "TranslucÃªncia nucal alterada pode indicar risco aumentado para aneuploidias, cardiopatias e outras alteraÃ§Ãµes fetais. Requer encaminhamento para avaliaÃ§Ã£o especializada, aconselhamento, exames complementares e seguimento conforme protocolo.",
        "transcultural": {
            "preservacao": ["Acolher crenÃ§as e sentimentos da famÃ­lia diante de possÃ­vel alteraÃ§Ã£o fetal."],
            "acomodacao": ["Garantir comunicaÃ§Ã£o clara, respeitosa e sem julgamento."],
            "repadronizacao": ["Evitar interpretaÃ§Ã£o definitiva do achado sem avaliaÃ§Ã£o especializada."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "MorfolÃ³gica do primeiro trimestre alterada",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "AlteraÃ§Ãµes na ultrassonografia morfolÃ³gica do primeiro trimestre podem indicar risco de anomalias estruturais, cromossÃ´micas ou alteraÃ§Ãµes do desenvolvimento fetal. A gestante deve ser encaminhada para avaliaÃ§Ã£o especializada e acompanhamento multiprofissional.",
        "transcultural": {
            "preservacao": ["Acolher espiritualidade, valores familiares e necessidades emocionais."],
            "acomodacao": ["Explicar a necessidade de exames complementares e seguimento especializado."],
            "repadronizacao": ["ReforÃ§ar que um achado alterado exige investigaÃ§Ã£o, nÃ£o conclusÃ£o isolada."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "MorfolÃ³gica do segundo trimestre nÃ£o realizada",
        "diagnostico": {"codigo": "10022155", "termo": "AdesÃ£o ao Regime TerapÃªutico, Prejudicada"},
        "resultado": {"codigo": "10030185", "termo": "AdesÃ£o ao Regime TerapÃªutico"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "A ultrassonografia morfolÃ³gica do segundo trimestre avalia anatomia fetal, placenta, lÃ­quido amniÃ³tico e crescimento. Quando nÃ£o realizada no perÃ­odo recomendado, deve-se providenciar agendamento ou encaminhamento conforme disponibilidade e idade gestacional.",
        "transcultural": {
            "preservacao": ["Valorizar o interesse da famÃ­lia em conhecer o desenvolvimento do bebÃª."],
            "acomodacao": ["Planejar o exame conforme acesso ao serviÃ§o e transporte."],
            "repadronizacao": ["ReforÃ§ar que o exame possui finalidade clÃ­nica, nÃ£o apenas identificaÃ§Ã£o do sexo fetal."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "MorfolÃ³gica do segundo trimestre alterada",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "AlteraÃ§Ã£o na morfolÃ³gica do segundo trimestre pode indicar malformaÃ§Ãµes fetais, alteraÃ§Ãµes placentÃ¡rias, restriÃ§Ã£o de crescimento, alteraÃ§Ãµes de lÃ­quido amniÃ³tico ou necessidade de investigaÃ§Ã£o complementar. Exige encaminhamento para avaliaÃ§Ã£o especializada.",
        "transcultural": {
            "preservacao": ["Acolher medo, ansiedade e valores familiares."],
            "acomodacao": ["Orientar prÃ³ximos passos de forma clara e respeitosa."],
            "repadronizacao": ["Evitar abandono do prÃ©-natal apÃ³s notÃ­cia de alteraÃ§Ã£o fetal."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Placenta prÃ©via suspeita",
        "diagnostico": {"codigo": "10003303", "termo": "Sangramento"},
        "resultado": {"codigo": "10028120", "termo": "Sangramento, Ausente"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Placenta prÃ©via suspeita aumenta risco de sangramento vaginal, parto prematuro e necessidade de planejamento obstÃ©trico. A gestante deve ser encaminhada para avaliaÃ§Ã£o, confirmaÃ§Ã£o diagnÃ³stica e orientaÃ§Ã£o sobre sinais de alerta.",
        "transcultural": {
            "preservacao": ["Acolher a gestante e sua famÃ­lia diante do medo de sangramento."],
            "acomodacao": ["Orientar repouso relativo e procura imediata em caso de sangramento conforme prescriÃ§Ã£o e protocolo."],
            "repadronizacao": ["Evitar minimizar qualquer sangramento vaginal na gestaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Descolamento placentÃ¡rio suspeito",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Suspeita de descolamento placentÃ¡rio Ã© emergÃªncia obstÃ©trica, principalmente quando hÃ¡ dor abdominal, hipertonia uterina, sangramento, sofrimento fetal ou instabilidade materna. Requer encaminhamento imediato para avaliaÃ§Ã£o obstÃ©trica.",
        "transcultural": {
            "preservacao": ["Acolher relatos da gestante sobre dor, sangramento e percepÃ§Ã£o fetal."],
            "acomodacao": ["Acionar rede de apoio e transporte de urgÃªncia conforme realidade local."],
            "repadronizacao": ["ReforÃ§ar que dor abdominal intensa com sangramento nÃ£o deve aguardar consulta agendada."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "RestriÃ§Ã£o de crescimento fetal suspeita",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "RestriÃ§Ã£o de crescimento fetal suspeita pode estar relacionada a insuficiÃªncia placentÃ¡ria, hipertensÃ£o, infecÃ§Ãµes, tabagismo, desnutriÃ§Ã£o ou outras condiÃ§Ãµes maternas e fetais. Exige avaliaÃ§Ã£o especializada, acompanhamento seriado do crescimento e, quando indicado, Doppler obstÃ©trico.",
        "transcultural": {
            "preservacao": ["Valorizar alimentos e prÃ¡ticas de cuidado seguros do territÃ³rio."],
            "acomodacao": ["Adequar orientaÃ§Ãµes nutricionais e de retorno Ã  realidade social da gestante."],
            "repadronizacao": ["ReforÃ§ar necessidade de acompanhamento seriado, mesmo sem sintomas maternos."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Macrossomia fetal suspeita",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "Alta",
        "fundamentacao": "Macrossomia fetal suspeita pode estar associada a diabetes gestacional, ganho ponderal excessivo e risco de distocia de ombro, trauma obstÃ©trico, cesariana e hipoglicemia neonatal. Deve-se avaliar controle glicÃªmico, crescimento fetal e plano de parto.",
        "transcultural": {
            "preservacao": ["Respeitar crenÃ§as familiares sobre bebÃª grande e saÃºde."],
            "acomodacao": ["Orientar relaÃ§Ã£o entre alimentaÃ§Ã£o, glicemia e crescimento fetal de forma simples."],
            "repadronizacao": ["Reorientar a ideia de que bebÃª muito grande sempre significa gestaÃ§Ã£o saudÃ¡vel."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "OligodrÃ¢mnio",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "OligodrÃ¢mnio pode estar associado a ruptura de membranas, insuficiÃªncia placentÃ¡ria, restriÃ§Ã£o de crescimento fetal, malformaÃ§Ãµes renais fetais ou pÃ³s-datismo. Exige avaliaÃ§Ã£o obstÃ©trica, investigaÃ§Ã£o da causa e monitoramento fetal.",
        "transcultural": {
            "preservacao": ["Acolher preocupaÃ§Ãµes da gestante sobre lÃ­quido e vitalidade fetal."],
            "acomodacao": ["Orientar sinais de alerta, como perda de lÃ­quido e reduÃ§Ã£o de movimentos fetais."],
            "repadronizacao": ["Evitar atribuir o achado apenas Ã  baixa ingestÃ£o de Ã¡gua sem avaliaÃ§Ã£o clÃ­nica."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "PolidrÃ¢mnio",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "PolidrÃ¢mnio pode estar associado a diabetes gestacional, malformaÃ§Ãµes fetais, infecÃ§Ãµes, gestaÃ§Ã£o mÃºltipla ou causas idiopÃ¡ticas. A gestante deve ser avaliada quanto a sintomas respiratÃ³rios, contraÃ§Ãµes, crescimento uterino aumentado e necessidade de investigaÃ§Ã£o complementar.",
        "transcultural": {
            "preservacao": ["Acolher a interpretaÃ§Ã£o da gestante sobre aumento abdominal."],
            "acomodacao": ["Orientar sinais de trabalho de parto prematuro e desconforto respiratÃ³rio."],
            "repadronizacao": ["ReforÃ§ar necessidade de investigaÃ§Ã£o, mesmo quando a gestante atribui o aumento apenas ao bebÃª grande."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "GestaÃ§Ã£o gemelar",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "GestaÃ§Ã£o gemelar apresenta maior risco de prematuridade, restriÃ§Ã£o de crescimento, anemia, sÃ­ndromes hipertensivas e complicaÃ§Ãµes fetais. Requer definiÃ§Ã£o de corionicidade, acompanhamento mais frequente e, quando indicado, prÃ©-natal de alto risco.",
        "transcultural": {
            "preservacao": ["Valorizar redes familiares de apoio Ã  gestante."],
            "acomodacao": ["Planejar consultas, exames e transporte considerando maior risco e maior frequÃªncia de acompanhamento."],
            "repadronizacao": ["ReforÃ§ar que gestaÃ§Ã£o gemelar demanda vigilÃ¢ncia ampliada mesmo sem sintomas."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "ApresentaÃ§Ã£o pÃ©lvica",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10045079", "termo": "Orientar sobre GestaÃ§Ã£o"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "A apresentaÃ§Ã£o pÃ©lvica pode ser transitÃ³ria antes do termo, mas quando persistente no final da gestaÃ§Ã£o pode influenciar planejamento do parto. A gestante deve ser orientada e acompanhada conforme idade gestacional, vitalidade fetal e avaliaÃ§Ã£o obstÃ©trica.",
        "transcultural": {
            "preservacao": ["Acolher crenÃ§as sobre posiÃ§Ã£o fetal e parto."],
            "acomodacao": ["Explicar que a posiÃ§Ã£o fetal pode mudar conforme idade gestacional."],
            "repadronizacao": ["Evitar manobras caseiras ou prÃ¡ticas sem seguranÃ§a para tentar mudar a posiÃ§Ã£o fetal."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "ApresentaÃ§Ã£o transversa",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "ApresentaÃ§Ã£o transversa persistente, especialmente no final da gestaÃ§Ã£o, estÃ¡ associada a maior risco no parto vaginal e requer avaliaÃ§Ã£o obstÃ©trica para planejamento seguro do parto e prevenÃ§Ã£o de complicaÃ§Ãµes.",
        "transcultural": {
            "preservacao": ["Acolher conhecimentos familiares sobre posiÃ§Ã£o do bebÃª."],
            "acomodacao": ["Orientar acompanhamento e avaliaÃ§Ã£o obstÃ©trica sem gerar culpa na gestante."],
            "repadronizacao": ["Evitar tentativas caseiras de mudanÃ§a de posiÃ§Ã£o fetal."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Doppler obstÃ©trico alterado",
        "diagnostico": {"codigo": "10012606", "termo": "Processo do Sistema CirculatÃ³rio, Prejudicado"},
        "resultado": {"codigo": "10028379", "termo": "Processo do Sistema CirculatÃ³rio, Positivo"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Doppler obstÃ©trico alterado pode indicar comprometimento da circulaÃ§Ã£o uteroplacentÃ¡ria ou fetal, associado a restriÃ§Ã£o de crescimento, insuficiÃªncia placentÃ¡ria, prÃ©-eclÃ¢mpsia e risco fetal. Exige avaliaÃ§Ã£o especializada e vigilÃ¢ncia materno-fetal.",
        "transcultural": {
            "preservacao": ["Acolher ansiedade da gestante diante de exame alterado."],
            "acomodacao": ["Explicar a importÃ¢ncia do seguimento e dos retornos seriados."],
            "repadronizacao": ["ReforÃ§ar que ausÃªncia de sintomas maternos nÃ£o exclui risco fetal."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "BCF ausente em exame",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Batimentos cardÃ­acos fetais ausentes em exame Ã© achado crÃ­tico e requer confirmaÃ§Ã£o imediata por avaliaÃ§Ã£o obstÃ©trica e exame apropriado, considerando idade gestacional, qualidade tÃ©cnica e condiÃ§Ã£o materno-fetal.",
        "transcultural": {
            "preservacao": ["Acolher a gestante e famÃ­lia com comunicaÃ§Ã£o humanizada."],
            "acomodacao": ["Garantir encaminhamento rÃ¡pido e suporte emocional."],
            "repadronizacao": ["Evitar conclusÃµes definitivas sem confirmaÃ§Ã£o adequada, mas nÃ£o retardar avaliaÃ§Ã£o urgente."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "MalformaÃ§Ã£o fetal suspeita",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Suspeita de malformaÃ§Ã£o fetal exige confirmaÃ§Ã£o diagnÃ³stica, avaliaÃ§Ã£o especializada, aconselhamento, planejamento do parto e organizaÃ§Ã£o da rede de cuidado neonatal quando necessÃ¡rio.",
        "transcultural": {
            "preservacao": ["Respeitar valores, espiritualidade e decisÃµes familiares."],
            "acomodacao": ["Oferecer informaÃ§Ã£o clara, apoio emocional e encaminhamento especializado."],
            "repadronizacao": ["Evitar estigmatizaÃ§Ã£o ou culpabilizaÃ§Ã£o da gestante pela alteraÃ§Ã£o fetal."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Colo uterino curto",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Colo uterino curto em exame de imagem estÃ¡ associado a maior risco de parto prematuro, especialmente em gestantes com histÃ³ria obstÃ©trica compatÃ­vel. Exige avaliaÃ§Ã£o obstÃ©trica, estratificaÃ§Ã£o de risco e condutas preventivas conforme protocolo.",
        "transcultural": {
            "preservacao": ["Acolher preocupaÃ§Ãµes da gestante sobre repouso e parto prematuro."],
            "acomodacao": ["Planejar acompanhamento considerando trabalho, deslocamento e rede de apoio."],
            "repadronizacao": ["ReforÃ§ar que ausÃªncia de dor nÃ£o exclui risco de prematuridade."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Risco de parto prematuro por imagem",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Materno-Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Achados de imagem como colo curto, alteraÃ§Ãµes placentÃ¡rias, polidrÃ¢mnio, gestaÃ§Ã£o mÃºltipla ou sinais de insuficiÃªncia placentÃ¡ria podem aumentar risco de parto prematuro. A gestante deve ser encaminhada para avaliaÃ§Ã£o, vigilÃ¢ncia e orientaÃ§Ãµes de sinais de alerta.",
        "transcultural": {
            "preservacao": ["Reconhecer estratÃ©gias familiares para proteÃ§Ã£o da gestante."],
            "acomodacao": ["Construir plano de deslocamento e busca de atendimento em caso de contraÃ§Ãµes, sangramento ou perda de lÃ­quido."],
            "repadronizacao": ["Reorientar a prÃ¡tica de aguardar melhora espontÃ¢nea diante de sinais de prematuridade."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Crescimento fetal discordante",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "Crescimento fetal discordante pode indicar restriÃ§Ã£o de crescimento, erro de dataÃ§Ã£o, insuficiÃªncia placentÃ¡ria ou complicaÃ§Ãµes em gestaÃ§Ã£o mÃºltipla. Requer avaliaÃ§Ã£o seriada, revisÃ£o da idade gestacional e acompanhamento especializado.",
        "transcultural": {
            "preservacao": ["Valorizar a percepÃ§Ã£o materna sobre crescimento abdominal e movimentos fetais."],
            "acomodacao": ["Orientar necessidade de retornos e exames seriados."],
            "repadronizacao": ["Evitar considerar apenas o tamanho da barriga como indicador confiÃ¡vel de crescimento fetal."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Circular de cordÃ£o descrita",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10045079", "termo": "Orientar sobre GestaÃ§Ã£o"},
        "prioridade": "Baixa",
        "fundamentacao": "Circular de cordÃ£o Ã© achado ultrassonogrÃ¡fico frequente e, isoladamente, geralmente nÃ£o define via de parto nem indica sofrimento fetal. Deve-se orientar a gestante, reduzir ansiedade e reforÃ§ar observaÃ§Ã£o dos movimentos fetais e acompanhamento habitual.",
        "transcultural": {
            "preservacao": ["Acolher crenÃ§as familiares sobre cordÃ£o umbilical e risco ao bebÃª."],
            "acomodacao": ["Explicar de forma simples quando o achado exige ou nÃ£o preocupaÃ§Ã£o adicional."],
            "repadronizacao": ["Reorientar a ideia de que circular de cordÃ£o isolada sempre exige cesariana."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "LÃ­quido amniÃ³tico alterado",
        "diagnostico": {"codigo": "10015146", "termo": "Risco de LesÃ£o"},
        "resultado": {"codigo": "10033682", "termo": "Estado Fetal, Eficaz"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "AlteraÃ§Ã£o do lÃ­quido amniÃ³tico, seja por reduÃ§Ã£o ou aumento, pode estar relacionada a ruptura de membranas, diabetes, malformaÃ§Ãµes, restriÃ§Ã£o de crescimento, infecÃ§Ã£o ou alteraÃ§Ãµes placentÃ¡rias. Exige avaliaÃ§Ã£o obstÃ©trica e definiÃ§Ã£o da causa.",
        "transcultural": {
            "preservacao": ["Acolher preocupaÃ§Ãµes e interpretaÃ§Ãµes culturais sobre lÃ­quido amniÃ³tico."],
            "acomodacao": ["Orientar sinais de alerta, como perda de lÃ­quido, contraÃ§Ãµes e reduÃ§Ã£o de movimentos fetais."],
            "repadronizacao": ["Evitar condutas caseiras isoladas sem avaliaÃ§Ã£o clÃ­nica."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Necessidade de repetir ultrassonografia",
        "diagnostico": {"codigo": "10024625", "termo": "Regime TerapÃªutico, Prejudicado"},
        "resultado": {"codigo": "10030185", "termo": "AdesÃ£o ao Regime TerapÃªutico"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "A repetiÃ§Ã£o da ultrassonografia pode ser necessÃ¡ria por exame inconclusivo, idade gestacional inadequada, dificuldade tÃ©cnica, necessidade de acompanhar crescimento fetal, lÃ­quido amniÃ³tico, placenta ou achados suspeitos. Deve-se orientar a finalidade da repetiÃ§Ã£o e garantir seguimento.",
        "transcultural": {
            "preservacao": ["Acolher dÃºvidas sobre por que repetir um exame jÃ¡ realizado."],
            "acomodacao": ["Planejar repetiÃ§Ã£o conforme acesso, transporte e disponibilidade do serviÃ§o."],
            "repadronizacao": ["ReforÃ§ar que repetir o exame nÃ£o significa necessariamente gravidade, mas necessidade de melhor avaliaÃ§Ã£o."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Dificuldade de acesso ao exame de imagem",
        "diagnostico": {"codigo": "10025806", "termo": "Comportamento de SaÃºde, Prejudicado"},
        "resultado": {"codigo": "10028276", "termo": "Comportamento de SaÃºde, Positivo"},
        "intervencao": {"codigo": "10035331", "termo": "Encaminhar para ServiÃ§o de SaÃºde"},
        "prioridade": "Alta",
        "fundamentacao": "A dificuldade de acesso ao exame de imagem pode atrasar diagnÃ³stico, estratificaÃ§Ã£o de risco e planejamento obstÃ©trico. A equipe deve articular regulaÃ§Ã£o, transporte sanitÃ¡rio, busca ativa e priorizaÃ§Ã£o conforme risco gestacional.",
        "transcultural": {
            "preservacao": ["Reconhecer barreiras territoriais, econÃ´micas, ribeirinhas, rurais ou familiares."],
            "acomodacao": ["Adequar agendamento aos dias de deslocamento, consulta e disponibilidade da rede."],
            "repadronizacao": ["Reorganizar o cuidado para reduzir iniquidades de acesso e perda de seguimento."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    },
    {
        "linha_cuidado": "PrÃ©-natal",
        "categoria": "Exames de imagem",
        "achado_clinico": "Exame de imagem atrasado",
        "diagnostico": {"codigo": "10022155", "termo": "AdesÃ£o ao Regime TerapÃªutico, Prejudicada"},
        "resultado": {"codigo": "10030185", "termo": "AdesÃ£o ao Regime TerapÃªutico"},
        "intervencao": {"codigo": "10024625", "termo": "Orientar sobre Regime TerapÃªutico"},
        "prioridade": "MÃ©dia",
        "fundamentacao": "Exame de imagem atrasado pode reduzir a utilidade clÃ­nica de avaliaÃ§Ãµes dependentes da idade gestacional, como dataÃ§Ã£o precoce, rastreamento morfolÃ³gico e monitoramento do crescimento fetal. Deve-se reagendar, priorizar conforme risco e registrar justificativa.",
        "transcultural": {
            "preservacao": ["Acolher dificuldades reais que levaram ao atraso."],
            "acomodacao": ["Pactuar novo plano viÃ¡vel de realizaÃ§Ã£o do exame."],
            "repadronizacao": ["ReforÃ§ar a importÃ¢ncia de realizar exames dentro da janela recomendada quando possÃ­vel."]
        },
        "referencias": ["MinistÃ©rio da SaÃºde.", "FEBRASGO.", "OMS.", "COFEN ResoluÃ§Ã£o nÂº 736/2024.", "Leininger."]
    }
]
