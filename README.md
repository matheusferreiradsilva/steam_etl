# steam_etl

Meu primeiro projeto de pipeline de dados, feito enquanto estudo engenharia de dados.

## O que faz

Recebe o ID de um jogo, busca os dados na API pública da Steam e transforma o JSON bruto retornado em uma planilha Excel estruturada e tratada.

## Fluxo

1. **Extração**: requisição na API da Steam a partir do ID do jogo (usei Hades 2 pra testar).
2. **Camada raw**: a resposta é salva em disco exatamente como veio, sem nenhum tratamento.
3. **Exploração**: o JSON é normalizado em DataFrame com pandas, e as colunas de interesse são selecionadas.
4. **Tratamento**: funções específicas resolvem cada problema encontrado nos dados:
   - Limpeza de tags HTML nas descrições
   - Conversão de colunas booleanas pra inteiro
   - Parsing da lista de gêneros (lista de dicionários) pra uma única string
   - Extração via regex de sistema operacional, processador, RAM e placa de vídeo, que vinham misturados num bloco de texto por plataforma (Windows, Mac e Linux)
5. **Orquestração**: todas as funções de tratamento foram centralizadas numa função orquestradora.
6. **Saída**: os dados tratados são exportados pra um arquivo Excel, com ajuste automático da largura das colunas.

## Arquitetura e Organização

O código do projeto foi totalmente modularizado, deixando de ser um script procedural único e passando a contar com uma estrutura de arquivos separada por responsabilidades para facilitar a manutenção e a escalabilidade.

## Tecnologias

- Python
- pandas
- requests
- BeautifulSoup (limpeza de HTML)
- openpyxl (exportação e formatação do Excel)
- regex

## Status

Projeto modularizado com sucesso. Próximo passo: continuar a evolução da arquitetura e expansão do pipeline de dados.

## Como rodar

```bash
pip install pandas requests beautifulsoup4 openpyxl
python src/main.py

O ID do jogo é definido na variável APP_ID no início do config.py.