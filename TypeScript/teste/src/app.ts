import express from "express"
import { convertCLTToPJ } from "./controllers/calculatorController.js";
const server = express();

server.get("/health", (req, res) => {
    res.send("All good")
})

server.get('/calculator', convertCLTToPJ)

server.listen(4000, () => {
    console.log("Server online...")
})