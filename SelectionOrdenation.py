lista = [17,4,6,8,9,2,3,4,5,2,456,7]

def ordenacao(lista):

    tamanhoReal = len(lista) -1
    tamanho = len(lista)
    for i in range(tamanhoReal):
        minIndice = i
        for j in  range(i+1,tamanho):
            if(lista[minIndice] > lista[j]):
                aux = lista[j]
                lista[j] =  lista[minIndice]
                lista[minIndice] = aux
    return lista

print(ordenacao(lista))
