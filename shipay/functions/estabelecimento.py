from shipay.models import Estabelecimento, Recebimento
from flask import jsonify
from shipay import db


def criar_estabelecimento(data):
    consulta = Estabelecimento.query.filter_by(cnpj=data['cnpj']).first()
    if consulta:
        return jsonify(error='Estabelecimento já cadastrado com este CNPJ.'), 400
    novo_estabelecimento = Estabelecimento(**data)
    db.session.add(novo_estabelecimento)
    try:
        db.session.flush()
    except Exception as e:
        raise f'Error: {str(e)}'

    db.session.commit()

    return jsonify(message = 'Inserido com sucesso')

def realizar_transacao(data):
    estabelecimento = data.get('estabelecimento', None)
    cliente = data.get('cliente', None)
    valor = data.get('valor', None)
    descricao = data.get('descricao', None)

    try:
        if estabelecimento and valor:
            estabelecimento = Estabelecimento.query.filter_by(cnpj=estabelecimento).first()
            if estabelecimento:
                data = dict(
                    estabelecimento_id  = estabelecimento.id,
                    cliente = cliente,
                    valor = valor,
                    descricao = descricao
                )
                nova_transacao = Recebimento(**data)
                db.session.add(nova_transacao)
                db.session.commit()
                return jsonify(aceito=True)
            else:
                return jsonify(aceito=False)
        else:
            return jsonify(aceito=False)
    except Exception as e:
        return jsonify(aceito=False)


def consulta_transacoes(estabelecimento):
    if not estabelecimento:
        return jsonify(error='Estabelecimento inválido')

    estabelecimento = Estabelecimento.query.filter_by(cnpj=estabelecimento).first()

    if not estabelecimento:
        return jsonify(error='Estabelecimento não encontrado')

    recebimentos = Recebimento.query.filter_by(estabelecimento_id = estabelecimento.id).all()

    data = dict(
        estabelecimento=estabelecimento.serialize,
        recebimentos=[recebimento.serialize for recebimento in recebimentos],
        total_recebido=round(sum([_.serialize['valor'] for _ in recebimentos]), 2)
    )

    return jsonify(data)
