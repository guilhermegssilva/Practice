/* Utilizando o método map, escreva a função dobrar que recebe um array de números inteiros e retorna um array com todos os valores do array original dobrados.

    Exemplo: dobrar([1,2,3]) → [2,4,6]
*/

function dobrar(numeros) {
    return numeros.map(numero => {
        return numero * 2;
    });
}