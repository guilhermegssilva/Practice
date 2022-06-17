function somar(num1, num2) {      //O comando function é usado para se criar uma função, o conteúdo da função deverá estar entre chaves
  let soma = num1 + num2;         //O comando let é usado para designar que o que vier após ele é uma variável, uma variável deve ser declarada apenas uma vez
  return soma;                    //O comando return retorna o resultado da função para dentro de uma variável
}                                 //Deverá ser colocado ; ao final de cada linha para melhor entendimento
resultado = somar(6, 4);          //O resultado da função é atribuído para uma variável
console.log(resultado)            //O comando console.log escreve na tela o que estiver dentro dos parênteses


//Ex 01: Crie uma função com nome primeiraFuncao. A função deve estar vazia, sem nenhum parâmetro nem código 
primeiraFuncao(); {
}

//Ex 02: Complete a função abaixo de forma que ela sempre retorne o parâmetro recebido 
function retornaParametro(parametro) {
  return parametro;
}

//Ex 03: Altere a função abaixo para que ela passe a retornar a soma dos três parâmetros
function somaTodos(num1, num2, num3) {
  return num1 + num2 + num3;
}