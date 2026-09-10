*Read this in other languages: [Português](README.pt-br.md)*

# steam_etl

My first data pipeline project, built while studying data engineering.

## What it does

Takes a game ID, fetches data from the public Steam API, and transforms the returned raw JSON into a structured and cleaned Excel spreadsheet.

## Flow

1. **Extraction**: Request to the Steam API using the game ID (I used Hades 2 for testing).
2. **Raw layer**: The response is saved to disk exactly as received, without any processing.
3. **Exploration**: The JSON is normalized into a DataFrame using pandas, and the columns of interest are selected.
4. **Data Cleaning**: Specific functions solve each issue found in the data:
   * Cleaning HTML tags from descriptions
   * Converting boolean columns to integers
   * Parsing the genre list (list of dictionaries) into a single string
   * Regex extraction of OS, processor, RAM, and graphics card, which came mixed in a text block per platform (Windows, Mac, and Linux)
5. **Orchestration**: All cleaning functions were centralized into a single orchestrator function.
6. **Output**: The cleaned data is exported to an Excel file, with automatic column width adjustment.

## Architecture and Organization

The project code was fully modularized, moving from a single procedural script to a file structure separated by responsibilities to facilitate maintenance and scalability.

## Technologies

* Python
* pandas
* requests
* BeautifulSoup (HTML cleaning)
* openpyxl (Excel export and formatting)
* regex

## Status

Project successfully modularized. Next step: continue evolving the architecture and expanding the data pipeline.

## How to run

```bash
pip install pandas requests beautifulsoup4 openpyxl
python src/main.py

The game ID is defined in the APP_ID variable at the top of config.py