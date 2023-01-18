import express from "express";
import { convertCLTToPJ } from "./controllers/calculatorController.js";
var server = express();
server.get("/health", function (req, res) {
    res.send("All good");
});
server.get('/calculator', convertCLTToPJ);
server.listen(4000, function () {
    console.log("Server online...");
});
