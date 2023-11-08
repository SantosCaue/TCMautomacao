import json

# Caminho para o arquivo JSON
json_file_path = "arquivo_compilado.json"
output_file = "arquivo_compilado.json"

# Lê o JSON do arquivo
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Transforma a lista de dicionários em um dicionário onde as chaves são os nomes em letras minúsculas
country_dict = {country["nome_en"].lower(): country for country in data}

with open(output_file, "w", encoding="utf-8") as outfile:
        json.dump(country_dict, outfile, ensure_ascii=False, indent=4)
