# --- Importações ---
# Importa as bibliotecas necessárias: Streamlit para a interface web e speedtest para a medição.
import streamlit as st
import speedtest

def main():
    # --- Configuração da Interface ---
    # Define os elementos visuais iniciais da página, como título, um divisor e um texto instrutivo.
    st.title('SpeedTest')
    st.divider()
    st.write('Clique no botão abaixo para iniciar o teste.')

    # --- Lógica do Teste de Velocidade ---
    # O código a seguir é executado somente após o usuário clicar no botão "Iniciar".
    if st.button('Iniciar'):
        # Envolve a lógica do teste em um bloco 'with st.spinner(...)' para mostrar um feedback
        # de carregamento ao usuário e em um 'try...except' para tratar erros de conexão.
        with st.spinner('Testando a velocidade da sua internet... ⏳'):
            try:
                # Inicializa o teste, mede as velocidades de download/upload e coleta os resultados.
                # Os valores são convertidos de bits/s para Megabits/s (Mbps) para melhor leitura.
                s = speedtest.Speedtest()
                s.get_best_server()
                download_speed = s.download() / 1_000_000
                upload_speed = s.upload() / 1_000_000
                results = s.results.dict()

                # --- Exibição dos Resultados ---
                # Apresenta os resultados de forma organizada na tela, incluindo barras de progresso
                # para uma visualização rápida da velocidade em relação a um teto de 1Gbps.
                max_speed_mbps = 1000
                st.write(f'**Velocidade de Download:** {download_speed:.2f} Mbps')
                st.progress(min(download_speed / max_speed_mbps, 1.0))
                st.write(f'**Velocidade de Upload:** {upload_speed:.2f} Mbps')
                st.progress(min(upload_speed / max_speed_mbps, 1.0))
                st.write(f"**Ping:** {results['ping']:.2f} ms")
                st.write(f"**Host:** {results['server']['host']}")

            # --- Tratamento de Erro ---
            # Se o teste falhar por não conseguir encontrar um servidor (comum sem internet),
            # uma mensagem de erro amigável é exibida.
            except speedtest.ConfigRetrievalError:
                st.error("Não foi possível conectar. Verifique sua conexão com a internet.")


# --- Ponto de Entrada do Script ---
# Garante que a função main() seja executada quando o arquivo é chamado diretamente.
if __name__ == '__main__':
    main()
