class Cuidadores:
    def __init__(self, nome, idade, documento):
        self._id = ObjectId()
        self.nome = nome
        self.idade = idade
        self.documento = documento

    def to_dict(self):
        return {
            '_id': self._id,
            'nome': self.nome,
            'idade': self.idade,
            'documento': self.documento
        }
