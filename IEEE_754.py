import math

#Ingresamos un número desde la consola
ingresa_numero = int(input('Ingrese un número: '))

#Creamos una lista donde se va a almacenar el número ingresado en diferentes ídinces 
almacena_numero = [int(x) for x in str(ingresa_numero)]

#Ingresamos el valor de b
ingresa_b = int(input('Ingresa el valor de b: '))

print('\n')

#La variable m cuenta la longitud que tiene la lista almacena número
m = len(almacena_numero)

#Imprime la longitud del número ingresado
#print(m) 

#almacena_division_numero almacena todos los números que serán divididos entre 2
almacena_division_numero = []

#almacena_binario almacena todos los resultados que cumplan la condición de la mantisa de ser "mayor o igual qué" o "menor qué" 0.5
almacena_binario = []

#Se añade a la lsita el número dividido el primer número ingresado en la consola "ingresa_numero"
almacena_division_numero.append(ingresa_numero)

#Creamos un contador que iniciará en -1
posicion_indice = -1

print(f'{ingresa_numero}')

#Creamos un ciclo while debido a que tenemos que hacer iteraciones indefinidas hasta llegar al número que empiece con "0.xxxxx......"
while True:
  #Comenzamos a contar:
  posicion_indice += 1

  #print(str(posicion_indice) + '\n') #Imprime la posición del número
  #print(almacena_division_numero[0])
  
  #Creamos una condicional donde preguntarmos si el decimal "0." empieza con esa característica, se rompe el ciclo while
  if str(almacena_division_numero[posicion_indice]).startswith('0.'):
    #En caso de ser cierta la condicional anterior, el ciclo se rompe
    break
  
  else:

    #Si la condición anterior no se cumple, seguimos iterando para dividir el número hasta llegar al "0.xxxxx....."
    dividir_numero = almacena_division_numero[int(posicion_indice)]/2

    #Alcmacenamos el número dividido
    almacena_division_numero.append(dividir_numero)
    
    print(f'{dividir_numero}') #Divide el número
    
    #Para poder tomar exclusivamente la parte fraccionaria de un número, tenemos que dividir en dos partes el número: La parte entra y la fraccionaria 
    parte_decimal = math.modf(dividir_numero)
    #print(parte_decimal[0])
    
    #Condicionamos en caso de la parte fraccionaria sea mayor o igual qué 0.5, se añade a la lista "almacena_binario" el número 1
    if float(parte_decimal[0] >= 0.5):
      #print(f'{parte_decimal[0]} es 1') #Imprime si la parte binaria es 0
      almacena_binario.append('1')

    #Condicionamos en caso de la parte fraccionaria sea menor qué 0.5, se añade a la lista "almacena_binario" el número 0
    if float(parte_decimal[0] < 0.5):
      #print(f'{parte_decimal[0]} es 0') #Imprime si la parte binaria es 0
      almacena_binario.append('0')
  
    #Y omitimos con pass para seguir iterando y evitar congelar el ciclo
    pass

print('\n')
#print(almacena_binario)

#Creamos una lista donde se almacena para leer de derecha a izquierda los binarios
almacena_binario_inverso = []

#Para cumplir con la condición de leer de derecha a izquierda los binarios encontrados, hacemos una iteración inversa
for item in reversed(almacena_binario):

  #Lo añadimos en la lista almacena_binario_inverso
  almacena_binario_inverso.append(item)

#Para ver estéticamente un poco mejor el resultado, eliminamos los caracteres de la cadena
binario_inverso = str(almacena_binario_inverso).replace('[', '').replace(']', '').replace('\'', '').replace(',', '')


#Imprimimos el número ingresado en la consola junto con el binario leído de derecha a izquierda
print(f'({ingresa_numero}){ingresa_b} = ({binario_inverso})2')

###### Decimal


print(f'Comprobación Decimal ({ingresa_numero})10:\n')
print(f'b = 10')
print(f'm = {m}')



numeros_j = []
for i in range(m):
  numeros_j.append(i)

j = str(numeros_j).replace('[', '').replace(']', '')
print(f'j = {j}')


almacena_numero_inverso = []
d = []
for i in range(0, len(almacena_numero)):
  a = (f'd{i}')
  #print(a)
  d.append(a)


contador = -1
for i in almacena_numero[::-1]:
  contador += 1
  #print(i)
  
  print(f'{d[contador]} = {i}')
  almacena_numero_inverso.append(i)



im = []
for i in range(len(numeros_j)):
  #print(f'{almacena_numero_inverso[i]} * 10^{numeros_j[i]}')
  im.append(f'{almacena_numero_inverso[i]} * 10^{numeros_j[i]}')

im = str(im).replace('[', '').replace(']', '').replace(',', ' +').replace('\'', '')

print(f'IM = {im}')

im1 = str(im).replace('^', '**')

resultado = eval(im1)

print(f'Im = {resultado}')






###### Binario

#Título de la comprobación en Binario
print(f'\nComprobación en Binario ({binario_inverso})2:\n')



#Imprimimos el valor de "b" que en el caso de binario es 2
print(f'b = 2')

#Imprimimos "m" que viene siendo la longitud de elementos que tiene la lista de binario inverso, pero "posicion_indice" es el contador de las veces que se dividió entre 2 hasta llegar a "0.xxxx...."
print(f'm = {posicion_indice}')

#Creamos una lista para contar la longitud de elementos de binario inverso, pero comenzando desde el 0
numeros_j = []

#Realizamos una iteración de la pocisión del las veces iteradas al obtener el resultado de "0.xxxxx...." para contar de 0 las veces que se iteró "posicion_indice"
for i in range(posicion_indice):

  #Se aladen a la lista numeros_j
  numeros_j.append(i)

#Para ver estéticamente mejor los números, eliminamos algunos caracteres de la cadena e imprimimos
j = str(numeros_j).replace('[', '').replace(']', '')
print(f'j = {j}')


#Se crea una lista e iteración para determinar los valor de "d0, d1....." tomando en consideración la cantidad de elemntos que exitan dentro de la lista de "almacena_binario_inverso"
d = []
for i in range(0, len(almacena_binario_inverso)):
  a = (f'd{i}')
  #print(a)
  d.append(a)

#Mediante un contador y una iteración inversa, añadimos los valores de "d0, d1....." y los vinculamos respectivamente con los binarios inversos
contador = -1
for i in almacena_binario_inverso[::-1]:
  contador += 1
  #print(i)
  
  print(f'{d[contador]} = {i}')


#Comenzamos a multuplicar los binarios inversos con los exponentes que vendrían siendo la variable "j", iterando con la cantidad de elementos que hay en la lista "numeros_j"
im = []
for i in range(len(numeros_j)):
  #print(f'{almacena_binario[i]} * 2^{numeros_j[i]}')
  im.append(f'{almacena_binario[i]} * 2^{numeros_j[i]}')

#Para ver estéticamente mejor los números, eliminamos algunos caracteres de la cadena e imprimimos
im = str(im).replace('[', '').replace(']', '')
im = str(im).replace(',', ' +').replace('\'', '')

#Imprimimos IM
print(f'IM = {im}')

#Reemplazamos el caracter "^" por el operador "**", esto a que tiene que ser evaluado y el caracter "^" no es un operador
im1 = str(im).replace('^', '**')

#Evaluamos la variable "im1"
resultado = eval(im1)

#Y arrojamos el resultado
print(f'Im = {resultado}')

