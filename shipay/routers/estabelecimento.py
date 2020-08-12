from flask import Blueprint, request
from shipay.functions.estabelecimento import (
    criar_estabelecimento, realizar_transacao, consulta_transacoes
)


bp_estabelecimento = Blueprint('bp_estabelecimento', __name__, url_prefix='/api/v1/')

@bp_estabelecimento.route('/estabelecimento', methods=['POST'])
def route_criar_estabelecimento():
    data = request.json
    return criar_estabelecimento(data)


@bp_estabelecimento.route('/transacao', methods=['POST'])
def route_transacao():
    data = request.json
    return realizar_transacao(data)


@bp_estabelecimento.route('/transacao/estabelecimento', methods=['GET'])
def route_consulta_transacao():
    cnpj = request.args.get('cnpj', None)
    return consulta_transacoes(cnpj)

def configure(app):
    app.register_blueprint(bp_estabelecimento)
