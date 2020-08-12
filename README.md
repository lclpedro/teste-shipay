### Deploy do projeto usando docker
Para executar o projeto, basta executar o seguintes comandos abaixo.
```bash
$ docker-compose build
$ docker-compose up
```
Pronto o serviço está sendo executado, agora precisamos executar a migration do banco de dados, para isso abra um outro terminal e execute

```bash
$ docker-compose exec api flask db upgrade
```
Agora a API está Online.


### Rotas de APIS

Essa rota é responsável por criar um estabelecimento.
`POST localhost:5000/api/v1/estabelecimento`
body
```json
{
  "cnpj": "00.000.000/0001-00",
  "dono": "Nome do proprietário",
  "nome": "Nome do empreendimento",
  "telefone": "68999999999"
}
```
Resposta esperada se existir estabelecimento
```json
{
  "error": "Estabelecimento já cadastrado com este CNPJ."
}
```
Resposta esperada não existir estabelecimento
```json
{
  "message": "Inserido com sucesso"
}
```

Essa rota é responsável por realizar alguma transação via Shipay.
`POST localhost:5000/api/v1/transacao`
body
```json
{
    "estabelecimento": "00.000.000/0001-00",
    "cliente": "000.000.000-00",
    "valor": 600,
    "descricao": "Compra de combo mensal pago via Shipay!"
}
```
Resposta esperada se o estabelecimento não existir ou se o valor não for no formato adequado.
```
{
    "aceito": false
}
```
Resposta esperada se todos os dados estiverem corretos
```
{
    "aceito": true
}
```

Essa rota é responsável por mostrar todo o extrato do estabelecimento.
`GET localhost:5000/api/v1/transacao/estabelecimento?cnpj=00.000.000/0001-00`
Resposta esperada

```json
{
  "estabelecimento": {
    "cnpj": "00.000.000/0001-00",
    "dono": "Nome do proprietário",
    "nome": "Nome do empreendimento",
    "telefone": "68999999999"
  },
  "recebimentos": [
    {
      "cliente": "000.000.000-00",
      "descricao": "Compra de combo mensal pago via Shipay!",
      "valor": 600.0
    },
    {
      "cliente": "000.000.000-00",
      "descricao": "Compra de combo semanal pago via Shipay!",
      "valor": 400.0
    }
  ],
  "total_recebido": 1000.0
}
```
