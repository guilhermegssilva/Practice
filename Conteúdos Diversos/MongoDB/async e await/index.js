//Como fazíamos:
function minhaFuncao() {
    const promise = (...); // qualquer código q retorne promise (axios, query, etc)
    
    promise.then(result => {
    // código executado só quando a promise voltar com sucesso
    });
    
    // código executado imediatamente (não espera a promise voltar)
    }
    
//Como fazemos com async/await:
async function minhaFuncao() {
    const result = await (...); // qualquer código q retorne promise (axios, query, etc)
    // código executado só quando a promise voltar com sucesso
    }
    
//E pra tratar erros, em vez de usar o .catch na promise, passamos a usar o try/catch:
//Como fazíamos:    
function minhaFuncao() {
    const promise = (...); // qualquer código q retorne promise (axios, query, etc)
    
    promise.then(result => {
    // código executado só quando a promise voltar com sucesso
    });
    
    promise.catch(error => {
    // código executado só quando a promise voltar com error
    });
    
    // código executado imediatamente (não espera a promise voltar)
    }
    
//Como fazemos com async/await:
async function minhaFuncao() {
    try {
    const result = await (...); // qualquer código q retorne promise (axios, query, etc)
    // código executado só quando a promise voltar com sucesso
    } catch(error) {
    // código executado só quando a promise voltar com error
    }
    }
    
//Isso é interessante porque agora podemos encadear promises bem mais fácil:
app.get('/livros', async (req,res) => {
try {
await mongoClient.connect();
const dbLivros = mongoClient.db("biblioteca");
const livrosCollection = dbLivros.collection("livros");
const livros = await livrosCollection.find({}).toArray();

res.send(livros);
mongoClient.close();
} catch (error) {
res.status(500).send('A culpa foi do estagiário')
mongoClient.close()
}

});

//Agora essa função passa a retornar uma promise:
async function minhaFuncao() { ... }

//e aí você pode usar o then ou o await pra pegar o valor dela:
const valor = await minhaFuncao();

//ou
const promise = minhaFuncao();
promise.then(valor => {
});
