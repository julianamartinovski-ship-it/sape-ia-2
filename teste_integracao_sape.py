"""Teste rápido de integridade do SAPE IA 2.0.

Execute na raiz do projeto:
    py teste_integracao_sape.py
"""
from modulos.banco_prenatal import BANCO_PRENATAL
from modulos.inferencia import executar_inferencia

ALVOS = {
    'Início tardio do pré-natal', 'Gestante faltosa', 'Área descoberta pela ESF',
    'Longa distância até a UBS', 'Transporte fluvial', 'Hipertensão arterial',
    'Proteinúria', 'Cefaleia persistente', 'Escotomas visuais', 'Edema importante',
    'Glicemia alterada', 'Diabetes gestacional', 'Anemia', 'Obesidade', 'Baixo peso',
    'Tabagismo', 'Uso de álcool', 'Uso de drogas', 'Idade materna menor que 15 anos',
    'Idade materna maior ou igual a 35 anos', 'Situação vacinal desconhecida',
    'Vacina dT incompleta', 'Vacina dTpa indicada', 'Vacina dTpa não realizada',
    'Vacina influenza indicada', 'Vacina influenza não realizada',
    'Vacina hepatite B incompleta', 'Vacina hepatite B não realizada',
    'Vacina COVID-19 indicada', 'Recusa vacinal', 'Medo de reação vacinal',
    'Falta de acesso à sala de vacina', 'Barreiras culturais relacionadas à vacinação',
    'Gestante ribeirinha com dificuldade de acesso à vacina', 'Gestante sem cartão vacinal',
}

assert len(BANCO_PRENATAL) == 197, f"Esperadas 197 regras; encontradas {len(BANCO_PRENATAL)}"

regras_alvo = [r for r in BANCO_PRENATAL if r.get('achado_clinico') in ALVOS]
assert regras_alvo, 'As regras-alvo não foram carregadas.'

for regra in regras_alvo:
    for campo in ('diagnostico', 'resultado', 'intervencao'):
        item = regra.get(campo)
        assert isinstance(item, dict), f"{regra.get('achado_clinico')}: {campo} inválido"
        assert item.get('codigo'), f"{regra.get('achado_clinico')}: {campo} sem código"
        assert item.get('termo'), f"{regra.get('achado_clinico')}: {campo} sem termo"

for achado in (
    'Hipertensão arterial',
    'Início tardio do pré-natal',
    'Vacina dTpa não realizada',
    'Barreiras culturais relacionadas à vacinação',
):
    sugestoes = executar_inferencia([achado], {}, 'CIPE®')
    assert sugestoes, f"Nenhuma sugestão gerada para: {achado}"
    primeira = sugestoes[0]
    assert primeira['cipe_diag'][0].get('codigo')
    assert primeira['cipe_res'][0].get('codigo')
    assert primeira['cipe_int'][0].get('codigo')

print('TESTE CONCLUÍDO COM SUCESSO')
print('Total de regras carregadas:', len(BANCO_PRENATAL))
print('Regras-alvo revisadas e codificadas:', len(regras_alvo))
print('Inferência clínica: OK')
