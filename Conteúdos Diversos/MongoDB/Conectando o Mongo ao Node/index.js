//Conectando o MongoDB ao Node
//Para fazer isso, precisamos instalar o pacote mongodb como dependência do nosso projeto:
npm i mongodb

//Então precisamos importar o MongoClient no nosso código:
import { MongoClient } from "mongodb";

//Agora nosso sistema precisa se conectar ao banco do Mongo:
const mongoClient = new MongoClient("mongodb://localhost:27017");
let db;

mongoClient.connect().then(() => {
	db = mongoClient.db("meu_lindo_projeto");
});

//Agora podemos fazer operações de inserção no banco!
db.collection("users").insertOne({
	email: "joao@email.com",
	password: "minha_super_senha"
});

//Podemos também fazer buscas:
db.collection("users").findOne({
	email: "joao@email.com"
}).then(user => {
	console.log(user); // imprimirá um objeto { "_id": ..., "email": ..., "password": ... } 
});

//Listar todos os documentos da coleção:
db.collection("users").find().toArray().then(users => {
	console.log(users); // array de usuários
});

///////////////////////////////////////////////////////////////////////////////////

//E finalmente podemos juntar isso no Express! Podemos fazer uma API:
import express from "express";
import { MongoClient } from "mongodb";

const app = express();
app.use(express.json());

// conectando ao banco
let db;
const mongoClient = new MongoClient("mongodb://localhost:27017");

mongoClient.connect().then(() => {
	db = mongoClient.db("meu_lindo_projeto");
});

app.get("/recipes", (req, res) => {
	// buscando receitas
	db.collection("recipes").find().toArray().then(recipes => {
		res.send(recipes);
	});
});

app.post("/recipes", (req, res) => {
	// inserindo receita
	db.collection("recipes").insertOne(req.body).then(() => {
		res.sendStatus(201);
	});
});

app.listen(5000);