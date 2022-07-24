//Arquitetura de Controllers

//Veja o seguinte código

//index.js
import express from 'express';

const app = express();

app.get('/participants', async (req, res) => { /// ...
    });

app.get('/messages', async (req, res) => { ///... 
    });

app.listen(5000, () => {
  console.log("Listening on 5000")
})

//Se organizarmos nosso projeto da seguinte maneira, estaremos dando um grande passo na arquitetura do código:

//arquivo index.js
import express from 'express';
import { getParticipants } from './participants.js';
import { getMessages } from './messages.js';

const app = express();

app.get('/participants', getParticipants);
app.get('/messages', getMessages);

app.listen(5000, () => {
  console.log("Listening on 5000")
})
///

//arquivo participants.js
export async function getParticipants(req, res) {
/// ....
}

//arquivo messages.js
export async function getMessages(req, res) {
/// ....
}
