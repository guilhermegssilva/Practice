function teste() {
    let texto = '';
    let alunos = ['Bia', 'Pedro', 'Carlos'];    //Uma variável lista vai estar entre colchetes
    console.log(alunos.sort())          //Organiza os elementos da variável em ordem crescente//
    console.log(alunos.length);         //Escreve na tela o número de elementos da variável alunos
    console.log(alunos[1]);             //Escreve na tela o elemento 1 da variável alunos (A variável começa do elemento 0)
    for (contador = 0; contador < alunos.length; contador = contador + 1){
        texto = texto + alunos[contador];       //A variável texto recebe ela mesma mais a variável alunos na posição do contador
    }
    return texto
}

function somarTodos(lista) {                         //Função que soma todos os elementos de uma lista
    let soma = 0
    for (let cont = 0; cont < lista.length; cont = cont+ 1){
        soma = soma + lista[cont];                   //A variável soma recebe ela mesma mais a variável lista na posição contador
    }
    return soma;
}

let numeros = [1, 2, 3, 4, 5]
for(let pos in numeros) {         //for loop que identa sobre cada elemento de uma array
  console.log(`A posição ${pos} tem o número ${numeros[pos]}.`)
}
let p = numeros.indexOf(3)        //Indica em que posição da array se encontra o elemento entre parênteses
console.log(`O número 3 está na posição ${p}.`)


//Ex 13: Implemente a função abaixo para que receba 3 nomes e retorne esses nomes em uma array
function listar(nome1, nome2, nome3) {
    return [nome1, nome2, nome3]
  }

//Ex 14: Implemente a função abaixo para que receba uma array e retorne a soma de todos os seus números multiplicados por 2
function dobraASoma(lista) {
    let soma = 0;
    for (let cont = 0; cont < lista.length; cont = cont + 1) {
      soma = soma + lista[cont]
      return soma * 2
    }
  }

/*Ex 15: Implemente a função abaixo para que receba uma array de números positivos diferentes entre si e retorne o índice do maior número encontrado.
Exemplo: se a array for [10,50,30], o maior número é o 50, então a função deve retornar o índice 1 */
function maiorIndice(lista) {
    let indice = 0;
    for (let cont = 0; cont < lista.length; cont = cont + 1) {
      if (lista[cont] > lista[indice]) {
        indice = cont;
      }
    }
    return indice
  }

/*Ex 16: Implemente a função abaixo para que retorne qual o dia da semana vai ser a partir de um dia passado como string e de uma quantidade de dias a ser avançado. 
Para isso, a função deve receber uma string e um número como parâmetros e retornar uma string */
function avancarDias(dia, quantidade) {
    let dias = ["Segunda-feira", "Terca-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado", "Domingo"];
    let indice = 0;
    for (let i = 0; i < dias.length; i++) {
      if (dias[i] === dia) {
        indice = i;
      }
    }
    indice = (indice + quantidade) % 7;
    return dias[indice];
  }

/*Ex 17: Implemente a função ao lado que recebe 3 números como parâmetros. Os dois primeiros delimitam um intervalo. A função deve retornar um array contendo os menores números pares 
dentro do intervalo. A quantidade de elementos nesse array deve ser igual ao 3o parâmetro passado */
function intervaloPares(inicio, fim, quantidade){
  let pares = [];
  let numero = inicio;
  while (pares.length < quantidade) {
    numero = numero + 1
    if (numero % 2 == 0) {
      pares.push(numero)
    }
  }
  return pares
}