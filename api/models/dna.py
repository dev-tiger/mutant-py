from . import db

from sqlalchemy.dialects.postgresql import ARRAY


class Dna(db.Model):
    __tablename__ = "dna_registers"
    id_dna = db.Column(db.String(), primary_key=True)
    dna = db.Column(ARRAY(db.String()))
    mutant = db.Column(db.Boolean)

    def __init__(self, id_dna, dna, mutant):
        self.id_dna = id_dna
        self.dna = dna
        self.mutant = mutant

    __table_args__ = {'schema': 'public'}
