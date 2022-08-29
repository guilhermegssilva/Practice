//Quando a intenção da nossa requisição HTTP for substituir/atualizar algum recurso, devemos utilizar o método PUT.
app.put('/users', (req, res) => {
    // ...
});

/*
- Geralmente, a forma ideal para se atualizar algum recurso, é o buscando por alguma chave única.
- Um exemplo de chave única é o `_id` que o MongoDB gera automaticamente na criação de um documento
- Para receber esse id na rota de put, a forma mais recomendada é envia-lo por params, da seguinte maneira: */
app.put('/users/:id', (req, res) => {
	const { id } = req.params;
	// ...
});

//Para atualizar um documento, primeiro precisamos ter certeza que ele existe, por ex:
app.put('/users/:id', (req, res) => {
	const { id } = req.params;
	
  try {
		await mongoClient.connect();
		const db = mongoClient.db("app")
		const usersColection = db.collection("users");
		const user = await usersColection.findOne({ _id: new ObjectId(id) })
		if (!user) {
			res.sendStatus(404)
			mongoClient.close()
		}
				
		res.sendStatus(200)
		mongoClient.close()
	 } catch (error) {
	  res.status(500).send(error)
		mongoClient.close()
	 }
});

//Agora, para atualizarmos um documento do mongo, precisamos utilizar a função updateOne(). Essa função espera uma configuração como segundo parâmetro dizendo qual operação de atualização queremos fazer.
app.put('/users/:id', (req, res) => {
	const { id } = req.params;
	
  try {
		await mongoClient.connect();
		const db = mongoClient.db("app")
		const usersColection = db.collection("users");
		const user = await usersColection.findOne({ _id: new ObjectId(id) })
		if (!user) {
			res.sendStatus(404)
			mongoClient.close()
			return;
		}

		await usersColection.updateOne({ 
			_id: user._id 
		}, { $set: req.body })
				
		res.sendStatus(200)
		mongoClient.close()
	 } catch (error) {
	  res.status(500).send(error)
		mongoClient.close()
	 }
});