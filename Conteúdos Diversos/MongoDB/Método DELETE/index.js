/*- Quando a intenção da nossa requisição HTTP for deletar algum recurso, devemos utilizar o método `DELETE`.
- Para utilizar configurar uma rota que espera por esse método no express, precisamos fazer o seguinte:  */
app.delete('/users', (req, res) => {
    // ...
  });


/*
- Geralmente, a forma ideal para se deletar algum recurso, é o buscando por alguma **chave única**.
- Um exemplo de chave única é o `_id` que o MongoDB gera automaticamente na criação de um documento.
- Para receber esse id na rota de DELETE, a forma mais recomendada é envia-lo por PARAMS, da seguinte maneira:  */
app.delete('/users/:id', (req, res) => {
	const { id } = req.params;
	// ...
});
      
//Agora, para deletarmos um documento do MongoDB, precisamos utilizar a função deleteOne():
app.delete('/users/:id', (req, res) => {
	const { id } = req.params;
	
  try {
		await mongoClient.connect();
		const db = mongoClient.db("app")
		const usersColection = db.collection("users");
		await usersColection.deleteOne({ _id: new ObjectId(id) })
				
		res.sendStatus(200)
		mongoClient.close()
	 } catch (error) {
	  res.status(500).send(error)
		mongoClient.close()
	 }
});