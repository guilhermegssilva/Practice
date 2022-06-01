//querySelector devolve o primeiro elemento encontrado no html
const tituloPagina = document.querySelector('h2') //Retornará o primeiro <h2>
const texto = document.querySelector('.paragrafo') //Retornará a primeira classe .paragrafo
const teste1 = document.querySelector('.classe.classe') //Buscará o elemento que contenha as duas classes
const teste2 = document.querySelector('.class <tag>') // Buscará o elemento que tenha contenha a <tag> e esteja dentro da .classe


//Após um elemento ter sido selecionado, o classList pode adicionar ou remover classes dele
tituloPagina.classList.add('cor') //Adiciona a classe cor na variável tituloPagina(<h2>)
texto.classList.remove('frase') //Remove a classe frase da variável texto(.paragrafo)
texto.classList.toggle('frase') //Alterna a classe na variável texto, se tiver a classe ele a excluí, se não tiver ele a adiciona
texto.innerHTML = 'Mudando o texto' //Altera o texto presente na variável texto(classe paragrafo)


//Função onclick, ao clicar a cor da tag <h2> será trocada
function trocarCor() {
    const trocaCor = document.querySelector('h2')
    trocaCor.classList.toggle('cor')
} 

//O parâmetro dessa função será o elemento em que o this está
function trocarCor1(h2) {
    h2.classList.toggle('cor')
}

