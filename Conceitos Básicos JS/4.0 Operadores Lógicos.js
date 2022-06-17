function aprovadoOuReprovado (nota1, nota2, nota3, faltas) {
    let media = (nota1 + nota2+ nota3) / 3;
    if (media >= 7 && faltas < 10) {            //O operador adiciona uma condição extra para ser cumprida
        return 'Aprovado';
 }  else {
        return 'Reprovado';
 }
}
aprovadoOuReprovado(5, 7, 10, 5)

function classificado (notaVestibular, notaEnem) {
    let aprovadoVestibular = notaVestibular > 8;       //A variável recebe o valor true ou false dependendo do que for estipulado 
    let aprovadoEnem = notaEnem > 700;                 //A variável recebe o valor true ou false dependendo do que for estipulado
    if (aprovadoEnem || aprovadoVestibular) {           //Se a variável for true a condição será executada
        return 'Classificado';                         //O operador || adiciona outra condição ao código, mas apenas uma delas deverá ser cumprida
}   else {
        return 'Desclassificado'
    }
    if (!aprovadoEnem || !aprovadoVestibular) {         //O operador ! em frente a uma variável condicional, fará ela ser executado caso ela seja falsa (if not alguma coisa)
        return('Que pena');                                         
 }
}                                


/*Ex 09: Implemente a função abaixo para que receba um preço e um booleano indicando se já está com desconto ou não. Se o preço for maior que 100 e não estiver com desconto, a função 
deve retornar Quero pechinchar. Caso contrário, deve retornar Negócio fechado */
function pecoDesconto(preco, estaComDesconto) {
    if (preco > 100 && !estaComDesconto) {
      return 'Quero pechinchar';
    }
    else {
      return 'Negócio fechado';
    }
}

//Ex 10:Implemente a função abaixo para que receba 3 números e retorne Tem negativo! caso pelo menos 1 deles seja menor que 0. Caso contrário, ela deve retornar Tudo positivo!
function tudoPositivo(num1, num2, num3) {
    if (num1 < 0 || num2 < 0 || num3 < 0) {
        return 'Tem negativo!';
 }  else {
        return 'Tudo positivo!';
  }
}
