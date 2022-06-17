function aprovadoOuReprovado(nota1, nota2, nota3) {
  let media = (nota1 * 3 + nota2 * 3 + nota3 * 4) / 10;
  if (media > 7) {                           //As condições deverão ser colocadas entre parênteses
    return('Aprovado');                      //O conteúdo das condições deverá estar entre chaves
 } else if (media < 7) {
     return('Recuperação');
 } else {
     return('Reprovado');
 }
}
aprovadoOuReprovado(6, 5, 5)


//Ex 07: Implemente a função abaixo para que retorne Maior de idade caso a idade passada seja maior que 18 ou Menor de idade caso contrário.
function maiorDeIdade(idade) {
  if (idade >= 18) {
     return 'Maior de idade';
 } else {
     return 'Menor de idade';
  }
}

//Ex 08: Implemente a função abaixo para que receba 3 notas e retorna as strings sim ou não, indicando se a média simples entre as 3 notas (somar e dividir por 3) é maior ou igual a 7.
function aprovado(nota1, nota2, nota3) {
  let media = (nota1 + nota2 + nota3) / 3;
  if (media >= 7) {
     return 'sim';
} else {
     return 'não';
}
  }
