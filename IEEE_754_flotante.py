import math

ingresa_numero = float(input('Ingresa un número: '))
#ingresa_numero = '10.3125'
ingresa_b = int(input('Ingresa el valor de b: '))
#ingresa_b = '10'

print(f'b = {ingresa_b}')

almacena_multiplicacion_numero = []
almacena_binario_inverso_final = []

posicion_indice = -1

print(f'{ingresa_numero}')

print('\n')

parte_decimal_numero_inicial = math.modf(float(ingresa_numero))
print(parte_decimal_numero_inicial[0])

almacena_multiplicacion_numero.append(parte_decimal_numero_inicial[0])
#print(f'{almacena_multiplicacion_numero[0]}')    


almacena_binario = []

while True:
  posicion_indice += 1

  #print(str(posicion_indice) + '\n') #Imprime la posición del número
  #print(almacena_multiplicacion_numero[0])
  
  #if str(almacena_multiplicacion_numero[posicion_indice]).startswith('.0'):
  if '.0' in str(almacena_multiplicacion_numero[posicion_indice]):
    break
  
  else:    
    
    multiplicar_numero = almacena_multiplicacion_numero[int(posicion_indice)]*2

    #print(f'{multiplicar_numero}--_jotototototot') #Multiplica el número
    
    parte_decimal = math.modf(multiplicar_numero)[0]
    parte_decimal_2 = math.modf(multiplicar_numero)
    almacena_multiplicacion_numero.append(parte_decimal_2[0])

    print(f'{parte_decimal}')
    #print(almacena_multiplicacion_numero)

    #if float(parte_decimal[0] >= 0.5):
    if float(multiplicar_numero >= 1):
      almacena_binario.append('1')
      almacena_binario_inverso_final.append('1')

    if float(multiplicar_numero < 1.0):
      #print(f'{parte_decimal[1]} es 1') #Imprime si la parte binaria es 0
      almacena_binario.append('0')
      almacena_binario_inverso_final.append('0')
  
    pass

almacena_binario = str(almacena_binario).replace('[', '').replace(']', '').replace('\'', '').replace(',', '')
print(f'({ingresa_numero}){ingresa_b} = ({almacena_binario})2')


almacena_binario_inverso = []

###### Binario

#Título de la comprobación en Binario
print(f'\nComprobación en Binario ({almacena_binario})2:\n')

#Imprimimos el valor de "b" que en el caso de decimal es 10
print(f'b = 2')

#Imprimimos "n" que viene siendo la longitud de elementos que tiene la lista de binario inverso, pero "posicion_indice" es el contador de las veces que se dividió entre 2 hasta llegar a "0.xxxx...."
print(f'n = {posicion_indice}')

#Creamos una lista para contar la longitud de elementos de binario inverso, pero comenzando desde el 0
numeros_j = []

#Realizamos una iteración de la pocisión del las veces iteradas al obtener el resultado de "0.xxxxx...." para contar de 0 las veces que se iteró "posicion_indice"
for i in range(1, posicion_indice+1):

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

for item in reversed(almacena_binario):

  #Lo añadimos en la lista almacena_binario_inverso
  almacena_binario_inverso.append(item)

#print(f'{almacena_binario_inverso_final}')
#print(f'{almacena_binario}-----brga')

#Mediante un contador y una iteración inversa, añadimos los valores de "d0, d1....." y los vinculamos respectivamente con los binarios inversos
contador = -1
for i in almacena_binario_inverso_final:
  contador += 1
  #print(i)
  
  print(f'd-{contador} = {i}')

#Comenzamos a multiplicar los binarios inversos con los exponentes que vendrían siendo la variable "j", iterando con la cantidad de elementos que hay en la lista "numeros_j"
pn = []
contador_final = -1
for i in range(len(numeros_j)):
  contador_final += 1
  #print(f'{almacena_binario_inverso_final[i]} * 2^(-{numeros_j[i]})')
  pn.append(f'{almacena_binario_inverso_final[i]} * 2^(-{numeros_j[i]})')

#Para ver estéticamente mejor los números, eliminamos algunos caracteres de la cadena e imprimimos
pn = str(pn).replace('[', '').replace(']', '')
pn = str(pn).replace(',', ' +').replace('\'', '')

#Imprimimos IM
print(f'Pn = {pn}')

#Reemplazamos el caracter "^" por el operador "**", esto a que tiene que ser evaluado y el caracter "^" no es un operador
pn1 = str(pn).replace('^', '**')

#Evaluamos la variable "im1"
resultado = eval(pn1)

#Y arrojamos el resultado
print(f'Pn = {resultado}')