const fs = require("fs");

const descricao = {
    "azerbaijan": {
        "descricao_pt": "O Azerbaijão, oficialmente República do Azerbaijão, é um país localizado no Cáucaso, no cruzamento entre a Ásia Ocidental e a Europa Oriental. Sua história é marcada por séculos de influência persa, turca e russa, e conquistou independência da União Soviética em 1991. O país é rico em recursos naturais, especialmente petróleo e gás, que desempenham um papel crucial em sua economia. Atualmente, o Azerbaijão é conhecido por sua modernização e desenvolvimento econômico, bem como pela sua herança cultural e arquitetura única.",
        "descricao_en": "Azerbaijan, officially the Republic of Azerbaijan, is a country located in the Caucasus, at the crossroads of Western Asia and Eastern Europe. Its history is marked by centuries of Persian, Turkish, and Russian influence, and it gained independence from the Soviet Union in 1991. The country is rich in natural resources, especially oil and gas, which play a crucial role in its economy. Today, Azerbaijan is known for its modernization and economic development, as well as its cultural heritage and unique architecture."
    },
    "bahamas": {
        "descricao_pt": "As Bahamas, oficialmente Comunidade das Bahamas, são um arquipélago situado no oceano Atlântico, composto por numerosas ilhas, ilhotas e ilhotas rochosas. A história das Bahamas é marcada pela presença dos povos indígenas Lucayans, bem como pela colonização espanhola e britânica. Atualmente, o país é um destino turístico popular devido às suas praias deslumbrantes, águas cristalinas e clima tropical. Além do turismo, as Bahamas têm uma economia baseada na pesca e na indústria financeira internacional.",
        "descricao_en": "The Bahamas, officially the Commonwealth of The Bahamas, is an archipelago situated in the Atlantic Ocean, comprising numerous islands, islets, and rocky outcrops. The history of The Bahamas is marked by the presence of the indigenous Lucayan people, as well as Spanish and British colonization. Today, the country is a popular tourist destination, known for its stunning beaches, crystal-clear waters, and tropical climate. Besides tourism, The Bahamas has an economy based on fishing and the international financial industry."
    },
    "bahrain": {
        "descricao_pt": "O Bahrein, oficialmente o Reino do Bahrein, é uma pequena nação insular no Golfo Pérsico. Sua história remonta a civilizações antigas e foi influenciada por impérios como os persas e os portugueses. Nos tempos modernos, o Bahrein emergiu como um centro financeiro e comercial no Golfo, graças à sua economia diversificada, incluindo o setor de petróleo. Atualmente, o país é conhecido por sua arquitetura moderna, cultura vibrante e como um importante centro financeiro no Oriente Médio.",
        "descricao_en": "Bahrain, officially the Kingdom of Bahrain, is a small island nation in the Persian Gulf. Its history dates back to ancient civilizations and has been influenced by empires like the Persians and the Portuguese. In modern times, Bahrain has emerged as a financial and commercial hub in the Gulf, thanks to its diversified economy, including the oil sector. Today, the country is known for its modern architecture, vibrant culture, and as a significant financial center in the Middle East."
    },
    "bangladesh": {
        "descricao_pt": "Bangladesh, oficialmente a República Popular de Bangladesh, é um país do sul da Ásia. Sua história é marcada pela luta pela independência do Paquistão em 1971. O país é caracterizado por uma paisagem dominada por rios e planícies e é um dos países mais densamente povoados do mundo. Atualmente, Bangladesh enfrenta desafios relacionados ao desenvolvimento, mas também é conhecido por sua rica cultura, têxteis e indústria de vestuário, bem como pela produção de arroz, que é um alimento básico na região.",
        "descricao_en": "Bangladesh, officially the People's Republic of Bangladesh, is a country in South Asia. Its history is marked by the struggle for independence from Pakistan in 1971. The country is characterized by a landscape dominated by rivers and plains and is one of the most densely populated countries in the world. Today, Bangladesh faces challenges related to development, but it is also known for its rich culture, textiles and garment industry, as well as rice production, which is a staple in the region."
    },
    "barbados": {
        "descricao_pt": "Barbados, oficialmente o Estado de Barbados, é uma ilha situada no mar do Caribe. Sua história é influenciada pela colonização britânica e pela escravidão. Atualmente, Barbados é um destino turístico popular, conhecido por suas praias de areias brancas e águas cristalinas. Além do turismo, a economia do país depende da produção de açúcar, rum e offshore financeiro. Barbados também tem uma rica herança cultural, incluindo música e festivais vibrantes.",
        "descricao_en": "Barbados, officially the State of Barbados, is an island located in the Caribbean Sea. Its history is influenced by British colonization and slavery. Today, Barbados is a popular tourist destination, known for its white sandy beaches and crystal-clear waters. Besides tourism, the country's economy relies on sugar production, rum, and offshore finance. Barbados also has a rich cultural heritage, including vibrant music and festivals."
    },
    "belarus": {
        "descricao_pt": "Belarus, oficialmente a República de Belarus, é uma nação localizada na Europa Oriental. Sua história é profundamente influenciada pela União Soviética, da qual fez parte. Atualmente, o país é conhecido por sua economia planificada, liderada pelo governo, e por seu presidente de longa data, Alexander Lukashenko. Belarus tem uma herança cultural rica, com influências russas, polonesas e lituanas. O país é conhecido por sua produção de tratores e maquinaria pesada.",
        "descricao_en": "Belarus, officially the Republic of Belarus, is a nation located in Eastern Europe. Its history is deeply influenced by the Soviet Union, of which it was a part. Today, the country is known for its planned economy, government-led, and its long-time president, Alexander Lukashenko. Belarus has a rich cultural heritage, with Russian, Polish, and Lithuanian influences. The country is known for its production of tractors and heavy machinery."
    },
    "belgium": {
        "descricao_pt": "A Bélgica, oficialmente o Reino da Bélgica, é um país situado no coração da Europa. Sua história é marcada por séculos de influência estrangeira devido à sua localização geográfica. Atualmente, a Bélgica é conhecida por ser a sede de várias instituições da União Europeia, incluindo o Parlamento Europeu. O país é famoso por sua culinária, incluindo chocolates, cervejas e batatas fritas. Além disso, a Bélgica tem uma rica herança artística e é o lar de várias cidades históricas encantadoras.",
        "descricao_en": "Belgium, officially the Kingdom of Belgium, is a country located in the heart of Europe. Its history is marked by centuries of foreign influence due to its geographical location. Today, Belgium is known for being the headquarters of several European Union institutions, including the European Parliament. The country is famous for its cuisine, including chocolates, beers, and french fries. Additionally, Belgium has a rich artistic heritage and is home to several charming historic cities."
    },
    "belize": {
        "descricao_pt": "Belize, oficialmente a Comunidade de Belize, é uma nação da América Central, com litoral no mar do Caribe. Sua história é influenciada pela presença de povos maias e pela colonização britânica. Atualmente, Belize é conhecido por sua biodiversidade, incluindo recifes de coral e selvas tropicais. O turismo desempenha um papel significativo na economia do país, com atividades como mergulho e observação de pássaros sendo populares. A nação também é famosa por sua herança multicultural e língua oficial, o inglês.",
        "descricao_en": "Belize, officially the Belizean Community, is a nation in Central America with a coastline along the Caribbean Sea. Its history is influenced by the presence of Mayan peoples and British colonization. Today, Belize is known for its biodiversity, including coral reefs and tropical jungles. Tourism plays a significant role in the country's economy, with activities like diving and bird-watching being popular. The nation is also famous for its multicultural heritage and official language, English."
    },
    "benin": {
        "descricao_pt": "O Benin, oficialmente a República do Benin, é um país da África Ocidental com uma rica herança cultural. Sua história inclui reinos antigos, como o Reino de Dahomey, e o envolvimento no comércio de escravos. Atualmente, o Benin é conhecido por sua arte e artesanato tradicionais, incluindo máscaras e esculturas. A economia do país é baseada na agricultura e na produção de algodão. Além disso, o Benin é famoso por ser o berço da religião vodu, que desempenha um papel importante na cultura local.",
        "descricao_en": "Benin, officially the Republic of Benin, is a country in West Africa with a rich cultural heritage. Its history includes ancient kingdoms like the Kingdom of Dahomey and involvement in the slave trade. Today, Benin is known for its traditional art and craftsmanship, including masks and sculptures. The country's economy is based on agriculture and cotton production. Additionally, Benin is famous for being the birthplace of Vodou religion, which plays a significant role in local culture."
    },
    "bhutan": {
        "descricao_pt": "O Butão, oficialmente o Reino do Butão, é um país situado na cordilheira do Himalaia, na Ásia. Sua história é marcada por séculos de isolamento e pela preservação de sua cultura única. Atualmente, o Butão é conhecido por sua ênfase na felicidade nacional bruta, um indicador alternativo de progresso que leva em consideração o bem-estar espiritual e psicológico da população. O país é famoso por suas paisagens deslumbrantes, mosteiros antigos e por ser o último reino budista do Himalaia.",
        "descricao_en": "Bhutan, officially the Kingdom of Bhutan, is a country situated in the Himalayas in Asia. Its history is marked by centuries of isolation and the preservation of its unique culture. Today, Bhutan is known for its emphasis on Gross National Happiness, an alternative indicator of progress that takes into account the spiritual and psychological well-being of the population. The country is famous for its stunning landscapes, ancient monasteries, and for being the last Buddhist kingdom in the Himalayas."
    },
    "brazil": {
        "descricao_pt": "O Brasil, oficialmente República Federativa do Brasil, é um país latino-americano situado no leste da América do Sul. É o maior país da região e o mais populoso. Colonizado pelos portugueses entre os séculos XV e XIX, o país é extremamente diverso, com influências europeias e africanas devido ao comércio de escravos, além das influências dos povos indígenas. O Brasil é marcado por suas grandes belezas naturais e riqueza cultural, além de seu destaque no futebol, o esporte mais popular do país.",
        "descricao_en": "Brazil, officially the Federative Republic of Brazil, is a Latin American country located in the eastern part of South America. It is the largest country in the region and the most populous. Colonized by the Portuguese between the 15th and 19th centuries, the country is extremely diverse, with significant European and African influences due to the slave trade, as well as influences from indigenous peoples. Brazil is known for its vast natural beauty, cultural richness, and its outstanding performance in football, the country's most popular sport."
    },
    "bolivia": {
        "descricao_pt": "A Bolívia é um país localizado no coração da América do Sul. Sua história é marcada pela civilização inca e pela colonização espanhola. A Bolívia é conhecida por sua diversidade geográfica, incluindo as montanhas dos Andes e a Amazônia. Atualmente, o país enfrenta desafios econômicos e políticos, mas sua cultura e tradições indígenas continuam a desempenhar um papel importante na sociedade boliviana.",
        "descricao_en": "Bolivia is a country located in the heart of South America. Its history is marked by the Inca civilization and Spanish colonization. Bolivia is known for its geographic diversity, including the Andes Mountains and the Amazon rainforest. Currently, the country faces economic and political challenges, but its indigenous culture and traditions continue to play a significant role in Bolivian society."
    },
    "bosnia and herzegovina": {
        "descricao_pt": "Bósnia e Herzegovina é um país dos Bálcãs, na Europa, com uma história complexa. Foi parte do Império Otomano e do Império Austro-Húngaro. Após a Guerra da Bósnia na década de 1990, o país se tornou independente. É conhecido por sua diversidade étnica e religiosa. Atualmente, a Bósnia e Herzegovina está em busca de estabilidade política e econômica.",
        "descricao_en": "Bosnia and Herzegovina is a country in the Balkans, in Europe, with a complex history. It was part of the Ottoman Empire and the Austro-Hungarian Empire. After the Bosnian War in the 1990s, the country became independent. It is known for its ethnic and religious diversity. Currently, Bosnia and Herzegovina is striving for political and economic stability."
    },
    "botswana": {
        "descricao_pt": "Botswana, um país no sul da África, é conhecido por sua estabilidade política e crescimento econômico. Sua história inclui períodos de domínio britânico e a independência em 1966. A nação é dominada pelo deserto do Kalahari, mas também possui áreas de rica vida selvagem. Hoje, Botswana é um dos países mais prósperos da África, com um governo democrático sólido.",
        "descricao_en": "Botswana, a country in southern Africa, is known for its political stability and economic growth. Its history includes periods of British rule and independence in 1966. The nation is dominated by the Kalahari Desert but also boasts areas of rich wildlife. Today, Botswana is one of the most prosperous countries in Africa, with a solid democratic government."
    },
    "brunei": {
        "descricao_pt": "Brunei, localizado na ilha de Bornéu, é um pequeno país rico em petróleo. Sua história envolve o comércio com potências coloniais e a influência islâmica. Brunei é uma monarquia absoluta governada por um sultão. Atualmente, o país desfruta de prosperidade econômica devido às suas reservas de petróleo, oferecendo um alto padrão de vida para seus cidadãos.",
        "descricao_en": "Brunei, located on the island of Borneo, is a small, oil-rich country. Its history involves trade with colonial powers and Islamic influence. Brunei is an absolute monarchy ruled by a sultan. Currently, the country enjoys economic prosperity due to its oil reserves, providing a high standard of living for its citizens."
    },
    "bulgaria": {
        "descricao_pt": "Bulgária, no sudeste da Europa, possui uma rica herança histórica que remonta aos trácios e ao Império Romano. Depois do domínio otomano, o país conquistou independência no século XIX. Hoje, é membro da União Europeia e da OTAN. A Bulgária enfrenta desafios econômicos, mas seu patrimônio cultural e sua beleza natural atraem visitantes de todo o mundo.",
        "descricao_en": "Bulgaria, in southeastern Europe, has a rich historical heritage dating back to the Thracians and the Roman Empire. After Ottoman rule, the country gained independence in the 19th century. Today, it is a member of the European Union and NATO. Bulgaria faces economic challenges, but its cultural heritage and natural beauty attract visitors from around the world."
    },
    "burkina faso": {
        "descricao_pt": "Burkina Faso, na África Ocidental, é um país sem litoral com uma história que inclui impérios antigos e o domínio colonial francês. O país obteve independência em 1960 e passou por mudanças políticas ao longo dos anos. Atualmente, Burkina Faso enfrenta desafios econômicos e de segurança, mas sua cultura vibrante e hospitalidade são pontos fortes.",
        "descricao_en": "Burkina Faso, in West Africa, is a landlocked country with a history that includes ancient empires and French colonial rule. The country gained independence in 1960 and has undergone political changes over the years. Currently, Burkina Faso faces economic and security challenges, but its vibrant culture and hospitality are strengths."
    },
    "burundi": {
        "descricao_pt": "Burundi, localizado na região dos Grandes Lagos da África, é um país com uma história marcada por tensões étnicas. Após a independência da Bélgica, o país enfrentou conflitos. Atualmente, Burundi está trabalhando para a reconciliação e a estabilidade política. Sua população é diversa, e o país é conhecido por suas belas paisagens naturais.",
        "descricao_en": "Burundi, located in the Great Lakes region of Africa, is a country with a history marked by ethnic tensions. After gaining independence from Belgium, the country faced conflicts. Currently, Burundi is working towards reconciliation and political stability. Its population is diverse, and the country is known for its beautiful natural landscapes."
    },
    "cambodia": {
        "descricao_pt": "Camboja, no sudeste asiático, possui uma história rica, incluindo o Império Khmer e o domínio francês. Após anos de conflito e genocídio, o país busca estabilidade e desenvolvimento. A cultura cambojana é influenciada pelo budismo, e os templos de Angkor Wat são um marco famoso. Atualmente, o turismo desempenha um papel importante na economia do Camboja.",
        "descricao_en": "Cambodia, in Southeast Asia, has a rich history, including the Khmer Empire and French colonial rule. After years of conflict and genocide, the country is seeking stability and development. Cambodian culture is influenced by Buddhism, and the temples of Angkor Wat are a famous landmark. Currently, tourism plays a significant role in Cambodia's economy."
    },
    "cameroon": {
        "descricao_pt": "Camarões, na África Central, possui uma diversidade étnica e geográfica impressionante. Sua história inclui impérios pré-coloniais e domínio francês e britânico. O país obteve independência na década de 1960. Atualmente, Camarões enfrenta desafios políticos e econômicos, mas sua rica cultura e biodiversidade são pontos fortes.",
        "descricao_en": "Cameroon, in Central Africa, has impressive ethnic and geographical diversity. Its history includes pre-colonial empires and French and British rule. The country gained independence in the 1960s. Currently, Cameroon faces political and economic challenges, but its rich culture and biodiversity are strengths."
    },
    "canada": {
        "descricao_pt": "O Canadá, um país localizado na América do Norte, é conhecido por sua vasta extensão territorial e beleza natural deslumbrante. A história do Canadá é marcada por sua colonização europeia, com influências francesas e britânicas. Atualmente, o país é uma nação multicultural, com uma população diversificada e um sistema de saúde e educação de alta qualidade.",
        "descricao_en": "Canada, a country located in North America, is known for its vast landmass and stunning natural beauty. The history of Canada is marked by European colonization, with French and British influences. Today, the country is a multicultural nation with a diverse population and a high-quality healthcare and education system."
    },
    "cape verde": {
        "descricao_pt": "Cabo Verde, localizado no oceano Atlântico, é um arquipélago formado por ilhas vulcânicas. A história do país está ligada à colonização portuguesa e ao comércio de escravos. Atualmente, Cabo Verde é uma nação independente, conhecida por sua música, cultura e belas praias.",
        "descricao_en": "Cape Verde, located in the Atlantic Ocean, is an archipelago of volcanic islands. The country's history is tied to Portuguese colonization and the slave trade. Today, Cape Verde is an independent nation known for its music, culture, and beautiful beaches."
    },
    "central african republic": {
        "descricao_pt": "A República Centro-Africana, situada no coração da África, tem uma história complexa de conflitos e instabilidade política. Apesar dos desafios, o país é rico em recursos naturais, incluindo vida selvagem e paisagens deslumbrantes. Na atualidade, a República Centro-Africana busca estabilidade e desenvolvimento.",
        "descricao_en": "The Central African Republic, located in the heart of Africa, has a complex history of conflicts and political instability. Despite the challenges, the country is rich in natural resources, including wildlife and stunning landscapes. Today, the Central African Republic seeks stability and development."
    },
    "chad": {
        "descricao_pt": "Chade, um país da África Central, possui uma história marcada por culturas diversas e civilizações antigas. Atualmente, o país enfrenta desafios socioeconômicos, mas é abençoado com paisagens variadas e uma população resiliente.",
        "descricao_en": "Chad, a country in Central Africa, has a history marked by diverse cultures and ancient civilizations. Today, the country faces socio-economic challenges but is blessed with diverse landscapes and a resilient population."
    },
    "chile": {
        "descricao_pt": "O Chile, uma nação alongada na costa oeste da América do Sul, possui uma história rica, incluindo o legado dos povos indígenas e influências coloniais espanholas. No presente, o Chile é conhecido por sua estabilidade política e economia em crescimento, além de suas paisagens espetaculares, como os Andes e o deserto do Atacama.",
        "descricao_en": "Chile, a long-nation on the west coast of South America, has a rich history, including the legacy of indigenous peoples and Spanish colonial influences. Today, Chile is known for its political stability and growing economy, as well as its spectacular landscapes, such as the Andes and the Atacama Desert."
    },
    "china": {
        "descricao_pt": "A China, um país no leste da Ásia, tem uma história milenar e é uma das civilizações mais antigas do mundo. Atualmente, a China é uma potência global, com uma economia em crescimento, cultura rica e uma população numerosa.",
        "descricao_en": "China, a country in East Asia, has a millennia-old history and is one of the world's oldest civilizations. Today, China is a global powerhouse, with a growing economy, rich culture, and a large population."
    },
    "colombia": {
        "descricao_pt": "A Colômbia, localizada na América do Sul, tem uma história complexa de culturas indígenas, colonização espanhola e conflitos internos. Na atualidade, a Colômbia está em processo de superar décadas de conflitos e violência, buscando paz e desenvolvimento.",
        "descricao_en": "Colombia, located in South America, has a complex history of indigenous cultures, Spanish colonization, and internal conflicts. Today, Colombia is in the process of overcoming decades of conflict and violence, seeking peace and development."
    },
    "comoros": {
        "descricao_pt": "As Comores, um pequeno arquipélago no Oceano Índico, têm uma história influenciada por várias culturas. Atualmente, o país enfrenta desafios econômicos, mas é conhecido por suas praias paradisíacas e cultura única.",
        "descricao_en": "Comoros, a small archipelago in the Indian Ocean, has a history influenced by various cultures. Today, the country faces economic challenges but is known for its paradise beaches and unique culture."
    },
    "democratic republic of congo": {
        "descricao_pt": "A República Democrática do Congo, na África Central, possui uma história complexa de colonização, independência e conflitos. O país é rico em recursos naturais, mas também enfrentou instabilidade política. Atualmente, a RD Congo busca estabilidade e desenvolvimento.",
        "descricao_en": "The Democratic Republic of Congo, in Central Africa, has a complex history of colonization, independence, and conflicts. The country is rich in natural resources but has also faced political instability. Today, the DRC seeks stability and development."
    },
    "congo": {
        "descricao_pt": "A República do Congo, localizada na África Central, tem uma rica história marcada por impérios antigos e colonização europeia. Com uma localização estratégica ao longo do rio Congo, o país desempenhou um papel importante no comércio de escravos. Hoje, o Congo é conhecido por sua diversidade étnica e cultural, bem como por sua exuberante vida selvagem nas florestas tropicais.",
        "descricao_en": "The Republic of the Congo, located in Central Africa, has a rich history marked by ancient empires and European colonization. With a strategic location along the Congo River, the country played a significant role in the slave trade. Today, Congo is known for its ethnic and cultural diversity, as well as its lush wildlife in the tropical rainforests."
    },
    "costa rica": {
        "descricao_pt": "A Costa Rica, na América Central, tem uma história de paz e estabilidade política. Sua geografia é impressionante, com praias deslumbrantes, vulcões ativos e selvas exuberantes. Atualmente, é reconhecida por seu compromisso com a conservação ambiental, com parques nacionais e uma ampla variedade de biodiversidade.",
        "descricao_en": "Costa Rica, in Central America, has a history of peace and political stability. Its geography is stunning, with gorgeous beaches, active volcanoes, and lush jungles. Today, it is renowned for its commitment to environmental conservation, with national parks and a wide variety of biodiversity."
    },
    "croatia": {
        "descricao_pt": "A Croácia, situada no sudeste da Europa, tem uma história marcada por impérios e guerras. Com sua costa no Mar Adriático e inúmeras ilhas, é famosa por suas belezas naturais e patrimônio histórico, incluindo a cidade murada de Dubrovnik. Atualmente, a Croácia é um destino turístico popular e membro da União Europeia.",
        "descricao_en": "Croatia, located in Southeast Europe, has a history marked by empires and wars. With its coastline along the Adriatic Sea and numerous islands, it is famous for its natural beauty and historical heritage, including the walled city of Dubrovnik. Today, Croatia is a popular tourist destination and a member of the European Union."
    },
    "cuba": {
        "descricao_pt": "Cuba, uma ilha no Caribe, tem uma história complexa que inclui colonização espanhola, revolução e socialismo. Sua localização estratégica a tornou um ponto de interesse para várias nações. Atualmente, Cuba é conhecida por sua cultura vibrante, música, dança e sistema de saúde universal.",
        "descricao_en": "Cuba, an island in the Caribbean, has a complex history that includes Spanish colonization, revolution, and socialism. Its strategic location made it a point of interest for various nations. Today, Cuba is known for its vibrant culture, music, dance, and universal healthcare system."
    },
    "cyprus": {
        "descricao_pt": "Chipre, no leste do Mediterrâneo, tem uma história rica e complexa devido à sua localização estratégica. Com divisões étnicas e conflitos, o país permanece dividido, mas a parte sul é conhecida por suas belas praias e história antiga. Atualmente, Chipre é um destino turístico popular.",
        "descricao_en": "Cyprus, in the eastern Mediterranean, has a rich and complex history due to its strategic location. With ethnic divisions and conflicts, the country remains divided, but the southern part is known for its beautiful beaches and ancient history. Today, Cyprus is a popular tourist destination."
    },
    "czechia": {
        "descricao_pt": "A República Tcheca, localizada na Europa Central, possui uma história marcada por reinos e impérios. Praga, sua capital, é famosa por sua arquitetura medieval e cervejas. Atualmente, a República Tcheca é uma nação moderna, membro da União Europeia e conhecida por sua rica herança cultural.",
        "descricao_en": "Czechia, located in Central Europe, has a history marked by kingdoms and empires. Prague, its capital, is famous for its medieval architecture and beers. Today, Czechia is a modern nation, a member of the European Union, and known for its rich cultural heritage."
    },
    "denmark": {
        "descricao_pt": "A Dinamarca, no norte da Europa, tem uma história que remonta a reinos vikings. É um país com uma elevada qualidade de vida e um sistema de bem-estar social abrangente. Atualmente, a Dinamarca é conhecida por sua gastronomia, design e liderança em questões de sustentabilidade.",
        "descricao_en": "Denmark, in northern Europe, has a history dating back to Viking kingdoms. It is a country with a high quality of life and a comprehensive social welfare system. Today, Denmark is known for its cuisine, design, and leadership in sustainability issues."
    },
    "djibouti": {
        "descricao_pt": "Djibouti, na região do Chifre da África, tem uma história ligada a antigas rotas comerciais. Sua localização estratégica no Mar Vermelho torna-o importante para o comércio internacional. Atualmente, Djibouti é um centro logístico crucial e um ponto de entrada para o Corno de África.",
        "descricao_en": "Djibouti, in the Horn of Africa region, has a history tied to ancient trade routes. Its strategic location on the Red Sea makes it important for international trade. Today, Djibouti is a crucial logistical hub and an entry point to the Horn of Africa."
    },
    "dominica": {
        "descricao_pt": "Dominica, no Caribe, é conhecida por sua natureza intocada, incluindo florestas tropicais e vulcões. Sua história inclui colonização europeia e influências africanas. Atualmente, a ilha é um destino popular para ecoturismo e tem uma cultura rica e diversificada.",
        "descricao_en": "Dominica, in the Caribbean, is known for its pristine nature, including rainforests and volcanoes. Its history includes European colonization and African influences. Today, the island is a popular destination for ecotourism and has a rich and diverse culture."
    },
    "dominican republic": {
        "descricao_pt": "A República Dominicana, também no Caribe, compartilha a ilha de Hispaniola com o Haiti. Sua história inclui a colonização espanhola e lutas pela independência. Atualmente, o país é famoso por suas praias deslumbrantes, resorts e cultura vibrante, incluindo a dança merengue.",
        "descricao_en": "The Dominican Republic, also in the Caribbean, shares the island of Hispaniola with Haiti. Its history includes Spanish colonization and struggles for independence. Today, the country is famous for its stunning beaches, resorts, and vibrant culture, including the merengue dance."
    },
    "ecuador": {
        "descricao_pt": "O Equador, oficialmente República do Equador, é um país situado na América do Sul. Sua história é marcada por civilizações antigas, como os Incas, antes da chegada dos espanhóis no século XVI. Atualmente, o Equador é conhecido por sua incrível diversidade geográfica, que inclui as montanhas dos Andes, a floresta amazônica e as belas praias do litoral. Além disso, o país é famoso por sua biodiversidade única, abrigando uma grande variedade de espécies de plantas e animais.",
        "descricao_en": "Ecuador, officially the Republic of Ecuador, is a country located in South America. Its history is marked by ancient civilizations, such as the Incas, before the arrival of the Spanish in the 16th century. Today, Ecuador is known for its incredible geographical diversity, including the Andes Mountains, the Amazon rainforest, and the beautiful coastal beaches. Moreover, the country is famous for its unique biodiversity, hosting a wide variety of plant and animal species."
    },
    "egypt": {
        "descricao_pt": "O Egito, oficialmente República Árabe do Egito, é um país do norte da África conhecido por sua rica história e legado cultural. O Egito é o berço de uma das civilizações mais antigas do mundo, com uma história que remonta a milênios. Atualmente, o país é famoso por suas antigas pirâmides, como as pirâmides de Gizé, bem como pelo rio Nilo, que desempenhou um papel vital na civilização egípcia. O Egito é uma nação vibrante com uma mistura de tradição e modernidade.",
        "descricao_en": "Egypt, officially the Arab Republic of Egypt, is a country in North Africa known for its rich history and cultural heritage. Egypt is the birthplace of one of the world's oldest civilizations, with a history that spans millennia. Today, the country is famous for its ancient pyramids, such as the Pyramids of Giza, as well as the Nile River, which played a vital role in Egyptian civilization. Egypt is a vibrant nation with a blend of tradition and modernity."
    },
    "el salvador": {
        "descricao_pt": "El Salvador, oficialmente República de El Salvador, é um país da América Central. Sua história inclui períodos de domínio indígena, colonização espanhola e, posteriormente, independência. Atualmente, El Salvador enfrenta desafios econômicos e sociais, mas também é conhecido por sua cultura, música e culinária únicas. As praias de El Salvador atraem turistas devido ao seu surfe de classe mundial.",
        "descricao_en": "El Salvador, officially the Republic of El Salvador, is a country in Central America. Its history includes periods of indigenous rule, Spanish colonization, and subsequent independence. Today, El Salvador faces economic and social challenges, but it is also known for its unique culture, music, and cuisine. El Salvador's beaches attract tourists due to their world-class surfing."
    },
    "equatorial guinea": {
        "descricao_pt": "Guiné Equatorial, oficialmente República da Guiné Equatorial, é um país da África Central localizado na costa oeste da África. Sua história inclui o domínio colonial por diferentes potências europeias, incluindo Espanha e França. Atualmente, a Guiné Equatorial é rica em recursos naturais, como petróleo, mas enfrenta desafios relacionados à governança e aos direitos humanos. O país é conhecido por sua diversidade cultural e suas belas praias tropicais.",
        "descricao_en": "Equatorial Guinea, officially the Republic of Equatorial Guinea, is a country in Central Africa located on the west coast of Africa. Its history includes colonial rule by different European powers, including Spain and France. Today, Equatorial Guinea is rich in natural resources, such as oil, but faces challenges related to governance and human rights. The country is known for its cultural diversity and beautiful tropical beaches."
    },
    "eritrea": {
        "descricao_pt": "Eritreia, oficialmente o Estado da Eritreia, é um país no Chifre da África, na costa leste da África. Sua história inclui períodos de domínio estrangeiro, incluindo o domínio italiano e a colonização britânica. Atualmente, a Eritreia é uma nação independente, mas enfrenta desafios políticos e econômicos. O país é conhecido por sua paisagem montanhosa, cultura diversificada e rica história.",
        "descricao_en": "Eritrea, officially the State of Eritrea, is a country in the Horn of Africa, on the east coast of Africa. Its history includes periods of foreign rule, including Italian rule and British colonization. Today, Eritrea is an independent nation but faces political and economic challenges. The country is known for its mountainous landscape, diverse culture, and rich history."
    },
    "estonia": {
        "descricao_pt": "Estônia, oficialmente República da Estônia, é um país no norte da Europa, às margens do Mar Báltico. Sua história inclui séculos de influências de várias potências, incluindo a Suécia, a Rússia e a Alemanha. Atualmente, a Estônia é uma nação moderna e desenvolvida, conhecida por sua alta tecnologia e conexão à internet em todo o país. O país também preserva sua cultura e tradições únicas.",
        "descricao_en": "Estonia, officially the Republic of Estonia, is a country in northern Europe, on the shores of the Baltic Sea. Its history includes centuries of influence from various powers, including Sweden, Russia, and Germany. Today, Estonia is a modern and developed nation known for its high technology and nationwide internet connectivity. The country also preserves its unique culture and traditions."
    },
    "eswatini": {
        "descricao_pt": "Essuatíni, anteriormente conhecido como Suazilândia, é um pequeno país no sul da África, cercado pela África do Sul e Moçambique. Sua história inclui tradições culturais ricas e a liderança de uma monarquia tradicional. Atualmente, o Essuatíni é conhecido por sua beleza natural, com paisagens deslumbrantes e vida selvagem diversificada. O país é famoso por suas danças tradicionais e festivais culturais.",
        "descricao_en": "Eswatini, formerly known as Swaziland, is a small country in southern Africa, surrounded by South Africa and Mozambique. Its history includes rich cultural traditions and the leadership of a traditional monarchy. Today, Eswatini is known for its natural beauty, with stunning landscapes and diverse wildlife. The country is famous for its traditional dances and cultural festivals."
    },
    "ethiopia": {
        "descricao_pt": "Etiópia, oficialmente a República Democrática Federal da Etiópia, é um país no Chifre da África. Sua história é antiga, com raízes que remontam a civilizações antigas, como os axumitas. Atualmente, a Etiópia é conhecida por sua diversidade étnica, culturas diversas e belas paisagens, incluindo as montanhas Simien e o Vale do Rift. O país também é famoso por sua herança religiosa e história.",
        "descricao_en": "Ethiopia, officially the Federal Democratic Republic of Ethiopia, is a country in the Horn of Africa. Its history is ancient, with roots dating back to ancient civilizations like the Axumites. Today, Ethiopia is known for its ethnic diversity, diverse cultures, and beautiful landscapes, including the Simien Mountains and the Great Rift Valley. The country is also famous for its religious heritage and history."
    },
    "fiji": {
        "descricao_pt": "Fiji é um país insular na Oceania, composto por um arquipélago de ilhas no Pacífico Sul. Sua história inclui o contato com exploradores europeus e o domínio britânico. Atualmente, Fiji é um destino turístico popular, conhecido por suas praias de areia branca, recifes de coral deslumbrantes e cultura calorosa. O país é famoso por sua tradição de receber visitantes com um espírito amigável e acolhedor.",
        "descricao_en": "Fiji is an island country in Oceania, composed of an archipelago of islands in the South Pacific. Its history includes contact with European explorers and British rule. Today, Fiji is a popular tourist destination, known for its white sandy beaches, stunning coral reefs, and warm culture. The country is famous for its tradition of welcoming visitors with a friendly and hospitable spirit."
    },
    "finland": {
        "descricao_pt": "Finlândia, oficialmente República da Finlândia, é um país no norte da Europa, conhecido por sua natureza intocada e qualidade de vida elevada. Sua história inclui períodos de domínio por outros países, como a Suécia e a Rússia. Atualmente, a Finlândia é um país inovador, líder em tecnologia e educação. Além disso, é famosa por suas paisagens naturais deslumbrantes, como lagos e florestas.",
        "descricao_en": "Finland, officially the Republic of Finland, is a country in northern Europe known for its pristine nature and high quality of life. Its history includes periods of rule by other countries, such as Sweden and Russia. Today, Finland is an innovative country, a leader in technology and education. Additionally, it is famous for its stunning natural landscapes, including lakes and forests."
    },
    "france": {
        "descricao_pt": "A França, oficialmente República Francesa, é um país europeu localizado na Europa Ocidental. Sua história é rica e marcada por eventos significativos, como a Revolução Francesa, que teve um impacto duradouro na política e nos direitos humanos. A França é conhecida por sua cultura, gastronomia e moda de classe mundial. O país é famoso por sua Torre Eiffel, vinho, queijo e museus renomados, como o Louvre.",
        "descricao_en": "France, officially the French Republic, is a European country located in Western Europe. Its history is rich and marked by significant events, such as the French Revolution, which had a lasting impact on politics and human rights. France is known for its world-class culture, cuisine, and fashion. The country is famous for its Eiffel Tower, wine, cheese, and renowned museums like the Louvre."
    },
    "gabon": {
        "descricao_pt": "O Gabão, oficialmente República Gabonesa, é um país da África Central. Sua história inclui períodos de colonização francesa e independência. O país é caracterizado por sua rica biodiversidade e paisagens naturais deslumbrantes, como florestas tropicais e parques nacionais. Hoje, o Gabão é conhecido por sua estabilidade política e esforços de conservação da natureza.",
        "descricao_en": "Gabon, officially the Gabonese Republic, is a country in Central Africa. Its history includes periods of French colonization and independence. The country is characterized by its rich biodiversity and stunning natural landscapes, such as tropical forests and national parks. Today, Gabon is known for its political stability and nature conservation efforts."
    },
    "gambia": {
        "descricao_pt": "A Gâmbia, oficialmente República da Gâmbia, é um pequeno país costeiro na África Ocidental. Sua história inclui períodos de colonização britânica e independência. O país é atravessado pelo rio Gâmbia e é conhecido por sua diversidade étnica e cultural. Na atualidade, a Gâmbia é um destino turístico popular devido às suas belas praias e vida selvagem.",
        "descricao_en": "Gambia, officially the Republic of The Gambia, is a small coastal country in West Africa. Its history includes periods of British colonization and independence. The country is crossed by the Gambia River and is known for its ethnic and cultural diversity. Today, The Gambia is a popular tourist destination due to its beautiful beaches and wildlife."
    },
    "georgia": {
        "descricao_pt": "A Geórgia, oficialmente República da Geórgia, é um país localizado no cruzamento da Europa Oriental e da Ásia Ocidental. Sua história remonta a antigas civilizações e impérios. A Geórgia é famosa por sua cultura, vinho e paisagens montanhosas espetaculares. Hoje, o país enfrenta desafios geopolíticos, mas mantém sua identidade única.",
        "descricao_en": "Georgia, officially the Republic of Georgia, is a country located at the crossroads of Eastern Europe and Western Asia. Its history dates back to ancient civilizations and empires. Georgia is famous for its culture, wine, and spectacular mountainous landscapes. Today, the country faces geopolitical challenges but maintains its unique identity."
    },
    "germany": {
        "descricao_pt": "A Alemanha, oficialmente República Federal da Alemanha, é uma nação europeia central com uma história que abrange desde o Sacro Império Romano até o período pós-Segunda Guerra Mundial. É conhecida por sua eficiência, indústria automobilística de renome e contribuições significativas para a filosofia e música. A Alemanha é uma potência econômica global e líder na União Europeia.",
        "descricao_en": "Germany, officially the Federal Republic of Germany, is a central European nation with a history spanning from the Holy Roman Empire to the post-World War II era. It is known for its efficiency, renowned automotive industry, and significant contributions to philosophy and music. Germany is a global economic powerhouse and a leader in the European Union."
    },
    "ghana": {
        "descricao_pt": "Gana, oficialmente República de Gana, é um país na África Ocidental. Sua história inclui reinos e impérios antigos, como o Império Axante. Gana é conhecida por sua cultura vibrante, música e dança. Hoje, o país é uma democracia estável e um dos principais produtores de ouro do mundo.",
        "descricao_en": "Ghana, officially the Republic of Ghana, is a country in West Africa. Its history includes ancient kingdoms and empires, such as the Ashanti Empire. Ghana is known for its vibrant culture, music, and dance. Today, the country is a stable democracy and one of the world's leading gold producers."
    },
    "greece": {
        "descricao_pt": "A Grécia, oficialmente República Helênica, é um país no sudeste da Europa com uma história rica que remonta à antiguidade clássica. É o berço da democracia, filosofia e dos Jogos Olímpicos. A Grécia é famosa por sua arquitetura antiga, como o Partenon, e suas ilhas deslumbrantes no Mar Egeu. Hoje, é um destino turístico popular.",
        "descricao_en": "Greece, officially the Hellenic Republic, is a country in southeastern Europe with a rich history dating back to classical antiquity. It is the birthplace of democracy, philosophy, and the Olympic Games. Greece is famous for its ancient architecture, such as the Parthenon, and its stunning islands in the Aegean Sea. Today, it is a popular tourist destination."
    },
    "grenada": {
        "descricao_pt": "Granada, oficialmente Estado de Granada, é uma ilha no Caribe. Sua história inclui períodos de colonização por europeus e independência. Granada é conhecida por suas praias de areia branca, paisagens vulcânicas e produção de nozes-moscada. Atualmente, é uma nação democrática e um destino turístico popular.",
        "descricao_en": "Grenada, officially the State of Grenada, is an island in the Caribbean. Its history includes periods of European colonization and independence. Grenada is known for its white sandy beaches, volcanic landscapes, and nutmeg production. Today, it is a democratic nation and a popular tourist destination."
    },
    "guatemala": {
        "descricao_pt": "A Guatemala, oficialmente República da Guatemala, é um país na América Central. Sua história inclui civilizações maias antigas e períodos de domínio colonial espanhol. A Guatemala é famosa por sua herança cultural, incluindo artesanato, música e culinária. Atualmente, o país enfrenta desafios econômicos e sociais, mas mantém sua rica cultura.",
        "descricao_en": "Guatemala, officially the Republic of Guatemala, is a country in Central America. Its history includes ancient Mayan civilizations and periods of Spanish colonial rule. Guatemala is famous for its cultural heritage, including crafts, music, and cuisine. Today, the country faces economic and social challenges but maintains its rich culture."
    },
    "guinea-bissau": {
        "descricao_pt": "Guiné-Bissau, oficialmente República da Guiné-Bissau, é um país na África Ocidental. Sua história envolve períodos de colonização portuguesa e independência. O país é conhecido por sua diversidade étnica e culturas tradicionais. Atualmente, Guiné-Bissau enfrenta desafios políticos e econômicos, mas mantém sua identidade única.",
        "descricao_en": "Guinea-Bissau, officially the Republic of Guinea-Bissau, is a country in West Africa. Its history involves periods of Portuguese colonization and independence. The country is known for its ethnic diversity and traditional cultures. Today, Guinea-Bissau faces political and economic challenges but maintains its unique identity."
    },
    "guinea": {
        "descricao_pt": "Guiné é um país situado na costa oeste da África. Durante os séculos XV a XVIII, a região foi palco de comércio de escravos e conflitos entre impérios europeus. Hoje, a Guiné é uma nação independente com uma rica herança cultural africana e uma economia em crescimento.",
        "descricao_en": "Guinea is a country located on the west coast of Africa. During the 15th to 18th centuries, the region witnessed the slave trade and conflicts between European empires. Today, Guinea is an independent nation with a rich African cultural heritage and a growing economy."
    },
    "guyana": {
        "descricao_pt": "Guiana é um país na América do Sul, conhecido por sua diversidade étnica e cultural. Colonizada por britânicos, holandeses e franceses, Guiana é agora uma república independente. Possui uma geografia diversificada e é famosa por suas florestas tropicais e rios.",
        "descricao_en": "Guyana is a country in South America, known for its ethnic and cultural diversity. Colonized by the British, Dutch, and French, Guyana is now an independent republic. It has a diverse geography and is famous for its rainforests and rivers."
    },
    "haiti": {
        "descricao_pt": "Haiti é uma nação caribenha na ilha de Hispaniola. Sua história é marcada por lutas pela independência e desafios econômicos. Hoje, o Haiti enfrenta desafios sociais e políticos, mas também é rico em cultura e tradições únicas.",
        "descricao_en": "Haiti is a Caribbean nation on the island of Hispaniola. Its history is marked by struggles for independence and economic challenges. Today, Haiti faces social and political challenges, but is also rich in culture and unique traditions."
    },
    "honduras": {
        "descricao_pt": "Honduras é uma nação da América Central. Sua história inclui civilizações antigas e o período colonial espanhol. Atualmente, Honduras enfrenta desafios econômicos e sociais, mas é conhecida por sua beleza natural e patrimônio cultural.",
        "descricao_en": "Honduras is a Central American nation. Its history includes ancient civilizations and the Spanish colonial period. Currently, Honduras faces economic and social challenges, but is known for its natural beauty and cultural heritage."
    },
    "hungary": {
        "descricao_pt": "Hungria é uma nação da Europa Central com uma rica história. Foi parte do Império Austro-Húngaro e enfrentou desafios durante guerras e regimes políticos. Hoje, a Hungria é uma democracia e um importante centro cultural europeu.",
        "descricao_en": "Hungary is a Central European nation with a rich history. It was part of the Austro-Hungarian Empire and faced challenges during wars and political regimes. Today, Hungary is a democracy and a significant European cultural center."
    },
    "iceland": {
        "descricao_pt": "Islândia é uma ilha no norte do Atlântico. Sua história inclui colonização nórdica e uma sociedade democrática. A Islândia é conhecida por suas paisagens naturais deslumbrantes e seu estilo de vida moderno e progressista.",
        "descricao_en": "Iceland is an island in the North Atlantic. Its history includes Norse colonization and a democratic society. Iceland is known for its stunning natural landscapes and its modern and progressive way of life."
    },
    "india": {
        "descricao_pt": "Índia é uma nação no sul da Ásia com uma história milenar. Foi lar de grandes impérios e desempenhou um papel importante no comércio global. Hoje, a Índia é uma democracia e uma potência econômica em crescimento.",
        "descricao_en": "India is a nation in South Asia with a millennia-old history. It was home to great empires and played a significant role in global trade. Today, India is a democracy and a growing economic powerhouse."
    },
    "indonesia": {
        "descricao_pt": "Indonésia é um arquipélago no sudeste da Ásia. Sua história inclui reinos marítimos e colonização. Atualmente, a Indonésia é a maior nação muçulmana do mundo e uma democracia em desenvolvimento.",
        "descricao_en": "Indonesia is an archipelago in Southeast Asia. Its history includes maritime kingdoms and colonization. Currently, Indonesia is the world's largest Muslim nation and a developing democracy."
    },
    "iran": {
        "descricao_pt": "Irã é uma nação do Oriente Médio com uma rica herança cultural e histórica. Foi o centro de impérios antigos e desempenha um papel importante na geopolítica moderna. Hoje, o Irã é uma república islâmica com desafios e realizações.",
        "descricao_en": "Iran is a Middle Eastern nation with a rich cultural and historical heritage. It was the center of ancient empires and plays a significant role in modern geopolitics. Today, Iran is an Islamic republic with challenges and achievements."
    },
    "iraq": {
        "descricao_pt": "Iraque é uma nação no Oriente Médio com uma história antiga. Foi lar de civilizações antigas e enfrentou conflitos recentes. Atualmente, o Iraque busca reconstrução e estabilidade após anos de turbulência.",
        "descricao_en": "Iraq is a nation in the Middle East with an ancient history. It was home to ancient civilizations and has faced recent conflicts. Currently, Iraq seeks reconstruction and stability after years of turmoil."
    },
    "ireland": {
        "descricao_pt": "Irlanda é uma ilha na Europa Ocidental com uma cultura rica e uma história de lutas por independência. Hoje, a Irlanda é uma nação próspera e democrática, conhecida por sua música, literatura e paisagens deslumbrantes.",
        "descricao_en": "Ireland is an island in Western Europe with a rich culture and a history of struggles for independence. Today, Ireland is a prosperous and democratic nation, known for its music, literature, and stunning landscapes."
    },
    "italy": {
        "descricao_pt": "Itália é uma nação no sul da Europa, famosa por sua história antiga e cultura. Foi o centro do Império Romano e é conhecida por sua arte, culinária e moda. Hoje, a Itália é uma democracia e um destino turístico popular.",
        "descricao_en": "Italy is a nation in Southern Europe, famous for its ancient history and culture. It was the center of the Roman Empire and is known for its art, cuisine, and fashion. Today, Italy is a democracy and a popular tourist destination."
    },
    "ivory coast": {
        "descricao_pt": "Costa do Marfim é um país na África Ocidental com uma história de comércio e colonização. Atualmente, a Costa do Marfim é uma nação em crescimento, com uma economia diversificada e uma população diversificada.",
        "descricao_en": "Ivory Coast is a country in West Africa with a history of trade and colonization. Currently, Ivory Coast is a growing nation with a diverse economy and population."
    },
    "jamaica": {
        "descricao_pt": "Jamaica é uma ilha no Caribe, famosa por sua música reggae e cultura vibrante. Sua história inclui colonização e influências africanas. Hoje, a Jamaica é um destino turístico popular e conhecida por sua hospitalidade.",
        "descricao_en": "Jamaica is an island in the Caribbean, famous for its reggae music and vibrant culture. Its history includes colonization and African influences. Today, Jamaica is a popular tourist destination and known for its hospitality."
    },
    "japan": {
        "descricao_pt": "Japão é uma nação insular no leste da Ásia, conhecida por sua cultura única e tecnologia avançada. Sua história inclui samurais e imperadores. Hoje, o Japão é uma potência econômica global e um centro de inovação.",
        "descricao_en": "Japan is an island nation in East Asia, known for its unique culture and advanced technology. Its history includes samurais and emperors. Today, Japan is a global economic powerhouse and a center of innovation."
    },
    "jordan": {
        "descricao_pt": "Jordânia é uma nação no Oriente Médio com uma história antiga e cenários naturais impressionantes. Atualmente, a Jordânia é um reino estável e pacífico em uma região marcada por conflitos.",
        "descricao_en": "Jordan is a nation in the Middle East with an ancient history and stunning natural landscapes. Currently, Jordan is a stable and peaceful kingdom in a region marked by conflicts."
    },
    "kazakhstan": {
        "descricao_pt": "Cazaquistão é o maior país sem litoral do mundo, conhecido por sua vasta estepe e história nômade. Hoje, o Cazaquistão é uma nação independente e em crescimento com recursos naturais abundantes.",
        "descricao_en": "Kazakhstan is the world's largest landlocked country, known for its vast steppe and nomadic history. Today, Kazakhstan is an independent and growing nation with abundant natural resources."
    },
    "kenya": {
        "descricao_pt": "Quênia é um país no leste da África, famoso por sua vida selvagem e paisagens diversas. Sua história inclui antigas civilizações e colonização britânica. Atualmente, o Quênia é uma democracia em desenvolvimento.",
        "descricao_en": "Kenya is a country in East Africa, famous for its wildlife and diverse landscapes. Its history includes ancient civilizations and British colonization. Currently, Kenya is a developing democracy."
    },
    "kiribati": {
        "descricao_pt": "Kiribati é uma nação insular no Pacífico Central, composta por atóis e recifes. Sua história inclui influências coloniais e desafios relacionados às mudanças climáticas. Hoje, Kiribati enfrenta ameaças de elevação do nível do mar.",
        "descricao_en": "Kiribati is an island nation in the Central Pacific, composed of atolls and reefs. Its history includes colonial influences and challenges related to climate change. Today, Kiribati faces threats from rising sea levels."
    },
    "kuwait": {
        "descricao_pt": "Kuwait é um país no Golfo Pérsico, conhecido por suas reservas de petróleo e modernização. Sua história inclui relações com impérios e conflitos regionais. Hoje, o Kuwait é uma nação rica e desenvolvida.",
        "descricao_en": "Kuwait is a country in the Persian Gulf, known for its oil reserves and modernization. Its history includes relationships with empires and regional conflicts. Today, Kuwait is a wealthy and developed nation."
    },
    "kyrgyzstan": {
        "descricao_pt": "O Quirguistão, oficialmente República Quirguiz, é uma nação da Ásia Central. Sua história é marcada por uma série de impérios e conquistadores ao longo dos séculos. No presente, o Quirguistão é conhecido por sua paisagem montanhosa deslumbrante e cultura nômade que perdura em algumas regiões do país.",
        "descricao_en": "Kyrgyzstan, officially the Kyrgyz Republic, is a nation in Central Asia. Its history is marked by a series of empires and conquerors over the centuries. In the present day, Kyrgyzstan is known for its stunning mountainous landscape and a nomadic culture that persists in some regions of the country."
    },
    "laos": {
        "descricao_pt": "O Laos, oficialmente República Democrática Popular do Laos, é um país situado no sudeste asiático. Ao longo de sua história, foi influenciado pelo Império Khmer, pelo Reino de Lan Xang e pelo domínio francês. Hoje, Laos é conhecido por sua beleza natural, incluindo as Planícies de Planícies e as montanhas de Luang Prabang.",
        "descricao_en": "Laos, officially the Lao People's Democratic Republic, is a country in Southeast Asia. Throughout its history, it was influenced by the Khmer Empire, the Kingdom of Lan Xang, and French colonial rule. Today, Laos is known for its natural beauty, including the Plain of Jars and the mountains of Luang Prabang."
    },
    "latvia": {
        "descricao_pt": "A Letônia é um país báltico localizado no norte da Europa. Sua história inclui períodos de dominação por impérios como o sueco e o russo. Atualmente, a Letônia é um estado independente com uma economia em crescimento e um ambiente cultural diversificado.",
        "descricao_en": "Latvia is a Baltic country located in Northern Europe. Its history includes periods of domination by empires such as the Swedish and the Russian. Today, Latvia is an independent state with a growing economy and a diverse cultural environment."
    },
    "lebanon": {
        "descricao_pt": "O Líbano é um país do Oriente Médio com uma história rica e complexa, incluindo influências fenícias, romanas, árabes e otomanas. Atualmente, o Líbano enfrenta desafios políticos e econômicos, mas é conhecido por sua culinária única e diversificada.",
        "descricao_en": "Lebanon is a Middle Eastern country with a rich and complex history, including Phoenician, Roman, Arab, and Ottoman influences. Today, Lebanon faces political and economic challenges but is known for its unique and diverse cuisine."
    },
    "lesotho": {
        "descricao_pt": "Lesoto é um pequeno país montanhoso localizado no sul da África. Foi fundado como um reino independente e tem uma história única. Atualmente, Lesoto é conhecido por suas paisagens deslumbrantes, incluindo as Montanhas Drakensberg.",
        "descricao_en": "Lesotho is a small, mountainous country located in Southern Africa. It was founded as an independent kingdom and has a unique history. Today, Lesotho is known for its stunning landscapes, including the Drakensberg Mountains."
    },
    "liberia": {
        "descricao_pt": "Libéria é um país da África Ocidental fundado por ex-escravos americanos. Sua história está ligada à luta pela liberdade e igualdade. Atualmente, a Libéria é uma democracia em desenvolvimento, enfrentando desafios econômicos e sociais.",
        "descricao_en": "Liberia is a country in West Africa founded by former American slaves. Its history is intertwined with the struggle for freedom and equality. Today, Liberia is a developing democracy, facing economic and social challenges."
    },
    "libya": {
        "descricao_pt": "A Líbia é um país do norte da África com uma história que remonta à antiguidade, incluindo a civilização cartaginesa e o domínio romano. No presente, a Líbia enfrenta instabilidade política e conflitos, mas é conhecida por suas riquezas de petróleo e gás.",
        "descricao_en": "Libya is a North African country with a history dating back to antiquity, including the Carthaginian civilization and Roman rule. Currently, Libya faces political instability and conflicts but is known for its oil and gas wealth."
    },
    "liechtenstein": {
        "descricao_pt": "Liechtenstein é uma nação alpina localizada na Europa Central. Possui uma história de soberania limitada e é conhecido por sua estabilidade política e economia próspera. O país também é famoso por seu cenário montanhoso deslumbrante.",
        "descricao_en": "Liechtenstein is an alpine nation located in Central Europe. It has a history of limited sovereignty and is known for its political stability and prosperous economy. The country is also famous for its stunning mountainous scenery."
    },
    "lithuania": {
        "descricao_pt": "A Lituânia é um país báltico com uma história que remonta à Idade Média. Foi um importante centro cultural e científico. Hoje, a Lituânia é uma nação independente com uma economia em crescimento e um forte senso de identidade nacional.",
        "descricao_en": "Lithuania is a Baltic country with a history dating back to the Middle Ages. It was an important cultural and scientific center. Today, Lithuania is an independent nation with a growing economy and a strong sense of national identity."
    },
    "luxembourg": {
        "descricao_pt": "Luxemburgo é uma nação europeia situada entre a Bélgica, a França e a Alemanha. Sua história inclui influências de impérios como o romano e o espanhol. Atualmente, Luxemburgo é conhecido por sua riqueza econômica e qualidade de vida elevada.",
        "descricao_en": "Luxembourg is a European nation situated between Belgium, France, and Germany. Its history includes influences from empires such as the Roman and Spanish. Today, Luxembourg is known for its economic wealth and high quality of life."
    },
    "madagascar": {
        "descricao_pt": "Madagáscar, oficialmente República de Madagáscar, é uma ilha na costa leste da África. Sua história é marcada por influências africanas e asiáticas. No presente, Madagáscar é famoso por sua biodiversidade única e paisagens espetaculares.",
        "descricao_en": "Madagascar, officially the Republic of Madagascar, is an island off the east coast of Africa. Its history is marked by African and Asian influences. Today, Madagascar is famous for its unique biodiversity and spectacular landscapes."
    },
    "malawi": {
        "descricao_pt": "Malawi é uma nação no sudeste da África. Sua história inclui a colonização britânica. Atualmente, o Malawi é conhecido por seu lago homônimo, o Lago Malawi, que é um dos maiores e mais profundos lagos de água doce do mundo.",
        "descricao_en": "Malawi is a nation in Southeast Africa. Its history includes British colonization. Currently, Malawi is known for its namesake lake, Lake Malawi, which is one of the largest and deepest freshwater lakes in the world."
    },
    "malaysia": {
        "descricao_pt": "A Malásia é uma nação do sudeste asiático que foi influenciada por várias culturas, incluindo a malaia, a chinesa e a indiana. Hoje, a Malásia é uma nação multicultural com uma economia em crescimento e é famosa por suas belas praias e florestas tropicais.",
        "descricao_en": "Malaysia is a Southeast Asian nation that has been influenced by various cultures, including Malay, Chinese, and Indian. Today, Malaysia is a multicultural nation with a growing economy and is famous for its beautiful beaches and tropical forests."
    },
    "maldives": {
        "descricao_pt": "As Maldivas, oficialmente República das Maldivas, são uma nação insular no Oceano Índico. Sua história está ligada ao comércio marítimo e à cultura islâmica. Atualmente, as Maldivas são conhecidas por suas praias paradisíacas e recifes de coral espetaculares.",
        "descricao_en": "Maldives, officially the Republic of Maldives, is an island nation in the Indian Ocean. Its history is linked to maritime trade and Islamic culture. Today, Maldives is known for its paradise beaches and spectacular coral reefs."
    },
    "mali": {
        "descricao_pt": "Mali é uma nação da África Ocidental com uma história rica, incluindo o Império do Mali, um dos maiores impérios africanos da história. Atualmente, Mali enfrenta desafios políticos e sociais, mas é conhecido por sua música tradicional e cultura vibrante.",
        "descricao_en": "Mali is a West African nation with a rich history, including the Mali Empire, one of the largest African empires in history. Today, Mali faces political and social challenges but is known for its traditional music and vibrant culture."
    },
    "malta": {
        "descricao_pt": "Malta é um arquipélago no Mar Mediterrâneo com uma história que remonta a civilizações antigas, incluindo os fenícios e os romanos. Atualmente, Malta é um país independente e membro da União Europeia, conhecido por sua arquitetura histórica e praias deslumbrantes.",
        "descricao_en": "Malta is an archipelago in the Mediterranean Sea with a history dating back to ancient civilizations, including the Phoenicians and Romans. Currently, Malta is an independent country and a member of the European Union, known for its historic architecture and stunning beaches."
    },
    "marshall islands": {
        "descricao_pt": "As Ilhas Marshall são uma nação insular no Oceano Pacífico. Sua história inclui a administração sob o domínio dos Estados Unidos. No presente, as Ilhas Marshall são conhecidas por suas belas praias de areia branca e sua cultura tradicional.",
        "descricao_en": "The Marshall Islands is an island nation in the Pacific Ocean. Its history includes administration under the United States. Currently, the Marshall Islands are known for their beautiful white-sand beaches and traditional culture."
    },
    "mauritania": {
        "descricao_pt": "Mauritânia é um país no noroeste da África com uma história que remonta ao Império Garamante. Atualmente, a Mauritânia enfrenta desafios econômicos e sociais, mas é conhecida por seu vasto deserto e tradições nômades.",
        "descricao_en": "Mauritania is a country in Northwest Africa with a history dating back to the Garamantian Empire. Today, Mauritania faces economic and social challenges but is known for its vast desert and nomadic traditions."
    },
    "mauritius": {
        "descricao_pt": "Maurício é uma ilha no Oceano Índico com uma história marcada por colonização europeia, incluindo o domínio francês e britânico. Atualmente, Maurício é conhecida por suas praias exuberantes e como um destino turístico popular.",
        "descricao_en": "Mauritius is an island in the Indian Ocean with a history marked by European colonization, including French and British rule. Currently, Mauritius is known for its lush beaches and as a popular tourist destination."
    },
    "mexico": {
        "descricao_pt": "O México é um país na América do Norte com uma história rica, incluindo civilizações antigas como os maias e os astecas. Atualmente, o México é uma nação diversa com uma cultura vibrante, famosa por sua comida, música e tradições únicas.",
        "descricao_en": "Mexico is a country in North America with a rich history, including ancient civilizations like the Maya and the Aztecs. Currently, Mexico is a diverse nation with a vibrant culture, famous for its food, music, and unique traditions."
    },
    "micronesia": {
        "descricao_pt": "A Micronésia, oficialmente conhecida como Estados Federados da Micronésia, é uma nação insular no Oceano Pacífico. Sua história é marcada por uma rica herança cultural, com várias ilhas e grupos étnicos habitando a região. Hoje, a Micronésia é um país pacífico, com uma economia voltada para a pesca e o turismo, graças à sua beleza natural e recifes de coral deslumbrantes.",
        "descricao_en": "Micronesia, officially known as the Federated States of Micronesia, is an island nation in the Pacific Ocean. Its history is marked by a rich cultural heritage, with various islands and ethnic groups inhabiting the region. Today, Micronesia is a peaceful country with an economy focused on fishing and tourism, thanks to its natural beauty and stunning coral reefs."
    },
    "moldova": {
        "descricao_pt": "Moldova, oficialmente a República da Moldávia, é um país localizado na Europa Oriental. Ao longo de sua história, Moldova foi influenciada por várias culturas e impérios. Atualmente, é um país independente com uma economia em desenvolvimento e uma sociedade que preserva suas tradições culturais únicas.",
        "descricao_en": "Moldova, officially the Republic of Moldova, is a country located in Eastern Europe. Throughout its history, Moldova has been influenced by various cultures and empires. Today, it is an independent country with a developing economy and a society that preserves its unique cultural traditions."
    },
    "monaco": {
        "descricao_pt": "Mônaco é um pequeno principado localizado na costa sul da França, conhecido por sua riqueza e glamour. Sua história está entrelaçada com a dinastia Grimaldi, que governa o país há séculos. Atualmente, Mônaco é um centro de turismo, negócios e entretenimento, com seu cassino famoso e belas paisagens à beira-mar.",
        "descricao_en": "Monaco is a small principality located on the southern coast of France, known for its wealth and glamour. Its history is intertwined with the Grimaldi dynasty, which has ruled the country for centuries. Today, Monaco is a hub for tourism, business, and entertainment, with its famous casino and beautiful seaside landscapes."
    },
    "mongolia": {
        "descricao_pt": "A Mongólia é uma nação da Ásia Central conhecida por suas vastas estepes e história nômade. Ao longo dos séculos, o império mongol conquistou territórios vastos sob Genghis Khan. Hoje, a Mongólia é uma república independente que preserva suas tradições culturais e está se desenvolvendo economicamente.",
        "descricao_en": "Mongolia is a nation in Central Asia known for its vast steppes and nomadic history. Over the centuries, the Mongol Empire conquered vast territories under Genghis Khan. Today, Mongolia is an independent republic that preserves its cultural traditions and is developing economically."
    },
    "montenegro": {
        "descricao_pt": "Montenegro, oficialmente conhecido como Montenegro, é um país dos Bálcãs, situado na costa leste do Mar Adriático. Com uma história que remonta aos tempos antigos, Montenegro é conhecido por sua beleza natural, incluindo montanhas imponentes e lindas praias. Atualmente, o país é uma república independente e um destino turístico em ascensão.",
        "descricao_en": "Montenegro, officially known as Montenegro, is a Balkan country located on the eastern coast of the Adriatic Sea. With a history dating back to ancient times, Montenegro is known for its natural beauty, including towering mountains and beautiful beaches. Today, the country is an independent republic and a rising tourist destination."
    },
    "morocco": {
        "descricao_pt": "Marrocos, oficialmente o Reino de Marrocos, é um país no norte da África com uma rica história e cultura. Berço de civilizações antigas, Marrocos é conhecido por seus souks, mesquitas e paisagens variadas, que vão desde o deserto do Saara até as montanhas do Atlas. Hoje, Marrocos é uma monarquia constitucional com uma economia diversificada.",
        "descricao_en": "Morocco, officially the Kingdom of Morocco, is a country in North Africa with a rich history and culture. Home to ancient civilizations, Morocco is known for its souks, mosques, and diverse landscapes, ranging from the Sahara Desert to the Atlas Mountains. Today, Morocco is a constitutional monarchy with a diversified economy."
    },
    "mozambique": {
        "descricao_pt": "Moçambique, oficialmente a República de Moçambique, é uma nação localizada na costa sudeste da África. Sua história envolveu o comércio de escravos e a colonização por potências europeias. Atualmente, Moçambique é uma república independente com uma economia em crescimento e uma cultura diversificada.",
        "descricao_en": "Mozambique, officially the Republic of Mozambique, is a nation located on the southeast coast of Africa. Its history involved the slave trade and colonization by European powers. Today, Mozambique is an independent republic with a growing economy and a diverse culture."
    },
    "myanmar": {
        "descricao_pt": "Mianmar, oficialmente a União de Mianmar, é um país do sudeste asiático com uma história rica e complexa. Marcado por governos militares e lutas políticas, Mianmar está atualmente passando por mudanças políticas significativas. O país é conhecido por sua cultura diversificada e paisagens deslumbrantes.",
        "descricao_en": "Myanmar, officially the Union of Myanmar, is a Southeast Asian country with a rich and complex history. Marked by military governments and political struggles, Myanmar is currently undergoing significant political changes. The country is known for its diverse culture and stunning landscapes."
    },
    "namibia": {
        "descricao_pt": "Namíbia, oficialmente a República da Namíbia, é um país no sudoeste da África com uma paisagem deslumbrante, incluindo o deserto do Namibe. Sua história inclui o domínio colonial alemão e sul-africano. Hoje, a Namíbia é uma república independente com uma economia em crescimento e um compromisso com a conservação da natureza.",
        "descricao_en": "Namibia, officially the Republic of Namibia, is a country in southwestern Africa with stunning landscapes, including the Namib Desert. Its history includes German and South African colonial rule. Today, Namibia is an independent republic with a growing economy and a commitment to nature conservation."
    },
    "nauru": {
        "descricao_pt": "Nauru é uma pequena nação insular no Pacífico Central, conhecida por sua dependência da mineração de fosfato. Sua história inclui o domínio colonial australiano e britânico. Atualmente, Nauru é uma república independente que enfrenta desafios econômicos, mas mantém sua identidade cultural única.",
        "descricao_en": "Nauru is a small island nation in the Central Pacific, known for its reliance on phosphate mining. Its history includes Australian and British colonial rule. Today, Nauru is an independent republic facing economic challenges but preserving its unique cultural identity."
    },
    "nepal": {
        "descricao_pt": "Nepal, oficialmente o Reino do Nepal, é um país no sul da Ásia conhecido por sua geografia montanhosa, incluindo o Monte Everest. Sua história é rica em tradições espirituais e culturais. Atualmente, Nepal é uma república federal com uma cultura diversificada e uma economia em desenvolvimento.",
        "descricao_en": "Nepal, officially the Kingdom of Nepal, is a country in South Asia known for its mountainous geography, including Mount Everest. Its history is rich in spiritual and cultural traditions. Today, Nepal is a federal republic with a diverse culture and a developing economy."
    },
    "netherlands": {
        "descricao_pt": "Os Países Baixos, oficialmente conhecidos como Reino dos Países Baixos, são uma nação na Europa Ocidental. Sua história inclui a Idade de Ouro dos Países Baixos e um império colonial. Atualmente, os Países Baixos são uma monarquia constitucional com uma economia avançada e uma cultura rica em arte e inovação.",
        "descricao_en": "The Netherlands, officially known as the Kingdom of the Netherlands, is a nation in Western Europe. Its history includes the Dutch Golden Age and a colonial empire. Today, the Netherlands is a constitutional monarchy with an advanced economy and a culture rich in art and innovation."
    },
    "new zealand": {
        "descricao_pt": "A Nova Zelândia é um país insular no sudoeste do Pacífico Sul, conhecido por suas paisagens deslumbrantes e cultura Maori. Sua história envolveu a migração polinésia e a colonização britânica. Atualmente, a Nova Zelândia é uma democracia parlamentar com uma economia desenvolvida e um foco na preservação ambiental.",
        "descricao_en": "New Zealand is an island nation in the southwestern South Pacific, known for its stunning landscapes and Maori culture. Its history involved Polynesian migration and British colonization. Today, New Zealand is a parliamentary democracy with a developed economy and a focus on environmental preservation."
    },
    "nicaragua": {
        "descricao_pt": "Nicarágua, oficialmente a República da Nicarágua, é um país na América Central com uma história de conflitos políticos e revoluções. Atualmente, a Nicarágua é uma república com desafios econômicos e políticos, mas também possui uma rica herança cultural e belezas naturais, como o Lago Nicarágua.",
        "descricao_en": "Nicaragua, officially the Republic of Nicaragua, is a country in Central America with a history of political conflicts and revolutions. Today, Nicaragua is a republic facing economic and political challenges, but it also has a rich cultural heritage and natural beauties, such as Lake Nicaragua."
    },
    "niger": {
        "descricao_pt": "Níger, oficialmente a República do Níger, é um país na África Ocidental, marcado por sua história como parte do Império Songhai e do comércio transaariano. Atualmente, o Níger é uma república independente com desafios econômicos, mas também com um patrimônio cultural diversificado e paisagens desérticas impressionantes.",
        "descricao_en": "Niger, officially the Republic of Niger, is a country in West Africa, marked by its history as part of the Songhai Empire and trans-Saharan trade. Today, Niger is an independent republic with economic challenges but also a diverse cultural heritage and stunning desert landscapes."
    },
    "nigeria": {
        "descricao_pt": "Nigéria, oficialmente a República Federal da Nigéria, é o país mais populoso da África, com uma história rica e complexa. O país abriga diversas etnias e culturas. Atualmente, a Nigéria é uma república democrática com uma economia em crescimento, embora enfrente desafios sociais e políticos.",
        "descricao_en": "Nigeria, officially the Federal Republic of Nigeria, is the most populous country in Africa, with a rich and complex history. The country is home to diverse ethnicities and cultures. Today, Nigeria is a democratic republic with a growing economy, although it faces social and political challenges."
    },
    "north korea": {
        "descricao_pt": "A Coreia do Norte, oficialmente a República Popular Democrática da Coreia, é um país na Península Coreana, conhecido por seu regime político fechado e isolado. A história da Coreia do Norte é marcada por divisões e tensões com a Coreia do Sul. Atualmente, o país é um estado totalitário com uma economia centralizada.",
        "descricao_en": "North Korea, officially the Democratic People's Republic of Korea, is a country on the Korean Peninsula, known for its closed and isolated political regime. North Korea's history is marked by divisions and tensions with South Korea. Today, the country is a totalitarian state with a centralized economy."
    },
    "north macedonia": {
        "descricao_pt": "Macedônia do Norte, oficialmente a República da Macedônia do Norte, é um país nos Bálcãs com uma história complexa, incluindo a herança da antiga Macedônia. Atualmente, a Macedônia do Norte é uma república independente, com uma economia em crescimento e um compromisso com a reconciliação étnica e a estabilidade na região.",
        "descricao_en": "North Macedonia, officially the Republic of North Macedonia, is a country in the Balkans with a complex history, including the legacy of ancient Macedonia. Today, North Macedonia is an independent republic with a growing economy and a commitment to ethnic reconciliation and stability in the region."
    },
    "norway": {
        "descricao_pt": "A Noruega, oficialmente conhecida como Reino da Noruega, é um país nórdico localizado na parte norte da Europa. Sua história é marcada por períodos de reinos unificados e independência, sendo governada por monarcas desde a Idade Média. Com uma geografia deslumbrante que inclui fiordes profundos e montanhas cobertas de neve, a Noruega é famosa por sua beleza natural. Atualmente, o país é conhecido por sua qualidade de vida elevada e pelo papel ativo na promoção da paz e dos direitos humanos no cenário internacional.",
        "descricao_en": "Norway, officially known as the Kingdom of Norway, is a Nordic country located in the northern part of Europe. Its history is marked by periods of unified kingdoms and independence, ruled by monarchs since the Middle Ages. With stunning geography that includes deep fjords and snow-covered mountains, Norway is famous for its natural beauty. Today, the country is known for its high quality of life and its active role in promoting peace and human rights on the international stage."
    },
    "oman": {
        "descricao_pt": "Omã, oficialmente Sultanato de Omã, é um país localizado na Península Arábica, no sudoeste da Ásia. Sua história remonta a impérios antigos, com influências árabes e persas. A nação é conhecida por suas paisagens desérticas e litorais espetaculares. Na atualidade, Omã é um país que passou por desenvolvimento econômico significativo, diversificando sua economia e investindo em infraestrutura e educação.",
        "descricao_en": "Oman, officially the Sultanate of Oman, is a country located on the Arabian Peninsula in southwestern Asia. Its history dates back to ancient empires, with Arab and Persian influences. The nation is known for its desert landscapes and spectacular coastlines. Today, Oman is a country that has undergone significant economic development, diversifying its economy and investing in infrastructure and education."
    },
    "pakistan": {
        "descricao_pt": "O Paquistão, oficialmente República Islâmica do Paquistão, está situado no sul da Ásia e faz fronteira com a Índia, o Afeganistão e o Irã. Sua história é rica, incluindo o período da antiga civilização do vale do Indo. O país é conhecido por sua diversidade cultural, línguas e tradições. Na atualidade, o Paquistão enfrenta desafios políticos e sociais, mas também busca promover o desenvolvimento econômico e a estabilidade.",
        "descricao_en": "Pakistan, officially the Islamic Republic of Pakistan, is located in South Asia and shares borders with India, Afghanistan, and Iran. Its history is rich, including the period of the ancient Indus Valley civilization. The country is known for its cultural diversity, languages, and traditions. Today, Pakistan faces political and social challenges, but it also strives to promote economic development and stability."
    },
    "palau": {
        "descricao_pt": "Palau, oficialmente República de Palau, é uma nação insular no Oceano Pacífico Ocidental. Sua história inclui influências culturais da Micronésia e da Espanha. As belas praias e recifes de coral tornam Palau um destino popular para o mergulho. Na atualidade, o país é reconhecido por seus esforços de conservação marinha e turismo sustentável.",
        "descricao_en": "Palau, officially the Republic of Palau, is an island nation in the Western Pacific Ocean. Its history includes cultural influences from Micronesia and Spain. The beautiful beaches and coral reefs make Palau a popular destination for diving. Today, the country is known for its marine conservation efforts and sustainable tourism."
    },
    "palestine": {
        "descricao_pt": "A Palestina, uma terra historicamente disputada no Oriente Médio, tem uma história marcada por conflitos e lutas políticas. É um lugar de importância religiosa para o judaísmo, o cristianismo e o islamismo. Na atualidade, a questão palestina continua a ser um tema complexo e de destaque na política global, com esforços em busca de paz e soluções duradouras.",
        "descricao_en": "Palestine, a historically disputed land in the Middle East, has a history marked by conflicts and political struggles. It holds religious significance for Judaism, Christianity, and Islam. Today, the Palestinian issue remains a complex and prominent topic in global politics, with efforts towards peace and lasting solutions."
    },
    "panama": {
        "descricao_pt": "O Panamá, oficialmente República do Panamá, é um país na América Central que se tornou conhecido por seu famoso canal, uma importante rota de comércio internacional. Sua história inclui períodos de domínio colonial espanhol e sua luta pela independência. Na atualidade, o Panamá é uma nação em crescimento econômico, com uma economia diversificada e uma paisagem que vai desde praias tropicais até montanhas exuberantes.",
        "descricao_en": "Panama, officially the Republic of Panama, is a country in Central America known for its famous canal, a major route for international trade. Its history includes periods of Spanish colonial rule and its struggle for independence. Today, Panama is a nation experiencing economic growth, with a diversified economy and a landscape that ranges from tropical beaches to lush mountains."
    },
    "papua new guinea": {
        "descricao_pt": "Papua Nova Guiné é um país na Oceania, localizado ao norte da Austrália. Sua história inclui uma grande diversidade de grupos étnicos e línguas. O país é conhecido por sua natureza exuberante, incluindo florestas tropicais e vida marinha única. Na atualidade, Papua Nova Guiné enfrenta desafios de desenvolvimento, mas também preserva sua rica cultura e biodiversidade.",
        "descricao_en": "Papua New Guinea is a country in Oceania, located north of Australia. Its history includes a wide diversity of ethnic groups and languages. The country is known for its lush nature, including tropical rainforests and unique marine life. Today, Papua New Guinea faces development challenges, but also preserves its rich culture and biodiversity."
    },
    "paraguay": {
        "descricao_pt": "O Paraguai, oficialmente República do Paraguai, é um país no coração da América do Sul, conhecido por sua língua oficial, o guarani, e sua história marcada por conflitos regionais. Sua economia depende da agricultura, e o país é famoso por sua erva-mate. Na atualidade, o Paraguai busca o desenvolvimento econômico e a estabilidade política.",
        "descricao_en": "Paraguay, officially the Republic of Paraguay, is a landlocked country in the heart of South America, known for its official language, Guarani, and its history marked by regional conflicts. Its economy relies on agriculture, and the country is famous for its yerba mate. Today, Paraguay seeks economic development and political stability."
    },
    "peru": {
        "descricao_pt": "O Peru, oficialmente República do Peru, é um país na América do Sul com uma rica herança cultural que remonta aos impérios Incas. Suas paisagens variam desde a majestosa Cordilheira dos Andes até a floresta amazônica. Na atualidade, o Peru é conhecido por sua culinária única, sítios arqueológicos e uma economia em crescimento.",
        "descricao_en": "Peru, officially the Republic of Peru, is a country in South America with a rich cultural heritage dating back to the Inca empires. Its landscapes range from the majestic Andes Mountains to the Amazon rainforest. Today, Peru is known for its unique cuisine, archaeological sites, and a growing economy."
    },
    "philippines": {
        "descricao_pt": "As Filipinas, oficialmente República das Filipinas, são um arquipélago no Sudeste Asiático com uma história que inclui influências espanholas e americanas. O país é conhecido por suas praias deslumbrantes, recifes de coral e biodiversidade marinha. Na atualidade, as Filipinas são uma nação em desenvolvimento, com uma economia em crescimento e desafios sociais a enfrentar.",
        "descricao_en": "The Philippines, officially the Republic of the Philippines, is an archipelago in Southeast Asia with a history that includes Spanish and American influences. The country is known for its stunning beaches, coral reefs, and marine biodiversity. Today, the Philippines is a developing nation, with a growing economy and social challenges to address."
    },
    "poland": {
        "descricao_pt": "A Polônia, oficialmente República da Polônia, está localizada na Europa Central e tem uma história rica, com uma forte tradição cultural e literária. O país é famoso por sua resistência durante a Segunda Guerra Mundial. Na atualidade, a Polônia é uma nação da União Europeia, com uma economia em crescimento e uma herança cultural valorizada.",
        "descricao_en": "Poland, officially the Republic of Poland, is located in Central Europe and has a rich history, with a strong cultural and literary tradition. The country is famous for its resistance during World War II. Today, Poland is a member of the European Union, with a growing economy and a valued cultural heritage."
    },
    "portugal": {
        "descricao_pt": "Portugal, oficialmente República Portuguesa, é um país no sudoeste da Europa com uma história marcada por descobrimentos marítimos e impérios coloniais. Sua língua, o português, é amplamente falada em todo o mundo. Na atualidade, Portugal é conhecido por suas paisagens costeiras deslumbrantes, vinhos e turismo.",
        "descricao_en": "Portugal, officially the Portuguese Republic, is a country in southwestern Europe with a history marked by maritime discoveries and colonial empires. Its language, Portuguese, is widely spoken around the world. Today, Portugal is known for its stunning coastal landscapes, wines, and tourism."
    },
    "qatar": {
        "descricao_pt": "O Catar, oficialmente Estado do Catar, é um país na Península Arábica com uma história que remonta a períodos pré-islâmicos. O país é conhecido por sua riqueza devido às reservas de gás natural e seu investimento em infraestrutura. Na atualidade, o Catar é um centro de negócios global e uma nação próspera.",
        "descricao_en": "Qatar, officially the State of Qatar, is a country on the Arabian Peninsula with a history dating back to pre-Islamic periods. The country is known for its wealth due to natural gas reserves and its investment in infrastructure. Today, Qatar is a global business hub and a prosperous nation."
    },
    "romania": {
        "descricao_pt": "A Romênia, oficialmente Romênia, é um país localizado na Europa Oriental, com uma história que inclui influências romanas e otomanas. Suas paisagens variam de montanhas a planícies férteis. Na atualidade, a Romênia é uma nação da União Europeia em crescimento, com uma cultura rica e patrimônio histórico.",
        "descricao_en": "Romania, officially Romania, is a country located in Eastern Europe, with a history that includes Roman and Ottoman influences. Its landscapes range from mountains to fertile plains. Today, Romania is a growing European Union nation with a rich culture and historical heritage."
    },
    "russia": {
        "descricao_pt": "A Rússia, oficialmente Federação Russa, é o maior país do mundo, estendendo-se pela Europa Oriental e Ásia do Norte. Sua história é rica e abrange desde o Império Russo até a União Soviética. Na atualidade, a Rússia é uma potência global, com uma cultura diversificada, vastas paisagens e uma economia complexa.",
        "descricao_en": "Russia, officially the Russian Federation, is the largest country in the world, spanning Eastern Europe and Northern Asia. Its history is rich, ranging from the Russian Empire to the Soviet Union. Today, Russia is a global powerhouse, with a diverse culture, vast landscapes, and a complex economy."
    },
    "rwanda": {
        "descricao_pt": "Ruanda, oficialmente República de Ruanda, é um país no leste da África conhecido por sua história de conflito étnico e genocídio. No entanto, o país fez progressos notáveis na reconciliação e no desenvolvimento pós-conflito. Na atualidade, Ruanda é reconhecida por seu crescimento econômico, estabilidade política e esforços de preservação ambiental.",
        "descricao_en": "Rwanda, officially the Republic of Rwanda, is a country in East Africa known for its history of ethnic conflict and genocide. However, the country has made significant progress in reconciliation and post-conflict development. Today, Rwanda is recognized for its economic growth, political stability, and environmental conservation efforts."
    },
    "saint kitts and nevis": {
        "descricao_pt": "São Cristóvão e Nevis é um pequeno país insular no Caribe, localizado no arquipélago das Pequenas Antilhas. Sua história remonta à colonização europeia, com diferentes potências coloniais governando as ilhas ao longo dos séculos. Atualmente, o país é conhecido por suas praias deslumbrantes e a indústria do turismo desempenha um papel importante em sua economia.",
        "descricao_en": "Saint Kitts and Nevis is a small island nation in the Caribbean, situated in the Lesser Antilles archipelago. Its history dates back to European colonization, with different colonial powers ruling the islands over the centuries. Today, the country is known for its stunning beaches, and the tourism industry plays a significant role in its economy."
    },
    "saint lucia": {
        "descricao_pt": "Santa Lúcia é uma ilha no mar do Caribe que foi colonizada pelos franceses e britânicos ao longo de sua história. Hoje, é uma nação independente com uma economia baseada principalmente no turismo. Suas belas praias, vulcões e florestas tropicais atraem visitantes de todo o mundo.",
        "descricao_en": "Saint Lucia is an island in the Caribbean Sea that has been colonized by both the French and the British throughout its history. Today, it is an independent nation with an economy primarily based on tourism. Its beautiful beaches, volcanoes, and rainforests attract visitors from all over the world."
    },
    "saint vincent and the grenadines": {
        "descricao_pt": "São Vicente e Granadinas é um país insular no mar do Caribe, composto por várias ilhas e ilhotas. Sua história inclui colonização europeia, principalmente por britânicos e franceses. Atualmente, o país é conhecido por suas praias intocadas e é um destino popular para iates e velejadores.",
        "descricao_en": "Saint Vincent and the Grenadines is an island nation in the Caribbean Sea, composed of multiple islands and islets. Its history includes European colonization, mainly by the British and the French. Today, the country is known for its unspoiled beaches and is a popular destination for yachts and sailors."
    },
    "samoa": {
        "descricao_pt": "Samoa é uma nação insular no Pacífico Sul, composta por várias ilhas. Sua história inclui períodos de governo alemão e neozelandês, antes de conquistar a independência em 1962. No presente, Samoa é conhecida por sua cultura polinésia única, praias deslumbrantes e hospitalidade calorosa.",
        "descricao_en": "Samoa is an island nation in the South Pacific, composed of multiple islands. Its history includes periods of German and New Zealand rule before gaining independence in 1962. Today, Samoa is known for its unique Polynesian culture, stunning beaches, and warm hospitality."
    },
    "san marino": {
        "descricao_pt": "San Marino é uma república no norte da Itália, completamente cercada pelo território italiano. É uma das nações mais antigas do mundo, com uma história que remonta à fundação em 301 d.C. San Marino é conhecida por sua arquitetura medieval impressionante e é um destino turístico popular.",
        "descricao_en": "San Marino is a republic in northern Italy, completely surrounded by Italian territory. It is one of the world's oldest nations, with a history dating back to its foundation in 301 AD. San Marino is known for its impressive medieval architecture and is a popular tourist destination."
    },
    "são tomé and príncipe": {
        "descricao_pt": "São Tomé e Príncipe é um país insular no Golfo da Guiné, na costa oeste da África Central. Sua história inclui o período colonial português, e a nação ganhou independência em 1975. Atualmente, o país é conhecido por suas paisagens tropicais, plantações de cacau e produção de café.",
        "descricao_en": "São Tomé and Príncipe is an island nation in the Gulf of Guinea, off the west coast of Central Africa. Its history includes the Portuguese colonial period, and the nation gained independence in 1975. Today, the country is known for its tropical landscapes, cocoa plantations, and coffee production."
    },
    "saudi arabia": {
        "descricao_pt": "Arábia Saudita é uma nação no Oriente Médio, conhecida por sua história rica e significativa importância no Islã. O país é lar das cidades sagradas de Meca e Medina e é conhecido por suas vastas reservas de petróleo. Nos dias de hoje, a Arábia Saudita passa por transformações econômicas e sociais significativas.",
        "descricao_en": "Saudi Arabia is a nation in the Middle East, known for its rich history and significant importance in Islam. The country is home to the holy cities of Mecca and Medina and is known for its vast oil reserves. Today, Saudi Arabia is undergoing significant economic and social transformations."
    },
    "senegal": {
        "descricao_pt": "Senegal é uma nação na África Ocidental com uma rica história que inclui a influência de impérios como o Mali e o Songhai. Atualmente, o país é conhecido por sua diversidade étnica, música vibrante e pela cidade costeira de Dakar, que é um centro cultural e econômico importante na região.",
        "descricao_en": "Senegal is a nation in West Africa with a rich history that includes the influence of empires like Mali and Songhai. Today, the country is known for its ethnic diversity, vibrant music, and the coastal city of Dakar, which is a significant cultural and economic hub in the region."
    },
    "serbia": {
        "descricao_pt": "Sérvia é um país localizado na região dos Bálcãs, no sudeste da Europa. Sua história inclui períodos de impérios como o Romano e o Otomano. Atualmente, a Sérvia é uma nação independente e é conhecida por sua cultura rica, belos mosteiros ortodoxos e a vibrante cidade de Belgrado.",
        "descricao_en": "Serbia is a country located in the Balkans region of Southeastern Europe. Its history includes periods of empires like the Roman and Ottoman. Today, Serbia is an independent nation and is known for its rich culture, beautiful Orthodox monasteries, and the vibrant city of Belgrade."
    },
    "seychelles": {
        "descricao_pt": "Seicheles é uma nação insular no oceano Índico, composta por várias ilhas. Sua história inclui influências francesas e britânicas. Atualmente, o país é um paraíso tropical conhecido por suas praias de areia branca, recifes de coral e biodiversidade marinha única.",
        "descricao_en": "Seychelles is an island nation in the Indian Ocean, composed of multiple islands. Its history includes French and British influences. Today, the country is a tropical paradise known for its white-sand beaches, coral reefs, and unique marine biodiversity."
    },
    "sierra leone": {
        "descricao_pt": "Serra Leoa é um país na África Ocidental com uma história marcada pelo comércio de escravos e o colonialismo britânico. Atualmente, o país se esforça para superar os desafios do passado e está trabalhando no desenvolvimento econômico e na construção de uma sociedade pacífica e democrática.",
        "descricao_en": "Sierra Leone is a country in West Africa with a history marked by the slave trade and British colonialism. Today, the country is striving to overcome the challenges of the past and is working on economic development and building a peaceful and democratic society."
    },
    "singapore": {
        "descricao_pt": "Singapura é uma cidade-estado no sudeste asiático, conhecida por sua transformação de uma pequena vila de pescadores em uma metrópole global de alta tecnologia. O país é um centro financeiro e de negócios importante e é famoso por sua limpeza e eficiência.",
        "descricao_en": "Singapore is a city-state in Southeast Asia, known for its transformation from a small fishing village into a high-tech global metropolis. The country is a major financial and business hub and is famous for its cleanliness and efficiency."
    },
    "slovakia": {
        "descricao_pt": "Eslováquia é uma nação na Europa Central, conhecida por sua paisagem montanhosa e história compartilhada com a República Tcheca. Após a separação pacífica, a Eslováquia se tornou independente em 1993. Atualmente, o país está prosperando economicamente e oferece belos cenários naturais.",
        "descricao_en": "Slovakia is a nation in Central Europe, known for its mountainous landscape and shared history with the Czech Republic. After a peaceful separation, Slovakia became independent in 1993. Today, the country is thriving economically and offers beautiful natural scenery."
    },
    "slovenia": {
        "descricao_pt": "Eslovênia é um país na Europa Central, anteriormente parte da Iugoslávia. Sua história inclui períodos de domínio estrangeiro. Atualmente, a Eslovênia é uma nação independente com uma economia estável e é conhecida por sua beleza natural, incluindo lagos e montanhas deslumbrantes.",
        "descricao_en": "Slovenia is a country in Central Europe, formerly part of Yugoslavia. Its history includes periods of foreign rule. Today, Slovenia is an independent nation with a stable economy and is known for its natural beauty, including stunning lakes and mountains."
    },
    "solomon islands": {
        "descricao_pt": "Ilhas Salomão é uma nação insular no Pacífico, conhecida por sua rica cultura indígena e biodiversidade única. Sua história inclui o período de governo britânico. Atualmente, o país está trabalhando no desenvolvimento econômico e na conservação de seus recursos naturais.",
        "descricao_en": "Solomon Islands is an island nation in the Pacific, known for its rich indigenous culture and unique biodiversity. Its history includes a period of British rule. Today, the country is working on economic development and the conservation of its natural resources."
    },
    "somalia": {
        "descricao_pt": "A Somália, oficialmente República Federal da Somália, é um país localizado no Chifre da África, na costa leste do continente africano. A história da Somália é marcada por civilizações antigas, comércio marítimo e influências culturais árabes e persas. No entanto, a nação passou por conflitos e instabilidade política nas últimas décadas. A Somália é conhecida por sua paisagem costeira espetacular e sua rica tradição oral.",
        "descricao_en": "Somalia, officially the Federal Republic of Somalia, is a country located in the Horn of Africa, on the eastern coast of the African continent. Somalia's history is marked by ancient civilizations, maritime trade, and Arab and Persian cultural influences. However, the nation has experienced conflict and political instability in recent decades. Somalia is known for its spectacular coastal landscape and rich oral tradition."
    },
    "south africa": {
        "descricao_pt": "A África do Sul, oficialmente República da África do Sul, é um país localizado no extremo sul do continente africano. A nação possui uma história complexa, incluindo o período do apartheid, que segregou a população com base na raça. Hoje, a África do Sul é uma democracia multirracial e possui uma diversidade cultural notável. O país é famoso por sua vida selvagem, com reservas de caça e parques nacionais.",
        "descricao_en": "South Africa, officially the Republic of South Africa, is a country located at the southernmost tip of the African continent. The nation has a complex history, including the period of apartheid, which segregated the population based on race. Today, South Africa is a multiracial democracy with remarkable cultural diversity. The country is famous for its wildlife, with game reserves and national parks."
    },
    "south korea": {
        "descricao_pt": "A Coreia do Sul, oficialmente República da Coreia, é um país localizado na península coreana, no leste da Ásia. A nação possui uma história milenar e é conhecida por sua cultura, tecnologia e economia avançadas. A Coreia do Sul é famosa por suas indústrias de tecnologia e entretenimento, incluindo empresas como Samsung e Hyundai. Além disso, o país é famoso por sua culinária, como o kimchi e o bulgogi.",
        "descricao_en": "South Korea, officially the Republic of Korea, is a country located on the Korean Peninsula in East Asia. The nation has a millennia-old history and is known for its advanced culture, technology, and economy. South Korea is famous for its technology and entertainment industries, including companies like Samsung and Hyundai. Additionally, the country is renowned for its cuisine, such as kimchi and bulgogi."
    },
    "south sudan": {
        "descricao_pt": "O Sudão do Sul é o país mais jovem do mundo, tendo conquistado sua independência do Sudão em 2011. Localizado na região da África Oriental, o Sudão do Sul enfrentou conflitos e desafios desde a sua formação. No entanto, o país abriga diversas culturas e etnias, e sua população é conhecida por sua resiliência. A nação possui recursos naturais significativos, incluindo petróleo.",
        "descricao_en": "South Sudan is the world's youngest country, having gained independence from Sudan in 2011. Located in the East African region, South Sudan has faced conflicts and challenges since its formation. However, the country is home to diverse cultures and ethnicities, and its population is known for its resilience. The nation possesses significant natural resources, including oil."
    },
    "spain": {
        "descricao_pt": "A Espanha, oficialmente Reino de Espanha, é um país localizado no sudoeste da Europa, na Península Ibérica. Com uma rica história que inclui a época dos impérios romano e mourisco, a Espanha é conhecida por sua cultura diversificada, com danças flamencas, festivais coloridos e pratos tradicionais, como a paella. Atualmente, a Espanha é uma democracia parlamentar e um destino turístico popular.",
        "descricao_en": "Spain, officially the Kingdom of Spain, is a country located in southwestern Europe on the Iberian Peninsula. With a rich history that includes the eras of the Roman and Moorish empires, Spain is known for its diverse culture, featuring flamenco dances, colorful festivals, and traditional dishes like paella. Today, Spain is a parliamentary democracy and a popular tourist destination."
    },
    "sri lanka": {
        "descricao_pt": "O Sri Lanka, oficialmente República Democrática Socialista do Sri Lanka, é uma ilha localizada no Oceano Índico, ao sul da Índia. O país possui uma história antiga e é conhecido por suas belezas naturais, como praias paradisíacas e montanhas exuberantes. O Sri Lanka também é famoso por seu chá Ceylon e locais históricos, como Anuradhapura e Polonnaruwa.",
        "descricao_en": "Sri Lanka, officially the Democratic Socialist Republic of Sri Lanka, is an island located in the Indian Ocean, south of India. The country has an ancient history and is known for its natural beauty, including idyllic beaches and lush mountains. Sri Lanka is also famous for its Ceylon tea and historical sites such as Anuradhapura and Polonnaruwa."
    },
    "sudan": {
        "descricao_pt": "O Sudão, oficialmente República do Sudão, é um país localizado no nordeste da África. A nação tem uma história rica que remonta aos tempos dos faraós e é atravessada pelo Rio Nilo, que desempenhou um papel vital na sua civilização. Atualmente, o Sudão é conhecido por sua diversidade étnica e cultural, mas também enfrentou conflitos e desafios políticos em sua história recente.",
        "descricao_en": "Sudan, officially the Republic of Sudan, is a country located in northeastern Africa. The nation has a rich history dating back to the time of the pharaohs and is traversed by the Nile River, which played a vital role in its civilization. Today, Sudan is known for its ethnic and cultural diversity but has also faced political conflicts and challenges in its recent history."
    },
    "suriname": {
        "descricao_pt": "Suriname, oficialmente República do Suriname, é um país localizado na costa norte da América do Sul. A nação tem uma história marcada pela colonização holandesa e pelo comércio de açúcar e escravos. Atualmente, o Suriname é conhecido por sua diversidade étnica, com influências culturais da Ásia, África e Europa. A exuberante floresta tropical amazônica cobre grande parte do país.",
        "descricao_en": "Suriname, officially the Republic of Suriname, is a country located on the northern coast of South America. The nation has a history marked by Dutch colonization and the sugar and slave trade. Today, Suriname is known for its ethnic diversity, with cultural influences from Asia, Africa, and Europe. The lush Amazon rainforest covers a significant portion of the country."
    },
    "sweden": {
        "descricao_pt": "A Suécia, oficialmente Reino da Suécia, é um país localizado no norte da Europa, na península escandinava. Com uma história que inclui os vikings, a Suécia é conhecida por seu sistema de bem-estar social, alta qualidade de vida e belas paisagens naturais, incluindo lagos e florestas. Atualmente, a nação é famosa por sua inovação tecnológica e design moderno.",
        "descricao_en": "Sweden, officially the Kingdom of Sweden, is a country located in northern Europe on the Scandinavian Peninsula. With a history that includes the Vikings, Sweden is known for its social welfare system, high quality of life, and beautiful natural landscapes, including lakes and forests. Today, the nation is famous for technological innovation and modern design."
    },
    "switzerland": {
        "descricao_pt": "A Suíça, oficialmente Confederação Suíça, é um país localizado na Europa Central. A nação é famosa por sua neutralidade política, sistema bancário sólido e paisagens alpinas deslumbrantes. A Suíça é conhecida por sua precisão na relojoaria, chocolates de alta qualidade e uma política de neutralidade em conflitos internacionais. O país abriga várias línguas, incluindo o alemão, francês, italiano e romanche.",
        "descricao_en": "Switzerland, officially the Swiss Confederation, is a country located in Central Europe. The nation is famous for its political neutrality, robust banking system, and stunning alpine landscapes. Switzerland is known for its precision in watchmaking, high-quality chocolates, and a policy of neutrality in international conflicts. The country is home to multiple languages, including German, French, Italian, and Romansh."
    },
    "syria": {
        "descricao_pt": "A Síria é um país localizado no Oriente Médio e tem uma história antiga que remonta às civilizações antigas, incluindo os impérios assírio e romano. No entanto, o país enfrentou conflitos e instabilidade nas últimas décadas. A Síria é conhecida por sua arquitetura histórica, como as cidades de Damasco e Aleppo, bem como pela sua culinária, que inclui pratos como o falafel e o kebab.",
        "descricao_en": "Syria is a country located in the Middle East and has an ancient history dating back to ancient civilizations, including the Assyrian and Roman empires. However, the country has faced conflicts and instability in recent decades. Syria is known for its historic architecture, such as the cities of Damascus and Aleppo, as well as its cuisine, which includes dishes like falafel and kebabs."
    },
    "tajikistan": {
        "descricao_pt": "O Tajiquistão é um país montanhoso localizado na Ásia Central. Possui uma história rica de influências culturais persas e soviéticas. A nação é conhecida por suas montanhas majestosas, como as Montanhas Pamir, e seu tapete persa tradicional. O Tajiquistão é um país de língua tajique e abriga uma cultura única enraizada nas tradições locais.",
        "descricao_en": "Tajikistan is a mountainous country located in Central Asia. It has a rich history of Persian and Soviet cultural influences. The nation is known for its majestic mountains, such as the Pamir Mountains, and its traditional Persian carpets. Tajikistan is a Tajik-speaking country and harbors a unique culture rooted in local traditions."
    },
    "tanzania": {
        "descricao_pt": "A Tanzânia é um país localizado na região da África Oriental e é conhecida por sua diversidade geográfica, que inclui montanhas, savanas e lindas praias à beira do Oceano Índico. A nação tem uma rica herança cultural, com diversas etnias e línguas. A Tanzânia é famosa por seus parques nacionais, incluindo o Serengeti, onde se pode observar a migração anual de gnus e zebras.",
        "descricao_en": "Tanzania is a country located in the East African region and is known for its geographical diversity, including mountains, savannahs, and beautiful beaches along the Indian Ocean. The nation has a rich cultural heritage, with diverse ethnicities and languages. Tanzania is famous for its national parks, including the Serengeti, where one can witness the annual migration of wildebeests and zebras."
    },
    "thailand": {
        "descricao_pt": "A Tailândia, oficialmente Reino da Tailândia, é um país localizado no sudeste da Ásia. A nação tem uma história rica de reinos e impérios, com uma cultura marcada pela religião budista. A Tailândia é conhecida por sua culinária picante e sabores exóticos, suas praias deslumbrantes e templos budistas impressionantes, como o Wat Pho. O turismo desempenha um papel importante na economia tailandesa.",
        "descricao_en": "Thailand, officially the Kingdom of Thailand, is a country located in Southeast Asia. The nation has a rich history of kingdoms and empires, with a culture marked by Buddhism. Thailand is known for its spicy cuisine and exotic flavors, stunning beaches, and impressive Buddhist temples, such as Wat Pho. Tourism plays a significant role in the Thai economy."
    },
    "timor-leste": {
        "descricao_pt": "Timor-Leste, também conhecido como Timor Oriental, é um pequeno país localizado no sudeste asiático. Possui uma história de luta pela independência e conquistou sua soberania em 2002. Timor-Leste é conhecido por sua cultura diversificada e línguas, incluindo o tétum e o português. A nação possui paisagens naturais deslumbrantes e uma rica herança cultural.",
        "descricao_en": "Timor-Leste, also known as East Timor, is a small country located in Southeast Asia. It has a history of struggle for independence and gained sovereignty in 2002. Timor-Leste is known for its diverse culture and languages, incluiding tetum and portuguese. The nation has beautiful natural landmarks and a rich cultural heritage."
    },
    "togo": {
        "descricao_pt": "Togo, oficialmente República Togolesa, é um país da África Ocidental. Sua história é marcada pela colonização alemã e francesa, e posteriormente, pela independência em 1960. Togo está localizado na costa do Golfo da Guiné e faz fronteira com Gana, Benin e Burkina Faso. Atualmente, o país enfrenta desafios econômicos e políticos, mas sua cultura diversificada e paisagens naturais atraem visitantes de todo o mundo.",
        "descricao_en": "Togo, officially the Togolese Republic, is a country in West Africa. Its history is marked by German and French colonization, and later, independence in 1960. Togo is located on the Gulf of Guinea coast and shares borders with Ghana, Benin, and Burkina Faso. Currently, the country faces economic and political challenges, but its diverse culture and natural landscapes attract visitors from around the world."
    },
    "tonga": {
        "descricao_pt": "Tonga, oficialmente Reino de Tonga, é uma nação insular no Pacífico Sul. Sua história inclui uma longa tradição de governantes hereditários. Localizada no Oceano Pacífico, Tonga é composta por várias ilhas e atóis. Hoje, o país é uma monarquia constitucional e é conhecido por suas praias deslumbrantes e cultura polinésia rica.",
        "descricao_en": "Tonga, officially the Kingdom of Tonga, is an island nation in the South Pacific. Its history includes a long tradition of hereditary rulers. Located in the Pacific Ocean, Tonga consists of several islands and atolls. Today, the country is a constitutional monarchy and is known for its stunning beaches and rich Polynesian culture."
    },
    "trinidad and tobago": {
        "descricao_pt": "Trinidad e Tobago é uma nação insular no Mar do Caribe, conhecida por sua diversidade étnica e cultural. Sua história inclui colonização espanhola, britânica e francesa. O país é formado pelas ilhas de Trinidad e Tobago, localizadas ao largo da costa da Venezuela. Atualmente, é uma república independente e tem uma economia diversificada com uma indústria de energia significativa.",
        "descricao_en": "Trinidad and Tobago is an island nation in the Caribbean Sea, known for its ethnic and cultural diversity. Its history includes Spanish, British, and French colonization. The country is made up of the islands of Trinidad and Tobago, located off the coast of Venezuela. It is currently an independent republic and has a diversified economy with a significant energy industry."
    },
    "tunisia": {
        "descricao_pt": "Tunísia, oficialmente República Tunisina, é um país do norte da África com uma história rica que inclui a influência de várias civilizações antigas, como fenícios, romanos e árabes. O país está localizado no litoral do Mar Mediterrâneo e faz fronteira com a Argélia e a Líbia. Atualmente, a Tunísia é uma república e é conhecida por suas praias, sítios arqueológicos e cultura única.",
        "descricao_en": "Tunisia, officially the Tunisian Republic, is a North African country with a rich history that includes the influence of various ancient civilizations such as Phoenicians, Romans, and Arabs. The country is located on the coast of the Mediterranean Sea and shares borders with Algeria and Libya. Currently, Tunisia is a republic and is known for its beaches, archaeological sites, and unique culture."
    },
    "turkey": {
        "descricao_pt": "Turquia, oficialmente República da Turquia, é um país transcontinental que se estende por parte da Europa e da Ásia. Sua história inclui o Império Otomano e a formação da República Turca. A Turquia faz fronteira com oito países e é cercada por três mares. Atualmente, é uma república democrática e secular, conhecida por sua rica herança histórica e cultura única.",
        "descricao_en": "Turkey, officially the Republic of Turkey, is a transcontinental country that spans both Europe and Asia. Its history includes the Ottoman Empire and the formation of the Turkish Republic. Turkey shares borders with eight countries and is surrounded by three seas. It is currently a democratic and secular republic, known for its rich historical heritage and unique culture."
    },
    "turkmenistan": {
        "descricao_pt": "Turcomenistão, oficialmente República do Turcomenistão, é um país da Ásia Central com uma história que remonta a impérios antigos, como o Império Parta. O país é conhecido por seu deserto de areia de Karakum e seu grande gás natural. Atualmente, é uma república presidencialista e está empenhado em desenvolver sua economia e infraestrutura.",
        "descricao_en": "Turkmenistan, officially the Republic of Turkmenistan, is a Central Asian country with a history dating back to ancient empires such as the Parthian Empire. The country is known for its Karakum Desert and abundant natural gas. It is currently a presidential republic and is committed to developing its economy and infrastructure."
    },
    "tuvalu": {
        "descricao_pt": "Tuvalu é uma nação insular na região do Pacífico. Sua história inclui o domínio colonial britânico e sua independência em 1978. Tuvalu é composta por nove pequenas ilhas e atóis. Atualmente, o país enfrenta desafios devido ao aumento do nível do mar, mas sua cultura única e beleza natural atraem atenção global.",
        "descricao_en": "Tuvalu is an island nation in the Pacific region. Its history includes British colonial rule and its independence in 1978. Tuvalu consists of nine small islands and atolls. Currently, the country faces challenges due to rising sea levels, but its unique culture and natural beauty attract global attention."
    },
    "uganda": {
        "descricao_pt": "Uganda é uma nação da África Oriental com uma história que inclui o domínio colonial britânico e a independência em 1962. O país é conhecido por sua biodiversidade e vida selvagem, incluindo os gorilas das montanhas. Uganda faz fronteira com vários países e é atravessada pelo Rio Nilo. Atualmente, é uma república e busca o desenvolvimento econômico e social.",
        "descricao_en": "Uganda is a country in East Africa with a history that includes British colonial rule and independence in 1962. The country is known for its biodiversity and wildlife, including mountain gorillas. Uganda shares borders with several countries and is traversed by the Nile River. Currently, it is a republic and seeks economic and social development."
    },
    "ukraine": {
        "descricao_pt": "Ucrânia, oficialmente Ucrânia, é um país no leste da Europa com uma história rica e complexa, incluindo períodos de dominação estrangeira e independência. A Ucrânia faz fronteira com vários países, incluindo Rússia e Polônia. Atualmente, o país é uma república e enfrenta desafios políticos e econômicos, mas também é conhecido por sua herança cultural e arquitetura impressionante.",
        "descricao_en": "Ukraine, officially Ukraine, is a country in Eastern Europe with a rich and complex history, including periods of foreign domination and independence. Ukraine shares borders with several countries, including Russia and Poland. Currently, the country is a republic and faces political and economic challenges, but is also known for its cultural heritage and impressive architecture."
    },
    "united arab emirates": {
        "descricao_pt": "Emirados Árabes Unidos, oficialmente Estados Unidos dos Emirados Árabes, é uma nação localizada no Golfo Pérsico. Sua história inclui a formação dos sete emirados e sua unificação em 1971. Os Emirados Árabes Unidos são conhecidos por sua riqueza, desenvolvimento moderno e cultura islâmica. Atualmente, é uma federação de emirados e um importante centro econômico na região.",
        "descricao_en": "United Arab Emirates, officially the United Arab Emirates, is a nation located in the Persian Gulf. Its history includes the formation of the seven emirates and their unification in 1971. The United Arab Emirates are known for their wealth, modern development, and Islamic culture. Currently, it is a federation of emirates and a major economic center in the region."
    },
    "united kingdom": {
        "descricao_pt": "O Reino Unido, oficialmente conhecido como Reino Unido da Grã-Bretanha e Irlanda do Norte, é uma nação insular localizada na Europa Ocidental. Sua história é marcada por um passado de império colonial, que abrangeu uma parte significativa do mundo. Hoje, o Reino Unido é uma monarquia constitucional composta por quatro nações constituintes: Inglaterra, Escócia, País de Gales e Irlanda do Norte. É conhecido por sua rica herança cultural, incluindo literatura, música e tradições históricas.",
        "descricao_en": "The United Kingdom, officially known as the United Kingdom of Great Britain and Northern Ireland, is an island nation located in Western Europe. Its history is marked by a colonial empire that spanned a significant portion of the world. Today, the UK is a constitutional monarchy comprising four constituent nations: England, Scotland, Wales, and Northern Ireland. It is known for its rich cultural heritage, including literature, music, and historical traditions."
    },
    "united states": {
        "descricao_pt": "Os Estados Unidos, oficialmente conhecidos como Estados Unidos da América, são uma nação situada na América do Norte. Sua história é marcada pela independência do domínio britânico em 1776 e pela expansão para o oeste, conhecida como a Marcha para o Oeste. Atualmente, os Estados Unidos são uma república federal composta por 50 estados e um distrito federal. É uma das maiores economias do mundo e um líder global em tecnologia, cultura e inovação.",
        "descricao_en": "The United States, officially known as the United States of America, is a nation located in North America. Its history is marked by the independence from British rule in 1776 and westward expansion, known as the Westward Expansion. Today, the United States is a federal republic comprising 50 states and a federal district. It is one of the world's largest economies and a global leader in technology, culture, and innovation."
    },
    "uruguay": {
        "descricao_pt": "O Uruguai, oficialmente a República Oriental do Uruguai, é um país situado na América do Sul. Sua história é marcada por lutas pela independência do domínio espanhol e português. Atualmente, o Uruguai é uma república democrática com uma economia diversificada e é conhecido por suas belas praias e tradições culturais, incluindo o tango e o carnaval de Montevidéu.",
        "descricao_en": "Uruguay, officially the Oriental Republic of Uruguay, is a country located in South America. Its history is marked by struggles for independence from Spanish and Portuguese rule. Today, Uruguay is a democratic republic with a diversified economy and is known for its beautiful beaches and cultural traditions, including tango and the Montevideo carnival."
    },
    "uzbekistan": {
        "descricao_pt": "Uzbequistão, oficialmente a República do Uzbequistão, é um país da Ásia Central. Sua história é rica em antigas civilizações, incluindo a Rota da Seda. Atualmente, o Uzbequistão é uma república com uma economia em desenvolvimento e é conhecido por sua arquitetura islâmica, incluindo a cidade antiga de Samarcanda, e sua tradição de tapetes e artesanato.",
        "descricao_en": "Uzbekistan, officially the Republic of Uzbekistan, is a country in Central Asia. Its history is rich in ancient civilizations, including the Silk Road. Today, Uzbekistan is a republic with a developing economy and is known for its Islamic architecture, including the ancient city of Samarkand, and its tradition of carpets and crafts."
    },
    "vanuatu": {
        "descricao_pt": "Vanuatu, oficialmente a República de Vanuatu, é uma nação insular situada no Oceano Pacífico. Sua história é marcada por uma mistura de culturas e influências coloniais. Atualmente, Vanuatu é uma república democrática e é conhecida por sua beleza natural, praias de areia branca e cultura única, incluindo cerimônias tradicionais e danças.",
        "descricao_en": "Vanuatu, officially the Republic of Vanuatu, is an island nation located in the Pacific Ocean. Its history is marked by a blend of cultures and colonial influences. Today, Vanuatu is a democratic republic and is known for its natural beauty, white sandy beaches, and unique culture, including traditional ceremonies and dances."
    },
    "venezuela": {
        "descricao_pt": "A Venezuela, oficialmente a República Bolivariana da Venezuela, é um país localizado na América do Sul. Sua história inclui a independência liderada por Simón Bolívar e um passado de riqueza petrolífera. Atualmente, a Venezuela enfrenta desafios econômicos e políticos, mas é conhecida por suas paisagens naturais impressionantes, incluindo o Salto Angel, a cachoeira mais alta do mundo.",
        "descricao_en": "Venezuela, officially the Bolivarian Republic of Venezuela, is a country located in South America. Its history includes independence led by Simón Bolívar and a history of oil wealth. Today, Venezuela faces economic and political challenges but is known for its stunning natural landscapes, including Angel Falls, the world's tallest waterfall."
    },
    "vietnam": {
        "descricao_pt": "O Vietnã, oficialmente a República Socialista do Vietnã, é um país no sudeste asiático. Sua história é marcada por conflitos, incluindo a Guerra do Vietnã. Atualmente, o Vietnã é uma república socialista em rápido crescimento e é conhecido por sua culinária única, belas paisagens, como a Baía de Halong, e sua história cultural rica.",
        "descricao_en": "Vietnam, officially the Socialist Republic of Vietnam, is a country in Southeast Asia. Its history is marked by conflicts, including the Vietnam War. Today, Vietnam is a rapidly growing socialist republic and is known for its unique cuisine, beautiful landscapes like Halong Bay, and rich cultural history."
    },
    "yemen": {
        "descricao_pt": "O Iêmen, oficialmente a República do Iêmen, é um país localizado na ponta sul da Península Arábica. Sua história é rica em civilizações antigas, incluindo os sabeus e os nabateus. Atualmente, o Iêmen enfrenta conflitos e desafios humanitários, mas é conhecido por sua herança cultural, incluindo a antiga cidade de Sanaa e a arquitetura de arranha-céus de barro.",
        "descricao_en": "Yemen, officially the Republic of Yemen, is a country located at the southern tip of the Arabian Peninsula. Its history is rich in ancient civilizations, including the Sabeans and Nabateans. Today, Yemen faces conflicts and humanitarian challenges but is known for its cultural heritage, including the ancient city of Sanaa and skyscraper-like clay architecture."
    },
    "zambia": {
        "descricao_pt": "A Zâmbia, oficialmente a República da Zâmbia, é um país localizado no sul da África. Sua história é marcada pela independência do domínio colonial britânico. Atualmente, a Zâmbia é uma república democrática em crescimento e é conhecida por suas paisagens naturais, incluindo as Cataratas Vitória, e uma diversidade étnica rica com várias línguas e culturas.",
        "descricao_en": "Zambia, officially the Republic of Zambia, is a country located in Southern Africa. Its history is marked by independence from British colonial rule. Today, Zambia is a growing democratic republic and is known for its natural landscapes, including Victoria Falls, and a rich ethnic diversity with multiple languages and cultures."
    },
    "zimbabwe": {
        "descricao_pt": "O Zimbábue, oficialmente a República do Zimbábue, é um país situado no sul da África. Sua história é marcada por civilizações antigas, como o Reino de Mutapa, e pela luta pela independência do domínio colonial britânico. Atualmente, o Zimbábue enfrenta desafios econômicos, mas é conhecido por suas paisagens naturais, como as Montanhas Inyanga, e sua rica herança cultural.",
        "descricao_en": "Zimbabwe, officially the Republic of Zimbabwe, is a country located in Southern Africa. Its history is marked by ancient civilizations, such as the Kingdom of Mutapa, and the struggle for independence from British colonial rule. Today, Zimbabwe faces economic challenges but is known for its natural landscapes, like the Inyanga Mountains, and its rich cultural heritage."
    }
};

