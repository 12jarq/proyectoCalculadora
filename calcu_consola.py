#Jose Antonio Rojas Quispe
sw = True
def sumar(num1, num2):
    s = num1 + num2
    print('la suma es: ', s)

def restar(num1, num2):
    s = num1 - num2
    print('la resta es: ', s)

def multiplicar(num1, num2):
    s = num1 * num2
    print('la multiplicacion es: ', s)

def dividir(num1, num2):
    try:
        s = num1 / num2
        print('la division es: ', s)
    except ZeroDivisionError:
        print("la division entre 0 no esta permitida ")

def opcion_no_disponible():
    print('Opcion no disponible')


def terminar_programa():
    print('Fin del programa')
    global sw
    sw = False


menu = '''
======= Calculadora ======
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir
'''
while sw:
    print(menu)
    opcion = int(input('Ingrese la opcion: '))
    if opcion != 5:
        n1 = int(input('Ingrese un numero: '))
        n2 = int(input('Ingrese otro numero: '))
        if opcion == 1:
            sumar(n1, n2)
        elif opcion == 2:
            restar(n1, n2)
        elif opcion == 3:
            multiplicar(n1, n2)
        elif opcion == 4:
            dividir(n1, n2)
        else:
            opcion_no_disponible()
    else:
        terminar_programa()
