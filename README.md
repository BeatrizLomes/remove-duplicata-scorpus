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
├── analise_duplicatas.py                    # Script principal de análise
├── export_*.csv                             # Arquivo exportado da Scopus
├── analise_duplicatas_resultado_*.txt       # Resultados da análise
├── documentacao_analise_duplicatas.md       # Documentação completa
├── resumo_analise_duplicatas.md            # Resumo executivo
├── .gitignore                              # Arquivos ignorados pelo Git
├── README.md                               # Este arquivo
└── venv/                                   # Ambiente virtual (não versionado)
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

### 4. Executar a análise
```bash
python analise_duplicatas.py
```

### 5. Visualizar resultados
Os resultados serão exibidos no terminal e salvos automaticamente em:
```
analise_duplicatas_resultado_[timestamp].txt
```

## 📊 Resultados

### Estatísticas Gerais
- **238 registros** analisados
- **0,92%** de duplicação por DOI
- **2,52%** de duplicação por título
- **1 duplicata verdadeira** identificada
- **2 casos** de possíveis republicações

Para mais detalhes, consulte:
- `documentacao_analise_duplicatas.md` - Análise completa
- `resumo_analise_duplicatas.md` - Resumo executivo

## 📝 Funcionalidades do Script

- ✅ Leitura de arquivos CSV da Scopus
- ✅ Validação de dados (campos nulos)
- ✅ Detecção de duplicatas por DOI
- ✅ Detecção de duplicatas por título (com normalização)
- ✅ Geração de relatórios detalhados
- ✅ Exportação de resultados em TXT
- ✅ Cálculo de estatísticas e taxas
- ✅ Saída dual (terminal + arquivo)

## 🔍 Metodologia

### Análise por DOI
- Identifica registros com DOI idêntico
- Método mais confiável de detecção

### Análise por Título
- Normalização: minúsculas + remoção de espaços
- Comparação exata após normalização
- Captura casos sem DOI

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

