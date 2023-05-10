from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

produto1 = Produto('Tenis da shopee', 20)
produto2 = Produto('Camisa original do Barça', 50)
produto3 = Produto('bermuda cyclone', 25)

carrinho.inserir_produto(produto1)
carrinho.inserir_produto(produto2)
carrinho.inserir_produto(produto3)

carrinho.lista_produtos()
print(f'soma dos produtos = {carrinho.soma_total()}')
