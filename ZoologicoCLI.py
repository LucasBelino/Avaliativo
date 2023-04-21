from models import AnimalModel, Cuidador, Habitat

class ZoologicoCLI:
    def __init__(self, database):
        self.db = database
        self.animal_model = AnimalModel(database)

    def run(self):
        while True:
            print("Bem vindo")
            print("1 - Cadastrar um animal")
            print("2 - Pesquisar um animal")
            print("3 - Atualizar um animal")
            print("4 - Deletar um animal")
            print("0 - Sair")
            opcao = input("Opção: ")

            if opcao == "1":
                animal = self.cadastrar_animal()
                if animal:
                    self.animal_model.create_animal(animal.nome, animal.especie, animal.idade, animal.habitat)
            elif opcao == "2":
                animal_id = input("Digite o ID do animal: ")
                self.animal_model.read_animal(animal_id)
            elif opcao == "3":
                animal_id = input("Digite o ID do animal: ")
                animal = self.cadastrar_animal()
                if animal:
                    self.animal_model.update_animal(animal_id, animal.nome, animal.especie, animal.idade, animal.habitat)
            elif opcao == "4":
                animal_id = input("Digite o ID do animal: ")
                self.animal_model.delete_animal(animal_id)
            elif opcao == "0":
                break
            else:
                print("Opção invalida!")

    def cadastrar_animal(self):
        print("Cadastro do animal:")
        nome = input("Nome: ")
        especie = input("Especie: ")
        idade = int(input("Idade: "))
        habitat = self.cadastrar_habitat()
        cuidador = self.cadastrar_cuidador()

        if nome and especie and idade and habitat and cuidador:
            return Animal(nome, especie, idade, habitat, cuidador)
        else:
            print("Dados invalidos!")
            return None

    def cadastrar_habitat(self):
        print("Cadastro do habitat:")
        nome = input("Nome: ")
        capacidade = int(input("Capacidade: "))

        if nome and capacidade:
            return Habitat(nome, capacidade)
        else:
            print("Dados invalidos!")
            return None

    def cadastrar_cuidador(self):
        print("Cadastro do cuidador:")
        nome = input("Nome: ")
        doc = input("Documento: ")

        if nome and documento:
            return Cuidador(nome, documento)
        else:
            print("Dados invalidos!")
            return None
