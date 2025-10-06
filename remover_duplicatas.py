#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para Remover Duplicatas do CSV da Scopus
Remove registros duplicados por título, mantendo apenas a primeira ocorrência
"""

import pandas as pd
import os
from datetime import datetime

print("="*80)
print("REMOÇÃO DE DUPLICATAS - ARQUIVO SCOPUS")
print("="*80)
print()

# ==============================================================================
# 1. LEITURA DO ARQUIVO ORIGINAL
# ==============================================================================
csv_original = "export_8f77fb33-532c-470c-9e41-4482d02a30ec_2025-10-05T231503.385218.csv"

if not os.path.exists(csv_original):
    print(f"ERRO: Arquivo '{csv_original}' não encontrado!")
    exit(1)

print(f"📄 Lendo arquivo original: {csv_original}")
df_original = pd.read_csv(csv_original)
total_original = len(df_original)
print(f"✅ Arquivo carregado!")
print(f"   Total de registros originais: {total_original}")
print()

# ==============================================================================
# 2. IDENTIFICAR DUPLICATAS POR TÍTULO
# ==============================================================================
print("🔍 Identificando duplicatas por título...")
print()

# Criar coluna com título normalizado
df_original['Title_Normalizado'] = df_original['Title'].str.strip().str.lower()

# Identificar duplicatas (mantendo apenas a primeira ocorrência)
duplicados = df_original[df_original.duplicated(subset=['Title_Normalizado'], keep='first')]

print(f"📊 Duplicatas identificadas:")
print(f"   Registros duplicados encontrados: {len(duplicados)}")
print(f"   Títulos únicos duplicados: {duplicados['Title_Normalizado'].nunique()}")
print()

# Mostrar quais registros serão removidos
if len(duplicados) > 0:
    print("⚠️  Registros que serão REMOVIDOS:")
    print("-" * 80)
    for idx, row in duplicados.iterrows():
        titulo = row['Title']
        if isinstance(titulo, str) and len(titulo) > 80:
            titulo = titulo[:80] + "..."
        print(f"   - [{idx}] {titulo}")
        print(f"     DOI: {row['DOI']}, Ano: {row['Year']}")
    print()

# ==============================================================================
# 3. REMOVER DUPLICATAS
# ==============================================================================
print("🗑️  Removendo duplicatas...")

# Remover duplicatas mantendo a primeira ocorrência
df_limpo = df_original.drop_duplicates(subset=['Title_Normalizado'], keep='first')

# Remover a coluna auxiliar de título normalizado
df_limpo = df_limpo.drop(columns=['Title_Normalizado'])

total_limpo = len(df_limpo)
removidos = total_original - total_limpo

print(f"✅ Duplicatas removidas!")
print(f"   Registros originais: {total_original}")
print(f"   Registros removidos: {removidos}")
print(f"   Registros no arquivo limpo: {total_limpo}")
print()

# ==============================================================================
# 4. SALVAR ARQUIVO LIMPO
# ==============================================================================
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
csv_limpo = f"export_scopus_sem_duplicatas_{timestamp}.csv"

print(f"💾 Salvando arquivo limpo...")
df_limpo.to_csv(csv_limpo, index=False)
print(f"✅ Arquivo salvo: {csv_limpo}")
print()

# ==============================================================================
# 5. ESTATÍSTICAS FINAIS
# ==============================================================================
print("="*80)
print("RESUMO DA LIMPEZA")
print("="*80)
print()
print(f"📊 ANTES:")
print(f"   Total de registros: {total_original}")
print()
print(f"📊 DEPOIS:")
print(f"   Total de registros: {total_limpo}")
print(f"   Registros removidos: {removidos}")
print(f"   Taxa de remoção: {(removidos / total_original * 100):.2f}%")
print()
print(f"📁 ARQUIVOS:")
print(f"   Original: {csv_original}")
print(f"   Limpo: {csv_limpo}")
print()
print("="*80)
print("LIMPEZA CONCLUÍDA COM SUCESSO!")
print("="*80)

