import sys 

#Funcion para obtener la lista de numeros
def numeros(num):
    lista=[] #Variable donde se almacenaran en list
    for i in range (num): #Comenzando desde uno, hasta el numero deseado
        lista.append(i) #Lo agrega
    
    return lista
    
#Funcion para determinar si el numero agregado es primo
def es_primo(num, n=2):
    if n >= num:
        #print("Es primo")
        return True
    elif num % n != 0:
        return es_primo(num, n + 1)
    else:
        
        return False

#Busca el primer argumento al ser llamado desde terminal y lo guarda en int
num1=int(sys.argv[1]) +1

#Llama a la funcion de listaje e imprime la misma
print(numeros(num1))


#Variable de list para los numeros primos 
num_primos=[]
#Busca los numeros primos dentro del rango de 1 hasta el numero obtenido
for i in range (num1):
    if es_primo(i):
        #print(i)
        num_primos.append(i)

#Imprime los numeros   
print (num_primos)
print (len(num_primos))

#dehwfu