//Sign-in, sessões e uuid
//Uma forma de gerarmos um token desse no back-end é utilizando uma lib que gera strings únicas aleatórias: a uuid.
//instalação
npm i uuid
//no arquivo
import { v4 as uuid } from 'uuid';

const token = uuid();

/*- Porém, não basta gerar um *token*: pra identificarmos futuramente se o usuário está mandando o token correto, precisamos armazená-lo. Em geral, o mais comum é termos uma coleção no banco para armazenar as sessões dos usuários.
- Uma sessão é uma janela de tempo em que o usuário está logado em um dispositivo. */

//sessions
{ 
	token: "um-token-aleatorio",
	userId: "id-do-usuario"
}

//Agora, no sign-in, basta criarmos uma sessão:
app.post("/sign-in", async (req, res) => {
    const { email, password } = req.body;
    
    const user = await db.collection('users').findOne({ email });

    if(user && bcrypt.compareSync(password, user.password)) {
        const token = uuid.v4();
        
				await db.collection("sessions").insertOne({
					userId: user._id,
					token
				})

        res.send(token);
    } else {
        // usuário não encontrado (email ou senha incorretos)
    }
});

//Futuramente, em próximos requests, podemos obter o token pelo header Authorization e buscar a session correspondente:
app.get("/posts", async (req,res) => {
  const { authorization } = req.header;
  const token = authorization?.replace('Bearer ', '');

  if(!token) return res.sendStatus(401);

  const session = await db.collections("sessions").findOne({ token });
            
  if (!session) {
      return res.sendStatus(401);
  }

	const user = await db.collections("users").findOne({ 
		_id: session.userId 
	})

  if(user) {
    // ...
  } else {
    res.sendStatus(401);
  }
});

//Ao devolver esse usuário para o front-end, devemos tomar o cuidado de não enviar dados sensíveis como senhas. Uma maneira fácil de retirar propriedades indesejadas de objetos é usando o operador delete.
app.get("/posts", async (req,res) => {
  const { authorization } = req.header;
  const token = authorization?.replace('Bearer ', '');

  if(!token) return res.sendStatus(401);

  const session = await db.collections("sessions").findOne({ token });
            
  if (!session) {
      return res.sendStatus(401);
  }

	const user = await db.collections("users").findOne({ 
		_id: session.userId 
	})

  if(user) {
		// deletando a propriedade password
		delete user.password;

		// _id, name, email
		res.send(user);
  } else {
    res.sendStatus(401);
  }
});