import openpyxl
import json
import codecs

# Carrega o arquivo .xlsx
workbook = openpyxl.load_workbook('paises.xlsx')
sheet = workbook['Planilha1']

# Cria um dicionário para armazenar os dados
dados = {}

# Percorre as células da coluna A
for cell in sheet['A1:A194']:
    valor_celula = cell[0].value
    if valor_celula:
        # Cria o dicionário com os dados
        dados[valor_celula] = {
            "nome_pt": "Brasil",
            "nome_en": "Brazil",
            "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
            "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
            "populacao": "218.689.757",
            "area": "8.515.770",
            "pib": "3.128.000.000.000",
            "moeda_pt": "Real Brasileiro",
            "moeda_en": "Brazilian Real",
            "idioma_pt": "Português",
            "idioma_en": "Portuguese",
            "capital_pt": "Brasília",
            "capital_en": "Brasília",
            "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/bc/BRA_orthographic.svg",
            "bandeira": "https://upload.wikimedia.org/wikipedia/commons/0/05/Flag_of_Brazil.svg"
        }

# Cria os arquivos JSON
for nome_arquivo, conteudo in dados.items():
    with codecs.open(f'{nome_arquivo}.json', 'w', encoding='utf-8') as arquivo_json:
        json.dump(conteudo, arquivo_json, ensure_ascii=False, indent=4)