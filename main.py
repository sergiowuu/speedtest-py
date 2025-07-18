import streamlit as st
import speedtest

def main():
    st.title('SpeedTest')
    st.divider()
    st.write('Clique no botão abaixo para iniciar o teste.')

    if st.button('Iniciar'):
        with st.spinner('Testando a velocidade da sua internet... ⏳'):
            try:
                s = speedtest.Speedtest()
                s.get_best_server()
                
                # O método download/upload retorna bits por segundo
                download_speed = s.download() / 1_000_000  # Converte para Mbps
                upload_speed = s.upload() / 1_000_000    # Converte para Mbps
                results = s.results.dict()

                # Defina uma velocidade máxima realista em Mbps para a barra de progresso
                max_speed_mbps = 1000 # Ex: 1000 Mbps (1 Gbps)

                st.write(f'**Velocidade de Download:** {download_speed:.2f} Mbps')
                # A barra de progresso espera um valor de 0 a 1
                st.progress(min(download_speed / max_speed_mbps, 1.0)) 

                st.write(f'**Velocidade de Upload:** {upload_speed:.2f} Mbps')
                st.progress(min(upload_speed / max_speed_mbps, 1.0))

                st.write(f"**Ping:** {results['ping']:.2f} ms")
                st.write(f"**Host:** {results['server']['host']}")

            except speedtest.ConfigRetrievalError:
                st.error("Não foi possível conectar. Verifique sua conexão com a internet.")


if __name__ == '__main__':
    main()