# config_categorias.py

# ==============================================================================
# DICIONÁRIO DE CATEGORIAS COM PRIORIDADES
# Este arquivo serve como a base de conhecimento para a categorização.
# Prioridade 1: Marcas e nomes de lojas (mais específico)
# Prioridade 2: Serviços ou tipos de loja bem definidos
# Prioridade 3: Termos genéricos (menos específico)
# ==============================================================================
DICIONARIO_CATEGORIAS = {
    # --- Alimentação: Restaurantes e Lanches ---
    'IFOOD':           {'categoria': 'Restaurantes e Lanches', 'prioridade': 1},
    'RAPPI':           {'categoria': 'Restaurantes e Lanches', 'prioridade': 1},
    'UBER EATS':       {'categoria': 'Restaurantes e Lanches', 'prioridade': 1},
    'MCDONALDS':       {'categoria': 'Restaurantes e Lanches', 'prioridade': 1},
    'BURGER KING':     {'categoria': 'Restaurantes e Lanches', 'prioridade': 1},
    'OUTBACK':         {'categoria': 'Restaurantes e Lanches', 'prioridade': 1},
    'RESTAURANTE':     {'categoria': 'Restaurantes e Lanches', 'prioridade': 3},
    'LANCHONETE':      {'categoria': 'Restaurantes e Lanches', 'prioridade': 3},
    'PADARIA':         {'categoria': 'Restaurantes e Lanches', 'prioridade': 2},

    # --- Alimentação: Supermercado e Mercearia ---
    'PAO DE ACUCAR':   {'categoria': 'Supermercado e Mercearia', 'prioridade': 1},
    'CARREFOUR':       {'categoria': 'Supermercado e Mercearia', 'prioridade': 1},
    'BIG BOMPRECO':    {'categoria': 'Supermercado e Mercearia', 'prioridade': 1},
    'SUPERMERCADO':    {'categoria': 'Supermercado e Mercearia', 'prioridade': 3},
    'MERCADO':         {'categoria': 'Supermercado e Mercearia', 'prioridade': 3},

    # --- Transporte ---
    'UBER':            {'categoria': 'Transporte', 'prioridade': 1},
    '99POP':           {'categoria': 'Transporte', 'prioridade': 1},
    'COMBUSTIVEL':     {'categoria': 'Transporte', 'prioridade': 2},
    'ESTACIONAMENTO':  {'categoria': 'Transporte', 'prioridade': 2},
    'PEDAGIO':         {'categoria': 'Transporte', 'prioridade': 2},
    'TRANSPORTE':      {'categoria': 'Transporte', 'prioridade': 3},

    # --- Viagens ---
    'GOL LINHAS':      {'categoria': 'Viagens', 'prioridade': 1},
    'LATAM':           {'categoria': 'Viagens', 'prioridade': 1},
    'DECOLAR':         {'categoria': 'Viagens', 'prioridade': 1},
    'BOOKING.COM':     {'categoria': 'Viagens', 'prioridade': 1},
    'AIRBNB':          {'categoria': 'Viagens', 'prioridade': 1},
    'HOTEL':           {'categoria': 'Viagens', 'prioridade': 2},
    'VIAGEM':          {'categoria': 'Viagens', 'prioridade': 3},

    # --- Moradia e Contas ---
    'VIVO':            {'categoria': 'Moradia e Contas', 'prioridade': 1},
    'TIM':             {'categoria': 'Moradia e Contas', 'prioridade': 1},
    'CLARO':           {'categoria': 'Moradia e Contas', 'prioridade': 1},
    'NETFLIX':         {'categoria': 'Moradia e Contas', 'prioridade': 1},
    'SPOTIFY':         {'categoria': 'Moradia e Contas', 'prioridade': 1},
    'HBO MAX':         {'categoria': 'Moradia e Contas', 'prioridade': 1},
    'ALUGUEL':         {'categoria': 'Moradia e Contas', 'prioridade': 2},
    'CONDOMINIO':      {'categoria': 'Moradia e Contas', 'prioridade': 2},

    # --- Saúde ---
    'FARMACIA PACHECO': {'categoria': 'Saúde', 'prioridade': 1},
    'DROGASIL':        {'categoria': 'Saúde', 'prioridade': 1},
    'PAGUE MENOS':     {'categoria': 'Saúde', 'prioridade': 1},
    'FARMACIA':        {'categoria': 'Saúde', 'prioridade': 2},
    'HOSPITAL':        {'categoria': 'Saúde', 'prioridade': 2},
    'PLANO DE SAUDE':  {'categoria': 'Saúde', 'prioridade': 2},

    # --- Compras e Vestuário ---
    'LOJAS RENNER':    {'categoria': 'Compras e Vestuário', 'prioridade': 1},
    'AMAZON':          {'categoria': 'Compras e Vestuário', 'prioridade': 1},
    'MERCADO LIVRE':   {'categoria': 'Compras e Vestuário', 'prioridade': 1},
    'ALIEXPRESS':      {'categoria': 'Compras e Vestuário', 'prioridade': 1},
    'SHOPEE':          {'categoria': 'Compras e Vestuário', 'prioridade': 1},
    'COMPRA':          {'categoria': 'Compras e Vestuário', 'prioridade': 3},

    # --- Outros ---
    'PAGAMENTO':       {'categoria': 'Outros', 'prioridade': 2},
    'LOTERICA':        {'categoria': 'Outros', 'prioridade': 2},
    'OTIMO':           {'categoria': 'Outros', 'prioridade': 3},
}