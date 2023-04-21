from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalModel:
    def __init__(self, database):
        self.db = database
        self.collection = database.collection

    def create_animal(self, nome: str, especie: str, idade: int, habitat: int) -> str:
        try:
            result = self.collection.insert_one({"nome": nome, "especie": especie, "idade": idade, "habitat": habitat})
            animal_id = str(result.inserted_id)
            print(f"{nome} foi criado com o id: {animal_id}")
            return animal_id
        except Exception as error:
            print(f"Ocorreu um erro: {error}")
            return None

    def read_animal(self, animal_id: str) -> dict:
        try:
            animal = self.collection.find_one({"_id": ObjectId(animal_id)})
            if animal:
                print(f"Animal encontrado: {animal}")
                return animal
            else:
                print(f"Nao foi possivel encontrar um animal com o id: {animal_id}")
                return None
        except Exception as error:
            print(f"Ocorreu um erro: {error}")
            return None

    def update_animal(self, animal_id: str, nome: str, especie: str, idade: int, habitat: int) -> int:
        try:
            result = self.collection.update_one({"_id": ObjectId(animal_id)}, {"$set": {"nome": nome, "especie": especie, "idade": idade, "habitat": habitat}})
            if result.modified_count:
                print(f"O animal de ID {animal_id} foi atualizado para nome {nome}, especie {especie}, idade {idade} anos e {habitat}")
            else:
                print(f"Nao foi encontrado animal com o id {animal_id}")
            return result.modified_count
        except Exception as error:
            print(f"Ocorreu um erro: {error}")
            return None

    def delete_animal(self, animal_id: str) -> int:
        try:
            result = self.collection.delete_one({"_id": ObjectId(animal_id)})
            if result.deleted_count:
                print(f"Animal de ID {animal_id} foi deletado !")
            else:
                print(f"Nao foi encontrado animal com o id {animal_id}")
            return result.deleted_count
        except Exception as error:
            print(f"Ocorreu um erro: {error}")
            return None