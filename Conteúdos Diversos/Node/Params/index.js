//Para criar uma rota que aceita parâmetros, precisamos configurá-la da seguinte maneira.

app.get('/:name', (req, res) => {
const name = req.params.name
res.send('Hello ' + name);
});

//Nesse caso o parâmetro name será modificado de acordo com a url acessada, dessa forma a mensagem recebida será Hello + nome na url.