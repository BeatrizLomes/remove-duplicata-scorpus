# Análise de Duplicatas em Base Bibliográfica Scopus

## 📋 Descrição

Projeto de análise de dados bibliográficos exportados da base Scopus, com foco na identificação e tratamento de registros duplicados para revisão sistemática da literatura.

## 🎯 Objetivos

- Identificar duplicatas por DOI (Digital Object Identifier)
- Identificar duplicatas por título de artigo
- Gerar relatórios detalhados com estatísticas
- Fornecer base para decisões de limpeza de dados

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Pandas** - Manipulação e análise de dados
- **Virtual Environment (venv)** - Isolamento de dependências

## 📁 Estrutura do Projeto

```
tcc/
├── analise_duplicatas.py                           # Script de análise de duplicatas
├── remover_duplicatas.py                           # Script de remoção de duplicatas
├── export_8f77fb33-*.csv                          # Arquivo original da Scopus (238 registros)
├── export_scopus_sem_duplicatas_*.csv             # Arquivo limpo sem duplicatas (235 registros)
├── analise_duplicatas_resultado_*.txt             # Resultados da análise
├── documentacao_analise_duplicatas.md             # Documentação completa
├── resumo_analise_duplicatas.md                   # Resumo executivo
├── .gitignore                                     # Arquivos ignorados pelo Git
├── README.md                                      # Este arquivo
└── venv/                                          # Ambiente virtual (não versionado)
```

## 🚀 Como Usar

### 1. Clonar o repositório
```bash
git clone <url-do-repositorio>
cd tcc
```

### 2. Criar e ativar ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 3. Instalar dependências
```bash
pip install pandas
```

### 4. Executar a análise de duplicatas
```bash
python analise_duplicatas.py
```

### 5. Visualizar resultados
Os resultados serão exibidos no terminal e salvos automaticamente em:
```
analise_duplicatas_resultado_[timestamp].txt
```

### 6. Remover duplicatas (opcional)
Para gerar um CSV limpo sem duplicatas:
```bash
python remover_duplicatas.py
```
Será gerado o arquivo:
```
export_scopus_sem_duplicatas_[timestamp].csv
```

## 📊 Resultados

### Análise de Duplicatas
- **238 registros** no arquivo original
- **0,92%** de duplicação por DOI (2 registros)
- **2,52%** de duplicação por título (6 registros)
- **1 duplicata verdadeira** identificada
- **2 casos** de possíveis republicações

### Arquivo Limpo
- **235 registros** após remoção de duplicatas
- **3 registros** removidos (duplicatas por título)
- **Taxa de remoção:** 1,26%

### Documentação
Para mais detalhes, consulte:
- `documentacao_analise_duplicatas.md` - Análise completa
- `resumo_analise_duplicatas.md` - Resumo executivo
- `analise_duplicatas_resultado_*.txt` - Resultados da execução

## 📝 Funcionalidades

### Script de Análise (`analise_duplicatas.py`)
- ✅ Leitura de arquivos CSV da Scopus
- ✅ Validação de dados (campos nulos)
- ✅ Detecção de duplicatas por DOI
- ✅ Detecção de duplicatas por título (com normalização)
- ✅ Geração de relatórios detalhados
- ✅ Exportação de resultados em TXT
- ✅ Cálculo de estatísticas e taxas
- ✅ Saída dual (terminal + arquivo)

### Script de Remoção (`remover_duplicatas.py`)
- ✅ Identificação de duplicatas por título
- ✅ Remoção automática de duplicatas (mantém primeira ocorrência)
- ✅ Geração de CSV limpo
- ✅ Relatório detalhado dos registros removidos
- ✅ Preservação do arquivo original

## 🔄 Fluxo de Trabalho Recomendado

1. **Análise:** Execute `analise_duplicatas.py` para identificar duplicatas
2. **Revisão:** Analise o relatório gerado em `analise_duplicatas_resultado_*.txt`
3. **Limpeza:** Execute `remover_duplicatas.py` para gerar CSV sem duplicatas
4. **Uso:** Utilize o arquivo `export_scopus_sem_duplicatas_*.csv` para as análises seguintes

## 🔍 Metodologia

### Análise por DOI
- Identifica registros com DOI idêntico
- Método mais confiável de detecção

### Análise por Título
- Normalização: minúsculas + remoção de espaços
- Comparação exata após normalização
- Captura casos sem DOI

### Remoção de Duplicatas
- Remove duplicatas por título normalizado
- Mantém a **primeira ocorrência** de cada título
- Preserva o arquivo original intacto

## 📚 Documentação

- **Completa**: `documentacao_analise_duplicatas.md`
- **Resumida**: `resumo_analise_duplicatas.md`
- **Resultados**: `analise_duplicatas_resultado_*.txt`

## 👤 Autor

Projeto desenvolvido para TCC

## 📅 Data

Outubro de 2025

## 📄 Licença

Este projeto é parte de um Trabalho de Conclusão de Curso (TCC).

