import express from 'express';

const app = express(); // cria um servidor
app.use(express.json());

const pessoas = [];

//Envia uma nova pessoa para o servidor
app.post('/pessoas', (req, res) => {
pessoas.push({ name: "Fulano" });
res.send(pessoas);
});

//Recebe a lista de pessoas do servidor
app.get('/pessoas', (req, res) => {
res.send(pessoas);
});

app.listen(4000);

