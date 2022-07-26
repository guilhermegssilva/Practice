//Sign-up e bcrypt

//Como fazíamos o login de usuário até agora:
app.post("/sign-up", async (req, res) => {
    // nome, email, senha
const user = req.body;
await db.collection('users').insertOne(user);
res.sendStatus(201);
});


app.post("/sign-in", async (req, res) => {
    // email, senha
const login = req.body;
const user = await db.collection('users').findOne(login);
if(user) {
    // sucesso, usuário encontrado com este email e senha!
} else {
    // usuário não encontrado (email ou senha incorretos)
}
});


//instalação
npm i bcrypt

//importação
import bcrypt from 'bcrypt';

const senha = '123456';
const senhaCriptografada = bcrypt.hashSync(senha, 10);

bcrypt.compareSync('123456', senhaCriptografada); // vai dar true!
bcrypt.compareSync('outro valor', senhaCriptografada); // vai dar false! 


//Com isso, agora podemos implementar nosso sign-up e sign-in de forma segura:
app.post("/sign-up", async (req, res) => {
    // nome, email, senha
const user = req.body;
const passwordHash = bcrypt.hashSync(password, 10);
await db.collection('users').insertOne({ ...user, senha: passwordHash }) 
res.sendStatus(201);
});


app.post("/sign-in", async (req, res) => {
    const { email, senha } = req.body;
    const user = await db.collection('users').findOne({ email });
    if(user && bcrypt.compareSync(senha, user.senha)) {
        // sucesso, usuário encontrado com este email e senha!
    } else {
        // usuário não encontrado (email ou senha incorretos)
    }
});