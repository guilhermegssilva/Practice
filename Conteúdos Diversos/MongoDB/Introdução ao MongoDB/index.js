//O mongo serve para armazenar os dados em servidor para que eles não sejam perdidos assim que o usuário recarregar a página.

//Comando para armazenar um usuário no banco de dados
db.users.insert({ email: "[joao@email.com](mailto:joao@email.com)", password: "minha_super_senha" });

//Comando para listar todos os usuários armazenados
db.users.find({});

//Podemos também buscar com filtros! Por exemplo, se quisermos encontrar o usuário com email [joao@email.com](mailto:joao@email.com):
db.users.find({ email: "[joao@email.com](mailto:joao@email.com)" });

//Para estes casos que desejamos buscar somente um dado, podemos usar findOne:
db.users.findOne({ email: "[joao@email.com](mailto:joao@email.com)" });

//Quando inserimos um dado no mongo, estamos inserindo numa coleção. Neste caso, a coleção se chama users. Além disso, o dado inserido se chama documento. Se dermos insert numa coleção que não existe, o Mongo cria ela automaticamente

////////////////////////////////////////////////////

