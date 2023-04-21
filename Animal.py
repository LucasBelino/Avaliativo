from bson.objectid import ObjectId

class Animal:
    def __init__(self, nome, especies, idade, habitat_id, _id=None):
        self._id = ObjectId()
        self.nome = nome
        self.especies = especies
        self.idade = idade
        self.habitat_id = habitat_id

    def to_dict(self):
        return {
            '_id': self._id,
            'nome': self.nome,
            'especies': self.especies,
            'idade': self.idade,
            'habitat_id': self.habitat_id
        }
