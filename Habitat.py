class Habitat:
    def __init__(self, nome, temperatura, area):
        self._id = ObjectId()
        self.nome = nome
        self.temperatura = temperatura
        self.area = area

    def to_dict(self):
        return {
            '_id': self._id,
            'nome': self.nome,
            'temperatura': self.temperatura,
            'area': self.area
        }
