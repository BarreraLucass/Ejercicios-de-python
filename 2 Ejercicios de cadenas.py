# https://aprendeconalf.es/docencia/python/ejercicios/cadenas/

while True:
    ejercicio = input('Que ejercicio quieres probar? (Ingrese "?" para ver la lista o "0" para salir) :')
    if ejercicio == "0":
        print("Gracias, vuelva prontos!")
        break
    elif ejercicio == "?":
        print("1) Repetir nombre n veces")
        print("2) Mostrar nombre en mayúsculas, minusculas e inicial con mayuscula")
        print("3) Contar la cantidad de letras del nombre")
        print("4) Extraer número de cel sin prefijo no extensión")
        print("5) Invertir una frase ingresada por el usuario")
        print("6) Reemplazar una vocal en la frase con mayúscula")
        print("7) Modificar el dominio de un correo electrónico")
        print("8) Separar el precio de un producto en euros y céntimos")
        print("9) Extrar día, mes y año de una fecha de nacimiento")
        print("10) Mostrar productos de una lista ingresada por el usuario")
        print("11) Fomatear el precio y unidades de un producto")


#Ejercicio 1
#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
    elif ejercicio == "1":
        name = input("Ingrese su numbre: ")
        repetir = int(input("Cuantas veces quiere repetir?: "))
        for i in range(repetir):
            print(name)


#Ejercicio 2
#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

    elif ejercicio == "2":
        nombre = input("Ingrese su nombre completo: ")
        print(nombre.lower())
        print(nombre.upper())
        print(nombre.title())

#Ejercicio 3
#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
    elif ejercicio == "3":
        nombre = input("Ingrese su nombre: ")
        longitud = nombre.split(" ")
        print(f"Su nombre: {nombre.upper()} tiene {len([letra for letra in nombre if letra != " "])} letras")


#Ejercicio 4
#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
    elif ejercicio == "4":
        numero = input("Ingrese el numero de telefono: ")
        partes = numero.split("-")
        print(f"El prefijo es: {partes[0]}, su numero es: {partes[1]} y su extension es: {partes[2]}")


#Ejercicio 5
#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
    elif ejercicio == "5":
        frase = input("Ingrese su frase: ")
        print(frase[::-1])


#Ejercicio 6
#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
    elif ejercicio == "6":
        frase = input("Introduzca su frase: ")
        vocal = input("Ingrese que vocal quiera en mayuscula: ")
        print(frase.replace(vocal, vocal.upper()))


#Ejercicio 7
#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
    elif ejercicio == "7":
        correo = input("Ingrese su correo: ")
        sin_dominio = correo.split("@")
        print(f"Su nuevo correo es: {sin_dominio[0]}@ceu.es")


#Ejercicio 8
#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
    elif ejercicio == "8":
        precio = input("Ingresa el valor del producto en euros con dos decimales: ")
        aux = precio.split(".")
        print(f"La cantidad de euros es de: ${aux[0]} y los centimos son {aux[1]}")


#Ejercicio 9
#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
    elif ejercicio == "9":
        nac = input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")
        if "/" in nac:
            fechas = nac.split("/")
            dia = fechas[0]
            mes = fechas[1]
            anio = fechas[2]
        else:
            dia = nac[:2]
            mes = nac[2:4]
            anio = nac[4:]
        print(f"Dia: {dia}, mes: {mes}, anio: {anio}")


#Ejercicio 10
#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
    elif ejercicio == "10":
        cesta = input("Ingrese los productos de su cesta (separados por comas): ")
        productos = [producto.strip() for producto in cesta.split(",")]  
        #.strip() elimina los espacios en blanco (o caracteres específicos) SOLO al inicio y al final de una cadena
        print("\n".join(productos))


#Ejercicio 11
#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
    elif ejercicio == "11":
        nombre = input("Ingrese el nombre del producto: ")
        precio_unitario = float(input("Ingrese el precio: "))
        unidades = int(input("Cuantos productos desea comprar?: "))
        coste_total = precio_unitario * unidades
        print(f"Producto {nombre}: ${precio_unitario:.2f}, {unidades}, total= ${coste_total:.2f}")
        #Formatear los numeros a devolver
        precio_unitario_str = f"{precio_unitario:08.2f}"  # :08 vendria representando el total de digitos "enteros" que devolvera y .2f el numero de "decimales"
        unidades_str = f"{unidades:03d}" # el 0 antes del 3 indica que debe rellenarse con 0
        coste_total_str = f"{coste_total:010.2f}"

        print(f"{nombre}: ${precio_unitario_str} unidades: {unidades_str}, coste total: ${coste_total_str}")
    
    else:
        print("La opcion ingresa es incorrecta o no esta disponible, intente nuevamente...")