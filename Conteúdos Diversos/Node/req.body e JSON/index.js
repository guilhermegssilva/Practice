//Com a variável req.body podemos acessar os dados que serão enviados para o servidor

//o comando app.use permite que o express receba dados em JSON

import express from 'express';

const app = express(); // cria um servidor
app.use(express.json());

const pessoas = [];

app.post('/pessoas', (req, res) => {
const pessoa = req.body; // será o objeto { name: "Fulano" }
pessoas.push(pessoa);
res.send(pessoa);
});

app.get('/pessoas', (req, res) => {
res.send(pessoas);
});

app.listen(4000);
