import * as React from "https://cdn.skypack.dev/react@17.0.1";
import * as ReactDOM from "https://cdn.skypack.dev/react-dom@17.0.1";

const produtos = [
  { nome: "Bolo de aniversário", icone: "🎂", preco: 20.9 },
  { nome: "Balão", icone: "🎈", preco: 5.6 },
  { nome: "Confete", icone: "🎉", preco: 2.9 },
  { nome: "Suco de caixinha", icone: "🧃", preco: 1.9 },
  { nome: "Doces diversos", icone: "🍬", preco: 12.3 }
];

function App() {
  const [total, setTotal] = React.useState(0);
  return ( //Caixa total o valor inicia em 0
    <>
      <Caixa total={total} />
      <div>
        { produtos.map((produto) => {
          const { nome, icone, preco } = produto;
          return <Produto // O componente produto necessita comunicar ao componente App qual é o valor total de produtos
                   nome={nome} 
                   icone={icone} 
                   preco={preco} 
                   callback={(valorProduto) => setTotal(total + valorProduto)}//A função setTotal, que atualiza o preço atual da compra, recebe ela mesma mais o preço do produto clicado
                 />;
        })}
      </div>
    </>
  );
}

function Caixa(props) {
  const { total } = props;
  return (
    <div className="caixa">
      <b>Total da compra:</b> R$<span>{total.toFixed(2)}</span>
    </div>
  );
}

function Produto(props) {
  const [selecionado, setSelecionado] = React.useState(false); //O estado começa como false, porque nenhum produto foi selecionado ainda
  const { nome, icone, preco, callback } = props; //A função callback usana no componente App poderá ser usada nesse componente por meio do props
  const precoAjustado = preco.toFixed(2).toString().replace(".", ",");

  const classCSS = `produto ${selecionado ? "selecionado" : ""}`; //Caso o produto esteja selecionado, ele receberá a classe CSS 'selecionado' senão ele não recebe nada
  return (
    <div className={classCSS} onClick={() => { //Função onClick, ao clicar o estado é alternado
        const estado = !selecionado;
        setSelecionado(estado);
        if(estado) callback(preco)
        else callback(preco * -1); 
      }}>
      {icone} {nome} - R$ {precoAjustado}
    </div>
  );
}

ReactDOM.render(<App />, document.querySelector(".root"));

//////////////////////////////////////////////////////////////////////////////////////////////////

import React from 'react';

export default function Produto(props) { //O componente produto recebe 3 props do seu componente pai(qtd, aumentarQtd, diminuirQtd)
  return (
    <div>
      <h1>Prato delicioso</h1>
      <div>
        <button onClick={props.aumentarQtd}>+</button>
        <div>{props.qtd}</div>
        <button onClick={props.diminuirQtd}>-</button>
      </div>
    </div>
  )
}


import React from 'react';

export default function ListaDeProdutos() { //No componente pai é possível gerenciar esses props que estão no componente filho
	const [qtd, setQtd] = React.useState(0);

	function aumentarQtd() {
		setQtd(qtd+1);
	}

	function diminuirQtd() {
		setQtd(qtd-1);
	}

  return (
		<>
	    <Produto 
				qtd={qtd} 
				aumentarQtd={aumentarQtd} 
				diminuirQtd={diminuirQtd} 
			/>
			<div>Total de itens: {qtd}</div>
		</>
  );
}