#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise de Duplicatas em Arquivo CSV da Scopus
Este script identifica e exibe duplicatas por DOI e por Título
"""

import pandas as pd
import os
import sys
from datetime import datetime

# ==============================================================================
# CONFIGURAÇÃO DE SAÍDA DUAL (Terminal + Arquivo)
# ==============================================================================
class DualOutput:
    """Classe para escrever simultaneamente no terminal e em arquivo"""
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, 'w', encoding='utf-8')
    
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    
    def flush(self):
        self.terminal.flush()
        self.log.flush()
    
    def close(self):
        self.log.close()

# Criar arquivo de saída com timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"analise_duplicatas_resultado_{timestamp}.txt"
sys.stdout = DualOutput(output_file)

# ==============================================================================
# 1. LEITURA DO ARQUIVO CSV
# ==============================================================================
print("="*80)
print("ANÁLISE DE DUPLICATAS - ARQUIVO SCOPUS")
print("="*80)
print()

# Nome do arquivo CSV
csv_file = "export_8f77fb33-532c-470c-9e41-4482d02a30ec_2025-10-05T231503.385218.csv"

# Verificar se o arquivo existe
if not os.path.exists(csv_file):
    print(f"ERRO: Arquivo '{csv_file}' não encontrado!")
    exit(1)

# Ler o arquivo CSV
print(f"📄 Lendo arquivo: {csv_file}")
df = pd.read_csv(csv_file)
print(f"✅ Arquivo carregado com sucesso!")
print(f"   Total de registros: {len(df)}")
print(f"   Colunas encontradas: {list(df.columns)}")
print()

# ==============================================================================
# 2. ANÁLISE DE DUPLICATAS POR DOI
# ==============================================================================
print("="*80)
print("ANÁLISE 1: DUPLICATAS POR DOI")
print("="*80)
print()

# Remover valores nulos de DOI para análise
df_doi_valido = df[df['DOI'].notna()].copy()
print(f"📊 Registros com DOI válido: {len(df_doi_valido)}")
print(f"📊 Registros sem DOI: {len(df) - len(df_doi_valido)}")
print()

# Identificar DOIs duplicados
# Considera duplicado quando um DOI aparece mais de 1 vez
duplicados_doi = df_doi_valido[df_doi_valido.duplicated(subset=['DOI'], keep=False)]

if len(duplicados_doi) > 0:
    # Ordenar por DOI para facilitar visualização
    duplicados_doi = duplicados_doi.sort_values('DOI')
    
    print(f"⚠️  DUPLICATAS ENCONTRADAS: {len(duplicados_doi)} registros duplicados")
    print(f"   Número de DOIs únicos duplicados: {duplicados_doi['DOI'].nunique()}")
    print()
    
    # Exibir tabela com as colunas mais importantes
    print("📋 Tabela de Duplicatas por DOI:")
    print("-" * 80)
    
    # Selecionar colunas relevantes
    colunas_exibir = ['DOI', 'Title', 'Authors', 'Year']
    tabela_doi = duplicados_doi[colunas_exibir].copy()
    
    # Truncar títulos longos para melhor visualização
    tabela_doi['Title'] = tabela_doi['Title'].apply(
        lambda x: (x[:80] + '...') if isinstance(x, str) and len(x) > 80 else x
    )
    
    # Truncar autores longos
    tabela_doi['Authors'] = tabela_doi['Authors'].apply(
        lambda x: (x[:50] + '...') if isinstance(x, str) and len(x) > 50 else x
    )
    
    # Configurar pandas para exibir todas as linhas e colunas
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    
    print(tabela_doi.to_string(index=False))
    print()
    
    # Estatísticas detalhadas por DOI duplicado
    print("📊 Detalhamento dos DOIs duplicados:")
    print("-" * 80)
    contagem_doi = duplicados_doi['DOI'].value_counts()
    for doi, count in contagem_doi.items():
        print(f"   DOI: {doi}")
        print(f"   Aparece {count} vezes")
        print()
else:
    print("✅ Nenhuma duplicata encontrada por DOI!")
    print()

# ==============================================================================
# 3. ANÁLISE DE DUPLICATAS POR TÍTULO
# ==============================================================================
print("="*80)
print("ANÁLISE 2: DUPLICATAS POR TÍTULO")
print("="*80)
print()

# Remover valores nulos de Title para análise
df_title_valido = df[df['Title'].notna()].copy()
print(f"📊 Registros com Título válido: {len(df_title_valido)}")
print(f"📊 Registros sem Título: {len(df) - len(df_title_valido)}")
print()

# Normalizar títulos para melhor comparação (remover espaços extras, converter para minúsculas)
df_title_valido['Title_Normalizado'] = df_title_valido['Title'].str.strip().str.lower()

# Identificar títulos duplicados
duplicados_title = df_title_valido[df_title_valido.duplicated(subset=['Title_Normalizado'], keep=False)]

if len(duplicados_title) > 0:
    # Ordenar por título normalizado para facilitar visualização
    duplicados_title = duplicados_title.sort_values('Title_Normalizado')
    
    print(f"⚠️  DUPLICATAS ENCONTRADAS: {len(duplicados_title)} registros duplicados")
    print(f"   Número de Títulos únicos duplicados: {duplicados_title['Title_Normalizado'].nunique()}")
    print()
    
    # Exibir tabela com as colunas mais importantes
    print("📋 Tabela de Duplicatas por Título:")
    print("-" * 80)
    
    # Selecionar colunas relevantes (usando o título original, não o normalizado)
    colunas_exibir = ['DOI', 'Title', 'Authors', 'Year']
    tabela_title = duplicados_title[colunas_exibir].copy()
    
    # Truncar títulos longos para melhor visualização
    tabela_title['Title'] = tabela_title['Title'].apply(
        lambda x: (x[:80] + '...') if isinstance(x, str) and len(x) > 80 else x
    )
    
    # Truncar autores longos
    tabela_title['Authors'] = tabela_title['Authors'].apply(
        lambda x: (x[:50] + '...') if isinstance(x, str) and len(x) > 50 else x
    )
    
    print(tabela_title.to_string(index=False))
    print()
    
    # Estatísticas detalhadas por título duplicado
    print("📊 Detalhamento dos Títulos duplicados:")
    print("-" * 80)
    # Criar um mapeamento do título normalizado para o original
    titulo_map = duplicados_title.groupby('Title_Normalizado')['Title'].first()
    contagem_title = duplicados_title['Title_Normalizado'].value_counts()
    
    for title_norm, count in contagem_title.items():
        titulo_original = titulo_map[title_norm]
        # Truncar título se muito longo
        titulo_exibir = (titulo_original[:100] + '...') if len(titulo_original) > 100 else titulo_original
        print(f"   Título: {titulo_exibir}")
        print(f"   Aparece {count} vezes")
        print()
else:
    print("✅ Nenhuma duplicata encontrada por Título!")
    print()

# ==============================================================================
# 4. RESUMO FINAL
# ==============================================================================
print("="*80)
print("RESUMO FINAL DA ANÁLISE")
print("="*80)
print()

print(f"📊 ESTATÍSTICAS GERAIS:")
print(f"   Total de registros no arquivo: {len(df)}")
print(f"   Registros com DOI válido: {len(df_doi_valido)}")
print(f"   Registros com Título válido: {len(df_title_valido)}")
print()

print(f"🔍 DUPLICATAS POR DOI:")
if len(duplicados_doi) > 0:
    print(f"   ⚠️  {len(duplicados_doi)} registros duplicados encontrados")
    print(f"   ⚠️  {duplicados_doi['DOI'].nunique()} DOIs únicos com duplicatas")
    print(f"   📈 Taxa de duplicação: {(len(duplicados_doi) / len(df_doi_valido) * 100):.2f}%")
else:
    print(f"   ✅ Nenhuma duplicata encontrada")
print()

print(f"🔍 DUPLICATAS POR TÍTULO:")
if len(duplicados_title) > 0:
    print(f"   ⚠️  {len(duplicados_title)} registros duplicados encontrados")
    print(f"   ⚠️  {duplicados_title['Title_Normalizado'].nunique()} Títulos únicos com duplicatas")
    print(f"   📈 Taxa de duplicação: {(len(duplicados_title) / len(df_title_valido) * 100):.2f}%")
else:
    print(f"   ✅ Nenhuma duplicata encontrada")
print()

# Verificar se há registros duplicados TANTO por DOI quanto por Título
if len(duplicados_doi) > 0 and len(duplicados_title) > 0:
    # Encontrar interseção
    indices_doi = set(duplicados_doi.index)
    indices_title = set(duplicados_title.index)
    intersecao = indices_doi.intersection(indices_title)
    
    print(f"🔗 DUPLICATAS COMUNS (DOI E TÍTULO):")
    print(f"   {len(intersecao)} registros são duplicados tanto por DOI quanto por Título")
    print()

print("="*80)
print("FIM DA ANÁLISE")
print("="*80)
print()
print(f"💾 Resultado salvo em: {output_file}")

# Fechar o arquivo de log
sys.stdout.close()
sys.stdout = sys.stdout.terminal  # Restaurar stdout original

