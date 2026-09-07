from pathlib import Path

# Definindo a raiz do projeto de forma dinâmica
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Configurações de API
APP_ID = 1145350
STEAM_API_URL = f"https://store.steampowered.com/api/appdetails?appids={APP_ID}&cc=br&l=portuguese"

# Configurações de Diretórios e Arquivos (apontando para a raiz)
PASTA_DADOS = BASE_DIR / "dados"
CAMINHO_BRUTO = PASTA_DADOS / f"{APP_ID}_bruto.json"

PASTA_XLSX = BASE_DIR / "xlsx_tratado"
CAMINHO_XLSX = PASTA_XLSX / "dados_jogo.xlsx"

# Colunas de Interesse
COLUNAS_DE_INTERESSE = [
    "name", "required_age", "genres",
    "pc_requirements.minimum", "pc_requirements.recommended",
    "mac_requirements.minimum", "mac_requirements.recommended",
    "linux_requirements.minimum", "linux_requirements.recommended",
    "price_overview.currency", "price_overview.initial",
    "price_overview.final", "price_overview.discount_percent",
    "price_overview.initial_formatted", "price_overview.final_formatted",
    "platforms.windows", "platforms.mac", "platforms.linux",
    "metacritic.score", "release_date.date",
]