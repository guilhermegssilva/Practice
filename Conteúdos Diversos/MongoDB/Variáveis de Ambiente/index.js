/*
-Ao criar a instância de `MongoClient` precisamos dar o endereço do banco de dados. Em ambiente de desenvolvimento é comum que sempre seja `mongodb://localhost:27017`. Mas no ambiente de produção (famoso *deploy*) este endereço pode ser outro!
- Desta forma, sempre que formos fazer deploy precisaríamos modificar esta URL, modificando o código somente para colocá-lo no ar.
- Isto mostra que este valor não deveria ser fixo no código, porque senão teríamos um código para desenvolvimento e outro para produção. Vimos algum tempo atrás sobre a existência de variáveis de ambiente. Podemos iniciar o Node desta forma:
*/

//No arquivo JSON, na linha scripts, altere a forma de start do arquivo
nomeVariavel=valorVariável node src/app.js //iniciando uma aplicação com variáveis

//E no nosso código podemos acessar este valor pela variável
const value = process.env.nomeVariavel;


//Já poderíamos aproveitar disso para injetar a URL do banco de dados e criar o MongoClient.
MONGO_URL=mongodb://localhost:27017 node src/app.js

const mongoCilent = new MongoClient(process.env.MONGO_URL);

//Com a ferramenta dotenv podemos criar um arquivo .env na pasta raiz do projeto e colocar todas as variáveis de ambiente lá.

//arquivo .env
MONGO_URI=mongodb://localhost:27017

//arquivo node
import dotenv from "dotenv";
dotenv.config();

//Agora, ao executar o projeto a biblioteca abrirá o arquivo .env e carregará todas as variáveis de ambiente!