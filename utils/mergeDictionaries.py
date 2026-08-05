def mergeDictionaries(keysDict: dict, valueDict: dict):
    faltando = keysDict.keys() - valueDict.keys()
    if faltando:
        raise KeyError(f"Colunas ausentes na planilha: {sorted(faltando)}")

    newDict = {}
    for chaveA, valorA in keysDict.items():
        newDict[valorA] = valueDict[chaveA]

    return newDict