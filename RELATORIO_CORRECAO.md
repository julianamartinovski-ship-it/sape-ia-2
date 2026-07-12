# SAPE IA 2.0 — versão corrigida

## Correções realizadas

- Preservadas **197 regras clínicas de pré-natal**.
- Corrigidas as **45 ocorrências originalmente sem código CIPE** nas categorias:
  - Captação e vínculo;
  - Fatores de risco;
  - Vacinação.
- Diagnósticos, resultados e intervenções dessas regras foram vinculados a termos oficiais da **CIPE 2019**, após revisão clínica.
- As formulações clínicas originais foram preservadas no campo `formulacao_clinica_original`.
- O banco `banco_dados/cipe.db` foi corrigido usando o PDF oficial incluído no projeto, eliminando termos truncados e caracteres corrompidos.
- O carregador `modulos/banco_prenatal.py` passou a validar os códigos no banco CIPE e a usar o termo oficial do código.
- O Processo de Enfermagem deixou de usar regras antigas como fallback e passou a usar o mesmo motor de inferência da tela de Apoio à Decisão.
- Corrigido o arquivo legado `modulos/inserir_regras_prenatal.py`, que continha erro de sintaxe.
- Criado backup anterior às correções em `backup_antes_correcao_45_regras/`.
- Criado o teste `teste_integracao_sape.py`.

## Como executar

No terminal aberto na pasta do projeto:

```powershell
py -m pip install -r requirements.txt
py teste_integracao_sape.py
py -m streamlit run app.py
```

O site normalmente abrirá em `http://localhost:8501`.

## Observação terminológica

As regras clínicas usam o achado selecionado como gatilho e apresentam diagnóstico, resultado e intervenção com código e termo oficial CIPE. Em situações nas quais a formulação clínica original não era um termo oficial pré-coordenado, foi escolhido um conceito CIPE oficial mais amplo e clinicamente compatível; a formulação original permanece preservada para auditoria.
