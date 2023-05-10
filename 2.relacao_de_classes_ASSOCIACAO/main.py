from classes import Pessoa, Caneta


p1 = Pessoa("Pedro")
caneta = Caneta('BIC')


print(p1.nome, p1.ferramenta)
print(caneta.marca)
print()

p1.ferramenta = caneta
print(p1.ferramenta.escrever())

print(p1.ferramenta)  # aparece o enderreco de memoria sem o metodo str na caneta
