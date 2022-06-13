export default function Menu() {  //O arquivo Menu será exportado e poderá ser chamado em outro arquivo (index.js)
    return (
	 <ul>
	 	<li><a href="...">Home</a></li>
	 	<li><a href="...">Sobre nós</a></li>
	 	<li><a href="...">Contato</a></li>
	 </ul>
    );
}

//////////////////////////////////////////////////////////

export default function Menu() {  //O arquivo Menu será exportado e poderá ser chamado em outro arquivo (index.js)
    return (
	 <div class="menu">
       <ul>
         <MenuItem link="link1" nome ="Home" />
          <MenuItem link="link2" nome ="Contato" />
          <MenuItem link="link3" nome ="Venha nos visitar!" />
       </ul>
    </div>
    );
}

//É criada uma função que recebe o parâmetro props. Esse parâmetro contém os atributos a serem passados, como se fossem variáveis. Se houverem vários itens com um código que mude apenas algumas informações é uma boa prática a se fazer.
function MenuItem(props) {
   return (
      <li><a href={props.link}>{props.nome}</a></li>
   )
}