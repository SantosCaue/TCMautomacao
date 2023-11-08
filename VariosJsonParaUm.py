import os
import json

def merge_json_files(input_folder, output_file):
    merged_data = []

    # Percorre os arquivos na pasta de entrada
    for filename in os.listdir(input_folder):
        if filename.endswith(".json"):
            with open(os.path.join(input_folder, filename), "r", encoding="utf-8") as file:
                data = json.load(file)
                if "nome_pt" in data and "nome_en" in data and "bandeira" in data:
                    merged_data.append({
                        "nome_pt": data["nome_pt"],
                        "nome_en": data["nome_en"],
                        "bandeira": data["bandeira"],
                        "descricao_pt": data["descricao_pt"],
                        "descricao_en": data["descricao_en"],
                        "populacao": data["populacao"],
                        "area": data["area"],
                        "pib": data["pib"],
                        "idioma_en": data["idioma_en"],
                        "idioma_pt": data['idioma_pt'],
                        "moeda_pt": data["moeda_pt"],
                        "moeda_en": data["moeda_en"],
                        "capital_en": data["capital_en"],
                        "capital_pt": data["capital_pt"],
                        "mapa": data["mapa"],
                        "bandeira": data["bandeira"]
                    })

    # Escreve os dados compilados no novo arquivo JSON
    with open(output_file, "w", encoding="utf-8") as outfile:
        json.dump(merged_data, outfile, ensure_ascii=False, indent=4)

    print(f"Arquivo compilado salvo em: {output_file}")

if __name__ == "__main__":  
    input_folder = "C:/Users/karol/Desktop/CAUE ETEC/arquivoshtml/paisesdados"
    output_file = "arquivo_compilado.json"
    merge_json_files(input_folder, output_file)