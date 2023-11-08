import os
import json

# Diretório da lista JSON original
lista_json_path = "C:\\Users\\karol\\Desktop\\CAUE ETEC\\TÉCNICO\\githubz\\assets\\paisesdados\\paisdodia2.json"
# Diretório da pasta com os arquivos JSON a serem preenchidos
arquivos_json_path = "C:\\Users\\karol\\Desktop\\CAUE ETEC\\TÉCNICO\\githubz\\assets\\paisesdados"

# Carrega a lista JSON original
with open(lista_json_path, "r", encoding="utf-8") as lista_json_file:
    lista_json = json.load(lista_json_file)

# Itera sobre os elementos da lista JSON
for key, value in lista_json.items():
    arquivo_html = value["Arquivo"]
    arquivo_json = arquivo_html.replace(".html", ".json")
    arquivo_json_path = os.path.join(arquivos_json_path, arquivo_json)

    # Verifica se o arquivo JSON existe na pasta
    if os.path.exists(arquivo_json_path):
        # Carrega o arquivo JSON existente
        with open(arquivo_json_path, "r", encoding='utf-8') as arquivo_json_file:
            try:
                dados_json = json.load(arquivo_json_file)
            except json.JSONDecodeError:
                dados_json = {}

        # Preenche os campos do arquivo JSON
        dados_json["nome_pt"] = value.get("PAISportugues", "")
        dados_json["nome_en"] = value.get("PAISingles", "")
        dados_json["bandeira"] = value.get("Bandeira", "")

        # Salva as alterações no arquivo JSON
        with open(arquivo_json_path, "w", encoding='utf-8') as arquivo_json_file:
            json.dump(dados_json, arquivo_json_file, indent=4, ensure_ascii=False)


# Verifica arquivos que têm nome_pt e nome_en e não receberam dados novos
arquivos_sem_dados_novos = []
for arquivo in os.listdir(arquivos_json_path):
    if arquivo.endswith(".json"):
        arquivo_json_path = os.path.join(arquivos_json_path, arquivo)
        with open(arquivo_json_path, "r", encoding="utf-8") as arquivo_json_file:
            dados_json = json.load(arquivo_json_file)
            
            if "nome_pt" in dados_json and "nome_en" in dados_json:
                if dados_json["nome_pt"] == "Brasil" and dados_json["nome_en"] == "Brazil":
                    arquivos_sem_dados_novos.append(arquivo)

# Imprime os arquivos que têm nome_pt e nome_en e não receberam dados novos
if arquivos_sem_dados_novos:
    print("Arquivos que têm nome_pt e nome_en e não receberam dados novos:")
    for arquivo in arquivos_sem_dados_novos:
        print(arquivo)
else:
    print("Todos os arquivos receberam dados novos.")
