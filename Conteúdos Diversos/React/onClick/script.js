function Botao() {
    
    function alertar(texto) {
        ////... /// Escre um texto na tela
	}


	function chamaComParametro() {
		alertar("Hello World"); //Como o onClick não aceita parâmetros é necessário criar esta função para passá-lo
	}

	return (
		<button onClick={chamaComParametro}>Clique aqui</button> //A função é passada entre chaves e sem os parênteses
	);
}

   
    //Como a função chamaComParametro() só serve para passar um parametro ela pode ser escrita em forma de arrow function
	<button onClick={() => alertar("Hello World!")}>Clique aqui</button>
	