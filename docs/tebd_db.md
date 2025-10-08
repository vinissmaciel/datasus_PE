## Instrução para criar um banco de dados PostgreSQL no Docker

1. Certifique-se de que o Docker está instalado em sua máquina.

2. Execute o comando abaixo para criar e iniciar um container PostgreSQL:

Exemplo:
```bash
docker run --name tebd_db -e POSTGRES_DB=tebd_db -e POSTGRES_USER=tebd -e POSTGRES_PASSWORD=tebd -p 5432:5432 -d postgres
```
