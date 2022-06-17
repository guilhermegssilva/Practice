function apresentar(nome) {
  let texto = 'Olá' + nome;
  return texto;
}
apresentar('Pedro');


//Ex 04: Implemente a função abaixo para que retorne a string "Hello World" 
function helloWorld() {
  return "Hello World";
}

//Ex 05: Implemente a função abaixo para que retorne a concatenação dos dois parâmetros que ela recebe
function concatenar(texto1, texto2) {
  return texto1 + texto2;
}

//Ex 06: Implemente a função abaixo, que soma dois números e retorna o texto A soma deu: x, sendo x o resultado da soma 
function somar(num1, num2) {
  let soma = num1 + num2
  return 'A soma deu' + soma;
}