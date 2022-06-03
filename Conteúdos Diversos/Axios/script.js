<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script> //O link da biblioteca axios (Deverá ser colocado ao final do body, antes dos scripts do Js)
const promise = axios.get('http://meuservidor.com/lalala') //Comando que faz uma requisição para o servidor (Está sendo armazenado em uma variável)

promise.then(promessaCumprida) //A função entre () será executada quando o conteúdo for recebido

let pessoas = []

function promessaCumprida(resposta) { //O parâmetro resposta é criado automaticamente pelo .then
    pessoas = resposta.data //Pega o conteúdo da requisição feita
} 


const novasPessoas = [{nome:"João", idade:25}, {nome:"Pedro", idade:14}]; // Dados a serem postados no servidor
const requisicao = axios.post('http://meuservidor.com/lalala', pessoas); //O comando post recebe a url do servidor e a variável que será mandada para ele
requisicao.then(tudoCerto) // A função entre parênteses será executada quando o conteúdo for postado
requisicao.catch(seFalhar) //A função entre parênteses será executada caso a requisição falhe

function tudoCerto(resposta) //O parâmetro resposta é criado automaticamente pelo .then
pessoas.push(novasPessoas)

function seFalhar(erro) //O parâmetro resposta é criado automaticamente pelo .catch
    alert('Deu ruim')