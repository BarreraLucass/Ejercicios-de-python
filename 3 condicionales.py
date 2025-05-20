# https://aprendeconalf.es/docencia/python/ejercicios/condicionales/

while True:
    ejercicio = input('Que ejercicio quieres probar? (Ingrese "?" para ver la lista o "0" para salir) :')
    if ejercicio == "0":
        print("Gracias, vuelva prontos!")
        break
    elif ejercicio == "?":
        print("1) Mayor de edad")
        print("2) Verificación de contraseña")
        print("3) Division segura")
        print("4) Par o impar")
        print("5) Tributacion")
        print("6) Asignacion de grupo")
        print("7) Impuesto sobre la renta")
        print("8) Evaluacion de empleados")
        print("9) Precio de entrada")
        print("10) Pizza personalizada")


#Ejercicio 1
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
    elif ejercicio == "1":
        edad = int(input("Ingrese su edad: "))
                                  #True if edad>17 else False
        print(f"Es mayor de edad?: {"Mayor de edad." if edad>17 else "Menor de edad."}")


#Ejercicio 2
#Escribir un programa que almacene la cadena de caracteres "contraseña" en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

    elif ejercicio == "2":
        contraseña_verificada = "contraseña"
        contraseña = input("Ingrese su contraseña: ")
        print(f"{"Ingreso exitoso." if contraseña==contraseña_verificada else "Contraseña incorrecta."}")
        

#Ejercicio 3
#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
    
    elif ejercicio == "3":
        num_1 = int(input("Ingrese el primer número: "))
        num_2 = int(input("Ingrese el segundo número: "))
        if num_2 == 0:
            print("Error, no se puede dividir algo por 0.")
        else:
            print(num_1 / num_2)

#Ejercicio 4
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
    elif ejercicio == "4":
        num = int(input("Ingrese un numero: "))
        print(f"El numero ingresado es: {"par" if num%2==0 else "impar"}")


#Ejercicio 5
#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
    elif ejercicio == "5":
        edad = int(input("Ingrese su edad: "))
        ingresos = int(input("Ingrese sus ingresos: $ "))
        if edad > 15 and ingresos > 999:
            print("Ustede debe tributar")
        else:
            print("Usted no debe tributar")



#Ejercicio 6
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
    elif ejercicio == "6":
        nombre = input("Ingrese su inicial: ").capitalize()
        sexo = input("Ingrese su sexo (M o F): ").capitalize()
        if (sexo == "F" and nombre < "M") or (sexo == "M" and nombre > "N"):
            print('Usted pertenece al grupo "A"')
        else:
            print('Usted pertenece al grupo "B"')     
        


#Ejercicio 7
#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

#Renta	                   Tipo impositivo
#Menos de 10000€	       5%
#Entre 10000€ y 20000€	   15%
#Entre 20000€ y 35000€	   20%
#Entre 35000€ y 60000€	   30%
#Más de 60000€	           45%

#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
    elif ejercicio =="7":
        renta = int(input("Ingrese su renta anual: $"))
        if renta < 10000:
            print("Su tipo de impositivo es de 5%")
        elif renta < 20000:
            print("Su tipo de impositivo es de 15%")
        elif renta < 35000:
            print("Su tipo de impositivo es de 20%")
        elif renta < 60000:
            print("Su tipo de impositivo es de 30%")
        else:
            print("Su tipo de impositivo es de: 45%")

#Ejercicio 8
#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

#Nivel	               Puntuación
#Inaceptable	       0.0
#Aceptable	           0.4
#Meritorio	           0.6 o más

#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

    elif ejercicio == "8":
        puntuacion = float(input("Ingrese su puntuación: "))
        if puntuacion == 0.0:
            print("Nivel de rendimiento: Inaceptable")
        elif puntuacion == 0.4:
            print(f"Nivel de rendimiento: aceptable \n Cantidad de dinero recibido: ${2400 * 0.4:.2f}")


#Ejercicio 9
#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.




#Ejercicio 10
#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.











    else:
        print("La opcion ingresa es incorrecta o no esta disponible, intente nuevamente...")