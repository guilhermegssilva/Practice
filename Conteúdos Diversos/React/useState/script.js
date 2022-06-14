import React from 'react';

function App(){
	const [title, setTitle] = useState('Hello World 3'); //A mensagem inicial será 'Hello World 3'
	const [showContent, setShowContent] = useState(false); //O estado inicial da função será falso


	function handleTitle() { //A mensagem que antes era 'Hello World 3' agora será 'Estado modificado'
	setTitle('Estado modificado');
	}   

	function handleContent() {  //Ao clicar o valor booleano será invertido
		setShowContent(!showContent);
	}

	return ( //Ao serem clicadas as funções onClick terão seus estados mudados de acordo com o estado determinado
		<div>
			<h1>{title}</h1> 
			{showContent && <ExclusiveContent/>}
			<button onClick={handleTitle}>Alterar o título</button> 
			<button onClick={handleContent}>{showContent ? 'Clique para esconder o conteúdo' : 'Clique para exibir o conteúdo'}</button>
		</div>
	);
}

	function ExclusiveContent() {
		return <h2>Mensagem nova</h2>
	}

export default App();

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

import * as React from "https://cdn.skypack.dev/react@17.0.1";
import * as ReactDOM from "https://cdn.skypack.dev/react-dom@17.0.1";

function App() {
  const [contagem, setContagem] = React.useState(0); // A contagem comeca em zero

  function aumentar() {
    setContagem(contagem); // Ao passar um novo valor para esta função, o react irá atualizar/renderizar novamente o componente
  }

  return ( //A variável contagem receberá o valor atualizado de likes
    <div className="container">
      <img
        src="https://yt3.ggpht.com/oZCGpPQc5qat2YIzVs_h1LTvrtpV6G--Q2CopkOoAa7d1WvHDohPzWO-vSEnQ4GljcQOO_6QkQ=s900-c-k-c0x00ffffff-no-rj"
        alt="driven"
      />
      <div className="contador-likes"> 
        <span className="likes">{contagem}</span> 
        <span> likes</span>
      </div>
      <button onClick={() => setContagem(contagem + 1)}>👍 like</button>
    </div>
  );
}

ReactDOM.render(<App />, document.querySelector(".root"));
