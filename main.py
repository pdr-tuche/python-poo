# from classes import WaterBottle -> assim importa é o arquivo WaterBottle.py, e nao a classe
from classes.WaterBottle import WaterBottle

# garrafaDagua = WaterBottle.WaterBottle('Voss', 20.9) com o import do arquivo, a instancia da classe teria que ser assim
garrafaDagua = WaterBottle('Voss', 20.9)
print(f'Produto: {garrafaDagua.name} -> Preço: R${garrafaDagua.price}')
