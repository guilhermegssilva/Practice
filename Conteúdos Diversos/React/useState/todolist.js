import React from 'react';
import ReactDom from 'react-dom'

function App() {
    const [thingsArray, setThingsArray] = React.useState(["Thing1", "Thing 2"]) //O estado começa com esses dois items


    function addItem() { //Função usada para trocar o estado da página adicionando mais items
        setThingsArray(valorAnterior => {//A função setThingArray muda o estado inicial de thingsArray
            return [...valorAnterior, `Thing ${valorAnterior.length + 1}`] //Retorna o valor anterior (Thing 1, Thing 2) acrescentado de "Thing 3"
        })
    }
    //Após a função, thingsArray se torna ["Thing 1", "Thing 2", "Thing 3"]
    const thingsElements = thingsArray.map(thing => <p>{thing}</p>)//Mapeia o thingsArray, cada elemento se torna ele mesmo entre <p> (<p>Thing 1</p>)

    return ( //Retorna um botão com a função para adicionar items seguido de todos os items
        <div>
            <button onClick={addItem}>Add Item</button>
            {thingsElements}
        </div>
    )
    }

ReactDOM.render(<App />, document.getElementById("root"))