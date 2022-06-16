/* Crie uma função chamada filtrarPorValorMinimo que recebe três parâmetros:

    um array de objetos (array)
    o nome do atributo que será usado como filtro (string)
    o valor mínimo que o atributo deve ter para passar no filtro (number)

    exemplo: filtrarPorValorMinimo([{nome:"diego", idade:22}, {nome:"luana", idade:44}], "idade", 44) -> [{nome: "luana", idade: 44}]
*/

function filtrarPorValorMinimo(array, attr, value) {
    return array.filter(item => {
      return item[attr] >= value;
    });
  }