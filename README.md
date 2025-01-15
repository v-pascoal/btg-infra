# Instruções
Repositório responsável pela infra de containers do projeto.

## Pré-requisitos
Para usar este repositório você vai precisar:

1. Docker (Engine, Desktop, Daemon, CLI)
2. Se você for usar local: Todas as APIs listadas na sessão [Aplicações deste container](#aplicações-deste-container) devidamente baixadas na pasta `containers`.

## Passo a passo
Siga estes passos para executar o container em sua máquina. Fique atento aos pré-requisitos.

1. Garanta que os pré-requisitos foram atendidos.
2. Abra o terminal de comando e navegue até a pasta raiz deste projeto.
3. Execute o comando abaixo para gerar as imagens do projeto:

    ```bash
    docker compose build
    ```

4. Execute o comando abaixo para iniciar os containers:

    ```bash
    docker compose up
    ```

O RabbitMQ UI deve estar disponível na porta padrão 15675 - [http://localhost:15675](http://localhost:15675)  
O MongoDB deve estar disponível na porta padrão 27017 - `mongodb://<usuario>:<senha>@localhost:27017`
O Pedidos API deve estar disponível na portal 80 - [http://localhost](http://localhost)

> **OBS:** Verifique no arquivo [docker-compose.yaml](./docker-compose.yaml) o usuário e senha para se conectar ao Dashboard do RabbitMQ e ao MongoDB.


## Aplicações deste container

- ![DONE](https://img.shields.io/badge/DONE-green) [`Api de Pedidos`](https://github.com/v-pascoal/btg-itderiv-api-pedidos)
-  ![TO-DO](https://img.shields.io/badge/TODO-gray) `Api de Identificação`
-  ![TO-DO](https://img.shields.io/badge/TODO-gray) `Api de Produtos`
-  ![TO-DO](https://img.shields.io/badge/TODO-gray) `Api de Carrinho`

## Como eu crio uma nova aplicação e integro ao container?
1. Crie a aplicação normalmente seguindo os padrões de arquitetura do BTG. Ao concluir, crie o `Dockerfile` na raiz desta aplicação.
2. No arquivo [docker-compose.yaml](./docker-compose.yaml) adicione as entradas para a sua aplicação seguindo o padrão `<funcionalidade-app>`.
3. Pare os containers (se estiverem rodando):

    ```bash
    docker compose down
    ```

4. Faça o build do novo docker compose:

    ```bash
    docker compose build
    ```

5. Inicie os containers:

    ```bash
    docker compose up
    ```