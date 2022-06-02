const pessoa = {nome: "João", telefone: "1234-4567", endereco: "Rua 37"} //Concede uma variável para cada um dos elementos de uma array, tornando mais fácil a visualização


const pessoas = [{nome: "Mario", telefone: "1111-1111", endereço: "Rua 1"},
                 {nome: "Daniel", telefone: "2222-2222", endereço: "Rua 2"},
                 {nome: "Augusto", telefone: "3333-3333", endereço: "Rua 3"}]

pessoas[2].telefone // "3333-3333" (variável telefone do elemento na posição 2 da array pessoas)


const vovos = [{
	nome: "Vovo Juju",
	netos: [{nome: "Irmão do Jorel"}, {nome: "Jorel"}]
}]

vovos[0].netos[0].nome //"Irmão do Jorel" 


const baloes = [{numero: 2, cor: "vermelha"},
                {numero: 5, cor: "verde"}, 
                {numero: 3, cor: "azul"}]

const div = document.querySelector('div') //A variável div recebe os elementos contidos na tag <div>
for (let i=0; i < baloes.length; i++) {
    div.innerHTML += // A variável div recebe ela mesma mais a string a seguir
        `
        <p>Existem ${baloes[i].numero} balões de cor ${baloes[i].cor}</p>
        `  // Nessa string é possível colocar variáveis e as classes escritas dentro da tag <p>, também serão adicionadas no Html

}
