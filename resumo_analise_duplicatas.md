# Resumo da Análise de Duplicatas - Base Scopus

## Objetivo

Identificar e quantificar registros duplicados na base de dados bibliográfica exportada da Scopus, visando garantir a qualidade dos dados para a revisão sistemática da literatura.

## Metodologia

### Base de Dados
- **238 artigos** exportados da Scopus em formato CSV
- Análise realizada usando Python 3 e biblioteca Pandas
- Ambiente virtual isolado (venv) para reprodutibilidade

### Critérios de Análise

**1. Duplicatas por DOI (Digital Object Identifier)**
- Identificador único de publicações acadêmicas
- Método mais confiável de detecção de duplicatas
- 218 registros com DOI válido (91,6%)

**2. Duplicatas por Título**
- Comparação após normalização (minúsculas, remoção de espaços)
- Captura duplicatas sem DOI ou com DOIs diferentes
- 238 registros com título válido (100%)

## Resultados Principais

| Critério | Registros Duplicados | Itens Únicos Duplicados | Taxa de Duplicação |
|----------|---------------------|-------------------------|-------------------|
| **DOI** | 2 | 1 | 0,92% |
| **Título** | 6 | 3 | 2,52% |
| **DOI + Título** | 2 | 1 | 0,84% |

### Casos Identificados

1. **Duplicata verdadeira** (1 caso)
   - Mesmo DOI e título aparecendo 2 vezes
   - DOI: 10.1109/ICORR58425.2023.10304712
   - Recomendação: **Remover**

2. **Possíveis republicações** (2 casos)
   - Mesmo título, DOIs e anos diferentes
   - Recomendação: **Análise manual**

## Conclusão

A base de dados apresenta **baixa taxa de duplicação** (< 1% por DOI), indicando boa qualidade da exportação. Foram identificadas 2 duplicatas verdadeiras que devem ser removidas, e 4 casos de possíveis republicações que requerem análise manual.

A metodologia automatizada permitiu análise sistemática e reproduzível, fundamental para a qualidade da revisão sistemática.

---

**Script desenvolvido:** `analise_duplicatas.py`  
**Relatório completo:** `analise_duplicatas_resultado_20251005_233345.txt`  
**Documentação detalhada:** `documentacao_analise_duplicatas.md`

