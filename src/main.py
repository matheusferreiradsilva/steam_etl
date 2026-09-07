import pandas as pd

# AQUI ESTÁ A CORREÇÃO:
# Mudamos de "from config import..." para "from config.settings import..."
from config.settings import STEAM_API_URL, APP_ID, COLUNAS_DE_INTERESSE, CAMINHO_XLSX

# As outras importações continuam iguais, apontando para as pastas e seus respectivos arquivos
from extract.steam_api import buscar_dados_steam
from transform.cleaner import orquestradora
from load.exporter import salvar_com_largura_ajustada

def main() -> None:
    print("Iniciando processo de ETL da Steam...")
    
    # 1. Extração
    dados = buscar_dados_steam(STEAM_API_URL, APP_ID)

    # Preparação
    tabela_dados = pd.json_normalize(dados)
    infojogo = tabela_dados.reindex(columns=COLUNAS_DE_INTERESSE)

    # 2. Transformação
    tratado = orquestradora(infojogo)

    # 3. Carga
    salvar_com_largura_ajustada(tratado, CAMINHO_XLSX, sheet_name=f"jogo ID{APP_ID}")
    
    print("Processo finalizado com sucesso!")

if __name__ == "__main__":
    main()