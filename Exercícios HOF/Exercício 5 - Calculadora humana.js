/* Crie uma função calcularAreaTotal que recebe um parâmetro:

    dimensoes: objeto que possui as propriedades altura e comprimento que são números inteiros

A função deve retornar a soma de todas as áreas.

Tome como base a entrada a seguir:

const dimensoes = [
  { altura: 10, comprimento: 20},
  { altura: 2, comprimento: 4},
  { altura: 1, comprimento: 1},
  { altura: 50, comprimento: 50}
]

Exemplo: calcularAreaTotal(dimensoes) → 2709
*/

function calcularAreaTotal(dimensoes) {
    let areaTotal = 0;
    dimensoes.forEach(dimensao => {
      areaTotal += dimensao.altura * dimensao.comprimento;
    });
  
    return areaTotal;
  }