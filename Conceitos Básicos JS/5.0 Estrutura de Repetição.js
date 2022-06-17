function umbridge() {                 //Função que escreve uma palavra 100 vezes
    let contador = 0;
    let frase = '';                  //A variável recebe uma string vazia 
    while (contador < 100) {         //Enquanto o contador for menor que 100 o loop irá se repetir
        frase = frase + 'Não devo contar mentiras';         //A variável recebe ela mesma mais a frase dada
        contador = contador + contador + 1       
    }
    return frase;
}


    function escrevePalavra(palavra) {          //Função que escreve uma palavra 100 vezes
    for (let contador = 0; contador <= 100; contador = contador + 1) {    //Um for loop, com um número de loops definido (início da variável, condição de parada, passos)
        console.log(palavra)
    }
}
escrevePalavra('Cat')


//Ex 11: 'Utilizando loops, implemente a função abaixo para que receba um texto e retorne uma string com o texto repetido 10 vezes
function vezes10(texto) {
    let frase = '';
    for(let contador = 0;  contador < 10;  contador = contador + 1) {
      frase = frase + texto;
    }
    return frase
  }

//Ex 12: Utilizando loops, implemente a função abaixo para que receba um texto e um número de repetições. Ela deve retornar uma string com o texto repetido n vezes, sendo n o número de repetições
function multiplica(texto, repeticoes) {
    let frase = '';
    for (let contador = 0; contador < repeticoes; contador = contador + 1) {
      frase = frase + texto;
    }
    return frase;
  }

