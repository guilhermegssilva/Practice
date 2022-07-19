/*A biblioteca express é uma das mais usadas para se criar um servidor usando o node, para instála-la é só executar o comando */
npm i express

//No arquivo js
import express from 'express';

const app = express(); // Cria um servidor

// Configura uma função pra ser executada quando bater um GET na rota "/"
app.get("/", (req, res) => {
// Manda como resposta o texto 'Hello World'
res.send('Hello World');
});

// Configura o servidor para rodar na porta 4000
app.listen(4000);
//Assim que o link designado for acessado o código de res.send será executado

/*É possível criar várias rotas adicionando múltiplos app.get(...), além disso é possível retornar objetos ou arrays ao invés de apenas frases.  */

import express from 'express';

const app = express();

app.get("/pessoa", (req, res) => {
const pessoa = {nome: "João", idade: 30};
res.send(pessoa);
})

app.get("/lista-pessoas", (req, res) => {
const pessoas = [{nome: "João", idade: 30},{nome: "Maria", idade: 20}];
res.send(pessoas);
})

app.listen(4000);

//Instalar pacote cors
npm i cors

import express from 'express';
import cors from 'cors';

const app = express();
app.use(cors());
