var agora = new Date()          /*Método usado para obter a hora atual do sistema*/
var hora = agora.getHours()     /*Variável hora recebe o horário do sistema em horas*/ 
var minuto = agora.getMinutes() /*Variável minuto recebe o horário do sistema em minutos*/
console.log(`Agora são exatamente ${hora} horas e ${minuto} minutos`)
if (hora < 12) {
    console.log('Bom dia')
} else if (hora < 18) {
    console.log('Boa tarde')
} else {
    console.log('Boa noite')
}


var agora = new Date()
var diaSem = agora.getDay()

switch (diaSem) {
    case 0:
        console.log('Domingo')
        break
    case 1:
        console.log('Segunda-feira')
        break
    case 2:
        console.log('Terça-feira')
        break
    case 3:
        console.log('Quarta-feira')
        break
    case 4:
        console.log('Quinta-feira')
        break
    case 5:
        console.log('Sexta feira')
        break
    case 6:
        console.log('Sábado')
        break
    default:
        console.log('Dia inválido')
}

