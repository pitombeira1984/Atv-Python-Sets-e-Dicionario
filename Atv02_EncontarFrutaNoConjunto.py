def EncontarFrutaNoConjunto():
    fruta = {'maça', 'banana', 'goiaba', 'acerola', 'caju', 'cajá'}
    fruta_encontrada = input("Digite a fruta a ser pesquisada: ").lower()
    if fruta_encontrada in fruta:
        print("A fruta está no conjunto.")
    else:
        print("A fruta não está no conjunto.")
EncontarFrutaNoConjunto()