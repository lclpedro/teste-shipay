from app import db

class Estabelecimento(db.Model):
    __tablename__ = 'estabelecimento'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nome = db.Column(db.String)
    cnpj = db.Column(db.String, unique=True)
    dono = db.Column(db.String)
    telefone = db.Column(db.String)

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return dict(
           nome=self.nome,
           cnpj=self.cnpj,
           dono=self.dono,
           telefone=self.telefone,
       )



