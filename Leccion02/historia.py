#Operadores Aritmeticos


operandoA = 3
operandoB = 2

suma = operandoA +  operandoB
print('El resultado de la suma es :' , suma)
print(f'El resultaso de la suma es : {suma}')

resta = operandoA - operandoB
print(f'El resultado de la resta es: {resta}')

multiplicacion = operandoA * operandoB
print(f'El resultado de la multiplicacion es: {multiplicacion}')

division = operandoA / operandoB
print(f'El resultado de la division es: {division}')

division_entera  = operandoA // operandoB
print(f'El resultado de la division es: {division_entera}')

exponente = operandoA ** operandoB
print(f'El resultado del exponente es: {exponente}')

residuo = operandoA % operandoB
print(f'El resultado del residuo es: {residuo}')

"""
#Area y Perimetro de un rectangulo*********************************************
altura = int(input("Ingresar la altura del rectangulo: "))
ancho = int(input("Ingresar el ancho del rectangulo: "))
area = altura * ancho
perimetro = (altura + ancho)*2
print(f'Area: {area}')
print(f'Perimetro: {perimetro}')


#Numero par o impar******************************************************************************

num = int(input("Ingresar un número: "))
resultado = num % 2

if resultado == 0:
    print(f'{num} Es un número Par')
else:
    print(f'{num} Es un número Impar')


# Es mayor de edad****************************************************************************

edad = int(input("Digitar su edad: "))

if edad >= 18:
    print(f'Eres mayor de edad')

else:
    print(f'Aun no eres mayor de edad')
    
    
    
#Valor dentro de un rango***********************************************************

numero = int(input("ingresar valor: "))
if numero >= 1 and numero<=10:
    print(f'{numero} se encounter en el rang del 1 - 10')
else:
    print(f'{numero} No est en el rang')


VACACIONES*************************************************
vacaciones = False
descanso = False

if vacaciones or descanso:
    print(f'Puedes asistir al juego de tu hijo')

else:
    print(f'No puedes asistir al juego de tu hijo')
    

#RANGO DE EDAD *************************************************
# si la persona esta entre los 20s y 30s años
edad = int(input("Ingresa tu edad: "))



if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
    print("Se encuentra entre los 20s y los 30s años de edad")
else:
    print("Su edad está fuera del rango especificado")


# OTRA FORMA

if (20 <= edad < 30) or (30 <= edad < 40):
    print("Se encuentra entre los 20s y los 30s años de edad x2")
else:
    print("Su edad está fuera del rango especificado x2")



"""

