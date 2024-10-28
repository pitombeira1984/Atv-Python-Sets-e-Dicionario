def RemoverItensDoConjunto():
    conjunto = {'morango', 'cereja', 'framboesa'}
    remover = input("Digite o item a ser removido do conjunto: ").lower()
    if remover in conjunto:
        conjunto.remove(remover)
        return f"""
        Item removido com sucesso!
        Conjunto atualizado: {conjunto}
        """
    else:
        return "Item não encontrado no conjunto."

resultado = RemoverItensDoConjunto()
print(resultado)