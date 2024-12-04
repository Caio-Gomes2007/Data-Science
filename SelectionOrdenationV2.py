lista = [1,234,42,5,423,65,6,54,7,4,7,45,7,245,32,43,2]

def ordem(lista):
    tamanho = len(lista)

    for i in range(tamanho-1):
        menor = i
        for j in range(i+1,tamanho):
            if(lista[menor] > lista[j]):
                aux = lista[j]
                lista[j] = lista[menor]
                lista[menor] =aux
    return lista

print(ordem(lista))
