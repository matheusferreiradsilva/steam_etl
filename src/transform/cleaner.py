import re
import pandas as pd
from bs4 import BeautifulSoup

def limpar_html(texto: str) -> str:
    """Remove tags HTML de uma célula de texto."""
    if isinstance(texto, str):
        return BeautifulSoup(texto, "html.parser").get_text(separator=" ").strip()
    return texto

def tratar_bool(infojogo: pd.DataFrame) -> pd.DataFrame:
    """Converte colunas booleanas (True/False) para inteiro (1/0)."""
    colunas_bool = infojogo.select_dtypes(include=["bool"]).columns
    infojogo[colunas_bool] = infojogo[colunas_bool].astype(int)
    return infojogo

def tratar_genero(infojogo: pd.DataFrame) -> str:
    """Transforma a lista de dicionários de gêneros em uma string separada por vírgulas."""
    coluna_genero = infojogo["genres"][0]
    if isinstance(coluna_genero, list):
        generos = [dicionario["description"] for dicionario in coluna_genero]
        return ", ".join(generos)
    return coluna_genero

def extrair_requisitos_steam(infojogo: pd.DataFrame) -> pd.DataFrame:
    """Extrai informações detalhadas (CPU, RAM, GPU) do bloco de texto original."""
    colunas_origem = {
        "pc_requirements.minimum": "pc_min", "pc_requirements.recommended": "pc_rec",
        "mac_requirements.minimum": "mac_min", "mac_requirements.recommended": "mac_rec",
        "linux_requirements.minimum": "linux_min", "linux_requirements.recommended": "linux_rec",
    }
    padroes = {
        "so": r"Sistema Operativo:\s*([^:]+?)(?=\s*Processador:|$)",
        "cpu": r"Processador:\s*([^:]+?)(?=\s*Memória:|$)",
        "ram_gb": r"Memória:\s*(\d+)\s*GB",
        "gpu": r"Placa gráfica:\s*([^:]+?)(?=\s*Espaço|$)",
        "disco_gb": r"(?:Espaço no disco:|espaço livre:)?\s*Requer\s*(\d+)\s*GB",
    }

    for col_origem, prefixo in colunas_origem.items():
        if col_origem not in infojogo.columns:
            continue
        infojogo[f"{prefixo}_so"] = infojogo[col_origem].str.extract(padroes["so"], flags=re.IGNORECASE, expand=False).str.strip()
        infojogo[f"{prefixo}_cpu"] = infojogo[col_origem].str.extract(padroes["cpu"], flags=re.IGNORECASE, expand=False).str.strip()
        ram_extraida = infojogo[col_origem].str.extract(padroes["ram_gb"], flags=re.IGNORECASE, expand=False)
        infojogo[f"{prefixo}_ram_gb"] = pd.to_numeric(ram_extraida, errors="coerce")
        infojogo[f"{prefixo}_gpu"] = infojogo[col_origem].str.extract(padroes["gpu"], flags=re.IGNORECASE, expand=False).str.strip()
        disco_extraido = infojogo[col_origem].str.extract(padroes["disco_gb"], flags=re.IGNORECASE, expand=False)
        infojogo[f"{prefixo}_disco_gb"] = pd.to_numeric(disco_extraido, errors="coerce")

    return infojogo

def orquestradora(infojogo: pd.DataFrame) -> pd.DataFrame:
    """Executa todas as etapas de tratamento sobre o DataFrame em ordem."""
    colunas_texto = (
        infojogo.select_dtypes(include=["string", "object"])
        .drop(columns=["genres"], errors="ignore").columns
    )
    infojogo[colunas_texto] = infojogo[colunas_texto].map(limpar_html)
    infojogo["genres"] = tratar_genero(infojogo)
    infojogo = tratar_bool(infojogo)
    infojogo = extrair_requisitos_steam(infojogo)

    colunas_antigas = [
        "pc_requirements.minimum", "pc_requirements.recommended",
        "mac_requirements.minimum", "mac_requirements.recommended",
        "linux_requirements.minimum", "linux_requirements.recommended",
    ]
    infojogo = infojogo.drop(columns=colunas_antigas)

    colunas_requisitos = [c for c in infojogo.columns if c.startswith(("pc_", "mac_", "linux_"))]
    infojogo[colunas_requisitos] = infojogo[colunas_requisitos].fillna("Não suportado")

    return infojogo