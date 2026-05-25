# // crear una funcion que reciba un numero y retorne su cuadrado
def cuadrado(num):
    return num ** 2 

# // crear una funcion que reciba una frase y conviert esa frase en una lista de palabras

def frase_a_lista(frase):
    return frase.split()        

input_frase = input("Ingrese una frase: ")
print(frase_a_lista(input_frase))

