# https://aprendeconalf.es/docencia/python/ejercicios/listas-tuplas/

while True:
    ejercicio = input('Que ejercicio quieres probar? (Ingrese "?" para ver la lista de ejercicios o "0" para salir) :')
    # Opcion para salir
    if ejercicio == "0":
        print("Gracias, vuelva prontos!")
        break
        
        # Opcion de lista de ejercicios
    if ejercicio == "?":
        print("1) Asignaturas del curso")
        print("2) Mensaje personalizado")
        print("3) Notas por asignatura")
        print("4) Lotería primitiva")
        print("5) Orden inverso")
        print("6) Asignaturas reprobadas")
        print("7) Abecedario filtrado")
        print("8) Palíndromos")
        print("9) Frecuencias de vocales")
        print("10) Precios mínimos y máximos")
        print("11) Producto escalar")
        print("12) Multiplicación de matrices")
        print("13) Media y desviación estándar")
        
#Ejercicio 1
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
    elif ejercicio == "1":
        asignaturas = input("Ingrese sus asignaturas sin espacios, por ejemplo: manzana,pera,banana,naranja*").split(",")
        print(asignaturas)


#Ejercicio 2
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

    elif ejercicio == "2":
        asignaturas = input("Ingrese sus asignaturas: ").split(",")
        for asignatura in asignaturas:
            print(f"Yo estudio {asignatura}")
           

#Ejercicio 3
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

    elif ejercicio == "3":
        asignaturas = input("Ingrese sus asignaturas: ").split(",")
        notas = input("Ingrese su nota: ").split(",")
        #validamos que se ingrese la misma cantidad de asignaturas y notas
        if len(asignaturas) != len(notas):
            print("Error: el número de sus asignaturas y notas no coinciden.")
        else:
            for i in range(len(asignaturas)):
            # .strip() se utiliza para eliminar los espacios en blanco y caracteres especificos al inicio y final de una cadena.
                print(f"En {asignaturas[i].strip()} has sacado: {notas[i].strip()}") 
            

#Ejercicio 4
#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
    elif ejercicio == "4":
        numeros = input("Ingrese los números ganadores de la lotería primitiva").split()
        numeros.sort()
        print(numeros)
    



#Ejercicio 5
#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

#Ejercicio 6
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

#Ejercicio 7
#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

#Ejercicio 8
#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

#Ejercicio 9
#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

#Ejercicio 10
#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

#Ejercicio 11
#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

#Ejercicio 12
#Escribir un programa que almacene las matrices:
#     (1 2 3)       (-1 0)
#A =  (4 5 6) y B = ( 0 1)
#                   ( 1 1)
#en una lista y muestre por pantalla su producto.
#Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.

#Ejercicio 13
#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.


    else:            
        print("La opcion ingresa es incorrecta o no esta disponible, intente nuevamente...")