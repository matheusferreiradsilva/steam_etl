# steam_etl

Python ETL pipeline that collects game details from the public Steam API,
cleans and transforms the data, and exports it to an Excel spreadsheet.

> Read this in other languages: [Português (Brasil)](README.pt-br.md)

## Overview

The pipeline reads a game `APP_ID`, requests the Steam `appdetails` endpoint,
saves the raw response as JSON, normalizes and cleans the selected fields with
pandas, and writes the result to `xlsx_tratado/dados_jogo.xlsx`.

The current default app ID is `1145350`, configured in
`src/config/settings.py`. Change `APP_ID` there to process another game.

## Stack

- Python 3.10+
- pandas
- requests
- Beautiful Soup
- openpyxl

## Project structure

```text
dados/                  # Raw API responses
src/config/             # Application settings
src/extract/            # Steam API extraction
src/transform/          # Data cleaning and normalization
src/load/               # Excel export
src/main.py             # ETL orchestration
tests/                  # Automated tests
xlsx_tratado/           # Generated Excel output
steam.py                # Previous monolithic implementation
```

## Installation and usage

```bash
python -m venv .venv

# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Linux/macOS
source .venv/bin/activate

python -m pip install pandas requests beautifulsoup4 openpyxl
python src/main.py
```

The raw JSON and formatted Excel file are created automatically in `dados/`
and `xlsx_tratado/`.

For the complete documentation, including the transformation details and
development notes, see [README.pt-br.md](README.pt-br.md).
