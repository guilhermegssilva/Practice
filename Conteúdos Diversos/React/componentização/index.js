import ReactDOM from 'react-dom'; //importar a biblioteca DOM para o React

function Lista() { //Retorna um elemento HTML diretamente, sem o uso de strings
    return (
        <ul>
            <li>Topico 1</li>
            <li>Topico 2</li>
            <li>Topico 3</li>
        </ul>
    );
}

const lista = Lista();
const elemento = document.querySelector(".classeDiv");
ReactDOM.render(lista, elemento); //O primeiro parâmetro é o elemento HTML a ser renderizado, e o segundo é o local no HTML em que ele será renderizado


//////////////////////////////////////////////

//Cada componente do HTML está separado dentro de sua própria função que irá retornar o código HTML

function App() {
    return (
        <div>
			<Topo />
			<Menu />
		</div>
    );
}

function Topo() {
    return (
    	<div>
      	<h1>Meu título</h1>
      </div>
    );
}

function Menu() {
    return (
	 <ul>
	 	<li><a href="...">Home</a></li>
	 	<li><a href="...">Sobre nós</a></li>
	 	<li><a href="...">Contato</a></li>
	 </ul>
    );
}

//A função App que contém os conteúdos do Topo e do Menu será renderizada na div que possui a classe .root
ReactDOM.render(<App />, document.querySelector(".root"));

////////////////////////////////////////////

import ReactDom from "react-dom";
import App from "./App"; //Importa o arquivo App para esse arquivo

ReactDOM.render(<App />, document.querySelector(".root"));

//Todos os arquivos estão em pastas separadas tornando a organização mais simples

//Os arquivos Menu e Topo estão sendos importados para a pasta App e esta por sua vez está sendo importada para cá para ser renderizada no HTML