/* Utilizando a função forEach, crie uma função clonar que recebe como parâmetro um objeto e cria uma cópia exata dela.

    utilize o método Object.getOwnPropertyNames para obter as propriedades do objeto.
*/

function clonaObjeto(alvo) {
    const propriedades = Object.getOwnPropertyNames(alvo);
    const copia = {};
    propriedades.forEach(function(propriedade) {
      copia[propriedade] = alvo[propriedade];
    });
  
    return copia;
  }