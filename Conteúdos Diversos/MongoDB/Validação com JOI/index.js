//Quando desejamos validar se algum campo foi preenchido ou não, não temos muito trabalho, basta algumas condições que tudo estará resolvido:
if (!req.body.name || !req.body.age || !req.body.email) {
	res.status(422).send("Todos os campos são obrigatórios");
}

//Porém, quando a tarefa é validar se não existem campos adicionais, ou, se o formato/tipo dos campos esta de acordo com o esperado (email, numero, etc), a coisa fica mais complexa. Para resolver esse tipo de problema Podemos utilizar a biblioteca joi.
import joi from 'joi'

const userSchema = joi.object({
    name: joi.string().required(),
	age: joi.number().required(),
    email: joi.string().email().required()
});

//A seguir é necessário validar o input do usuário
const user = { name: "Fulano", age: "20", email: "fulano@email.com" }

const validation = userSchema.validate(user);


//Podemos pedir para a validação parar no primeiro erro encontrado configurando o método da seguinte maneira
const user = { name: "Fulano", age: "20", email: "fulano@email.com" }

const validation = userSchema.validate(user, { abortEarly: true });



//E para mostrar os erros para o usuário, basta fazer o seguinte:
const user = { name: "Fulano", age: "20", email: "fulano@email.com" }

const validation = userSchema.validate(user, { abortEarly: false });

if (validation.error) {
  console.log(validation.error.details)
}