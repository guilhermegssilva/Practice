//Tipos não primitivos: o que é salvo na variável é apenas uma referência para o valor, que está salvo internamente em outro local
const variavel = { nome: "João" }; 

/* O valor { nome: "João" } está salvo internamente
em outro local e o que fica salvo na variável é
somente uma identificação de onde ele está salvo
*/


//Isso significa que se você faz coisas como:
const pessoa1 = { nome: "João" };
const pessoa2 = pessoa1;

pessoa2.nome = "Maria"; // Tanto pessoa2 quanto pessoa1 serão alterados, pois estamos alterando o mesmo objeto


/************************************************************/


//Por isso, ES6 introduziu o Spread Operator:

// novoArray contém os mesmos valores que array, mas novoArray !== array
const array = [1, 2, 3];
const novoArray = [...array];


//Também podemos colocar outros valores na nova array:
const array1 = [1, 2, 3];
const novoArray1 = [...array, 4];
const outroArray = [0, ...array];

// novoArray1 contém 1, 2, 3 e 4
// outroArray1 contém 0, 1, 2 e 3


/**********************************************/


//O operador também pode ser utilizado para copiar objetos:
const pessoa = { nome: "João", idade: 20 };
const copia = { ...pessoa };


//E podemos criar uma cópia adicionando ou modificando propriedades:
const pessoa2 = { nome: "João", idade: 20 };
const novaPessoa = { ...pessoa, idade: 21, email: "joao@email.com" };

console.log(novaPessoa);
// imprimirá { nome: "João", idade: 21, email: "joao@email.com" }