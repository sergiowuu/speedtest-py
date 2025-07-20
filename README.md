# SpeedTest com Streamlit

![Badge de Tecnologias](https://skillicons.dev/icons?i=py)

Aplicativo web construído com Python e Streamlit para medir a velocidade da sua conexão de internet em tempo real.

## 🚀 Demonstração

![Design sem nome (1)](https://github.com/user-attachments/assets/c3ce85c9-4ddf-435b-9007-bbec2a0beda7)

## ✨ Funcionalidades

-   **Teste de Download:** Mede a velocidade de download em Mbps.
-   **Teste de Upload:** Mede a velocidade de upload em Mbps.
-   **Ping:** Exibe a latência (ping) da sua conexão em milissegundos.
-   **Host do Teste:** Mostra qual servidor foi utilizado para realizar a medição.
-   **Interface Simples:** Interface limpa e intuitiva criada com o framework Streamlit.
-   **Feedback Visual:** Barras de progresso para uma visualização rápida das velocidades.
-   **Tratamento de Erros:** Exibe uma mensagem amigável caso não haja conexão com a internet.

## 🛠️ Tecnologias Utilizadas

-   [Python](https://www.python.org/)
-   [Streamlit](https://streamlit.io/)
-   [speedtest-cli](https://pypi.org/project/speedtest-cli/)

## ⚙️ Como Executar o Projeto

Siga os passos abaixo para configurar e executar o projeto no seu ambiente local.

### Pré-requisitos

-   Certifique-se de ter o [Python 3.8+](https://www.python.org/downloads/) instalado em seu sistema.

### Passos para Execução

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/sergiowuu/speedtest-py.git
    cd speedtest-py
    ```

2.  **Execute o aplicativo Streamlit:**
    Com as dependências instaladas, inicie o aplicativo com o comando:
    ```bash
    streamlit run main.py
    ```
    *Se o comando acima não for encontrado, utilize este:*
    ```bash
    python -m streamlit run main.py
    ```

Após executar o comando, o aplicativo será aberto automaticamente no seu navegador padrão.
