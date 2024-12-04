lista = [1,2,3,4,5,6,7,8,9,10]

def PesquisaBinaria(lista,indice):
    inicio = 0
    final = len(lista) - 1 
    while inicio <= final:
        meio = (inicio + final) //2
        if(lista[meio] == indice):
            return meio
        elif(lista[meio] < indice):
            inicio = meio +1
        elif(lista[meio] > indice):
            final = meio -1
        
    return -1
            

TrueOrFalse = PesquisaBinaria(lista , 7)
if TrueOrFalse  != -1:
    print("foi")
else:
    print("não foi")

