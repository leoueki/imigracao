import csv
import json

# Nome dos arquivos
csv_file = "data-all.csv"  # Substitua pelo nome do seu arquivo CSV
json_file = "dados.json"  # Nome do arquivo de saída

# Lendo o CSV e convertendo para JSON
with open(csv_file, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)  # Lê o CSV como dicionário
    data = list(reader)  # Converte para uma lista de dicionários

# Salvando como JSON
with open(json_file, mode="w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)  # Salva com indentação para melhor leitura

print(f"Arquivo {json_file} gerado com sucesso!")
