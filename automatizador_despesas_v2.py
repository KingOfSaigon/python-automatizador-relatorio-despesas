# automatizador_despesas_v2.py

import pandas as pd
import re
# Importa o dicionário do nosso arquivo de configuração externo.
from config_categorias import DICIONARIO_CATEGORIAS

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
    # Garante que a descrição seja uma string antes de usar métodos de string
    if not isinstance(descricao, str):
        return CATEGORIA_PADRAO

    descricao_upper = descricao.upper()
    melhor_categoria_encontrada = CATEGORIA_PADRAO
    maior_prioridade = 999

    for palavra_chave, info in DICIONARIO_CATEGORIAS.items():
        # re.escape() lida com caracteres especiais na palavra-chave (ex: DISNEY+)
        # \b garante que estamos procurando por uma "palavra inteira".
        padrao = r'\b' + re.escape(palavra_chave.upper()) + r'\b'
        
        if re.search(padrao, descricao_upper):
            if info['prioridade'] < maior_prioridade:
                maior_prioridade = info['prioridade']
                melhor_categoria_encontrada = info['categoria']
    
    return melhor_categoria_encontrada

# --- LÓGICA PRINCIPAL DO SCRIPT ---

# Garante que o script só rode quando executado diretamente
if __name__ == "__main__":
    # 1. Carregar os dados do .csv
    print(f"Lendo o arquivo de entrada: {ARQUIVO_ENTRADA}...")
    try:
        df = pd.read_csv(ARQUIVO_ENTRADA)
    except FileNotFoundError:
        print(f"ERRO: O arquivo '{ARQUIVO_ENTRADA}' não foi encontrado. Verifique se ele está na mesma pasta do script.")
        exit() # Encerra o script se o arquivo não for encontrado

    # 2. Aplicar a função de categorização aprimorada
    print("Categorizando despesas com a lógica de prioridades e Regex...")
    df['Categoria'] = df['Descricao'].apply(categorizar_despesa_regex)

    # 3. IMPLEMENTANDO O FEEDBACK LOOP
    print("\n--- Verificando despesas não categorizadas ---")
    despesas_outros = df[df['Categoria'] == CATEGORIA_PADRAO]

    if despesas_outros.empty:
        print("Ótimo! Todas as despesas foram categorizadas com sucesso.")
    else:
        print(f"AVISO: {len(despesas_outros)} despesa(s) não categorizada(s) encontrada(s):")
        for index, row in despesas_outros.iterrows():
            print(f"  - Descrição: '{row['Descricao']}'")
    print("---------------------------------------------\n")

    # 4. Calcular o total gasto por categoria
    print("Calculando totais por categoria...")
    resumo_por_categoria = df.groupby('Categoria')['Valor'].sum().reset_index()

    # 5. Gerar o relatório final em Excel com o gráfico
    print(f"Gerando o relatório final: {ARQUIVO_SAIDA}...")
    try:
        with pd.ExcelWriter(ARQUIVO_SAIDA, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Detalhes', index=False)
            resumo_por_categoria.to_excel(writer, sheet_name='Resumo', index=False)

            workbook = writer.book
            worksheet = writer.sheets['Resumo']
            
            # Garante que há dados para plotar o gráfico
            if not resumo_por_categoria.empty:
                chart = pd.io.excel.ExcelChart(chart_type='pie')
                labels = pd.io.excel.ExcelChartReference(worksheet, range_string=f'Resumo!$A$2:$A${len(resumo_por_categoria)+1}')
                data = pd.io.excel.ExcelChartReference(worksheet, range_string=f'Resumo!$B$2:$B${len(resumo_por_categoria)+1}')
                
                chart.add_series(data, title_from_data=True, labels=labels)
                chart.title = 'Gastos por Categoria'
                
                worksheet.add_chart(chart, 'D2')

        print(f"Relatório final gerado com sucesso em '{ARQUIVO_SAIDA}'!")
    
    except Exception as e:
        print(f"ERRO: Não foi possível gerar o arquivo Excel. Motivo: {e}")