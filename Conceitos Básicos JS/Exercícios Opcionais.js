//Ex 18: Implemente a função abaixo para que receba como parâmetros uma string e uma letra e retorne a quantidade de ocorrências da letra passada na string passada
function contaLetras(string, letra) {
    let contador = 0;
    for(let cont = 0; cont < string.length; cont = cont + 1){
        if (string[cont] == letra){
            contador = contador + 1
        }
    }
    return contador
}

/*Ex 19: Implemente a função abaixo para que receba uma string como parâmetro e retorne a string original, mas com o número 1 no lugar das vogais
Exemplo: se for passada a palavra “uva”, a função deve retornar “1v1” */
function trocaVogais(string) {
    let novaString = "";
    for (let i = 0; i < string.length; i++) {
      let caractere = string[i];
      if (caractere === "a" || caractere === "e" || caractere === "i" || caractere === "o" || caractere === "u") {
        novaString += "1";
      } else {
        novaString += caractere;
      }
    }
  
    return novaString;
  }

/* Ex 20: Implemente a função ao lado que recebe como parâmetro uma string, misturando letras e números, e deve retornar uma string contendo
apenas as letras da string passada na mesma ordem. Exemplo: se for passada a string “ab2c4d”, a função deve retornar “abcd” */
function tiraNumeros(string) {
    let novaString = ''
    for (cont = 0; cont < string.length; cont = cont + 1){
        caractere = string[cont]
        if (caractere == 1 || caractere == 2 || caractere == 3 || caractere == 4 || caractere == 5 || caractere == 6 || caractere == 7 || caractere == 8 || caractere == 9 || caractere == 10){
            novaString = novaString
}       else {
            novaString = novaString + caractere
}   
    }
    return novaString
    }

/* Ex 21: Implemente a função abaixo para que receba 2 números como parâmetros e retorne um array contendo os números consecutivos ao 1o parâmetro
até o valor em que, ao somar todos os números no array, temos o valor passado no 2o parâmetro */
function somaAteMeta(inicio, meta) {
    let lista = [];
    let cont = inicio + 1;
    soma = 0;
    while (soma <= meta) {
        lista.push(cont);
        cont = cont + 1;
        soma = soma + cont;
}   return lista;
    }

// Ex 21: Implemente a função abaixo para que receba dois arrays como parâmetro e retorne true caso o 2o array seja uma subsequência do 1o array e false caso contrário
function subArray(array, subarray) {
	let indiceMenor = 0;

	for (let i = 0; i < array.length; i++) {
    if (array[i] === subarray[indiceMenor]) {
			indiceMenor++;

			if (indiceMenor === subarray.length) break;
		}
  }

	return indiceMenor === subarray.length;

//Ex 22: Implemente a função abaixo para que receba uma string como parâmetro e retorne um array contendo as letras repetidas na string passada
function letrasRepetidas(string) {
	let letras = [];
	let acumuladoQuantidade = [];
	
	for (let i = 0; i < string.length; i++) {
		let letra = string[i];
		let limite = i;
		let quantidade = 0;

		for (let j = 0; j < limite; j++) {
			if (string[j] === letra) quantidade++;
		}
		acumuladoQuantidade.push(quantidade);
	}

	for (let i = 0; i < acumuladoQuantidade.length; i++) {
		if (acumuladoQuantidade[i] === 1) letras.push(string[i]);
	}
}
	return letras;
}
