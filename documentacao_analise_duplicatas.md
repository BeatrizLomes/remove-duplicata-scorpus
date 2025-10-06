# Análise de Duplicatas em Base de Dados Bibliográfica Scopus

## 1. Introdução

No contexto de revisões sistemáticas da literatura e mapeamentos bibliográficos, a identificação e remoção de registros duplicados é uma etapa crucial do processo de seleção de estudos. Registros duplicados podem ocorrer devido a exportações múltiplas, indexações diferentes da mesma publicação, ou versões preliminares e finais de um mesmo trabalho.

Este documento descreve o processo de análise de duplicatas realizado em uma base de dados exportada da plataforma Scopus, contendo artigos científicos relacionados ao tema de pesquisa.

## 2. Metodologia

### 2.1. Base de Dados Analisada

- **Fonte:** Scopus (Elsevier)
- **Arquivo:** `export_8f77fb33-532c-470c-9e41-4482d02a30ec_2025-10-05T231503.385218.csv`
- **Total de registros:** 238 artigos científicos
- **Formato:** CSV (Comma-Separated Values)
- **Campos principais:** Authors, Title, Year, DOI, Source title, Abstract, Keywords

### 2.2. Ferramentas Utilizadas

A análise foi realizada utilizando:
- **Linguagem de Programação:** Python 3
- **Biblioteca Principal:** Pandas (para manipulação e análise de dados)
- **Ambiente:** Virtual environment (venv) isolado para gerenciamento de dependências

### 2.3. Critérios de Identificação de Duplicatas

A análise de duplicatas foi realizada em duas etapas distintas, utilizando diferentes critérios:

#### 2.3.1. Análise por DOI (Digital Object Identifier)

O DOI é um identificador único e persistente atribuído a publicações acadêmicas. A identificação de duplicatas por DOI é considerada o método mais confiável, pois:
- Cada publicação deveria ter apenas um DOI único
- DOIs idênticos indicam que se trata exatamente do mesmo documento
- É independente de variações em títulos, nomes de autores ou metadados

**Processo:**
1. Filtragem dos registros com DOI válido (não nulo)
2. Identificação de DOIs que aparecem mais de uma vez na base
3. Agrupamento e contabilização das ocorrências

#### 2.3.2. Análise por Título

A identificação por título complementa a análise por DOI, capturando possíveis duplicatas que:
- Não possuem DOI cadastrado
- Possuem DOIs diferentes mas são a mesma publicação (raro, mas possível)
- Representam versões diferentes indexadas separadamente

**Processo:**
1. Normalização dos títulos (conversão para minúsculas e remoção de espaços extras)
2. Comparação exata entre títulos normalizados
3. Identificação de títulos que aparecem múltiplas vezes

### 2.4. Implementação Técnica

Foi desenvolvido um script Python (`analise_duplicatas.py`) que:
- Lê o arquivo CSV exportado da Scopus
- Realiza validação dos dados (identificação de campos nulos)
- Aplica os critérios de detecção de duplicatas
- Gera relatórios detalhados com estatísticas
- Exporta os resultados tanto no terminal quanto em arquivo TXT

## 3. Resultados

### 3.1. Estatísticas Gerais

- **Total de registros analisados:** 238
- **Registros com DOI válido:** 218 (91,6%)
- **Registros sem DOI:** 20 (8,4%)
- **Registros com Título válido:** 238 (100%)

### 3.2. Duplicatas Identificadas por DOI

**Resultados:**
- **Registros duplicados:** 2
- **DOIs únicos com duplicatas:** 1
- **Taxa de duplicação:** 0,92%

**Caso identificado:**
- DOI: `10.1109/ICORR58425.2023.10304712`
- Título: "Does the Level of Focus in Serious Games in Immersive VR Correlate with the Quality of Movement?"
- Ano: 2023
- Aparições: 2 vezes

### 3.3. Duplicatas Identificadas por Título

**Resultados:**
- **Registros duplicados:** 6
- **Títulos únicos com duplicatas:** 3
- **Taxa de duplicação:** 2,52%

