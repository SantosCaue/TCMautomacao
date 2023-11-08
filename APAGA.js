const fs = require('fs');
const path = require('path');

const pasta = 'c:/Users/karol/Desktop/CAUE ETEC/TÉCNICO/githubz'; // Substitua pelo caminho da sua pasta
const arquivosParaExcluir = [
    'Antigua and Barbuda.html',
    'Bosnia and Herzegovina.html',
    'Burkina Faso.html',
    'Cape Verde.html',
    'Central African Republic.html',
    'Democratic Republic of Congo.html',
    'Costa Rica.html',
    'Dominican Republic.html',
    'El Salvador.html',
    'Equatorial Guinea.html',
    'Ivory Coast.html',
    'Marshall Islands.html',
    'New Zealand.html',
    'North Korea.html',
    'North Macedonia.html',
    'Papua New Guinea.html',
    'Saint Kitts and Nevis.html',
    'Saint Lucia.html',
    'Saint Vincent and the Grenadines.html',
    'San Marino.html',
    'São Tomé and Príncipe.html',
    'Saudi Arabia.html',
    'Sierra Leone.html',
    'Solomon Islands.html',
    'South Africa.html',
    'South Korea.html',
    'South Sudan.html',
    'Sri Lanka.html',
    'Trinidad and Tobago.html',
    'United Arab Emirates.html',
    'United Kingdom.html',
    'United States.html'
  ]; // Substitua pelos nomes dos arquivos que deseja excluir

arquivosParaExcluir.forEach(arquivo => {
  const caminhoArquivo = path.join(pasta, arquivo);

  // Verifique se o arquivo existe antes de tentar excluí-lo
  if (fs.existsSync(caminhoArquivo)) {
    fs.unlink(caminhoArquivo, (err) => {
      if (err) {
        console.error(`Erro ao excluir ${arquivo}: ${err}`);
      } else {
        console.log(`${arquivo} foi excluído com sucesso.`);
      }
    });
  } else {
    console.error(`${arquivo} não foi encontrado na pasta.`);
  }
});
