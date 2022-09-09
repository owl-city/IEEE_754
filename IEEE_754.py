import math



ingresa_numero = int(input('Ingrese un número: '))

almacena_numero = [int(x) for x in str(ingresa_numero)]


ingresa_b = int(input('Ingresa el valor de b: '))

print('\n')


m = len(almacena_numero)
#print(m) #Imprime la longitud del número ingresado





almacena_division_numero = []

almacena_binario = []

almacena_division_numero.append(ingresa_numero)


posicion_indice = -1

print(f'{ingresa_numero}')
while True:
  posicion_indice += 1
  #print(str(posicion_indice) + '\n') #Imprime la posición del número
  #print(almacena_division_numero[0])
  

  if '0.' in str(almacena_division_numero):
    break
  else:
    dividir_numero = almacena_division_numero[int(posicion_indice)]/2
    almacena_division_numero.append(dividir_numero)
    
    print(f'{dividir_numero}') #Divide el número
    
    parte_decimal = math.modf(dividir_numero)
    #print(parte_decimal[0])

    if float(parte_decimal[0] >= 0.5):
      #print(f'{parte_decimal[0]} es 1') #Imprime si la parte binaria es 0
      almacena_binario.append('1')
    if float(parte_decimal[0] < 0.5):
      #print(f'{parte_decimal[0]} es 0') #Imprime si la parte binaria es 0
      almacena_binario.append('0')

    pass

print('\n')
#print(almacena_binario)


almacena_binario_inverso = []
for item in reversed(almacena_binario):
  almacena_binario_inverso.append(item)
print(f'({ingresa_numero}){ingresa_b} = ({almacena_binario_inverso})2')

print(f'm = {posicion_indice}')
print(f'b = {ingresa_b}')

numeros_j = []
for i in range(posicion_indice):
  numeros_j.append(i)

j = str(numeros_j).replace('[', '').replace(']', '')
print(f'j = {j}')


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


im = []
for i in range(len(numeros_j)):
  #print(f'{almacena_binario[i]} * 2^{numeros_j[i]}')
  im.append(f'{almacena_binario[i]} * 2^{numeros_j[i]}')


im = str(im).replace('[', '').replace(']', '')
im = str(im).replace(',', ' +').replace('\'', '')

print(f'IM = {im}')

im1 = str(im).replace('^', '**')

resultado = eval(im1)

print(f'Im = {resultado}')

