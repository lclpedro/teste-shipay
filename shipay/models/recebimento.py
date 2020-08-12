from app import db

from shipay.models.estabelecimento import Estabelecimento


class Recebimento(db.Model):
    __tablename__ = 'recebimento'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    estabelecimento_id = db.Column(db.ForeignKey('estabelecimento.id'))
    cliente = db.Column(db.String)
    valor = db.Column(db.Float)
    descricao = db.Column(db.String)

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return dict(
           cliente=self.cliente,
           valor=self.valor,
           descricao=self.descricao
       )

