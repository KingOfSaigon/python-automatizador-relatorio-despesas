# automatizador_despesas_v2.py

import pandas as pd
import re
# Importa o dicionário do nosso arquivo de configuração externo.
from config_categorias import DICIONARIO_CATEGORIAS
# Importa as classes necessárias para criar o gráfico.
from openpyxl.chart import PieChart, Reference


# --- CONFIGURAÇÕES ---
ARQUIVO_ENTRADA = 'extrato.csv'
ARQUIVO_SAIDA = 'resumo_despesas_final.xlsx'
CATEGORIA_PADRAO = 'Outros'

# --- FUNÇÕES ---

def categorizar_despesa_regex(descricao):
    """
    Categoriza uma despesa usando Regex para garantir a correspondência de palavras inteiras.
    Busca todas as palavras-chave na descrição e retorna a categoria
    da palavra-chave com a maior prioridade (menor número).
    """
    if not isinstance(descricao, str):
        return CATEGORIA_PADRAO

    descricao_upper = descricao.upper()
    melhor_categoria_encontrada = CATEGORIA_PADRAO
    maior_prioridade = 999

    for palavra_chave, info in DICIONARIO_CATEGORIAS.items():
        padrao = r'\b' + re.escape(palavra_chave.upper()) + r'\b'
        
        if re.search(padrao, descricao_upper):
            if info['prioridade'] < maior_prioridade:
                maior_prioridade = info['prioridade']
                melhor_categoria_encontrada = info['categoria']
    
    return melhor_categoria_encontrada

# --- LÓGICA PRINCIPAL DO SCRIPT ---

# Garante que o script só rode quando executado diretamente
if __name__ == "__main__":
    print(f"Lendo o arquivo de entrada: {ARQUIVO_ENTRADA}...")
    try:
        df = pd.read_csv(ARQUIVO_ENTRADA)
    except FileNotFoundError:
        print(f"ERRO: O arquivo '{ARQUIVO_ENTRADA}' não foi encontrado. Verifique se ele está na mesma pasta do script.")
        exit()

    print("Categorizando despesas com a lógica de prioridades e Regex...")
    df['Categoria'] = df['Descricao'].apply(categorizar_despesa_regex)

    print("\n--- Verificando despesas não categorizadas ---")
    despesas_outros = df[df['Categoria'] == CATEGORIA_PADRAO]

    if despesas_outros.empty:
        print("Ótimo! Todas as despesas foram categorizadas com sucesso.")
    else:
        print(f"AVISO: {len(despesas_outros)} despesa(s) não categorizada(s) encontrada(s):")
        for index, row in despesas_outros.iterrows():
            print(f"  - Descrição: '{row['Descricao']}'")
    print("---------------------------------------------\n")

    print("Calculando totais por categoria...")
    resumo_por_categoria = df.groupby('Categoria')['Valor'].sum().reset_index()

    print(f"Gerando o relatório final: {ARQUIVO_SAIDA}...")
    try:
        with pd.ExcelWriter(ARQUIVO_SAIDA, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Detalhes', index=False)
            resumo_por_categoria.to_excel(writer, sheet_name='Resumo', index=False)

            # --- Bloco CORRIGIDO para criar o gráfico ---
            workbook = writer.book
            worksheet = writer.sheets['Resumo']

            if not resumo_por_categoria.empty:
                chart = PieChart()
                
                labels = Reference(worksheet, min_col=1, min_row=2, max_row=len(resumo_por_categoria) + 1)
                data = Reference(worksheet, min_col=2, min_row=2, max_row=len(resumo_por_categoria) + 1)
                
                chart.add_data(data, titles_from_data=True)
                chart.set_categories(labels)
                chart.title = "Gastos por Categoria"
                
                worksheet.add_chart(chart, "D2")

        print(f"\nRelatório final gerado com sucesso em '{ARQUIVO_SAIDA}'!")
    
    except Exception as e:
        print(f"ERRO: Não foi possível gerar o arquivo Excel. Motivo: {e}")
