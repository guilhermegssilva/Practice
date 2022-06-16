/* Dada uma lista de objetos que contém o nome de um aluno e sua média final, implemente a função 'aprovados' que recebe esta lista e retorna somente os alunos que foram aprovados.

Para isto, utilize a função filter.

const alunos = [
  { nome: 'Diogo', media: 5.5 },
  { nome: 'Julia', media: 9.5 },
  { nome: 'Roberto', media: 1.5 },
  { nome: 'Tiago', media: 6.0 }
];

Exemplo: aprovados(alunos, 6.5) → [ { nome: 'Julia', media: 9.5 } ]
*/

function aprovados(alunos, media) {
    return alunos.filter(function(aluno){
      return aluno.media >= media;
    });
  }