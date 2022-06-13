import Topo from "./Topo" //Importa o arquivo de nome Topo para esse arquivo
import Menu from "./Menu" //Importa o arquivo de nome Menu  para esse arquivo

export default function App() {  //O arquivo App será exportado e poderá ser chamado em outro arquivo (index.js)
    return (
        <div>
			<Topo />
			<Menu />
		</div>
    );
}