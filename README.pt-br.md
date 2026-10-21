# steam_etl

Pipeline ETL em Python para coletar detalhes de jogos da API pública da
Steam, tratar os dados e exportá-los para uma planilha Excel.

> Leia em outros idiomas: [English](README.md)

## Visão geral

O projeto recebe um `APP_ID` de jogo, consulta o endpoint
`appdetails` da Steam em português do Brasil e executa três etapas:

1. **Extração:** faz a requisição HTTP e salva a resposta original em JSON na
   pasta `dados/`.
2. **Transformação:** normaliza o JSON com pandas, seleciona as colunas de
   interesse, remove HTML, converte valores booleanos, transforma gêneros em
   texto e extrai requisitos de sistema por plataforma com expressões
   regulares.
3. **Carga:** grava os dados tratados em
   `xlsx_tratado/dados_jogo.xlsx`, ajustando automaticamente a largura das
   colunas.

O valor configurado atualmente em `src/config/settings.py` é o app `1145350`.
Para processar outro jogo, altere `APP_ID`; a URL da Steam e os caminhos de
saída são derivados automaticamente dessa configuração.

## Tecnologias

- Python 3.10 ou superior
- [pandas](https://pandas.pydata.org/)
- [requests](https://requests.readthedocs.io/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [openpyxl](https://openpyxl.readthedocs.io/)
- `re`, biblioteca padrão do Python, para extração dos requisitos

## Estrutura do projeto

```text
.
├── dados/                  # Respostas brutas da API em JSON
├── src/
│   ├── config/settings.py  # APP_ID, URL, caminhos e colunas selecionadas
│   ├── extract/            # Consulta à API e persistência da camada raw
│   ├── transform/          # Limpeza e normalização dos dados
│   ├── load/               # Exportação e formatação do Excel
│   └── main.py             # Orquestração do pipeline
├── tests/                  # Espaço para testes automatizados
├── xlsx_tratado/           # Planilha gerada pelo pipeline
└── steam.py                # Implementação monolítica anterior do pipeline
```

## Pré-requisitos

- Python 3.10 ou superior
- Acesso à internet para consultar a API da Steam

É recomendado criar um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual:

```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Linux/macOS
source .venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install pandas requests beautifulsoup4 openpyxl
```

## Como executar

Na raiz do projeto, execute:

```bash
python src/main.py
```

Ao finalizar, o pipeline gera:

- `dados/1145350_bruto.json`: resposta original recebida da Steam;
- `xlsx_tratado/dados_jogo.xlsx`: dados tratados, em uma aba nomeada com o
  ID do jogo.

Os diretórios de saída são criados automaticamente quando necessário.

## Dados tratados

O pipeline mantém informações como nome, idade recomendada, gêneros, preços,
plataformas, nota do Metacritic e data de lançamento. Também cria campos
específicos para requisitos mínimos e recomendados de Windows, macOS e Linux,
incluindo:

- sistema operacional;
- processador;
- memória RAM em GB;
- placa de vídeo;
- espaço em disco em GB.

Plataformas sem requisitos disponíveis são preenchidas com `Não suportado`.

## Desenvolvimento

Para executar os testes, instale o pytest e rode:

```bash
python -m pip install pytest
python -m pytest
```

O arquivo `steam.py` permanece no repositório como referência da versão
monolítica original. A execução recomendada é `src/main.py`, que usa a
implementação modularizada.

## Limitações e próximos passos

- O pipeline processa um jogo por execução.
- O `APP_ID` ainda é configurado diretamente no código.
- Não há um arquivo de dependências fixadas (`requirements.txt` ou
  equivalente).
- A cobertura de testes automatizados pode ser expandida.

Possíveis evoluções incluem receber o ID por argumento de linha de comando,
adicionar tratamento de timeout e retries na requisição, fixar versões das
dependências e ampliar a cobertura de testes.

## Licença

Nenhuma licença foi definida no repositório até o momento.
