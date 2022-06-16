/* Escreva o método caps que recebe um array de strings e retorna um outro array com todas as strings do array original em CAIXA ALTA. Use a função toUpperCase do tipo String.

    Exemplo: caps(['oi', 'tudo', 'bem?']) → ['OI', 'TUDO', 'BEM?']
*/

function caps(palavras) {
    return palavras.map(palavra => {
        return palavra.toUpperCase();
    });
}