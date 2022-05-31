 /* Podemos usar a função .forEach() para iterar sobre cada item de um array, ou seja, passar por cada item de um array. Esta função não tem retorno. */

const nomes = ["joel", "manuel", "baruel"];
function cumprimentarPessoa(pessoa) {
	console.log(`Olá, ${pessoa}! Tudo bem?`);
}

nomes.forEach(cumprimentarPessoa);
// Olá, Joel! Tudo bem?
// Olá, Manuel! Tudo bem?
// Olá, Baruel! Tudo bem?




/* Podemos usar a função .map() para "mapear" um array retornando um novo array. O .map() irá passar para a função recebida como parâmetro, o item e o índice, e para cada vez que passar por um elemento irá retornar um valor, criando um novo array. Não é possível filtrar os elementos do array com a função .map(), ou seja, sempre iremos receber um novo array com a mesma quantidade de elementos.*/

const numeros = [1, 2, 3, 4, 5];
function dobrar (num) {
	return num * 2;
}
const numerosDobrados = numeros.map(dobrar); //[2, 4, 6, 8, 10]



/* Se quisermos filtrar os elementos de um array podemos usar a função .filter(). O .filter() irá passar por cada elemento executando a função recebida como parâmetro, caso essa função retorne true aquele elemento será retornado, caso contrário não irá retornar nada.
Obs: Não é possível modificar os elementos do array com a função .filter(), ela apenas separa quais elementos serão retornados dos elementos não retornados. */

const num = [1, 2, 3, 4, 5];
function ePar (numero) {
	if (num % 2 === 0) {
		return true;
	}
}

const pares = num.filter(ePar); //[2, 4]