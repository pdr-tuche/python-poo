from classes import Endereco, Cliente

cliente1 = Cliente('Robso', 32)
cliente1.insere_endereco('JOAOPESSOA', 'PB')
print(cliente1.nome)
cliente1.lista_enderecos()
print("=== ====")

cliente2 = Cliente("JOSEFA", 76)
cliente2.insere_endereco('JOAOPESSOA', 'PB')
cliente2.insere_endereco('MANMANGUAPE', 'PB')
print(cliente2.nome)
cliente2.lista_enderecos()
print("=== ====")

cliente3 = CLiente('CLARA', 18)
cliente3.insere_endereco("ITAPECERICA", "MG")
cliente3.insere_endereco("ITAPIPOCA", "CE")
print(cliente2.nome)
cliente2.lista_enderecos()
print("=== ====")