var dados = {
    "afghanistan": {
        "nome_pt": "Afeganistão",
        "nome_en": "Afghanistan",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Flag_of_Afghanistan.svg",
        "descricao_pt": "O Afeganistão, oficialmente conhecido como República Islâmica do Afeganistão, é um país localizado no Sul da Ásia. Sua rica história é marcada por diversos impérios, como o Persa, Grego e Islâmico. Geograficamente, o Afeganistão é uma nação sem litoral, cercada pelo Paquistão, Irã, Turcomenistão, Uzbequistão, Tajiquistão e China. Nos tempos recentes, o Afeganistão enfrentou instabilidade política e conflitos, mas continua a trabalhar em direção à estabilidade e paz.",
        "descricao_en": "Afghanistan, officially known as the Islamic Republic of Afghanistan, is a country located in South Asia. It has a rich history characterized by various empires, such as the Persian, Greek, and Islamic empires. Geographically, Afghanistan is a landlocked nation, bordered by Pakistan, Iran, Turkmenistan, Uzbekistan, Tajikistan, and China. In recent times, Afghanistan has faced political instability and conflict, but it continues to work towards stability and peace.",
        "populacao": "39.232.003 (2023 est.)",
        "area": " 652.230",
        "pib": "$20.240.000.000 (2017 est.)",
        "idioma_en": "Dari and Pashto",
        "idioma_pt": "Dari e Pastó",
        "capital_en": "Kabul",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/1/19/Afghanistan_%28orthographic_projection%29.svg",
        "idh": 0.478
    },
    "albania": {
        "nome_pt": "Albânia",
        "nome_en": "Albania",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/3/36/Flag_of_Albania.svg",
        "descricao_pt": "A Albânia, oficialmente conhecida como República da Albânia, é um país localizado no Sudeste da Europa. Sua história é marcada pelos Impérios Bizantino e Otomano. A Albânia é conhecida por suas deslumbrantes costas no Mar Adriático e Jônico. Atualmente, é uma democracia parlamentar que trabalha no fortalecimento de sua economia e instituições políticas.",
        "descricao_en": "Albania, officially known as the Republic of Albania, is a country located in Southeastern Europe. Its history is marked by the Byzantine and Ottoman Empires. Albania is known for its stunning Adriatic and Ionian coastlines. Today, it is a parliamentary democracy and is working on strengthening its economy and political institutions.",
        "populacao": "3.101.621 (2023 est.)",
        "area": " 28.748",
        "pib": "$15.273.000.000 (2019 est.)",
        "idioma_en": "Albanian",
        "idioma_pt": "Albanês",
        "capital_en": "Tirana (Tirane)",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/d/d5/Albania_%28orthographic_projection%29.svg",
        "idh": 0.796
    },
    "algeria": {
        "nome_pt": "Argélia",
        "nome_en": "Algeria",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/7/77/Flag_of_Algeria.svg",
        "descricao_pt": "A Argélia, oficialmente conhecida como República Democrática Popular da Argélia, é o maior país da África e está localizada no Norte da África. Sua história inclui períodos de domínio romano e árabe. A Argélia possui paisagens diversas, que vão desde o Deserto do Saara até a costa do Mediterrâneo. Nos dias de hoje, é uma república com uma economia em crescimento.",
        "descricao_en": "Algeria, officially known as the People's Democratic Republic of Algeria, is the largest country in Africa and is located in North Africa. Its history includes periods of Roman and Arab rule. Algeria boasts diverse landscapes, from the Sahara Desert to the Mediterranean coastline. In the present day, it is a republic with a growing economy.",
        "populacao": "44.758.398 (2023 est.)",
        "area": " 2.381.740",
        "pib": "$169.912.000.000 (2019 est.)",
        "idioma_en": "Arabic, French and Berber;",
        "idioma_pt": "Arábe, Francês e Berbere;",
        "capital_en": "Algiers",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/2/25/Algeria_%28orthographic_projection%29.svg",
        "idh": 0.745
    },
    "andorra": {
        "nome_pt": "Andorra",
        "nome_en": "Andorra",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/1/19/Flag_of_Andorra.svg",
        "descricao_pt": "Andorra é um pequeno país europeu localizado nos Pirenéus orientais, fazendo fronteira com a França e Espanha. Tem uma história única de co-principado, com o Presidente da França e o Bispo de Urgell na Espanha servindo como seus co-príncipes. Andorra é conhecida por suas paisagens pitorescas e é um destino popular para turistas. Hoje, é uma democracia parlamentar.",
        "descricao_en": "Andorra is a small European country located in the eastern Pyrenees mountains, bordered by France and Spain. It has a unique history of co-principality, with the President of France and the Bishop of Urgell in Spain serving as its co-princes. Andorra is known for its picturesque landscapes and is a popular destination for tourists. Today, it is a parliamentary democracy.",
        "populacao": "85.468 (2023 est.)",
        "area": " 468",
        "pib": "$2.712.000.000 (2016 est.)",
        "idioma_en": "Catalan",
        "idioma_pt": "Catalão",
        "capital_en": "Andorra la Vella",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Location_Andorra_Europe.png/255px-Location_Andorra_Europe.png",
        "idh": 0.858
    },
    "angola": {
        "nome_pt": "Angola",
        "nome_en": "Angola",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/9/9d/Flag_of_Angola.svg",
        "descricao_pt": "Angola, oficialmente conhecida como República de Angola, é um país no Sul da África. Tem uma história de colonização portuguesa e uma longa luta pela independência. Geograficamente, Angola possui uma paisagem diversificada, incluindo uma extensa costa ao longo do Oceano Atlântico. Na era contemporânea, Angola é uma república que trabalha para reconstruir sua economia após um período de guerra civil.",
        "descricao_en": "Angola, officially known as the Republic of Angola, is a country in Southern Africa. It has a history of Portuguese colonization and a long struggle for independence. Geographically, Angola has a diverse landscape, including a lengthy coastline along the Atlantic Ocean. In the contemporary era, Angola is a republic working to rebuild its economy after a period of civil war.",
        "populacao": "35.981.281 (2023 est.)",
        "area": " 1.246.700",
        "pib": "$97.261.000.000 (2019 est.)",
        "idioma_en": "Portuguese",
        "idioma_pt": "Português",
        "capital_en": "Luanda",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/8/89/Angola_%28orthographic_projection%29.svg",
        "idh": 0.586
    },
    "antigua and barbuda": {
        "nome_pt": "Antígua e Barbuda",
        "nome_en": "Antigua and Barbuda",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/8/89/Flag_of_Antigua_and_Barbuda.svg",
        "descricao_pt": "Antígua e Barbuda é uma nação caribenha localizada nas Índias Ocidentais. Tem uma história de colonização britânica e é conhecida por suas belas praias e recifes de coral. Hoje, é uma monarquia constitucional e democracia parlamentar, com foco no turismo e serviços financeiros.",
        "descricao_en": "Antigua and Barbuda is a Caribbean nation located in the West Indies. It has a history of British colonization and is known for its beautiful beaches and coral reefs. Today, it is a constitutional monarchy and parliamentary democracy with a focus on tourism and financial services.",
        "populacao": "101.489 (2023 est.)",
        "area": " 443 (Antigua 280; Barbuda 161)",
        "pib": "$1.524.000.000 (2017 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Saint John's",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/ATG_orthographic.svg/255px-ATG_orthographic.svg.png",
        "idh": 0.788
    },
    "argentina": {
        "nome_pt": "Argentina",
        "nome_en": "Argentina",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Flag_of_Argentina.svg",
        "descricao_pt": "A Argentina, oficialmente conhecida como República Argentina, é um país sul-americano com uma rica história de colonização espanhola e imigração. Geograficamente, é conhecida por suas paisagens diversas, incluindo as montanhas dos Andes e as planícies das Pampas. A Argentina é uma república federal com uma sólida base agrícola e industrial.",
        "descricao_en": "Argentina, officially known as the Argentine Republic, is a South American country with a rich history of Spanish colonization and immigration. Geographically, it is known for its diverse landscapes, including the Andes mountains and the Pampas plains. Argentina is a federal republic with a strong agricultural and industrial base.",
        "populacao": "46.621.847 (2023 est.)",
        "area": " 2.780.400",
        "pib": "$447.467.000.000 (2019 est.)",
        "idioma_en": "Spanish",
        "idioma_pt": "Espanhol",
        "capital_en": "Buenos Aires",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/bd/Argentina_orthographic.svg",
        "idh": 0.842
    },
    "armenia": {
        "nome_pt": "Armênia",
        "nome_en": "Armenia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Flag_of_Armenia.svg",
        "descricao_pt": "A Armênia é um país sem litoral na região do Cáucaso do Sul da Eurásia. Tem uma longa história que remonta à antiguidade e experimentou vários impérios e conflitos. Hoje, a Armênia é uma república e está trabalhando no desenvolvimento de sua economia e na promoção da estabilidade na região.",
        "descricao_en": "Armenia is a landlocked country in the South Caucasus region of Eurasia. It has a long history dating back to ancient times and has experienced various empires and conflicts. Today, Armenia is a republic and is working to develop its economy and promote stability in the region.",
        "populacao": "2.989.091 (2023 est.)",
        "area": " 29.743",
        "pib": "$13.694.000.000 (2019 est.)",
        "idioma_en": "Armenian",
        "idioma_pt": "Armênio",
        "capital_en": "Yerevan",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/9/96/Armenia_%28orthographic_projection%29.svg",
        "idh": 0.759
    },
    "australia": {
        "nome_pt": "Austrália",
        "nome_en": "Australia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/8/88/Flag_of_Australia_%28converted%29.svg",
        "descricao_pt": "A Austrália, oficialmente conhecida como Comunidade da Austrália, é uma grande nação insular e continente localizado no Hemisfério Sul. Tem uma história única como colônia britânica e é conhecida por suas paisagens naturais deslumbrantes e vida selvagem. Na era moderna, a Austrália é uma monarquia constitucional parlamentar federal.",
        "descricao_en": "Australia, officially known as the Commonwealth of Australia, is a large island nation and continent located in the Southern Hemisphere. It has a unique history as a British colony and is known for its stunning natural landscapes and wildlife. In the modern era, Australia is a federal parliamentary constitutional monarchy.",
        "populacao": "26.461.166 (2023 est.)",
        "area": " 7.741.220",
        "pib": "$1.390.790.000.000 (2019 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Canberra",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/7/7d/Australia_%28orthographic_projection%29.svg",
        "idh": 0.951
    },
    "austria": {
        "nome_pt": "Áustria",
        "nome_en": "Austria",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/4/41/Flag_of_Austria.svg",
        "descricao_pt": "A Áustria, oficialmente conhecida como República da Áustria, é um país sem litoral na Europa Central. Tem uma história intimamente ligada à monarquia dos Habsburgos e ao Império Austro-Húngaro. Geograficamente, a Áustria é conhecida por suas deslumbrantes paisagens alpinas. Na era contemporânea, a Áustria é uma república federal com uma forte herança cultural e ênfase nas artes.",
        "descricao_en": "Austria, officially known as the Republic of Austria, is a landlocked country in Central Europe. It has a history closely tied to the Habsburg monarchy and the Austro-Hungarian Empire. Geographically, Austria is known for its stunning Alpine landscapes. In the contemporary era, Austria is a federal republic with a strong cultural heritage and emphasis on the arts.",
        "populacao": "8.940.860 (2023 est.)",
        "area": " 83.871",
        "pib": "$445.025.000.000 (2019 est.)",
        "idioma_en": "German",
        "idioma_pt": "Alemão",
        "capital_en": "Vienna",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/3/38/EU-Austria_%28orthographic_projection%29.svg",
        "idh": 0.916
    },
    "azerbaijan": {
        "nome_pt": "Azerbaijão",
        "nome_en": "Azerbaijan",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/d/dd/Flag_of_Azerbaijan.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "10.420.515 (2023 est.)",
        "area": " 86.600",
        "pib": "$48.104.000.000 (2019 est.)",
        "idioma_en": "Azeri",
        "idioma_pt": "Azeri",
        "capital_en": "Baku (Baki, Baky)",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/0/01/Azerbaijan_%28orthographic_projection%29.svg",
        "idh": 0.745
    },
    "bahamas": {
        "nome_pt": "Bahamas",
        "nome_en": "Bahamas",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/9/93/Flag_of_the_Bahamas.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "358.508 (2023 est.)",
        "area": " 13.880",
        "pib": "$12.160.000.000 (2017 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Nassau",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/d/de/The_Bahamas_on_the_globe_%28Americas_centered%29.svg",
        "idh": 0.812
    },
    "bahrain": {
        "nome_pt": "Bahrein",
        "nome_en": "Bahrain",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/2/2c/Flag_of_Bahrain.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "1.553.886 (2023 est.)",
        "area": " 760",
        "pib": "$38.472.000.000 (2019 est.)",
        "idioma_en": "Arabic",
        "idioma_pt": "Arábe",
        "capital_en": "Manama",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/8/83/Map_of_Bahrain.svg",
        "idh": 0.875
    },
    "bangladesh": {
        "nome_pt": "Bangladesh",
        "nome_en": "Bangladesh",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/f/f9/Flag_of_Bangladesh.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "167.184.465 (2023 est.)",
        "area": " 148.460",
        "pib": "$329.545.000.000 (2020 est.)",
        "idioma_en": "Bangla",
        "idioma_pt": "Bengali",
        "capital_en": "Dhaka",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/f/f2/Bangladesh_%28orthographic_projection%29.svg",
        "idh": 0.661
    },
    "barbados": {
        "nome_pt": "Barbados",
        "nome_en": "Barbados",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/e/ef/Flag_of_Barbados.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "303.431 (2023 est.)",
        "area": " 430",
        "pib": "$4.990.000.000 (2017 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Bridgetown",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/a/a1/BRB_orthographic.svg",
        "idh": 0.79
    },
    "belarus": {
        "nome_pt": "Bielorrússia",
        "nome_en": "Belarus",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/8/85/Flag_of_Belarus.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "9.383.853 (2023 est.)",
        "area": " 207.600",
        "pib": "$63.168.000.000 (2019 est.)",
        "idioma_en": "Russian and Belarusian",
        "idioma_pt": "Russo e Belarusian",
        "capital_en": "Minsk",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Belarus_%28orthographic_projection%29.svg",
        "idh": 0.808
    },
    "belgium": {
        "nome_pt": "Bélgica",
        "nome_en": "Belgium",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/6/65/Flag_of_Belgium.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "11.913.633 (2023 est.)",
        "area": " 30.528",
        "pib": "$533.028.000.000 (2019 est.)",
        "idioma_en": "Dutch, French and German",
        "idioma_pt": "Neerlandês, Francês e Alemão",
        "capital_en": "Brussels",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/7/79/Belgium_%28orthographic_projection%29.svg",
        "idh": 0.937
    },
    "belize": {
        "nome_pt": "Belize",
        "nome_en": "Belize",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/e/e7/Flag_of_Belize.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "419.137 (2023 est.)",
        "area": " 22.966",
        "pib": "$1.854.000.000 (2017 est.)",
        "idioma_en": "English,",
        "idioma_pt": "Inglês,",
        "capital_en": "Belmopan",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/4/43/BLZ_orthographic.svg",
        "idh": 0.683
    },
    "benin": {
        "nome_pt": "Benin",
        "nome_en": "Benin",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Flag_of_Benin.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "14.219.908 (2023 est.)",
        "area": " 112.622",
        "pib": "$10.315.000.000 (2018 est.)",
        "idioma_en": "French",
        "idioma_pt": "Francês",
        "capital_en": "Porto-Novo (de jure), Cotonou (de facto)",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/0/01/Benin_%28orthographic_projection_with_inset%29.svg",
        "idh": 0.525
    },
    "bhutan": {
        "nome_pt": "Butão",
        "nome_en": "Bhutan",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/9/91/Flag_of_Bhutan.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "876.181 (2023 est.)",
        "area": " 38.394",
        "pib": "$2.405.000.000 (2017 est.)",
        "idioma_en": "Dzongkha",
        "idioma_pt": "Dzonga",
        "capital_en": "Thimphu",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/c/ce/Bhutan_%28orthographic_projection%29.svg",
        "idh": 0.666
    },
    "bolivia": {
        "nome_pt": "Bolívia",
        "nome_en": "Bolivia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/d/de/Flag_of_Bolivia_%28state%29.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "12.186.079 (2023 est.)",
        "area": " 1.098.581",
        "pib": "$40.822.000.000 (2019 est.)",
        "idioma_en": "Spanish, Quechua, Aymara, Guarani and other indigineous languages",
        "idioma_pt": "Espanhol, Quéchua, Aimará, Guarani e other indigineous languages",
        "capital_en": "La Paz (administrative capital); Sucre (constitutional [legislative and judicial] capital)",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Bolivia_%28orthographic_projection%29.svg",
        "idh": 0.692
    },
    "bosnia and herzegovina": {
        "nome_pt": "Bósnia e Herzegovina",
        "nome_en": "Bosnia and Herzegovina",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/b/bf/Flag_of_Bosnia_and_Herzegovina.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "3.807.764 (2023 est.)",
        "area": " 51.197",
        "pib": "$20.078.000.000 (2019 est.)",
        "idioma_en": "Bosnian, Serbian and Croatian",
        "idioma_pt": "Bósnio, Sérvio e Croata",
        "capital_en": "Sarajevo",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/2/24/Bosnia_and_Herzegovina_%28orthographic_projection%29.svg",
        "idh": 0.78
    },
    "botswana": {
        "nome_pt": "Botsuana",
        "nome_en": "Botswana",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Flag_of_Botswana.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "2.417.596 (2023 est.)",
        "area": " 581.730",
        "pib": "$18.335.000.000 (2019 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Gaborone",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/c/c1/BWA_orthographic.svg",
        "idh": 0.693
    },
    "brazil": {
        "nome_pt": "Brasil",
        "nome_en": "Brazil",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/0/05/Flag_of_Brazil.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "218.689.757 (2023 est.)",
        "area": " 8.515.770",
        "pib": "$1.877.942.000.000 (2019 est.)",
        "idioma_en": "Portuguese",
        "idioma_pt": "Português",
        "capital_en": "Brasília",
        "capital_pt": "Brasí­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/bc/BRA_orthographic.svg",
        "idh": 0.754
    },
    "brunei": {
        "nome_pt": "Brunei",
        "nome_en": "Brunei",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/9/9c/Flag_of_Brunei.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "484.991",
        "area": " 5.765",
        "pib": "$12.130.000.000 (2017 est.)",
        "idioma_en": "Malay",
        "idioma_pt": "Malaio",
        "capital_en": "Bandar Seri Begawan",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/c/c0/Brunei_in_its_region_%28special_marker%29.svg",
        "idh": 0.829
    },
    "bulgaria": {
        "nome_pt": "Bulgária",
        "nome_en": "Bulgaria",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Flag_of_Bulgaria.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "6.827.736 (2023 est.)",
        "area": " 110.879",
        "pib": "$68.489.999.999..99.999 (2019 est.)",
        "idioma_en": "Bulgarian",
        "idioma_pt": "Búlgaro",
        "capital_en": "Sofia",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Bulgaria_%28orthographic_projection%29.svg",
        "idh": 0.795
    },
    "burkina faso": {
        "nome_pt": "Burquina Faso",
        "nome_en": "Burkina Faso",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/3/31/Flag_of_Burkina_Faso.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "22.489.126 (2023 est.)",
        "area": " 274.200",
        "pib": "$14.271.000.000 (2018 est.)",
        "idioma_en": "French",
        "idioma_pt": "Francês",
        "capital_en": "Ouagadougou",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/8/86/Burkina_Faso_%28orthographic_projection%29.svg",
        "idh": 0.449
    },
    "burundi": {
        "nome_pt": "Burundi",
        "nome_en": "Burundi",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/5/50/Flag_of_Burundi.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "13.162.952 (2023 est.)",
        "area": " 27.830",
        "pib": "$3.027.000.000 (2019 est.)",
        "idioma_en": "Kirundi, French and English",
        "idioma_pt": "Kirundi, Francês e Inglês",
        "capital_en": "Gitega",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/2/27/Burundi_%28orthographic_projection%29.svg",
        "idh": 0.426
    },
    "cambodia": {
        "nome_pt": "Camboja",
        "nome_en": "Cambodia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/8/83/Flag_of_Cambodia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "16.891.245 (2023 est.)",
        "area": " 181.035",
        "pib": "$22.090.000.000 (2017 est.)",
        "idioma_en": "Khmer",
        "idioma_pt": "Khmer",
        "capital_en": "Phnom Penh",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/bc/BRA_orthographic.svg",
        "idh": 0.593
    },
    "cameroon": {
        "nome_pt": "Camarões",
        "nome_en": "Cameroon",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/4/4f/Flag_of_Cameroon.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "30.135.732 (2023 est.)",
        "area": " 475.440",
        "pib": "$34.990.000.000 (2017 est.)",
        "idioma_en": "English and French",
        "idioma_pt": "Inglês e Francês",
        "capital_en": "Yaounde",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/b4/Cameroon_%28orthographic_projection%29.svg",
        "idh": 0.576
    },
    "canada": {
        "nome_pt": "Canadá",
        "nome_en": "Canada",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/d/d9/Flag_of_Canada_%28Pantone%29.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "38.516.736 (2023 est.)",
        "area": " 9.984.670",
        "pib": "$1.741.865.000.000 (2019 est.)",
        "idioma_en": "English and French",
        "idioma_pt": "Inglês e Francês",
        "capital_en": "Ottawa",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/c/c7/Canada_%28orthographic_projection%29.svg",
        "idh": 0.936
    },
    "cape verde": {
        "nome_pt": "Cabo Verde",
        "nome_en": "Cape Verde",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/3/38/Flag_of_Cape_Verde.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "603.901 (2023 est.)",
        "area": " 4.033",
        "pib": "$1.971.000.000 (2019 est.)",
        "idioma_en": "Portuguese",
        "idioma_pt": "Português",
        "capital_en": "Praia",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/4/47/Cape_Verde_%28orthographic_projection%29.svg",
        "idh": 0.662
    },
    "central african republic": {
        "nome_pt": "República Centro-Africana",
        "nome_en": "Central African Republic",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Flag_of_the_Central_African_Republic.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "5.552.228 (2023 est.)",
        "area": " 622.984",
        "pib": "$1.937.000.000 (2017 est.)",
        "idioma_en": "French and Sangho",
        "idioma_pt": "Francês e Sango",
        "capital_en": "Bangui",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/c/c4/Central_African_Republic_%28orthographic_projection%29.svg",
        "idh": 0.404
    },
    "chad": {
        "nome_pt": "Chade",
        "nome_en": "Chad",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Flag_of_Chad.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "18.523.165 (2023 est.)",
        "area": " 1.284 million",
        "pib": "$10.912.000.000 (2019 est.)",
        "idioma_en": "French and Arabic",
        "idioma_pt": "Francês e Arábe",
        "capital_en": "N'Djamena",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/4/46/Chad_%28orthographic_projection%29.svg",
        "idh": 0.394
    },
    "chile": {
        "nome_pt": "Chile",
        "nome_en": "Chile",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/7/78/Flag_of_Chile.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "18.549.457 (2023 est.)",
        "area": " 756.102",
        "pib": "$282.655.000.000 (2019 est.)",
        "idioma_en": "Spanish",
        "idioma_pt": "Espanhol",
        "capital_en": "Santiago",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/d/d5/Chile_%28orthographic_projection%29.svg",
        "idh": 0.855
    },
    "china": {
        "nome_pt": "China",
        "nome_en": "China",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Flag_of_the_People%27s_Republic_of_China.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "1.413.142.846 (2023 est.)",
        "area": " 9.596.960",
        "pib": "$14.327.359.000.000 (2019 est.)",
        "idioma_en": "Mandarin, Zhuang, Yue, Mongolian, Uygur, Kyrgyz and Tibetan",
        "idioma_pt": "Mandarim, Xuém, Cantonês, Mongól, Uigur, Quirguiz e Tibetano",
        "capital_en": "Beijing",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/7/78/People%27s_Republic_of_China_%28orthographic_projection%29.svg",
        "idh": 0.768
    },
    "colombia": {
        "nome_pt": "Colômbia",
        "nome_en": "Colombia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/2/21/Flag_of_Colombia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "49.336.454 (2023 est.)",
        "area": " 1.138.910",
        "pib": "$323.255.000.000 (2019 est.)",
        "idioma_en": "Spanish",
        "idioma_pt": "Espanhol",
        "capital_en": "Bogota",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/6/6f/COL_orthographic.svg",
        "idh": 0.752
    },
    "comoros": {
        "nome_pt": "Comores",
        "nome_en": "Comoros",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/9/94/Flag_of_the_Comoros.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "888.378 (2023 est.)",
        "area": " 2.235",
        "pib": "$1.186.000.000 (2019 est.)",
        "idioma_en": "Arabic, French and Shikomoro",
        "idioma_pt": "Arábe, Francês e Shikomoro",
        "capital_en": "Moroni",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/a/ad/Comoros_%28orthographic_projection%29.svg",
        "idh": 0.558
    },
    "democratic republic of congo": {
        "nome_pt": "República Democrática do Congo",
        "nome_en": "Democratic Republic of Congo",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Flag_of_the_Democratic_Republic_of_the_Congo.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "111.859.928 (2023 est.)",
        "area": " 2.344.858",
        "pib": "$47.160.000.000 (2019 est.)",
        "idioma_en": "French",
        "idioma_pt": "Francês",
        "capital_en": "Kinshasa",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/bc/BRA_orthographic.svg",
        "idh": 0.479
    },
    "congo": {
        "nome_pt": "Congo",
        "nome_en": "Congo",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/9/92/Flag_of_the_Republic_of_the_Congo.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "5.677.493 (2023 est.)",
        "area": " 342.000",
        "pib": "$8.718.000.000 (2017 est.)",
        "idioma_en": "French",
        "idioma_pt": "Francês",
        "capital_en": "Brazzaville",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Republic_of_the_Congo_%28orthographic_projection%29.svg",
        "idh": 0.571
    },
    "costa rica": {
        "nome_pt": "Costa Rica",
        "nome_en": "Costa Rica",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Flag_of_Costa_Rica_%28state%29.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "5.256.612 (2023 est.)",
        "area": " 51.100",
        "pib": "$61.855.000.000 (2019 est.)",
        "idioma_en": "Spanish and English",
        "idioma_pt": "Espanhol e Inglês",
        "capital_en": "San Jose",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/c/c4/Costa_Rica_%28orthographic_projection%29.svg",
        "idh": 0.809
    },
    "croatia": {
        "nome_pt": "Croácia",
        "nome_en": "Croatia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Flag_of_Croatia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "4.169.239 (2023 est.)",
        "area": " 56.594",
        "pib": "$60.687.000.000 (2019 est.)",
        "idioma_en": "Croatian",
        "idioma_pt": "Croata",
        "capital_en": "Zagreb",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/9/92/Europe-Croatia.svg",
        "idh": 0.858
    },
    "cuba": {
        "nome_pt": "Cuba",
        "nome_en": "Cuba",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/b/bd/Flag_of_Cuba.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "10.985.974 (2023 est.)",
        "area": " 110.860",
        "pib": "$93.79 billion undefined",
        "idioma_en": "Spanish",
        "idioma_pt": "Espanhol",
        "capital_en": "Havana",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/0/01/Cuba_%28orthographic_projection%29.svg",
        "idh": 0.764
    },
    "cyprus": {
        "nome_pt": "Chipre",
        "nome_en": "Cyprus",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Flag_of_Cyprus.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "1.308.120 (2023 est.)",
        "area": " 9.251 (of which 3.355 are in north Cyprus)",
        "pib": "$24.946.000.000 (2019 est.)",
        "idioma_en": "Greek and Turkish",
        "idioma_pt": "Grego e Turco",
        "capital_en": "Nicosia",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/6/6e/EU-Cyprus_highlighted.svg",
        "idh": 0.896
    },
    "czechia": {
        "nome_pt": "Tchéquia",
        "nome_en": "Czechia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/c/cb/Flag_of_the_Czech_Republic.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "10.706.242 (2023 est.)",
        "area": " 78.867",
        "pib": "$250.631.000.000 (2019 est.)",
        "idioma_en": "Czech",
        "idioma_pt": "Tcheco",
        "capital_en": "Prague",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/3/31/EU-Czech_Republic.svg",
        "idh": 0.889
    },
    "denmark": {
        "nome_pt": "Dinamarca",
        "nome_en": "Denmark",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/9/9c/Flag_of_Denmark.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "5.946.984 (2023 est.)",
        "area": " 43.094",
        "pib": "$350.037.000.000 (2019 est.)",
        "idioma_en": "Danish",
        "idioma_pt": "Dinamarquês",
        "capital_en": "Copenhagen",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Denmark_%28orthographic_projection%29.svg",
        "idh": 0.948
    },
    "djibouti": {
        "nome_pt": "Djibouti",
        "nome_en": "Djibouti",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/3/34/Flag_of_Djibouti.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "976.143 (2023 est.)",
        "area": " 23.200",
        "pib": "$3.323.000.000 (2019 est.)",
        "idioma_en": "French and Arabic",
        "idioma_pt": "Francês e Arábe",
        "capital_en": "Djibouti",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/b7/Djibouti_%28orthographic_projection%29.svg",
        "idh": 0.509
    },
    "dominica": {
        "nome_pt": "Dominica",
        "nome_en": "Dominica",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/c/c4/Flag_of_Dominica.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "74.656 (2023 est.)",
        "area": " 751",
        "pib": "$557.000.000 (2017 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Roseau",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/7/78/Dominica_on_the_globe_%28Americas_centered%29.svg",
        "idh": 0.72
    },
    "dominican republic": {
        "nome_pt": "República Dominicana",
        "nome_en": "Dominican Republic",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Flag_of_the_Dominican_Republic.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "10.790.744 (2023 est.)",
        "area": " 48.670",
        "pib": "$88.956.000.000 (2019 est.)",
        "idioma_en": "Spanish",
        "idioma_pt": "Espanhol",
        "capital_en": "Santo Domingo",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/9/95/Dominican_Republic_%28orthographic_projection%29.svg",
        "idh": 0.767
    },
    "ecuador": {
        "nome_pt": "Equador",
        "nome_en": "Ecuador",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/e/e8/Flag_of_Ecuador.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "17.483.326 (2023 est.)",
        "area": " 283.561",
        "pib": "$107.436.000.000 (2019 est.)",
        "idioma_en": "Spanish",
        "idioma_pt": "Espanhol",
        "capital_en": "Quito",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/c/c8/Ecuador_%28orthographic_projection%29.svg",
        "idh": 0.74
    },
    "egypt": {
        "nome_pt": "Egito",
        "nome_en": "Egypt",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Flag_of_Egypt.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "109.546.720 (2023 est.)",
        "area": " 1.001.450",
        "pib": "$323.763.000.000 (2019 est.)",
        "idioma_en": "Arabic",
        "idioma_pt": "Arábe",
        "capital_en": "Cairo",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Egypt_%28orthographic_projection%29.svg",
        "idh": 0.731
    },
    "el salvador": {
        "nome_pt": "El Salvador",
        "nome_en": "El Salvador",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/3/34/Flag_of_El_Salvador.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "6.602.370 (2023 est.)",
        "area": " 21.041",
        "pib": "$27.023.000.000 (2019 est.)",
        "idioma_en": "Spanish",
        "idioma_pt": "Espanhol",
        "capital_en": "San Salvador",
        "capital_pt": "Braslia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/e/e3/El_Salvador_%28orthographic_projection%29.svg",
        "idh": 0.675
    },
    "equatorial guinea": {
        "nome_pt": "Guiné Equatorial",
        "nome_en": "Equatorial Guinea",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/3/31/Flag_of_Equatorial_Guinea.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "1.737.695 (2023 est.)",
        "area": " 28.051",
        "pib": "$10.634.000.000 (2019 est.)",
        "idioma_en": "Spanish, Portuguese and French",
        "idioma_pt": "Espanhol, Português e Francês",
        "capital_en": "Malabo",
        "capital_pt": "Braslia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/b9/GNQ_orthographic.svg",
        "idh": 0.596
    },
    "eritrea": {
        "nome_pt": "Eritreia",
        "nome_en": "Eritrea",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/2/29/Flag_of_Eritrea.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "6.274.796 (2023 est.)",
        "area": " 117.600",
        "pib": "$5.813.000.000 (2017 est.)",
        "idioma_en": "Tigrinya, Arabic and English",
        "idioma_pt": "Tigrínia, Arábe e Inglês",
        "capital_en": "Asmara",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/4/43/Eritrea_%28Africa_orthographic_projection%29.svg",
        "idh": 0.492
    },
    "estonia": {
        "nome_pt": "Estônia",
        "nome_en": "Estonia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/8/8f/Flag_of_Estonia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "1.202.762 (2023 est.)",
        "area": " 45.228",
        "pib": "$31.461.000.000 (2019 est.)",
        "idioma_en": "Estonian",
        "idioma_pt": "Estoniano",
        "capital_en": "Tallinn",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/a/a2/EU-Estonia.svg",
        "idh": 0.89
    },
    "eswatini": {
        "nome_pt": "Eswatini",
        "nome_en": "Eswatini",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/1/1e/Flag_of_Eswatini.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "1.130.043 (2023 est.)",
        "area": " 17.364",
        "pib": "$4.484.000.000 (2019 est.)",
        "idioma_en": "English and siSwati",
        "idioma_pt": "Inglês e suázi",
        "capital_en": "Mbabane",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/6/63/LocationEswatini.svg",
        "idh": 0.597
    },
    "ethiopia": {
        "nome_pt": "Etiópia",
        "nome_en": "Ethiopia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/7/71/Flag_of_Ethiopia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "116.462.712 (2023 est.)",
        "area": " 1.104.300",
        "pib": "$92.154.000.000 (2019 est.)",
        "idioma_en": "Oromo, Amharic, Somali, Tigrigna and Afar",
        "idioma_pt": "Oromo, Amárico, Somali, Tigrínia e Afar",
        "capital_en": "Addis Ababa",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/d/dd/Ethiopia_%28Africa_orthographic_projection%29.svg",
        "idh": 0.498
    },
    "fiji": {
        "nome_pt": "Fiji",
        "nome_en": "Fiji",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/b/ba/Flag_of_Fiji.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "947.760 (2023 est.)",
        "area": " 18.274",
        "pib": "$4.891.000.000 (2017 est.)",
        "idioma_en": "English, iTaukei and Fiji Hindi",
        "idioma_pt": "Inglês, iTaukei e Híndi fijiano",
        "capital_en": "Suva (on Viti Levu)",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Fiji_%28orthographic_projection%29.svg",
        "idh": 0.73
    },
    "finland": {
        "nome_pt": "Finlândia",
        "nome_en": "Finland",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Flag_of_Finland.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "5.614.571 (2023 est.)",
        "area": " 338.145",
        "pib": "$269.259.000.000 (2019 est.)",
        "idioma_en": "Finnish and Swedish",
        "idioma_pt": "Finlandês e Sueco",
        "capital_en": "Helsinki",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Finland_%28orthographic_projection%29.svg",
        "idh": 0.94
    },
    "france": {
        "nome_pt": "França",
        "nome_en": "France",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Flag_of_France.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "68.521.974 (2023 est.)",
        "area": " 643.801",
        "pib": "$2.716.000.000 (2019 est.)",
        "idioma_en": "French",
        "idioma_pt": "Francês",
        "capital_en": "Paris",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/e/e1/France_%28orthographic_projection%29.svg",
        "idh": 0.903
    },
    "gabon": {
        "nome_pt": "Gabão",
        "nome_en": "Gabon",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/0/04/Flag_of_Gabon.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "2.397.368 (2023 est.)",
        "area": " 267.667",
        "pib": "$16.064.000.000 (2019 est.)",
        "idioma_en": "French",
        "idioma_pt": "Francês",
        "capital_en": "Libreville",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/bf/Gabon_%28orthographic_projection%29.svg",
        "idh": 0.706
    },
    "gambia": {
        "nome_pt": "Gâmbia",
        "nome_en": "Gambia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/7/77/Flag_of_The_Gambia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "2.468.569 (2023 est.)",
        "area": " 11.300",
        "pib": "$1.746.000.000 (2019 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Banjul",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/1/16/Gambia_%28orthographic_projection_with_inset%29.svg",
        "idh": 0.5
    },
    "georgia": {
        "nome_pt": "Geórgia",
        "nome_en": "Georgia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Flag_of_Georgia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "4.936.390 (2023 est.)",
        "area": " 69.700",
        "pib": "$17.694.000.000 (2019 est.)",
        "idioma_en": "Georgian and Abkhaz",
        "idioma_pt": "Georgiano e Abcázio",
        "capital_en": "Tbilisi",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Georgia_%28orthographic_projection%29.svg",
        "idh": 0.802
    },
    "germany": {
        "nome_pt": "Alemanha",
        "nome_en": "Germany",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/b/ba/Flag_of_Germany.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "84.220.184 (2023 est.)",
        "area": " 357.022",
        "pib": "$3.860.923.000.000 (2019 est.)",
        "idioma_en": "German",
        "idioma_pt": "Alemão",
        "capital_en": "Berlin",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/9/95/Germany_%28orthographic_projection%29.svg",
        "idh": 0.942
    },
    "ghana": {
        "nome_pt": "Gana",
        "nome_en": "Ghana",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/1/19/Flag_of_Ghana.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "33.846.114 (2023 est.)",
        "area": " 238.533",
        "pib": "$65.363.000.000 (2019 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Accra",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/3/30/Ghana_%28orthographic_projection%29.svg",
        "idh": 0.632
    },
    "greece": {
        "nome_pt": "Grécia",
        "nome_en": "Greece",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Flag_of_Greece.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "10.497.595 (2023 est.)",
        "area": " 131.957",
        "pib": "$209.790.000.000 (2019 est.)",
        "idioma_en": "Greek",
        "idioma_pt": "Grego",
        "capital_en": "Athens",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/f/f7/EU-Greece_%28orthographic_projection%29.svg",
        "idh": 0.887
    },
    "grenada": {
        "nome_pt": "Granada",
        "nome_en": "Grenada",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Flag_of_Grenada.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "114.299 (2023 est.)",
        "area": " 344",
        "pib": "$1.119.000.000 (2017 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Saint George's",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/bc/BRA_orthographic.svg",
        "idh": 0.795
    },
    "guatemala": {
        "nome_pt": "Guatemala",
        "nome_en": "Guatemala",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Flag_of_Guatemala.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "17.980.803 (2023 est.)",
        "area": " 108.889",
        "pib": "$76.678.000.000 (2019 est.)",
        "idioma_en": "Spanish and 21 Maya languages",
        "idioma_pt": "Espanhol e 21 línguas maias",
        "capital_en": "Guatemala City",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/7/70/Guatemala_%28orthographic_projection%29.svg",
        "idh": 0.627
    },
    "guinea-bissau": {
        "nome_pt": "Guiné-Bissau",
        "nome_en": "Guinea-Bissau",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/0/01/Flag_of_Guinea-Bissau.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "2.078.820 (2023 est.)",
        "area": " 36.125",
        "pib": "$1.339.000.000 (2019 est.)",
        "idioma_en": "Portuguese",
        "idioma_pt": "Português",
        "capital_en": "Bissau",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/bc/BRA_orthographic.svg",
        "idh": 0.483
    },
    "guinea": {
        "nome_pt": "Guiné",
        "nome_en": "Guinea",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/e/ed/Flag_of_Guinea.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "13.607.249 (2023 est.)",
        "area": " 245.857",
        "pib": "$13.550.000.000 (2019 est.)",
        "idioma_en": "French",
        "idioma_pt": "Francês",
        "capital_en": "Conakry",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/e/e4/Guinea_%28orthographic_projection%29.svg",
        "idh": 0.465
    },
    "guyana": {
        "nome_pt": "Guiana",
        "nome_en": "Guyana",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/9/99/Flag_of_Guyana.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "791.739 (2023 est.)",
        "area": " 214.969",
        "pib": "$3.561.000.000 (2017 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Georgetown",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/2/20/Guyana_%28orthographic_projection%29.svg",
        "idh": 0.714
    },
    "haiti": {
        "nome_pt": "Haiti",
        "nome_en": "Haiti",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/5/56/Flag_of_Haiti.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "11.470.261 (2023 est.)",
        "area": " 27.750",
        "pib": "$8.608.000.000 (2017 est.)",
        "idioma_en": "French and Creole",
        "idioma_pt": "Francês e Crioulo",
        "capital_en": "Port-au-Prince",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Haiti_%28orthographic_projection%29.svg",
        "idh": 0.535
    },
    "honduras": {
        "nome_pt": "Honduras",
        "nome_en": "Honduras",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/8/82/Flag_of_Honduras.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "9.571.352 (2023 est.)",
        "area": " 112.090",
        "pib": "$25.145.000.000 (2019 est.)",
        "idioma_en": "Spanish",
        "idioma_pt": "Espanhol",
        "capital_en": "Tegucigalpa",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Honduras_%28orthographic_projection%29.svg",
        "idh": 0.621
    },
    "hungary": {
        "nome_pt": "Hungria",
        "nome_en": "Hungary",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Flag_of_Hungary.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "9.670.009 (2023 est.)",
        "area": " 93.028",
        "pib": "$163.251.000.000 (2019 est.)",
        "idioma_en": "Hungarian",
        "idioma_pt": "Hungáro",
        "capital_en": "Budapest",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/6/60/EU-Hungary.svg",
        "idh": 0.846
    },
    "iceland": {
        "nome_pt": "Islândia",
        "nome_en": "Iceland",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/c/ce/Flag_of_Iceland.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "360.872 (2023 est.)",
        "area": " 103.000",
        "pib": "$24.614.000.000 (2019 est.)",
        "idioma_en": "Icelandic",
        "idioma_pt": "Islandês",
        "capital_en": "Reykjavik",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Iceland_%28orthographic_projection%29.svg",
        "idh": 0.959
    },
    "india": {
        "nome_pt": "Índia",
        "nome_en": "India",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/4/41/Flag_of_India.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "1.399.179.585 (2023 est.)",
        "area": " 3.287.263",
        "pib": "$2.836.000.000 (2019 est.)",
        "idioma_en": "English, Hindi, Bengali, Marathi, Telugu, Tamil, Gujarati, Urdu, Kannada, Odia, Malayalam, Punjabi, Assamese, Maithili and others official languages",
        "idioma_pt": "Inglês, Híndi, Bengali, Marata, Telugo, Tâmil, Guzerate, Urdu, Canarim, Oriá, Malaioalam, Panjabi, Assamês, Maithili e outras línguas oficias",
        "capital_en": "New Delhi",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/bb/India_%28orthographic_projection%29.svg",
        "idh": 0.633
    },
    "indonesia": {
        "nome_pt": "Indonésia",
        "nome_en": "Indonesia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Flag_of_Indonesia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "279.476.346 (2023 est.)",
        "area": " 1.904.569",
        "pib": "$1.119.720.000.000 (2019 est.)",
        "idioma_en": "Bahasa Indonesia",
        "idioma_pt": "Indonésio",
        "capital_en": "Jakarta",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/0/05/Indonesia_%28orthographic_projection%29.svg",
        "idh": 0.705
    },
    "iran": {
        "nome_pt": "Irã",
        "nome_en": "Iran",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/c/ca/Flag_of_Iran.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "87.590.873 (2023 est.)",
        "area": " 1.648.195",
        "pib": "$581.252.000.000 (2019 est.)",
        "idioma_en": "Persian Farsi",
        "idioma_pt": "Pérsio",
        "capital_en": "Tehran",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/a/a8/Iran_%28orthographic_projection%29.svg",
        "idh": 0.774
    },
    "iraq": {
        "nome_pt": "Iraque",
        "nome_en": "Iraq",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/f/f6/Flag_of_Iraq.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "41.266.109 (2023 est.)",
        "area": " 438.317",
        "pib": "$231.994.000.000 (2019 est.)",
        "idioma_en": "Arabic, Kurdish, Turkmen and Syriac",
        "idioma_pt": "Arábe, Curdo, Turcomeno e Siríaco",
        "capital_en": "Baghdad",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/5/59/Iraq_%28orthographic_projection%29.svg",
        "idh": 0.686
    },
    "ireland": {
        "nome_pt": "Irlanda",
        "nome_en": "Ireland",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/4/45/Flag_of_Ireland.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "5.323.991 (2023 est.)",
        "area": " 70.273",
        "pib": "$398.476.000.000 (2019 est.)",
        "idioma_en": "English and Irish",
        "idioma_pt": "Inglês e Irlandês",
        "capital_en": "Dublin",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/3/38/EU-Ireland_%28orthographic_projection%29.svg",
        "idh": 0.945
    },
    "italy": {
        "nome_pt": "Itália",
        "nome_en": "Italy",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/0/03/Flag_of_Italy.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "61.021.855 (2023 est.)",
        "area": " 301.340",
        "pib": "$2.002.763.000.000 (2019 est.)",
        "idioma_en": "Italian",
        "idioma_pt": "Italiano",
        "capital_en": "Rome",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Italy_%28orthographic_projection%29.svg",
        "idh": 0.895
    },
    "ivory coast": {
        "nome_pt": "Costa do Marfim",
        "nome_en": "Ivory Coast",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Flag_of_C%C3%B4te_d%27Ivoire.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "29.344.847 (2023 est.)",
        "area": " 322.463",
        "pib": "$42.498.000.000 (2018 est.)",
        "idioma_en": "French",
        "idioma_pt": "Francês",
        "capital_en": "Yamoussoukro (de jure), Abidjan (de facto)",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/bc/BRA_orthographic.svg",
        "idh": 0.55
    },
    "jamaica": {
        "nome_pt": "Jamaica",
        "nome_en": "Jamaica",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Flag_of_Jamaica.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "2.820.982 (2023 est.)",
        "area": " 10.991",
        "pib": "$15.847.000.000 (2019 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Kingston",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Jamaica_%28orthographic_projection%29.svg",
        "idh": 0.709
    },
    "japan": {
        "nome_pt": "Japão",
        "nome_en": "Japan",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Flag_of_Japan.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "123.719.238 (2023 est.)",
        "area": " 377.915",
        "pib": "$5.078.679.000.000 (2019 est.)",
        "idioma_en": "Japanese",
        "idioma_pt": "Japonês",
        "capital_en": "Tokyo",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/6/62/Japan_%28orthographic_projection%29.svg",
        "idh": 0.925
    },
    "jordan": {
        "nome_pt": "Jordânia",
        "nome_en": "Jordan",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/c/c0/Flag_of_Jordan.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "11.086.716 (2023 est.)",
        "area": " 89.342",
        "pib": "$44.568.000.000 (2019 est.)",
        "idioma_en": "Arabic",
        "idioma_pt": "Arábe",
        "capital_en": "Amman",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/b2/Jordan_%28orthographic_projection%29.svg",
        "idh": 0.72
    },
    "kazakhstan": {
        "nome_pt": "Cazaquistão",
        "nome_en": "Kazakhstan",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Flag_of_Kazakhstan.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "19.543.464 (2023 est.)",
        "area": " 2.724.900",
        "pib": "$181.194.000.000 (2019 est.)",
        "idioma_en": "Kazakh and Russian",
        "idioma_pt": "Cazaque e Russo",
        "capital_en": "Astana",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Kazakhstan_%28orthographic_projection%29.svg",
        "idh": 0.811
    },
    "kenya": {
        "nome_pt": "Quênia",
        "nome_en": "Kenya",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "57.052.004 (2023 est.)",
        "area": " 580.367",
        "pib": "$95.520.000.000 (2019 est.)",
        "idioma_en": "English and Kiswahili",
        "idioma_pt": "Inglês e Suaíli",
        "capital_en": "Nairobi",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Kenya_%28orthographic_projection%29.svg",
        "idh": 0.575
    },
    "kiribati": {
        "nome_pt": "Kiribati",
        "nome_en": "Kiribati",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Flag_of_Kiribati.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "115.372 (2023 est.)",
        "area": " 811",
        "pib": "$197.000.000 (2017 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Tarawa",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/d/d9/Kiribati_on_the_globe_%28Polynesia_centered%29.svg",
        "idh": 0.624
    },
    "kuwait": {
        "nome_pt": "Kuwait",
        "nome_en": "Kuwait",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/a/aa/Flag_of_Kuwait.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "3.103.580",
        "area": " 17.818",
        "pib": "$134.638.000.000 (2019 est.)",
        "idioma_en": "Arabic",
        "idioma_pt": "Arábe",
        "capital_en": "Kuwait City",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/4/41/KWT_orthographic.svg",
        "idh": 0.831
    },
    "kyrgyzstan": {
        "nome_pt": "Quirguistão",
        "nome_en": "Kyrgyzstan",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/c/c7/Flag_of_Kyrgyzstan.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "6.122.781 (2023 est.)",
        "area": " 199.951",
        "pib": "$8.442.000.000 (2019 est.)",
        "idioma_en": "Kyrgyz and Russian",
        "idioma_pt": "Quirguiz e Russo",
        "capital_en": "Bishkek",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/7/7c/Kyrgyzstan_%28orthographic_projection%29.svg",
        "idh": 0.692
    },
    "laos": {
        "nome_pt": "Laos",
        "nome_en": "Laos",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/5/56/Flag_of_Laos.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "7.852.377 (2023 est.)",
        "area": " 236.800",
        "pib": "$169.699.999.99..999.998 (2017 est.)",
        "idioma_en": "Lao",
        "idioma_pt": "Laonio",
        "capital_en": "Vientiane",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Laos_%28orthographic_projection%29.svg",
        "idh": 0.607
    },
    "latvia": {
        "nome_pt": "Letônia",
        "nome_en": "Latvia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/8/84/Flag_of_Latvia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "1.821.750 (2023 est.)",
        "area": " 64.589",
        "pib": "$340.840.000.00..000.004 (2019 est.)",
        "idioma_en": "Latvian",
        "idioma_pt": "Letão",
        "capital_en": "Riga",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/3/32/EU-Latvia.svg",
        "idh": 0.863
    },
    "lebanon": {
        "nome_pt": "Líbano",
        "nome_en": "Lebanon",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/5/59/Flag_of_Lebanon.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "5.331.203 (2023 est.)",
        "area": " 10.400",
        "pib": "$53.253.000.000 (2019 est.)",
        "idioma_en": "Arabic",
        "idioma_pt": "Arábe",
        "capital_en": "Beirut",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/9/96/Lebanon_%28orthographic_projection%29.svg",
        "idh": 0.706
    },
    "lesotho": {
        "nome_pt": "Lesoto",
        "nome_en": "Lesotho",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Flag_of_Lesotho.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "2.210.646 (2023 est.)",
        "area": " 30.355",
        "pib": "$2.462.000.000 (2019 est.)",
        "idioma_en": "Sesotho and English",
        "idioma_pt": "Sesoto e Inglês",
        "capital_en": "Maseru",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/f/f1/Lesotho_%28orthographic_projection%29.svg",
        "idh": 0.514
    },
    "liberia": {
        "nome_pt": "Libéria",
        "nome_en": "Liberia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Flag_of_Liberia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "5.506.280 (2023 est.)",
        "area": " 111.369",
        "pib": "$3.071.000.000 (2019 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Monrovia",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/9/91/Liberia_%28orthographic_projection%29.svg",
        "idh": 0.481
    },
    "libya": {
        "nome_pt": "Líbia",
        "nome_en": "Libya",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/0/05/Flag_of_Libya.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "7.252.573 (2023 est.)",
        "area": " 1.759.540",
        "pib": "$52.259.000.000 (2019 est.)",
        "idioma_en": "Arabic",
        "idioma_pt": "Arábe",
        "capital_en": "Tripoli",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Libya_%28Libya_centered%3B_orthographic_projection%29.svg",
        "idh": 0.718
    },
    "liechtenstein": {
        "nome_pt": "Liechtenstein",
        "nome_en": "Liechtenstein",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/4/47/Flag_of_Liechtenstein.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "39.993 (2023 est.)",
        "area": " 160",
        "pib": "$6.672.000.000 (2014 est.)",
        "idioma_en": "German",
        "idioma_pt": "Alemão",
        "capital_en": "Vaduz",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/bc/BRA_orthographic.svg",
        "idh": 0.935
    },
    "lithuania": {
        "nome_pt": "Lituânia",
        "nome_en": "Lithuania",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/1/11/Flag_of_Lithuania.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "2.655.755 (2023 est.)",
        "area": " 65.300",
        "pib": "$54.597.000.000 (2019 est.)",
        "idioma_en": "Lithuanian",
        "idioma_pt": "Lituano",
        "capital_en": "Vilnius",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/e/ec/EU-Lithuania.svg",
        "idh": 0.875
    },
    "luxembourg": {
        "nome_pt": "Luxemburgo",
        "nome_en": "Luxembourg",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/d/da/Flag_of_Luxembourg.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "660.924 (2023 est.)",
        "area": " 2.586",
        "pib": "$71.089.000.000 (2019 est.)",
        "idioma_en": "Luxembourgish, French and German",
        "idioma_pt": "Luxemburguês, Francês e Alemão",
        "capital_en": "Luxembourg",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/c/c3/EU-Luxembourg.svg",
        "idh": 0.93
    },
    "madagascar": {
        "nome_pt": "Madagascar",
        "nome_en": "Madagascar",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Flag_of_Madagascar.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "28.812.195 (2023 est.)",
        "area": " 587.041",
        "pib": "$13.964.000.000 (2019 est.)",
        "idioma_en": "Malagasy and French",
        "idioma_pt": "Malgaxe e Francês",
        "capital_en": "Antananarivo",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/9/99/Madagascar_%28orthographic_projection%29.svg",
        "idh": 0.501
    },
    "malawi": {
        "nome_pt": "Malawi",
        "nome_en": "Malawi",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/d/d1/Flag_of_Malawi.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "21.279.597 (2023 est.)",
        "area": " 118.484",
        "pib": "$7.766.000.000 (2019 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Lilongwe",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Malawi_%28orthographic_projection%29.svg",
        "idh": 0.512
    },
    "malaysia": {
        "nome_pt": "Malásia",
        "nome_en": "Malaysia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/6/66/Flag_of_Malaysia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "34.219.975 (2023 est.)",
        "area": " 329.847",
        "pib": "$364.631.000.000 (2019 est.)",
        "idioma_en": "Bahasa Malaysia",
        "idioma_pt": "Bahasa Malaiosia",
        "capital_en": "Kuala Lumpur",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/2/23/Malaysia_%28orthographic_projection%29.svg",
        "idh": 0.803
    },
    "maldives": {
        "nome_pt": "Maldivas",
        "nome_en": "Maldives",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Flag_of_Maldives.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "389.568 (2023 est.)",
        "area": " 298",
        "pib": "$4.505.000.000 (2017 est.)",
        "idioma_en": "Dhivehi",
        "idioma_pt": "diveí",
        "capital_en": "Male",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Maldives_%28orthographic_projection%29.svg",
        "idh": 0.747
    },
    "mali": {
        "nome_pt": "Mali",
        "nome_en": "Mali",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/9/92/Flag_of_Mali.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "21.359.722 (2023 est.)",
        "area": " 1.240.192",
        "pib": "$17.508.000.000 (2019 est.)",
        "idioma_en": "Bambara",
        "idioma_pt": "Bambara",
        "capital_en": "Bamako",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/8/8b/Mali_%28orthographic_projection%29.svg",
        "idh": 0.428
    },
    "malta": {
        "nome_pt": "Malta",
        "nome_en": "Malta",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/7/73/Flag_of_Malta.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "467.138 (2023 est.)",
        "area": " 316",
        "pib": "$14.986.000.000 (2019 est.)",
        "idioma_en": "Maltese and English",
        "idioma_pt": "Maltês e Inglês",
        "capital_en": "Valletta",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/6/63/EU-Malta.svg",
        "idh": 0.918
    },
    "marshall islands": {
        "nome_pt": "Ilhas Marshall",
        "nome_en": "Marshall Islands",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Flag_of_the_Marshall_Islands.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "80.966 (2023 est.)",
        "area": " 181",
        "pib": "$222.000.000 (2017 est.)",
        "idioma_en": "Marshallese",
        "idioma_pt": "Marshallesa",
        "capital_en": "Majuro",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/bc/BRA_orthographic.svg",
        "idh": 0.639
    },
    "mauritania": {
        "nome_pt": "Mauritânia",
        "nome_en": "Mauritania",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/4/43/Flag_of_Mauritania.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "4.244.878 (2023 est.)",
        "area": " 1.030.700",
        "pib": "$706.000.000 (2018 est.)",
        "idioma_en": "Arabic (Hassaniya), Pular, Soninke and Wolof",
        "idioma_pt": "Arábe (Hassaniya), Fula, Soninquês e Uolofe",
        "capital_en": "Nouakchott",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/a/ac/Mauritania_%28orthographic_projection%29.svg",
        "idh": 0.556
    },
    "mauritius": {
        "nome_pt": "Maurício",
        "nome_en": "Mauritius",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/7/77/Flag_of_Mauritius.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "1.309.448 (2023 est.)",
        "area": " 2.040",
        "pib": "$14.004.000.000 (2019 est.)",
        "idioma_en": "Creole and English",
        "idioma_pt": "Crioulo e Inglês",
        "capital_en": "Port Louis",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/e/ed/Mauritius_%28orthographic_projection%29.svg",
        "idh": 0.802
    },
    "mexico": {
        "nome_pt": "México",
        "nome_en": "Mexico",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/f/fc/Flag_of_Mexico.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "129.875.529 (2023 est.)",
        "area": " 1.964.375",
        "pib": "$1.269.956.000.000 (2019 est.)",
        "idioma_en": "Spanish",
        "idioma_pt": "Espanhol",
        "capital_en": "Mexico City",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/c/c9/Mexico_%28orthographic_projection%29.svg",
        "idh": 0.758
    },
    "micronesia": {
        "nome_pt": "Micronésia",
        "nome_en": "Micronesia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/e/e4/Flag_of_the_Federated_States_of_Micronesia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "100.319 (2023 est.)",
        "area": " 702",
        "pib": "$328.000.000 (2017 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Palikir",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/c/c6/Micronesia_on_the_globe_%28small_islands_magnified%29_%28Polynesia_centered%29.svg",
        "idh": 0.628
    },
    "moldova": {
        "nome_pt": "Moldávia",
        "nome_en": "Moldova",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/2/27/Flag_of_Moldova.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "3.250.532 (2023 est.)",
        "area": " 33.851",
        "pib": "$11.982.000.000 (2019 est.)",
        "idioma_en": "Romanian and Russian",
        "idioma_pt": "Romeno e Russo",
        "capital_en": "Chisinau",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Location_Moldova_Europe.png",
        "idh": 0.767
    },
    "monaco": {
        "nome_pt": "Mônaco",
        "nome_en": "Monaco",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Flag_of_Monaco.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "31.597 (2023 est.)",
        "area": " 2",
        "pib": "$6.006.000.000 (2015 est.)",
        "idioma_en": "French",
        "idioma_pt": "Francês",
        "capital_en": "Monaco",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/f/f5/Location_Monaco_Europe.png",
        "idh": null
    },
    "mongolia": {
        "nome_pt": "Mongólia",
        "nome_en": "Mongolia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Flag_of_Mongolia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "3.255.468 (2023 est.)",
        "area": " 1.564.116",
        "pib": "$11.140.000.000 (2017 est.)",
        "idioma_en": "Mongolian",
        "idioma_pt": "Mongól",
        "capital_en": "Ulaanbaatar",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Mongolia_%28orthographic_projection%29.svg",
        "idh": 0.739
    },
    "montenegro": {
        "nome_pt": "Montenegro",
        "nome_en": "Montenegro",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/6/64/Flag_of_Montenegro.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "602.445 (2023 est.)",
        "area": " 13.812",
        "pib": "$5.486.000.000 (2019 est.)",
        "idioma_en": "Montenegrin",
        "idioma_pt": "Montenegrino",
        "capital_en": "Podgorica",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/3/38/Montenegro_%28orthographic_projection%29.svg",
        "idh": 0.832
    },
    "morocco": {
        "nome_pt": "Marrocos",
        "nome_en": "Morocco",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/2/2c/Flag_of_Morocco.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "37.067.420 (2023 est.)",
        "area": " 716.550",
        "pib": "$118.858.000.000 (2019 est.)",
        "idioma_en": "Arabic",
        "idioma_pt": "Arábe",
        "capital_en": "Rabat",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/7/78/Morocco_%28orthographic_projection%2C_WS_claimed%29.svg",
        "idh": 0.683
    },
    "mozambique": {
        "nome_pt": "Moçambique",
        "nome_en": "Mozambique",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/d/d0/Flag_of_Mozambique.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "32.513.805 (2023 est.)",
        "area": " 799.380",
        "pib": "$14.964.000.000 (2019 est.)",
        "idioma_en": "Portuguese",
        "idioma_pt": "Português",
        "capital_en": "Maputo",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/8/84/Mozambique_%28orthographic_projection%29.svg",
        "idh": 0.446
    },
    "myanmar": {
        "nome_pt": "Myanmar",
        "nome_en": "Myanmar",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Flag_of_Myanmar.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "57.970.293 (2023 est.)",
        "area": " 676.578",
        "pib": "$76.606.000.000 (2019 est.)",
        "idioma_en": "Burmese",
        "idioma_pt": "Burmês",
        "capital_en": "Nay Pyi Taw",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/bc/BRA_orthographic.svg",
        "idh": 0.585
    },
    "namibia": {
        "nome_pt": "Namíbia",
        "nome_en": "Namibia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/0/00/Flag_of_Namibia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "2.777.232 (2023 est.)",
        "area": " 824.292",
        "pib": "$12.372.000.000 (2019 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Windhoek",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Namibia_%28orthographic_projection%29.svg",
        "idh": 0.615
    },
    "nauru": {
        "nome_pt": "Nauru",
        "nome_en": "Nauru",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/3/30/Flag_of_Nauru.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "9.852 (2023 est.)",
        "area": " 21",
        "pib": "$114.000.000 (2017 est.)",
        "idioma_en": "Nauruan and English",
        "idioma_pt": "nauruana e Inglês",
        "capital_en": "Yaren District (de facto)",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/bc/BRA_orthographic.svg",
        "idh": null
    },
    "nepal": {
        "nome_pt": "Nepal",
        "nome_en": "Nepal",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/9/9b/Flag_of_Nepal.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "30.899.443 (2023 est.)",
        "area": " 147.181",
        "pib": "$24.880.000.000 (2017 est.)",
        "idioma_en": "Nepali",
        "idioma_pt": "Nepalês",
        "capital_en": "Kathmandu",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Nepal_%28orthographic_projection%29.svg",
        "idh": 0.602
    },
    "netherlands": {
        "nome_pt": "Países Baixos",
        "nome_en": "Netherlands",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/2/20/Flag_of_the_Netherlands.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "17.463.930 (2023 est.)",
        "area": " 41.543",
        "pib": "$907.042.000.000 (2019 est.)",
        "idioma_en": "Dutch",
        "idioma_pt": "Neerlandês",
        "capital_en": "Amsterdam (de jure), Hague (de facto)",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/5/52/Netherlands_%28orthographic_projection%29.svg",
        "idh": 0.941
    },
    "new zealand": {
        "nome_pt": "Nova Zelândia",
        "nome_en": "New Zealand",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Flag_of_New_Zealand.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "5.109.702 (2023 est.)",
        "area": " 268.838",
        "pib": "$205.202.000.000 (2019 est.)",
        "idioma_en": "English and Maori",
        "idioma_pt": "Inglês e Maori",
        "capital_en": "Wellington",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/d/d8/New_Zealand_%28orthographic_projection%29.svg",
        "idh": 0.937
    },
    "nicaragua": {
        "nome_pt": "Nicarágua",
        "nome_en": "Nicaragua",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/1/19/Flag_of_Nicaragua.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "6.359.689 (2023 est.)",
        "area": " 130.370",
        "pib": "$12.570.000.000 (2019 est.)",
        "idioma_en": "Spanish",
        "idioma_pt": "Espanhol",
        "capital_en": "Managua",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/3/38/Nicaragua_%28orthographic_projection%29.svg",
        "idh": 0.667
    },
    "niger": {
        "nome_pt": "Níger",
        "nome_en": "Niger",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/f/f4/Flag_of_Niger.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "25.396.840 (2023 est.)",
        "area": " 1.267 million",
        "pib": "$12.926.000.000 (2019 est.)",
        "idioma_en": "French",
        "idioma_pt": "Francês",
        "capital_en": "Niamey",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/8/88/Niger_%28orthographic_projection%29.svg",
        "idh": 0.4
    },
    "nigeria": {
        "nome_pt": "Nigéria",
        "nome_en": "Nigeria",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/7/79/Flag_of_Nigeria.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "230.842.743 (2023 est.)",
        "area": " 923.768",
        "pib": "$475.062.000.000 (2019 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Abuja",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Nigeria_%28orthographic_projection%29.svg",
        "idh": 0.535
    },
    "north korea": {
        "nome_pt": "Coreia do Norte",
        "nome_en": "North Korea",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/5/51/Flag_of_North_Korea.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "26.072.217 (2023 est.)",
        "area": " 120.538",
        "pib": "$28.000.000.000 (2013 est.)",
        "idioma_en": "Korean",
        "idioma_pt": "Coreano",
        "capital_en": "Pyongyang",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/7/7b/North_Korea_%28orthographic_projection%29.svg",
        "idh": null
    },
    "north macedonia": {
        "nome_pt": "Macedônia do Norte",
        "nome_en": "North Macedonia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/f/f8/Flag_of_North_Macedonia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "2.133.410 (2023 est.)",
        "area": " 25.713",
        "pib": "$12.696.000.000 (2019 est.)",
        "idioma_en": "Macedonian and Albanian",
        "idioma_pt": "Macedônio e Albanês",
        "capital_en": "Skopje",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/0/0a/North_Macedonia_%28orthographic_projection%29.svg",
        "idh": 0.77
    },
    "norway": {
        "nome_pt": "Noruega",
        "nome_en": "Norway",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/d/d9/Flag_of_Norway.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "5.597.924 (2023 est.)",
        "area": " 323.802",
        "pib": "$405.695.000.000 (2019 est.)",
        "idioma_en": "Norwegian",
        "idioma_pt": "Norueguês",
        "capital_en": "Oslo",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/2/28/Norway_%28orthographic_projection%29.svg",
        "idh": 0.961
    },
    "oman": {
        "nome_pt": "Omã",
        "nome_en": "Oman",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/d/dd/Flag_of_Oman.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "3.833.465 (2023 est.)",
        "area": " 309.500",
        "pib": "$76.883.000.000 (2019 est.)",
        "idioma_en": "Arabic",
        "idioma_pt": "Arábe",
        "capital_en": "Muscat",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/bc/BRA_orthographic.svg",
        "idh": 0.816
    },
    "pakistan": {
        "nome_pt": "Paquistão",
        "nome_en": "Pakistan",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/3/32/Flag_of_Pakistan.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "247.653.551 (2023 est.)",
        "area": " 796.095",
        "pib": "$253.183.000.000 (2019 est.)",
        "idioma_en": "Punjabi, Pashto, Sindhi, Saraiki, Urdu, Balochi, Hindko, Brahui",
        "idioma_pt": "Panjabi, Pastó, Sindis, Seraiki, Urdu, Balúchi, Hindko, Brahui",
        "capital_en": "Islamabad",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/e/ea/PAK_orthographic.svg",
        "idh": 0.544
    },
    "palau": {
        "nome_pt": "Palau",
        "nome_en": "Palau",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/4/48/Flag_of_Palau.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "21.779 (2023 est.)",
        "area": " 459",
        "pib": "$292.000.000 (2017 est.)",
        "idioma_en": "Palauan and English",
        "idioma_pt": "Palauense e Inglês",
        "capital_en": "Ngerulmud",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/5/57/Palau_on_the_globe_%28Southeast_Asia_centered%29_%28small_islands_magnified%29.svg",
        "idh": 0.767
    },
    "palestine": {
        "nome_pt": "Palestina",
        "nome_en": "Palestine",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/0/00/Flag_of_Palestine.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "218.689.757",
        "area": "8.515.770",
        "pib": "3.128.000.000.000 undefined undefined",
        "idioma_en": "Arabic",
        "idioma_pt": "Arábe",
        "capital_en": "Brasília",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/a/ad/State_of_Palestine_%28orthographic_projection%29.svg",
        "idh": 0.715
    },
    "panama": {
        "nome_pt": "Panamá",
        "nome_en": "Panama",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/a/ab/Flag_of_Panama.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "4.404.108 (2023 est.)",
        "area": " 75.420",
        "pib": "$66.801.000.000 (2019 est.)",
        "idioma_en": "Spanish",
        "idioma_pt": "Espanhol",
        "capital_en": "Panama City",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/e/e1/Panama_%28orthographic_projection%29.svg",
        "idh": 0.805
    },
    "papua new guinea": {
        "nome_pt": "Papua-Nova Guiné",
        "nome_en": "Papua New Guinea",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Flag_of_Papua_New_Guinea.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "9.819.350 (2023 est.)",
        "area": " 462.840",
        "pib": "$19.820.000.000 (2017 est.)",
        "idioma_en": "Tok Pisin, English and Hiri Motu",
        "idioma_pt": "Tok Pisin, Inglês e Hiri Motu",
        "capital_en": "Port Moresby",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/7/79/Papua_New_Guinea_%28orthographic_projection%29.svg",
        "idh": 0.558
    },
    "paraguay": {
        "nome_pt": "Paraguai",
        "nome_en": "Paraguay",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/2/27/Flag_of_Paraguay.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "7.439.863 (2023 est.)",
        "area": " 406.752",
        "pib": "$38.940.000.000 (2017 est.)",
        "idioma_en": "Spanish and Guarani",
        "idioma_pt": "Espanhol e Guarani",
        "capital_en": "Asuncion",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/8/80/Paraguay_%28orthographic_projection%29.svg",
        "idh": 0.717
    },
    "peru": {
        "nome_pt": "Peru",
        "nome_en": "Peru",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/c/cf/Flag_of_Peru.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "32.440.172 (2023 est.)",
        "area": " 1.285.216",
        "pib": "$230.707.000.000 (2019 est.)",
        "idioma_en": "Spanish, Quechua and Aymara",
        "idioma_pt": "Espanhol, Quéchua e Aimará",
        "capital_en": "Lima",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/8/84/Peru_%28orthographic_projection%29.svg",
        "idh": 0.762
    },
    "philippines": {
        "nome_pt": "Filipinas",
        "nome_en": "Philippines",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/9/99/Flag_of_the_Philippines.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "116.434.200 (2023 est.)",
        "area": " 300.000",
        "pib": "$377.205.000.000 (2019 est.)",
        "idioma_en": "Tagalog and English",
        "idioma_pt": "Tagalo e Inglês",
        "capital_en": "Manila",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/5/50/Philippines_%28orthographic_projection%29.svg",
        "idh": 0.699
    },
    "poland": {
        "nome_pt": "Polônia",
        "nome_en": "Poland",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/1/12/Flag_of_Poland.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "37.991.766 (2023 est.)",
        "area": " 312.685",
        "pib": "$595.720.000.000 (2019 est.)",
        "idioma_en": "Polish",
        "idioma_pt": "Polonês",
        "capital_en": "Warsaw",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Poland_%28orthographic_projection%29.svg",
        "idh": 0.876
    },
    "portugal": {
        "nome_pt": "Portugal",
        "nome_en": "Portugal",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Flag_of_Portugal.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "10.223.150 (2023 est.)",
        "area": " 92.090",
        "pib": "$237.698.000.000 (2019 est.)",
        "idioma_en": "Portuguese and Mirandese",
        "idioma_pt": "Português e Mirandês",
        "capital_en": "Lisbon",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/8/8f/Portugal_%28orthographic_projection%29.svg",
        "idh": 0.866
    },
    "qatar": {
        "nome_pt": "Catar",
        "nome_en": "Qatar",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/6/65/Flag_of_Qatar.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "2.532.104 (2023 est.)",
        "area": " 11.586",
        "pib": "$191.290.000.000 (2018 est.)",
        "idioma_en": "Arabic",
        "idioma_pt": "Arábe",
        "capital_en": "Doha",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/d/d4/QAT_orthographic.svg",
        "idh": 0.855
    },
    "romania": {
        "nome_pt": "Romênia",
        "nome_en": "Romania",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/7/73/Flag_of_Romania.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "18.326.327 (2023 est.)",
        "area": " 238.391",
        "pib": "$249.543.000.000 (2019 est.)",
        "idioma_en": "Romanian",
        "idioma_pt": "Romeno",
        "capital_en": "Bucharest",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/8/87/Romania_%28orthographic_projection%29.svg",
        "idh": 0.821
    },
    "russia": {
        "nome_pt": "Rússia",
        "nome_en": "Russia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Flag_of_Russia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "141.698.923 (2023 est.)",
        "area": " 17.098.242",
        "pib": "$1.702.361.000.000 (2019 est.)",
        "idioma_en": "Russian",
        "idioma_pt": "Russo",
        "capital_en": "Moscow",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Russian_Federation_%28orthographic_projection%29_-_Crimea_disputed.svg",
        "idh": 0.829
    },
    "rwanda": {
        "nome_pt": "Ruanda",
        "nome_en": "Rwanda",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_Rwanda.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "13.400.541 (2023 est.)",
        "area": " 26.338",
        "pib": "$9.136.000.000 (2017 est.)",
        "idioma_en": "Kinyarwanda, French, English and Swahili",
        "idioma_pt": "Quiniaruanda, Francês, Inglês e Suaíli",
        "capital_en": "Kigali",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/6/60/Location_Rwanda_AU_Africa.svg",
        "idh": 0.534
    },
    "saint kitts and nevis": {
        "nome_pt": "São Cristóvão e Nevis",
        "nome_en": "Saint Kitts and Nevis",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Flag_of_Saint_Kitts_and_Nevis.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "54.817 (2023 est.)",
        "area": " 261 (Saint Kitts 168; Nevis 93)",
        "pib": "$964.000.000 (2017 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Basseterre",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/5/5d/KNA_orthographic.svg",
        "idh": 0.777
    },
    "saint lucia": {
        "nome_pt": "Santa Lúcia",
        "nome_en": "Saint Lucia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Flag_of_Saint_Lucia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "167.591 (2023 est.)",
        "area": " 616",
        "pib": "$1.686.000.000 (2017 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Castries",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/9/97/Saint_Lucia_on_the_globe_%28Americas_centered%29.svg",
        "idh": 0.715
    },
    "saint vincent and the grenadines": {
        "nome_pt": "São Vicente e Granadinas",
        "nome_en": "Saint Vincent and the Grenadines",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Flag_of_Saint_Vincent_and_the_Grenadines.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "100.804 (2023 est.)",
        "area": " 389 (Saint Vincent 344)",
        "pib": "$785.000.000 (2017 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Kingstown",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/7/70/VCT_orthographic.svg",
        "idh": 0.751
    },
    "samoa": {
        "nome_pt": "Samoa",
        "nome_en": "Samoa",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/3/31/Flag_of_Samoa.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "207.501 (2023 est.)",
        "area": " 2.831",
        "pib": "$841.000.000 (2017 est.)",
        "idioma_en": "Samoan and English",
        "idioma_pt": "Samoano e Inglês",
        "capital_en": "Apia",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/7/74/Samoa_on_the_globe_%28Polynesia_centered%29.svg",
        "idh": 0.707
    },
    "san marino": {
        "nome_pt": "San Marino",
        "nome_en": "San Marino",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Flag_of_San_Marino.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "34.892 (2023 est.)",
        "area": " 61",
        "pib": "$1.643.000.000 (2017 est.)",
        "idioma_en": "Italian",
        "idioma_pt": "Italiano",
        "capital_en": "San Marino (city)",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/7/79/Location_San_Marino_Europe.png",
        "idh": 0.853
    },
    "são tomé and príncipe": {
        "nome_pt": "São Tomé e Príncipe",
        "nome_en": "São Tomé and Príncipe",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/4/4f/Flag_of_Sao_Tome_and_Principe.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "220.372 (2023 est.)",
        "area": " 964",
        "pib": "$0 (2018 est.)",
        "idioma_en": "Portuguese",
        "idioma_pt": "Português",
        "capital_en": "Sao Tome",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Sao_Tome_and_Principe_in_its_region.svg",
        "idh": 0.618
    },
    "saudi arabia": {
        "nome_pt": "Arábia Saudita",
        "nome_en": "Saudi Arabia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/0/0d/Flag_of_Saudi_Arabia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "35.939.806 (2023 est.)",
        "area": " 2.149.690",
        "pib": "$792.849.000.000 (2019 est.)",
        "idioma_en": "Arabic",
        "idioma_pt": "Arábe",
        "capital_en": "Riyadh",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/4/47/Saudi_Arabia_%28orthographic_projection%29.svg",
        "idh": 0.875
    },
    "senegal": {
        "nome_pt": "Senegal",
        "nome_en": "Senegal",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/f/fd/Flag_of_Senegal.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "18.384.660 (2023 est.)",
        "area": " 196.722",
        "pib": "$23.576.000.000 (2019 est.)",
        "idioma_en": "French",
        "idioma_pt": "Francês",
        "capital_en": "Dakar",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Senegal_%28orthographic_projection%29.svg",
        "idh": 0.511
    },
    "serbia": {
        "nome_pt": "Sérvia",
        "nome_en": "Serbia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/f/ff/Flag_of_Serbia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "6.693.375 (2023 est.)",
        "area": " 77.474",
        "pib": "$51.449.000.000 (2019 est.)",
        "idioma_en": "Serbian",
        "idioma_pt": "Sérvio",
        "capital_en": "Belgrade",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/e/e8/Serbia_%28orthographic_projection%29.svg",
        "idh": 0.802
    },
    "seychelles": {
        "nome_pt": "Seicheles",
        "nome_en": "Seychelles",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/f/fc/Flag_of_Seychelles.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "97.617 (2023 est.)",
        "area": " 455",
        "pib": "$1.748.000.000 (2019 est.)",
        "idioma_en": "Seychellois Creole, English and French",
        "idioma_pt": "Seychellois Crioulo, Inglês e Francês",
        "capital_en": "Victoria",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/bd/Location_Seychelles_AU_Africa.svg",
        "idh": 0.785
    },
    "sierra leone": {
        "nome_pt": "Serra Leoa",
        "nome_en": "Sierra Leone",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_Sierra_Leone.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "8.908.040 (2023 est.)",
        "area": " 71.740",
        "pib": "$413.199.999.9.9.999.995 (2020 est.)",
        "idioma_en": "English, Mende, Temne and Krio",
        "idioma_pt": "Inglês, Mende, Timenés e Krio",
        "capital_en": "Freetown",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/3/38/Sierra_Leone_%28orthographic_projection%29.svg",
        "idh": 0.477
    },
    "singapore": {
        "nome_pt": "Singapura",
        "nome_en": "Singapore",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/4/48/Flag_of_Singapore.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "5.975.383 (2023 est.)",
        "area": " 719",
        "pib": "$372.088.000.000 (2019 est.)",
        "idioma_en": "English and Mandarin",
        "idioma_pt": "Inglês e Mandarim",
        "capital_en": "Singapore",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/bc/BRA_orthographic.svg",
        "idh": 0.939
    },
    "slovakia": {
        "nome_pt": "Eslováquia",
        "nome_en": "Slovakia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Flag_of_Slovakia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "5.425.319 (2023 est.)",
        "area": " 49.035",
        "pib": "$105.388.000.000 (2019 est.)",
        "idioma_en": "Slovak",
        "idioma_pt": "Eslovaco",
        "capital_en": "Bratislava",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/1/1d/EU-Slovakia.svg",
        "idh": 0.848
    },
    "slovenia": {
        "nome_pt": "Eslovênia",
        "nome_en": "Slovenia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/f/f0/Flag_of_Slovenia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "2.099.790 (2023 est.)",
        "area": " 20.273",
        "pib": "$54.160.000.000 (2019 est.)",
        "idioma_en": "Slovene",
        "idioma_pt": "Eslovênio",
        "capital_en": "Ljubljana",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/8/84/EU-Slovenia.svg",
        "idh": 0.918
    },
    "solomon islands": {
        "nome_pt": "Ilhas Salomão",
        "nome_en": "Solomon Islands",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/7/74/Flag_of_the_Solomon_Islands.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "714.766 (2023 est.)",
        "area": " 28.896",
        "pib": "$1.298.000.000 (2017 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Honiara",
        "capital_pt": "Bras­lia",
        "mapa": "https://en.wikipedia.org/wiki/File:Flag_of_the_Solomon_Islands.svg",
        "idh": 0.564
    },
    "somalia": {
        "nome_pt": "Somália",
        "nome_en": "Somalia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/a/a0/Flag_of_Somalia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "12.693.796 (2023 est.)",
        "area": " 637.657",
        "pib": "$7.052.000.000 (2017 est.)",
        "idioma_en": "Somali and Arabic",
        "idioma_pt": "Somali e Arábe",
        "capital_en": "Mogadishu",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Somalia_%28orthographic_projection%29.svg",
        "idh": null
    },
    "south africa": {
        "nome_pt": "África do Sul",
        "nome_en": "South Africa",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/a/af/Flag_of_South_Africa.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "58.048.332 (2023 est.)",
        "area": " 1.219.090",
        "pib": "$350.032.000.000 (2019 est.)",
        "idioma_en": "isiZulu, isiXhosa, Afrikaans, Sepedi, Setswana, English, Sesotho, Xitsonga, Tshivenda and isiNdebele",
        "idioma_pt": "Zulu, Xhosa, Africâner, Sepedi, Tswana, Inglês, Sesoto, Tsonga, Venda e Ndebele do norte",
        "capital_en": "Pretoria, Cape Town, Bloemfontein",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/6/6e/South_Africa_%28orthographic_projection%29.svg",
        "idh": 0.713
    },
    "south korea": {
        "nome_pt": "Coreia do Sul",
        "nome_en": "South Korea",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/0/09/Flag_of_South_Korea.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "51.966.948 (2023 est.)",
        "area": " 99.720",
        "pib": "$1.646.604.000.000 (2019 est.)",
        "idioma_en": "Korean",
        "idioma_pt": "Coreano",
        "capital_en": "Seoul",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/9/95/South_Korea_%28orthographic_projection%29.svg",
        "idh": 0.925
    },
    "south sudan": {
        "nome_pt": "Sudão do Sul",
        "nome_en": "South Sudan",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Flag_of_South_Sudan.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "12.118.379 (2023 est.)",
        "area": " 644.329",
        "pib": "$3.060.000.000 (2017 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Juba",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/6/65/South_Sudan_%28orthographic_projection%29.svg",
        "idh": 0.385
    },
    "spain": {
        "nome_pt": "Espanha",
        "nome_en": "Spain",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Flag_of_Spain.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "47.222.613 (2023 est.)",
        "area": " 505.370",
        "pib": "$1.393.351.000.000 (2019 est.)",
        "idioma_en": "Spanish",
        "idioma_pt": "Espanhol",
        "capital_en": "Madrid",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/8/81/Spain_%28orthographic_projection%29.svg",
        "idh": 0.905
    },
    "sri lanka": {
        "nome_pt": "Sri Lanka",
        "nome_en": "Sri Lanka",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/1/11/Flag_of_Sri_Lanka.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "23.326.272 (2023 est.)",
        "area": " 65.610",
        "pib": "$84.016.000.000 (2019 est.)",
        "idioma_en": "Sinhala and Tamil",
        "idioma_pt": "Cingalês e Tâmil",
        "capital_en": "Sri Jayewardenepura Kotte",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/9/96/Sri_Lanka_%28orthographic_projection%29.svg",
        "idh": 0.782
    },
    "sudan": {
        "nome_pt": "Sudão",
        "nome_en": "Sudan",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/0/01/Flag_of_Sudan.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "49.197.555 (2023 est.)",
        "area": " 1.861.484",
        "pib": "$24.918.000.000 (2019 est.)",
        "idioma_en": "Arabic and English",
        "idioma_pt": "Arábe e Inglês",
        "capital_en": "Khartoum",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/c/ca/Sudan_%28orthographic_projection%29.svg",
        "idh": 0.508
    },
    "suriname": {
        "nome_pt": "Suriname",
        "nome_en": "Suriname",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/6/60/Flag_of_Suriname.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "639.759 (2023 est.)",
        "area": " 163.820",
        "pib": "$3.419.000.000 (2017 est.)",
        "idioma_en": "Dutch",
        "idioma_pt": "Neerlandês",
        "capital_en": "Paramaribo",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/8/87/Suriname_%28orthographic_projection%29.svg",
        "idh": 0.73
    },
    "sweden": {
        "nome_pt": "Suécia",
        "nome_en": "Sweden",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Flag_of_Sweden.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "10.536.338 (2023 est.)",
        "area": " 450.295",
        "pib": "$531.350.000.000 (2019 est.)",
        "idioma_en": "Swedish",
        "idioma_pt": "Sueco",
        "capital_en": "Stockholm",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/3/30/Sweden_%28orthographic_projection%29.svg",
        "idh": 0.947
    },
    "switzerland": {
        "nome_pt": "Suíça",
        "nome_en": "Switzerland",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/0/08/Flag_of_Switzerland_%28Pantone%29.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "8.563.760 (2023 est.)",
        "area": " 41.277",
        "pib": "$731.502.000.000 (2019 est.)",
        "idioma_en": "German, French, Italian and Romansh",
        "idioma_pt": "Alemão, Francês, Italiano e Romanche",
        "capital_en": "Bern (de facto)",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/6/63/Switzerland_%28orthographic_projection%29.svg",
        "idh": 0.962
    },
    "syria": {
        "nome_pt": "Síria",
        "nome_en": "Syria",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/5/53/Flag_of_Syria.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "22.933.531 (2023 est.)",
        "area": " 187.437",
        "pib": "$24.600.000.000 (2014 est.)",
        "idioma_en": "Arabic",
        "idioma_pt": "Arábe",
        "capital_en": "Damascus",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/1/11/Syria_%28orthographic_projection%29.svg",
        "idh": 0.577
    },
    "tajikistan": {
        "nome_pt": "Tajiquistão",
        "nome_en": "Tajikistan",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/d/d0/Flag_of_Tajikistan.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "9.245.937 (2023 est.)",
        "area": " 144.100",
        "pib": "$2.522.000.000 (2019 est.)",
        "idioma_en": "Tajik",
        "idioma_pt": "Tajique",
        "capital_en": "Dushanbe",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/a/a1/Tajikistan_%28orthographic_projection%29.svg",
        "idh": 0.685
    },
    "tanzania": {
        "nome_pt": "Tanzânia",
        "nome_en": "Tanzania",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/3/38/Flag_of_Tanzania.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "65.642.682 (2023 est.)",
        "area": " 947.300",
        "pib": "$60.633.000.000 (2019 est.)",
        "idioma_en": "Swahili and English",
        "idioma_pt": "Suaíli e Inglês",
        "capital_en": "Dodoma",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Tanzania_%28orthographic_projection%29.svg",
        "idh": 0.549
    },
    "thailand": {
        "nome_pt": "Tailândia",
        "nome_en": "Thailand",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Flag_of_Thailand.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "69.794.997 (2023 est.)",
        "area": " 513.120",
        "pib": "$543.798.000.000 (2019 est.)",
        "idioma_en": "Thai",
        "idioma_pt": "Tailandês",
        "capital_en": "Bangkok",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Thailand_%28orthographic_projection%29.svg",
        "idh": 0.8
    },
    "timor-leste": {
        "nome_pt": "Timor-Leste",
        "nome_en": "Timor-Leste",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/2/26/Flag_of_East_Timor.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "1.476.042 (2023 est.)",
        "area": " 14.874",
        "pib": "$2.775.000.000 (2017 est.)",
        "idioma_en": "Portuguese",
        "idioma_pt": "Português",
        "capital_en": "Dili",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Timor_Leste_%28orthographic_projection%29.svg",
        "idh": 0.607
    },
    "togo": {
        "nome_pt": "Togo",
        "nome_en": "Togo",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/6/68/Flag_of_Togo.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "8.703.961 (2023 est.)",
        "area": " 56.785",
        "pib": "$5.232.000.000 (2018 est.)",
        "idioma_en": "French",
        "idioma_pt": "Francês",
        "capital_en": "Lome",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Location_Togo_AU_Africa.svg",
        "idh": 0.539
    },
    "tonga": {
        "nome_pt": "Tonga",
        "nome_en": "Tonga",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Flag_of_Tonga.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "105.221 (2023 est.)",
        "area": " 747",
        "pib": "$455.000.000 (2017 est.)",
        "idioma_en": "Tongan",
        "idioma_pt": "Tonganês",
        "capital_en": "Nuku'alofa",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/c/ce/Tonga_on_the_globe_%28Polynesia_centered%29.svg",
        "idh": 0.745
    },
    "trinidad and tobago": {
        "nome_pt": "Trinidad e Tobago",
        "nome_en": "Trinidad and Tobago",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/6/64/Flag_of_Trinidad_and_Tobago.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "1.407.460 (2023 est.)",
        "area": " 5.128",
        "pib": "$24.031.000.000 (2019 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Port of Spain",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/e/ed/Trinidad_and_Tobago_%28orthographic_projection%29.svg",
        "idh": 0.81
    },
    "tunisia": {
        "nome_pt": "Tunísia",
        "nome_en": "Tunisia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/c/ce/Flag_of_Tunisia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "11.976.182 (2023 est.)",
        "area": " 163.610",
        "pib": "$38.884.000.000 (2019 est.)",
        "idioma_en": "Arabic",
        "idioma_pt": "Arábe",
        "capital_en": "Tunis",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/d/da/Tunisia_%28orthographic_projection%29.svg",
        "idh": 0.731
    },
    "turkey": {
        "nome_pt": "Turquia",
        "nome_en": "Turkey",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/b/b4/Flag_of_Turkey.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "83.593.483 (2023 est.)",
        "area": " 783.562",
        "pib": "$760.028.000.000 (2019 est.)",
        "idioma_en": "Turkish",
        "idioma_pt": "Turco",
        "capital_en": "Ankara",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/d/dd/Turkey_%28orthographic_projection%29.svg",
        "idh": 0.838
    },
    "turkmenistan": {
        "nome_pt": "Turcomenistão",
        "nome_en": "Turkmenistan",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Flag_of_Turkmenistan.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "5.690.818 (2023 est.)",
        "area": " 488.100",
        "pib": "$40.819.000.000 (2018 est.)",
        "idioma_en": "Turkmen",
        "idioma_pt": "Turcomeno",
        "capital_en": "Ashgabat",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/d/d1/Turkmenistan_on_the_globe_%28Afro-Eurasia_centered%29.svg",
        "idh": 0.745
    },
    "tuvalu": {
        "nome_pt": "Tuvalu",
        "nome_en": "Tuvalu",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/3/38/Flag_of_Tuvalu.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "11.639 (2023 est.)",
        "area": " 26",
        "pib": "$40.000.000 (2017 est.)",
        "idioma_en": "Tuvaluan and English",
        "idioma_pt": "Tuvaluano e Inglês",
        "capital_en": "Funafuti",
        "capital_pt": "Brasília",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/b/bc/BRA_orthographic.svg",
        "idh": 0.641
    },
    "uganda": {
        "nome_pt": "Uganda",
        "nome_en": "Uganda",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Flag_of_Uganda.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "47.729.952 (2023 est.)",
        "area": " 241.038",
        "pib": "$34.683.000.000 (2019 est.)",
        "idioma_en": "English and Swahili",
        "idioma_pt": "Inglês e Suaíli",
        "capital_en": "Kampala",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Uganda_%28orthographic_projection%29.svg",
        "idh": 0.525
    },
    "ukraine": {
        "nome_pt": "Ucrânia",
        "nome_en": "Ukraine",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Ukraine.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "43.306.477 (2023 est.)",
        "area": " 603.550",
        "pib": "$155.082.000.000 (2019 est.)",
        "idioma_en": "Ukrainian",
        "idioma_pt": "Ucrâniano",
        "capital_en": "Kyiv",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Ukraine_-_disputed_%28orthographic_projection%29.svg",
        "idh": 0.773
    },
    "united arab emirates": {
        "nome_pt": "Emirados Árabes Unidos",
        "nome_en": "United Arab Emirates",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/c/cb/Flag_of_the_United_Arab_Emirates.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "9.973.449 (2023 est.)",
        "area": " 83.600",
        "pib": "$421.077.000.000 (2019 est.)",
        "idioma_en": "Arabic",
        "idioma_pt": "Arábe",
        "capital_en": "Abu Dhabi",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/c/cd/United_Arab_Emirates_%28orthographic_projection%29.svg",
        "idh": 0.911
    },
    "united kingdom": {
        "nome_pt": "Reino Unido",
        "nome_en": "United Kingdom",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Flag_of_the_United_Kingdom.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "68.138.484 (2023 est.)",
        "area": " 243.610",
        "pib": "$2.827.918.000.000 (2019 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "London",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/0/07/United_Kingdom_%28orthographic_projection%29.svg",
        "idh": 0.929
    },
    "united states": {
        "nome_pt": "Estados Unidos",
        "nome_en": "United States",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Flag_of_the_United_States.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "339.665.118 (2023 est.)",
        "area": " 9.833.517",
        "pib": "$21.433.228.000.000 (2019 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Washington, DC",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/7/70/United_States_%28orthographic_projection%29.svg",
        "idh": 0.921
    },
    "uruguay": {
        "nome_pt": "Uruguai",
        "nome_en": "Uruguay",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Flag_of_Uruguay.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "3.416.264 (2023 est.)",
        "area": " 176.215",
        "pib": "$56.108.000.000 (2019 est.)",
        "idioma_en": "Spanish",
        "idioma_pt": "Espanhol",
        "capital_en": "Montevideo",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/8/8d/Uruguay_%28orthographic_projection%29.svg",
        "idh": 0.809
    },
    "uzbekistan": {
        "nome_pt": "Uzbequistão",
        "nome_en": "Uzbekistan",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/8/84/Flag_of_Uzbekistan.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "31.360.836 (2023 est.)",
        "area": " 447.400",
        "pib": "$57.789.000.000 (2019 est.)",
        "idioma_en": "Uzbek",
        "idioma_pt": "Uzbeque",
        "capital_en": "Tashkent (Toshkent)",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/7/76/%D0%A3%D0%B7%D0%B1%D0%B5%D0%BA%D0%B8%D1%81%D1%82%D0%B0%D0%BD_%D0%BD%D0%B0_%D0%B3%D0%BB%D0%BE%D0%B1%D1%83%D1%81%D0%B5.svg",
        "idh": 0.727
    },
    "vanuatu": {
        "nome_pt": "Vanuatu",
        "nome_en": "Vanuatu",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Flag_of_Vanuatu_%28official%29.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "313.046 (2023 est.)",
        "area": " 12.189",
        "pib": "$870.000.000 (2017 est.)",
        "idioma_en": "Bislama, English and French",
        "idioma_pt": "Bislamá, Inglês e Francês",
        "capital_en": "Port-Vila",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/d/d9/Vanuatu_on_the_globe_%28Polynesia_centered%29.svg",
        "idh": 0.607
    },
    "venezuela": {
        "nome_pt": "Venezuela",
        "nome_en": "Venezuela",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/0/06/Flag_of_Venezuela.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "30.518.260 (2023 est.)",
        "area": " 912.050",
        "pib": "$210.100.000.000 (2017 est.)",
        "idioma_en": "Spanish",
        "idioma_pt": "Espanhol",
        "capital_en": "Caracas",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/5/5e/VEN_orthographic.svg",
        "idh": 0.691
    },
    "vietnam": {
        "nome_pt": "Vietn",
        "nome_en": "Vietnam",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/2/21/Flag_of_Vietnam.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "104.799.174 (2023 est.)",
        "area": " 331.210",
        "pib": "$259.957.000.000 (2019 est.)",
        "idioma_en": "Vietnamese",
        "idioma_pt": "Vietnamita",
        "capital_en": "Hanoi",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/2/28/Vietnam_%28orthographic_projection%29.svg",
        "idh": 0.703
    },
    "yemen": {
        "nome_pt": "Iêmen",
        "nome_en": "Yemen",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/8/89/Flag_of_Yemen.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "31.565.602 (2023 est.)",
        "area": " 527.968",
        "pib": "$54.356.000.000 (2018 est.)",
        "idioma_en": "Arabic",
        "idioma_pt": "Arábe",
        "capital_en": "Sanaa",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Yemen_on_the_globe_%28Yemen_centered%29.svg",
        "idh": 0.455
    },
    "zambia": {
        "nome_pt": "Zâmbia",
        "nome_en": "Zambia",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/0/06/Flag_of_Zambia.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "20.216.029 (2023 est.)",
        "area": " 752.618",
        "pib": "$25.710.000.000 (2017 est.)",
        "idioma_en": "English",
        "idioma_pt": "Inglês",
        "capital_en": "Lusaka",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/2/26/Zambia_%28orthographic_projection%29.svg",
        "idh": 0.565
    },
    "zimbabwe": {
        "nome_pt": "Zimbábue",
        "nome_en": "Zimbabwe",
        "bandeira": "https://upload.wikimedia.org/wikipedia/commons/6/6a/Flag_of_Zimbabwe.svg",
        "descricao_pt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "descricao_en": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quo, rerum sequi ut quibusdam neque assumenda, laborum autem deserunt nam perferendis quod reiciendis praesentium ipsam! Obcaecati dolore dolorum iure adipisci quasi.",
        "populacao": "15.418.674 (2023 est.)",
        "area": " 390.757",
        "pib": "$21.441.000.000 (2019 est.)",
        "idioma_en": "Shona, Ndebele and English",
        "idioma_pt": "Xona, Ndebele e Inglês",
        "capital_en": "Harare",
        "capital_pt": "Bras­lia",
        "mapa": "https://upload.wikimedia.org/wikipedia/commons/5/50/Zimbabwe_%28orthographic_projection%29.svg",
        "idh": 0.593
    }
};

for(c = 0; c < Object.keys(descricao).length; c++){
    try{
    dados[Object.keys(descricao)[c]].descricao_en = descricao[Object.keys(descricao)[c]].descricao_en;
    dados[Object.keys(descricao)[c]].descricao_pt = descricao[Object.keys(descricao)[c]].descricao_pt;
    }catch(error){
        console.log(Object.keys(descricao)[c])
    }
}

fs.writeFileSync("DadosDescritos.json", JSON.stringify(dados), "utf-8");

