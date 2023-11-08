import openpyxl

# Carrega o arquivo .xlsx
workbook = openpyxl.load_workbook('paises.xlsx')
sheet = workbook['Planilha1']

# Resto do código...
sheet = workbook['Planilha1']

# Itera sobre os valores da coluna A
for row in sheet.iter_rows(min_row=1, max_row=194, min_col=1, max_col=1, values_only=True):
    cell_value = row[0]

    # Cria o nome do arquivo HTML
    file_name = str(cell_value) + '.html'

    # Cria o conteúdo do arquivo HTML
    html_content = """<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
    <link rel="icon" href="assets/imgs/globe2.svg">
    <link rel="stylesheet" href="assets/css/pais.css">
</head>

<body>
    <header>
        <div id="titulo">
            <img src="assets/imgs/logotipo.png" onclick="window.location.href = 'index.html'">
            <a href="index.html">
                <h1>WIKI DOS PAÍSES</h1>
            </a>
        </div>
        <div id="menu" onclick="menulateral()">
            <svg xmlns="http://www.w3.org/2000/svg" width="90" height="90" fill="white" class="bi bi-list"
                viewBox="0 0 16 16">
                <path fill-rule="evenodd"
                    d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z" />
            </svg>
        </div>
    </header>
    <nav>
        <ul>
            <li class="item-menu">
                <a href="quiz.html">
                    <span class="icon"><i class="bi bi-question-circle-fill"></i></span>
                    <span class="txt-link">QUIZ</span>
                </a>
            </li>
            <li class="item-menu">
                <a href="continentes.html">
                    <span class="icon"><i class="bi bi-globe-europe-africa"></i></span>
                    <span class="txt-link">CONTINENTES</span>
                </a>
            </li>
            <li class="item-menu">
                <a href="paises.html">
                    <span class="icon"><i class="bi bi-flag"></i></i></span>
                    <span class="txt-link">PAÍSES</span>
                </a>
            </li>
            <li class="item-menu">
                <a href="paisaleatorio.html">
                    <span class="icon"><i class="bi bi-globe-central-south-asia"></i></span>
                    <span class="txt-link">PAÍS ALEATÓRIO</span>
                </a>
            </li>
            <li class="item-menu">
                <a onclick="traduzir()">
                    <span class="icon"><i class="bi bi-translate"></i></span>
                    <span class="txt-link">MUDAR IDIOMA</span>
                </a>
            </li>
        </ul>
    </nav>
    <main>
        <div id="left">
            <div id="nome">
                <h2 id="country"></h2>
            </div>
            <div id="meio">
                <p id="descricao"></p>
            </div>
            <div id="dados">
                <p id="populacao"></p>
                <p id="pib"></p>
                <p id="area"></p>
                <p id="moeda"></p>
                <p id="idioma"></p>
                <p id="capital"></p>
                <p id="bibliografia"></p>
            </div>
        </div>
        <div id="right">
            <div><img id="bandeira"></div>

            <img id="mapa">
        </div>
    </main>
    <footer>
        <p>TODOS OS DIREITOS RESERVADOS CAUÊ GONÇALVES SANTOS &COPY; 2023</p>
    </footer>
</body>
<script src="assets/js/pais.js"></script>

</html>
"""
    # Escreve o conteúdo no arquivo HTML
    if(file_name != file_name.replace(" ", "_")):
        with open("htmls/"+file_name.replace(" ", "_"), 'w', encoding='utf-8') as file:
            file.write(html_content)
