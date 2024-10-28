def AdicionarItensNoConjunto():
    conjunto = set()
    while True:
        item = input("Digite um item para adicionar ao conjunto (ou 'sair' para encerrar): ")
        if item.lower() == 'sair':
            break
        conjunto.add(item)
    return conjunto
conjunto = AdicionarItensNoConjunto()
print(conjunto)