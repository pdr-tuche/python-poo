class Pessoa:
    def __init__(self, valor):
        if isinstance(valor, str):
            self.__nome = valor
        else:
            self.__nome = 'FULANINHO'

        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        return f'caneta {self.__marca} esta escrevendo...'

    def __str__(self):
        return f'sou a caneta: {self.marca}'
