# 📊 Automatizador de Relatório de Despesas em Python

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-1.5.3-150458?style=for-the-badge&logo=pandas)

Script em Python que lê um extrato de transações de um arquivo `.csv`, categoriza cada despesa de forma inteligente usando um sistema de prioridades e Regex, e gera um relatório completo em Excel com um resumo e um gráfico de pizza.

---

### 演示 | Demonstração do Relatório Final

*A imagem abaixo mostra um exemplo do arquivo `resumo_despesas_final.xlsx` gerado automaticamente pelo script.*

![Demonstração do Relatório](caminho/para/sua/imagem.png)  ---

### 🚀 Funcionalidades Principais

- **Categorização Inteligente:** Utiliza um dicionário externo com um sistema de prioridades (Marca > Serviço > Genérico) para resolver ambiguidades.
- **Busca Precisa com Regex:** Emprega Expressões Regulares (`\b`) para garantir a correspondência de palavras inteiras, evitando falsos positivos (ex: não confundir "TIM" com "OTIMO").
- **Código Organizado:** Separa a lógica (`automatizador_despesas_v2.py`) da configuração (`config_categorias.py`), facilitando a manutenção e adição de novas categorias.
- **Feedback Loop:** Informa ao usuário quais despesas não foram categorizadas, facilitando a melhoria contínua do dicionário.
- **Relatório Automatizado:** Gera um arquivo Excel profissional com duas abas: uma com os dados detalhados e outra com o resumo e um gráfico de pizza.

---

### 🛠️ Ferramentas e Bibliotecas

* **Python 3**
* **Pandas:** Para manipulação e análise dos dados.
* **Openpyxl:** Motor utilizado pelo Pandas para escrever os arquivos `.xlsx` e o gráfico.

---

### 📋 Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/python-automatizador-relatorio-despesas.git](https://github.com/SEU-USUARIO/python-automatizador-relatorio-despesas.git)
    cd python-automatizador-relatorio-despesas
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS / Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o script:**
    ```bash
    python automatizador_despesas_v2.py
    ```

5.  O arquivo `resumo_despesas_final.xlsx` será gerado no diretório.

---
### 📁 Estrutura do Projeto
![image](https://github.com/user-attachments/assets/00c8c493-4d1f-4401-829b-c1e76579f0ff)

