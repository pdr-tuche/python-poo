class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.classe = self.__class__.__name__  # saber a classe que chamou o init

    def falar(self):
        print(f'{self.nome} esta falando ... ')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome} esta comprando ...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome} esta estudando...')
