Para selecionar dados:
SELECT * FROM clientes WHERE nome = 'Luiz' --strings entre aspas simples
SELECT * FROM clientes WHERE uf = 'RS'; --ponto e vírgula opcional
SELECT * FROM clientes WHERE nome <> 'Luiz' --diferente
SELECT * FROM clientes WHERE idade > 18 --maior
SELECT * FROM clientes WHERE idade <= 18 --menor ou igual

Para inserir dados:
INSERT INTO usuarios (idade,email,senha) VALUES (25, 'fulano@hotmail.com', '123456');

Para atualizar dados:
UPDATE usuarios SET senh='010101' WHERE id = 2;

Para deletar dados:
DELETE FROM usuarios WHERE id = 2;

Conectando o Node ao Postgres

import pg from 'pg';

const { Pool } = pg;

const user = 'postgres';
const password = '123456';
const host = 'localhost';
const port = 5432;
const database = 'meu_banco_de_dados';

const connection = new Pool({
  user,
  password,
  host,
  port,
  database
});

const query = connection.query('SELECT * FROM produtos');

query.then(result => {
    console.log(result.rows);
});