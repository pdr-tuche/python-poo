from classes import Pessoa, Cliente, Aluno

cliente = Cliente('robervaldo', 32)
cliente.falar()
cliente.comprar()

aluno = Aluno('Junin', 17)
aluno.falar()
aluno.estudar()

pessoa = Pessoa('Alici', 18)
pessoa.falar()
# Pessoa nao tem acesso aos metodos de Aluno ou Cliente
pessoa.estudar()
pessoa.comprar()
