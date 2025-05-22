# itens[0] = itens[2]*2 + itens[3]

# cantores = ['Chico buarque', 'gal costa', 'maria betania', 'gil','pericles'];

# pessoas = cantores;

# print(pessoas)

# soma = 0
# for i in range(0, 4):
#     cant = cantores[i]
#     print = cant


# # tam_indice = len(indice)

# # print(tam_indice)

# print("hello world!")

# valores = input("Digite os valores na mesma linha").split()

# valores = [None]*2
# for i in range (len(valores)):
#     valores[i] = input("Digite um valor.")

# print(valores)


# Subprogramas
def escrever(valores):
    for item in valores:
        print (item, end = '')
    print()
    return None

def ler (valores):
    for i in range (len(valores)):
        valores[i] = float(input("Valores["+str(i+1)+"]="))
    return None

def ordenar(valores):
    return None

#Programa Principal
TAM = 10
numeros = [0.0]*TAM
ler(numeros)
escrever(numeros)
ordenar(numeros)
escrever(numeros)


# print(numeros)

def selectionSort(lyst): i = 0 while i < len(lyst) - 1: minIndex = i
    j = i + 1 while j < len(lyst):
    j += 1 if minIndex != i: swap(lyst, minIndex, i) i += 1 