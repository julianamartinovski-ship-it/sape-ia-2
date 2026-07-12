from .captacao_vinculo import REGRAS as CAPTACAO_VINCULO
from .fatores_risco import REGRAS as FATORES_RISCO
from .exames_laboratoriais import REGRAS as EXAMES_LABORATORIAIS
from .vacinacao import REGRAS as VACINACAO
from .sinais_sintomas import REGRAS as SINAIS_SINTOMAS
from .intercorrencias import REGRAS as INTERCORRENCIAS
from .medicacoes import REGRAS as MEDICACOES
from .exames_imagem import REGRAS as EXAMES_IMAGEM

REGRAS = (
    CAPTACAO_VINCULO
    + FATORES_RISCO
    + EXAMES_LABORATORIAIS
    + VACINACAO
    + SINAIS_SINTOMAS
    + INTERCORRENCIAS
    + MEDICACOES
    + EXAMES_IMAGEM
)
