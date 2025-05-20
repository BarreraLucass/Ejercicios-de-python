""" Ejercicio 1
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla."""
clave = input("Que ejercicio queres probar?")
materias = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
if clave == "1":
    print(materias)
#####################################
#Ejercicio 2
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
elif clave == "2":
    for materia in materias:
        print("Yo estudio ", materia)
######################################
#Ejercicio 3
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
elif clave == "3":
    notas = []
    for materia in materias:
        nota = input("¿Que nota sacaste en " + materia + "?")
        notas.append(nota)
    for i in range(len(materias)):
        print("En ", materias[i], " sacaste ", notas[i])
#Ejercicio 4
#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
elif clave == "4":
    num_ganadores = []
    ganadores = int(input("Ingrese los números ganadores: "))
    for i in range(ganadores):
        numero = int(input(f"Ingrese el numero ganador {i+1}: "))
        num_ganadores.append(numero)
    num_ganadores.sort()
    print("Los números ganadores ordenados son: ", num_ganadores)
#Ejercicio 5
#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
elif clave == "5":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numeros.reverse()
    for numero in numeros:
        print(numero, end = ", ")
#Ejercicio 6
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
elif clave == "6":
    notas = []
    for materia in materias:
        nota = int(input(f"Que nota sacaste en {materia}?."))
        notas.append(nota)
    recursar = []
    for i in range(len(materias)):
        if notas[i] < 6:
            recursar.append(materias[i])
    print("las materias que debes recursar son:", ", ".join(recursar))
