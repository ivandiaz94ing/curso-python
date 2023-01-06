#Imprimir el numero mayor

num1 = int(input("Proporciona el numero1: "))
num2 = int(input("Proporciona el numero2: "))

if num1 > num2:
    print(f'El número mayor es: {num1}')
else:
    if num2 > num1:
        print(f'El número mayor es: {num2}')
    else:
        print(f'Los numeros son iguales')

