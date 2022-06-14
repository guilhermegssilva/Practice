import React from "react"
import Joke from "./Joke"
import jokesData from "./jokesData"

export default function App() { //Cada elemento do objeto jokesData retorna um componente <Joke />, usando as propriedades setup e punchline presentes no objeto jokesData
    const jokeElements = jokesData.map(joke => { 
        return <Joke setup={joke.setup} punchline={joke.punchline} />
    })

    return (
        <div>
            {jokeElements}
        </div>
    )
}

   /***  ARQUIVO jokesData  ***/
[
    {
        setup: "I got my daughter a fridge for her birthday.",
        punchline: "I can't wait to see her face light up when she opens it."
    },
    {
        setup: "How did the hacker escape the police?",
        punchline: "He just ransomware!"
    },
    {
        setup: "Why don't pirates travel on mountain roads?",
        punchline: "Scurvy."
    },
    {
        setup: "Why do bees stay in the hive in the winter?",
        punchline: "Swarm."
    },
    {
        setup: "What's the best thing about Switzerd?",
        punchline: "I don't know, but the flag is a big plus!"
    }
]

function Joke(props) {
    return (
        <div>
            <h3>Setup: {props.setup}</h3>
            <p>Punchline: {props.punchline}</p>
            <hr />
        </div>
    )
}