**Casos identificados:**

1. **"An overview on the use of serious games in physical therapy and rehabilitation"**
   - Aparições: 2 vezes
   - DOIs diferentes: `10.4018/978-1-4666-4422-9.ch038` (2013) e `10.4018/978-1-4666-0149-9.ch061` (2012)
   - Observação: Provável republicação ou capítulo duplicado em livros diferentes

2. **"Does the Level of Focus in Serious Games in Immersive VR Correlate with the Quality of Movement?"**
   - Aparições: 2 vezes
   - Mesmo DOI: `10.1109/ICORR58425.2023.10304712`
   - Observação: Duplicata confirmada (detectada também na análise por DOI)

3. **"Using instructional games: A teaching strategy for increasing student participation and retention"**
   - Aparições: 2 vezes
   - DOI: `10.1300/J003v15n01_03` (2001) e um registro sem DOI (2012)
   - Observação: Possível reedição ou republicação

### 3.4. Duplicatas Comuns (DOI e Título)

**Registros duplicados tanto por DOI quanto por Título:** 2

Este resultado confirma que há uma duplicata "verdadeira" no banco de dados, onde o mesmo artigo foi indexado/exportado duas vezes com o mesmo DOI e título.

## 4. Discussão

### 4.1. Qualidade da Base de Dados

A base de dados apresenta uma taxa de duplicação relativamente baixa:
- 0,92% de duplicação por DOI
- 2,52% de duplicação por título

Estes valores indicam uma boa qualidade da exportação da Scopus, com poucos registros genuinamente duplicados.

### 4.2. Tipos de Duplicatas Encontradas

Foram identificados três tipos de situações:

1. **Duplicatas verdadeiras:** Mesmo artigo exportado duas vezes (1 caso)
2. **Republicações legítimas:** Mesmo trabalho publicado em diferentes contextos com DOIs diferentes (2 casos)
3. **Versões diferentes:** Artigos com títulos idênticos mas anos e DOIs diferentes

### 4.3. Recomendações para Tratamento

Para a continuidade da pesquisa, recomenda-se:

1. **Remoção da duplicata verdadeira** (DOI `10.1109/ICORR58425.2023.10304712`)
2. **Análise manual dos casos de republicação** para decidir se devem ser:
   - Considerados como estudos independentes
   - Mantido apenas um registro (o mais completo ou mais recente)
3. **Registro da 8,4% de artigos sem DOI** para verificação manual, pois podem conter duplicatas não detectadas

## 5. Conclusão

A análise automatizada de duplicatas permitiu identificar de forma sistemática e reproduzível os registros duplicados na base de dados exportada da Scopus. O processo revelou uma taxa baixa de duplicação (0,92% por DOI e 2,52% por título), indicando boa qualidade dos dados.

A metodologia empregada, utilizando Python e Pandas, mostrou-se eficiente e escalável, podendo ser aplicada em bases de dados de qualquer tamanho. A dupla verificação (por DOI e por título) fornece maior confiabilidade na identificação de duplicatas, capturando tanto duplicatas exatas quanto possíveis republicações.

Os resultados desta análise fundamentam as próximas etapas da revisão sistemática, garantindo que apenas registros únicos sejam considerados nas análises subsequentes.

---

## Apêndice A: Script Desenvolvido

O script completo está disponível em: `analise_duplicatas.py`

### Principais Funcionalidades:
- Leitura e validação de arquivos CSV da Scopus
- Detecção automática de duplicatas por DOI
- Detecção automática de duplicatas por título (com normalização)
- Geração de relatórios detalhados
- Exportação de resultados em formato TXT
- Cálculo de estatísticas e taxas de duplicação

### Exemplo de Uso:
```bash
# Ativar ambiente virtual
source venv/bin/activate

# Executar análise
python analise_duplicatas.py

# Resultado gerado automaticamente em:
# analise_duplicatas_resultado_[timestamp].txt
```

---

**Data da análise:** 05 de outubro de 2025  
**Arquivo de resultado:** `analise_duplicatas_resultado_20251005_233345.txt`

