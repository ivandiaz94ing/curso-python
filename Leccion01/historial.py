#Este el la forma de hacer un comentario en python

print("Este es mi saludo desde Python")

#SECCION DE VARIABLES
#Video 1 ********************************************************
miVariable = "Hola Mundo desde Python"
print(miVariable)
print(miVariable)

miVariable = 10

print(miVariable)

#Video 2 *****************************************************
x = 10
y = 2
z = x + y
print(x)
print(y)
print(z)
print(id(y))

#Video 3 ejercicio de variables *******************************
#Declaración de variables

nombre = "Ivan Arturo Diaz Rosso"
telefono = "3187524030"
correo = "ivandiaz94ing@gmail.com"

print(nombre)
print(telefono)
print(correo)

#Video 4 ***************************************************************
#TIPOS DE VARIABLES
x: int = 10.5
print(10)
print(type(x))
y: str = "Hola Mundo"
print(y)
print(type(y))

#Manejo de cadenas ******************************************************************************************************
#Concatenar cadena
miGrupoFavorito = "Don Omar"
print("Mi grupo favorito es: " + miGrupoFavorito)

miGrupoFavorito = "Don Omar"
comentario = "El rey del reguaetton"
print('Mi artista favorito es:', miGrupoFavorito, comentario)

numero1 = "1"
numero2 = "2"
print("Concatenacion", numero1 + numero2)
print("Suma:", int(numero1) + int(numero2))

#Tipos de datos Boleanos ****************************************************************************************
# Datos boolean

mivar = True
print(mivar)

mivar = 3 > 5
print(mivar)

if mivar:
 print('El resultado fue verdadero')
else: print("el resultado fue falso")


#La funcion input para procesar entrada del usuario *****************************************************
num1 = input("ingresar un numero: ")
num2 = input("ingresar un numero: ")

# Mi manejo de errores
try:
    print('La suma es:', int(num1) + int(num2))


except:
    [print('error al convertir los datos')]

# Califica tu día *************************************************************************

dia = int(input("Como estuvo tu dia (1 al 10) : "))
print("Mi dia estuvo de: ", dia)


#Se solicita incluir la siguiente informacion acerca de un libro***************************

titulo = input("Proporciona el titulo del libro: ")
autor = input("Escribe quien es el autor del libro: ")

print(titulo, "fue escrito por" , autor)