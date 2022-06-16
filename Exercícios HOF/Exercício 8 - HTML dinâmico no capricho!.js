/* Crie uma função chamada converterParaHTML que recebe como parâmetro um array objetos e retorna um array com as informações destes objetos convertidas.

Exemplo:

const elementos = [
  {tag: "img", atributos: [{chave: "alt", valor:"imagem!"}, {chave: "src", valor: "imagem.png"}], conteudo:""},
  {tag: "p", atributos: [{chave: "class", valor:"texto"}], conteudo: "sou um parágrafo!"},
  {tag: "h1", atributos:[], conteudo: "sou um título"}
];

const HTML = converterParaHTML(elementos);
console.log(HTML);
// resultado
[
  "<img src="imagem.png" alt="imagem!" />",
  "<p class="texto">sou um parágrafo!</p>",
  "<h1>sou um título</h1>"
]
*/

function converterParaHTML(elementos) {
    return elementos.map(elemento => {
      const tag = elemento.tag;
      const attrs = elemento.atributos;
      const conteudo = elemento.conteudo;
  
      let elementoHTML = `<${tag}`;
      let attrsHTML = "";
      attrs.forEach(attr => {
        attrsHTML+=` ${attr.chave}="${attr.valor}"`;
      });
      elementoHTML += attrsHTML;
  
      if(conteudo) {
        elementoHTML += '>';
        elementoHTML += `${conteudo}</${tag}>`;
      } else {
        elementoHTML += ' />';
      }
  
      return elementoHTML;
    })
  }