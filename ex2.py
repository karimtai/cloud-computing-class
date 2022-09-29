import sys 

#Funcion para obtener la lista de numeros
def numeros(num):
    lista=[] #Variable donde se almacenaran en list
    for i in range (1, num): #Comenzando desde uno, hasta el numero deseado
        lista.append(i) #Lo agrega
    
    return lista
    
#Funcion para determinar si el numero agregado es primo
def es_primo(num, n=2): 
    """
    Comienza con el numero que se busca sea primo, se sabe que 0, 1 y 2 
    ya son numeros primos, por lo que se comienza la busqueda si se es mayor a 2
    
    Si son iguales n y num, es porque despues de todo el proceso de 
    retroalimentacion nunca se regreso un valor booleano falso, por lo que 
    si es primo
    """
    if n >= num: 
        return True
    #Si tiene residuos la division, significa que no es multipo, por lo que
    #se regresa a la funcion agregando un valor a n"""
    elif num % n != 0:
        return es_primo(num, n + 1)
    
   #Por lo contrario, si el residuo es 0, es un multiplo y el numero 
    #proporcionado no es primo
    else:
        #print(num)
        #print("No es primo", n, "es divisor")
        return False

#Busca el primer argumento al ser llamado desde terminal y lo guarda en int
num1=int(sys.argv[1]) +1

#Llama a la funcion de listaje e imprime
print(numeros(num1))


#Busca los numeros primos dentro del 
num_primos=[]
for i in range (1, num1):
    if es_primo(i):
        num_primos.append(i)

print (len(num_primos))
print ((num_primos))
