import json

# Lista JSON original
json_data = '''
[
    {
        "alt": "Burundi",
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/27/Burundi_%28orthographic_projection%29.svg/80px-Burundi_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Comoros",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/ad/Comoros_%28orthographic_projection%29.svg/80px-Comoros_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Djibouti",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b7/Djibouti_%28orthographic_projection%29.svg/80px-Djibouti_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Eritrea",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/43/Eritrea_%28Africa_orthographic_projection%29.svg/80px-Eritrea_%28Africa_orthographic_projection%29.svg"
    },
    {
        "alt": "Ethiopia",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/dd/Ethiopia_%28Africa_orthographic_projection%29.svg/80px-Ethiopia_%28Africa_orthographic_projection%29.svg"
    },
    {
        "alt": "Kenya",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Kenya_%28orthographic_projection%29.svg/80px-Kenya_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Madagascar",
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/99/Madagascar_%28orthographic_projection%29.svg/80px-Madagascar_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Malawi",
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Malawi_%28orthographic_projection%29.svg/80px-Malawi_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Mauritius",
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/ed/Mauritius_%28orthographic_projection%29.svg/80px-Mauritius_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Mozambique",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/84/Mozambique_%28orthographic_projection%29.svg/80px-Mozambique_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Tanzania",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Tanzania_%28orthographic_projection%29.svg/80px-Tanzania_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Somalia",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Somalia_%28orthographic_projection%29.svg/80px-Somalia_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Uganda",
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Uganda_%28orthographic_projection%29.svg/80px-Uganda_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Lesotho",
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/f1/Lesotho_%28orthographic_projection%29.svg/80px-Lesotho_%28orthographic_projection%29.svg"
    },
    {
        "alt": "South Africa",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6e/South_Africa_%28orthographic_projection%29.svg/80px-South_Africa_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Zambia",
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/26/Zambia_%28orthographic_projection%29.svg/80px-Zambia_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Zimbabwe",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/50/Zimbabwe_%28orthographic_projection%29.svg/80px-Zimbabwe_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Angola",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/89/Angola_%28orthographic_projection%29.svg/80px-Angola_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Cameroon",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b4/Cameroon_%28orthographic_projection%29.svg/80px-Cameroon_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Chad",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/46/Chad_%28orthographic_projection%29.svg/80px-Chad_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Gabon",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/bf/Gabon_%28orthographic_projection%29.svg/80px-Gabon_%28orthographic_projection%29.svg"
    },
    {
        "alt": "South Sudan",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/65/South_Sudan_%28orthographic_projection%29.svg/80px-South_Sudan_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Algeria",
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/25/Algeria_%28orthographic_projection%29.svg/80px-Algeria_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Egypt",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Egypt_%28orthographic_projection%29.svg/80px-Egypt_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Libya",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Libya_%28Libya_centered%3B_orthographic_projection%29.svg/80px-Libya_%28Libya_centered%3B_orthographic_projection%29.svg"
    },
    {
        "alt": "Morocco",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/78/Morocco_%28orthographic_projection%2C_WS_claimed%29.svg/80px-Morocco_%28orthographic_projection%2C_WS_claimed%29.svg"
    },
    {
        "alt": "Sudan",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/ca/Sudan_%28orthographic_projection%29.svg/80px-Sudan_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Tunisia",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/da/Tunisia_%28orthographic_projection%29.svg/80px-Tunisia_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Benin",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/01/Benin_%28orthographic_projection_with_inset%29.svg/80px-Benin_%28orthographic_projection_with_inset%29.svg"
    },
    {
        "alt": "Burkina Faso",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/86/Burkina_Faso_%28orthographic_projection%29.svg/80px-Burkina_Faso_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Cape Verde",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/47/Cape_Verde_%28orthographic_projection%29.svg/80px-Cape_Verde_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Gambia",
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/16/Gambia_%28orthographic_projection_with_inset%29.svg/80px-Gambia_%28orthographic_projection_with_inset%29.svg"
    },
    {
        "alt": "Ghana",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/30/Ghana_%28orthographic_projection%29.svg/80px-Ghana_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Guinea",
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e4/Guinea_%28orthographic_projection%29.svg/80px-Guinea_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Liberia",
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/91/Liberia_%28orthographic_projection%29.svg/80px-Liberia_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Mali",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/8b/Mali_%28orthographic_projection%29.svg/80px-Mali_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Mauritania",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/ac/Mauritania_%28orthographic_projection%29.svg/80px-Mauritania_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Niger",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/88/Niger_%28orthographic_projection%29.svg/80px-Niger_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Nigeria",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Nigeria_%28orthographic_projection%29.svg/80px-Nigeria_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Senegal",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Senegal_%28orthographic_projection%29.svg/80px-Senegal_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Sierra Leone",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/38/Sierra_Leone_%28orthographic_projection%29.svg/80px-Sierra_Leone_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Canada",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c7/Canada_%28orthographic_projection%29.svg/80px-Canada_%28orthographic_projection%29.svg"
    },
    {
        "alt": "United States",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/70/United_States_%28orthographic_projection%29.svg/80px-United_States_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Mexico",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c9/Mexico_%28orthographic_projection%29.svg/80px-Mexico_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Guatemala",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/70/Guatemala_%28orthographic_projection%29.svg/80px-Guatemala_%28orthographic_projection%29.svg"
    },
    {
        "alt": "El Salvador",
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e3/El_Salvador_%28orthographic_projection%29.svg/80px-El_Salvador_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Honduras",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Honduras_%28orthographic_projection%29.svg/80px-Honduras_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Nicaragua",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/38/Nicaragua_%28orthographic_projection%29.svg/80px-Nicaragua_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Costa Rica",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c4/Costa_Rica_%28orthographic_projection%29.svg/80px-Costa_Rica_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Panama",
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e1/Panama_%28orthographic_projection%29.svg/80px-Panama_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Trinidad and Tobago",
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/ed/Trinidad_and_Tobago_%28orthographic_projection%29.svg/80px-Trinidad_and_Tobago_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Cuba",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/01/Cuba_%28orthographic_projection%29.svg/80px-Cuba_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Dominican Republic",
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/95/Dominican_Republic_%28orthographic_projection%29.svg/80px-Dominican_Republic_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Haiti",
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Haiti_%28orthographic_projection%29.svg/80px-Haiti_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Jamaica",
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Jamaica_%28orthographic_projection%29.svg/80px-Jamaica_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Argentina",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/bd/Argentina_orthographic.svg/80px-Argentina_orthographic.svg"
    },
    {
        "alt": "Bolivia",
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Bolivia_%28orthographic_projection%29.svg/80px-Bolivia_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Brazil",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/bc/BRA_orthographic.svg/80px-BRA_orthographic.svg"
    },
    {
        "alt": "Chile",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d5/Chile_%28orthographic_projection%29.svg/80px-Chile_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Colombia",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6f/COL_orthographic.svg/80px-COL_orthographic.svg"
    },
    {
        "alt": "Ecuador",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c8/Ecuador_%28orthographic_projection%29.svg/80px-Ecuador_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Guyana",
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/20/Guyana_%28orthographic_projection%29.svg/80px-Guyana_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Paraguay",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/80/Paraguay_%28orthographic_projection%29.svg/80px-Paraguay_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Peru",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/84/Peru_%28orthographic_projection%29.svg/80px-Peru_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Suriname",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/87/Suriname_%28orthographic_projection%29.svg/80px-Suriname_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Uruguay",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/8d/Uruguay_%28orthographic_projection%29.svg/80px-Uruguay_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Venezuela",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/5e/VEN_orthographic.svg/80px-VEN_orthographic.svg"
    },
    {
        "alt": "China",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/78/People%27s_Republic_of_China_%28orthographic_projection%29.svg/80px-People%27s_Republic_of_China_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Japan",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/62/Japan_%28orthographic_projection%29.svg/80px-Japan_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Mongolia",
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Mongolia_%28orthographic_projection%29.svg/80px-Mongolia_%28orthographic_projection%29.svg"
    },
    {
        "alt": "North Korea",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7b/North_Korea_%28orthographic_projection%29.svg/80px-North_Korea_%28orthographic_projection%29.svg"
    },
    {
        "alt": "South Korea",
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/95/South_Korea_%28orthographic_projection%29.svg/80px-South_Korea_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Kazakhstan",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Kazakhstan_%28orthographic_projection%29.svg/80px-Kazakhstan_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Tajikistan",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a1/Tajikistan_%28orthographic_projection%29.svg/80px-Tajikistan_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Kyrgyzstan",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7c/Kyrgyzstan_%28orthographic_projection%29.svg/80px-Kyrgyzstan_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Uzbekistan",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/76/%D0%A3%D0%B7%D0%B1%D0%B5%D0%BA%D0%B8%D1%81%D1%82%D0%B0%D0%BD_%D0%BD%D0%B0_%D0%B3%D0%BB%D0%BE%D0%B1%D1%83%D1%81%D0%B5.svg/80px-%D0%A3%D0%B7%D0%B1%D0%B5%D0%BA%D0%B8%D1%81%D1%82%D0%B0%D0%BD_%D0%BD%D0%B0_%D0%B3%D0%BB%D0%BE%D0%B1%D1%83%D1%81%D0%B5.svg"
    },
    {
        "alt": "Indonesia",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/05/Indonesia_%28orthographic_projection%29.svg/80px-Indonesia_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Malaysia",
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/23/Malaysia_%28orthographic_projection%29.svg/80px-Malaysia_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Philippines",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/50/Philippines_%28orthographic_projection%29.svg/80px-Philippines_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Thailand",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Thailand_%28orthographic_projection%29.svg/80px-Thailand_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Afghanistan",
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/19/Afghanistan_%28orthographic_projection%29.svg/80px-Afghanistan_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Bangladesh",
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/f2/Bangladesh_%28orthographic_projection%29.svg/80px-Bangladesh_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Bhutan",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/ce/Bhutan_%28orthographic_projection%29.svg/80px-Bhutan_%28orthographic_projection%29.svg"
    },
    {
        "alt": "India",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/bb/India_%28orthographic_projection%29.svg/80px-India_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Maldives",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Maldives_%28orthographic_projection%29.svg/80px-Maldives_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Nepal",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Nepal_%28orthographic_projection%29.svg/80px-Nepal_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Pakistan",
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/PAK_orthographic.svg/80px-PAK_orthographic.svg"
    },
    {
        "alt": "Sri Lanka",
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/96/Sri_Lanka_%28orthographic_projection%29.svg/80px-Sri_Lanka_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Georgia",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Georgia_%28orthographic_projection%29.svg/80px-Georgia_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Armenia",
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/96/Armenia_%28orthographic_projection%29.svg/80px-Armenia_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Azerbaijan",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/01/Azerbaijan_%28orthographic_projection%29.svg/80px-Azerbaijan_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Iran",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a8/Iran_%28orthographic_projection%29.svg/80px-Iran_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Iraq",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/59/Iraq_%28orthographic_projection%29.svg/80px-Iraq_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Israel",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/42/Israel_%28orthographic_projection%29.svg/80px-Israel_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Jordan",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b2/Jordan_%28orthographic_projection%29.svg/80px-Jordan_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Saudi Arabia",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/47/Saudi_Arabia_%28orthographic_projection%29.svg/80px-Saudi_Arabia_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Palestine",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/ad/State_of_Palestine_%28orthographic_projection%29.svg/80px-State_of_Palestine_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Syria",
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/11/Syria_%28orthographic_projection%29.svg/80px-Syria_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Lebanon",
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/96/Lebanon_%28orthographic_projection%29.svg/80px-Lebanon_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Turkey",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/dd/Turkey_%28orthographic_projection%29.svg/80px-Turkey_%28orthographic_projection%29.svg"
    },
    {
        "alt": "United Arab Emirates",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/cd/United_Arab_Emirates_%28orthographic_projection%29.svg/80px-United_Arab_Emirates_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Albania",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d5/Albania_%28orthographic_projection%29.svg/80px-Albania_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Armenia",
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/96/Armenia_%28orthographic_projection%29.svg/80px-Armenia_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Azerbaijan",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/01/Azerbaijan_%28orthographic_projection%29.svg/80px-Azerbaijan_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Belarus",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Belarus_%28orthographic_projection%29.svg/80px-Belarus_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Belgium",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/79/Belgium_%28orthographic_projection%29.svg/80px-Belgium_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Bosnia and Herzegovina",
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/24/Bosnia_and_Herzegovina_%28orthographic_projection%29.svg/80px-Bosnia_and_Herzegovina_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Bulgaria",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Bulgaria_%28orthographic_projection%29.svg/80px-Bulgaria_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Denmark",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Denmark_%28orthographic_projection%29.svg/80px-Denmark_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Finland",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Finland_%28orthographic_projection%29.svg/80px-Finland_%28orthographic_projection%29.svg"
    },
    {
        "alt": "France",
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e1/France_%28orthographic_projection%29.svg/80px-France_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Georgia",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Georgia_%28orthographic_projection%29.svg/80px-Georgia_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Germany",
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/95/Germany_%28orthographic_projection%29.svg/80px-Germany_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Iceland",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Iceland_%28orthographic_projection%29.svg/80px-Iceland_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Italy",
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Italy_%28orthographic_projection%29.svg/80px-Italy_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Kazakhstan",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Kazakhstan_%28orthographic_projection%29.svg/80px-Kazakhstan_%28orthographic_projection%29.svg"
    },
    {
        "alt": "North Macedonia",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/0a/North_Macedonia_%28orthographic_projection%29.svg/80px-North_Macedonia_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Montenegro",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/38/Montenegro_%28orthographic_projection%29.svg/80px-Montenegro_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Netherlands",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/52/Netherlands_%28orthographic_projection%29.svg/80px-Netherlands_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Norway",
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/28/Norway_%28orthographic_projection%29.svg/80px-Norway_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Poland",
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Poland_%28orthographic_projection%29.svg/80px-Poland_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Portugal",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/8f/Portugal_%28orthographic_projection%29.svg/80px-Portugal_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Romania",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/87/Romania_%28orthographic_projection%29.svg/80px-Romania_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Russia",
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Russian_Federation_%28orthographic_projection%29_-_Crimea_disputed.svg/80px-Russian_Federation_%28orthographic_projection%29_-_Crimea_disputed.svg"
    },
    {
        "alt": "Serbia",
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e8/Serbia_%28orthographic_projection%29.svg/80px-Serbia_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Spain",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/81/Spain_%28orthographic_projection%29.svg/80px-Spain_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Sweden",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/30/Sweden_%28orthographic_projection%29.svg/80px-Sweden_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Switzerland",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/63/Switzerland_%28orthographic_projection%29.svg/80px-Switzerland_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Turkey",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/dd/Turkey_%28orthographic_projection%29.svg/80px-Turkey_%28orthographic_projection%29.svg"
    },
    {
        "alt": "United Kingdom",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/07/United_Kingdom_%28orthographic_projection%29.svg/80px-United_Kingdom_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Australia",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7d/Australia_%28orthographic_projection%29.svg/80px-Australia_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Fiji",
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Fiji_%28orthographic_projection%29.svg/80px-Fiji_%28orthographic_projection%29.svg"
    },
    {
        "alt": "New Zealand",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d8/New_Zealand_%28orthographic_projection%29.svg/80px-New_Zealand_%28orthographic_projection%29.svg"
    },
    {
        "alt": "Papua New Guinea",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/79/Papua_New_Guinea_%28orthographic_projection%29.svg/80px-Papua_New_Guinea_%28orthographic_projection%29.svg"
    }
]
'''

# Converter JSON para uma lista de dicionários
data = json.loads(json_data)

# Percorrer cada item na lista
for item in data:
    # Obter o índice da primeira ocorrência de ".svg" na URL
    index = item['url'].find('.svg')
    if index != -1:
        # Remover o texto após a primeira ocorrência de ".svg"
        item['url'] = item['url'][:index + 4]

# Converter a lista de dicionários de volta para JSON
updated_json_data = json.dumps(data, indent=4)

# Imprimir o JSON atualizado
print(updated_json_data)
