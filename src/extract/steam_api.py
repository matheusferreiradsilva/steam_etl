import json
import requests
from pathlib import Path
from config.settings import CAMINHO_BRUTO

def salvar_camada_bruta(dados_json: dict, caminho_arquivo: Path) -> None:
    """Guarda a resposta original da API em disco, sem nenhuma alteração."""
    caminho_arquivo.parent.mkdir(parents=True, exist_ok=True)
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados_json, f, ensure_ascii=False, indent=4)
    print(f"✅ Dado bruto salvo com sucesso em: {caminho_arquivo}")

def buscar_dados_steam(url: str, app_id: int) -> dict:
    """Faz a requisição na Steam API e devolve só o dicionário 'data' do jogo."""
    resposta_api = requests.get(url)
    resposta_api.raise_for_status()

    resposta_json = resposta_api.json()
    salvar_camada_bruta(resposta_json, CAMINHO_BRUTO)

    chave_app = str(app_id)
    bloco_app = resposta_json.get(chave_app)

    if bloco_app is None or not bloco_app.get("success"):
        raise ValueError(f"Steam API não retornou dados válidos para o app_id {app_id}")

    return bloco_app["data"]