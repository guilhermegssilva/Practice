/*
Para executar um arquivo no node basta apenas abrir o terminal e digitar node nomeDoArquivo.js (Deve-se estar dentro da pasta que contém o arquivo antes de executar o comando)

É possível também exportar diferentes arquivos para um mesmos arquivo alvo como no React. */

//arquivo random.js
export default function randomNumber(min, max) {
return Math.floor(Math.random() * (max - min + 1) + min)
}
//arquivo alvo para a função
import randomNumber from './random.js';

/*O processo para importar bibliotecas no node é semelhante ao front-end mas com algumas ressalvas.
Primeiro é necessário iniciar o gerenciador de depêndencias do node:   */
//no console
npm init -y

//Depois as bibliotecas podem ser instaladas e importadas normalmente:
//no console
npm i axios

//no seu arquivo
import axios from 'axios';

//Para habilitar essas mudanças o arquivo package.json deve ser alterado da seguitne forma:
"type": "module"
