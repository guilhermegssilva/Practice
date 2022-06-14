import { BrowserRouter, Routes, Route } from "react-router-dom"; //Elementos a serem importados da biblioteca

import PaginaPrincipal from "./PaginaPrincipal";
import Contato from "./Contato";

function App() {
	return (
		<BrowserRouter> {/*A tag BrowserRouter vai englobar todos os elementos do App()*/}
            <MenuPincipal/>{/*O elemento MenuPrincipal ficará estático na página pois não está dentro de nenhuma Routes*/}
                <Routes> {/*O que estiver dentro da tag Routes irá receber um caminho único */}
                    <Route path="/" element={<PaginaPrincipal />} /> {/*O link '/' recebe o elemento presente em PaginaPrincipal*/}
                    <Route path="/contato" element={<Contato />} /> {/*O link '/contato' recebe o elemento presente em Contato*/}
                </Routes>
		</BrowserRouter>
	);
}

/* - No código acima, estamos dizendo para o React:
    - Quando a rota acessada for `/`, exiba aqui o componente `PaginaPrincipal`
    - Quando a rota acessada for `/contato`, exiba aqui o componente `Contato`
*/

///////////////////////////////////////////////////////////////////////////////////////////////


// E agora, se desejamos mudar de rota, podemos utilizar o componente Link do React Router DOM
import { Link } from "react-router-dom";

function PaginaPrincipal() {
	return (
		<>
			<h1>Página principal</h1>
			<Link to="/contato">Contato</Link> {/* Funciona como uma âncora, ao clicar o usuário será direcionado ao caminho especificado*/}
		</>
	);
}