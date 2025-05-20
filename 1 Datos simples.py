# https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/
while True:
    ejercicio = input('Que ejercicio quieres probar?(Ingrese "?" para ver la lista o "0" para salir)')
    if ejercicio == "0":
        print("¡Gracias, vuelva prontos!")
        break

    elif ejercicio == "?":
        print("Ejercicios disponibles actualmente:")
        print("1) Hola mundo")
        print("2) Mostrar variable")
        print("3) Saludar con nombre")
        print("4) Operación aritmética")
        print("5) Pagas por horas trabajadas")
        print("6) Suma de enteros")
        print("7) Indice de masa corporal")
        print("8) Division con cociente y resto")
        print("9) Inversion con intereses")
        print("10) Peso de paquete de juguetes")
        print("11) Cuenta de ahorros")
        print("12) Panadería con descuento")
        print("0) Salir")

    
#Ejercicio 1
#Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.


    elif ejercicio == "1":
        print("¡Hola Mundo!.")


#Ejercicio 2
#Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

    elif ejercicio == "2":
        saludo = "¡Hola Mundo!."
        print(saludo)


#Ejercicio 3
#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

    elif ejercicio == "3":
        name = input("Introduzca su nombre: ")
        print(f"¡Hola {name}!")


#Ejercicio 4
#Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética 
#((3 + 2) / (2 * 5))^2

    elif ejercicio == "4":
        print(((3 + 2) / (2 * 5))**2)


#Ejercicio 5
#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

    elif ejercicio == "5":
        horas = int(input("Cuantas horas trabajaste?: "))
        coste = int(input("Cuanto pagan por hora?: $"))
        print("Tu pago correspondiente es de: $", horas * coste)


#Ejercicio 6
#Escribir un programa que lea un entero positivo, n, introducido por el usuario y 
# después muestre en pantalla la suma de todos los enteros desde 1 hasta n
# La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma: suma = (n * (n + 1)) / 2

    elif ejercicio == "6":
        n = int(input("Ingrese un número:"))
        print(int((n * (n + 1)) / 2))


#Ejercicio 7
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase donde es el índice de masa corporal calculado redondeado con dos decimales.Tu índice de masa corporal es <imc><imc>

    elif ejercicio == "7":
        kg = float(input("Ingrese su peso en kg: "))
        altura = float(input("Ingrese su altura en cm: ")) /100
        mc = kg / (altura ** 2)
        print("Su masa corporal es de: ", round(mc, 2)) #round() se usa para redondear numeros a un numero especifico de decimales -> round(numero, decimales (opcional)) -->
        #print(round(5.76543, 2))   Redondea a 2 decimales → 5.77 
        #print(round(5.76543))      Redondea al entero más cercano → 6
        #print(round(5.5))          Redondea al entero más cercano → 6
        #print(round(5.4))          Redondea al entero más cercano → 5

#Ejercicio 8
#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

    elif ejercicio == "8":
        n = int(input("Ingrese el primer número entero: "))
        m = int(input("Ingrese el segundo número entero: "))
        c = n // m  #con // se obtiene el cociente # 10 / 3 = 3
        r = n % m   #con % se obtiene el resto     # 10 % 3 = 1
        print(n, "entre", m, "da un cociente de", c, ("y un resto de"), r)


#Ejercicio 9
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

    elif ejercicio == "9":
        while True:
            opc = input("Ingrese que tipo de inversion quiere hacer: 1 para normal o 2 para compuesta (lo generado tras cumplir el año se vuelve a reinvertir) o 0 para salir al menu anterior: ")
            if opc == "0":
                break
            #validamos que el usuario ingrese bien los datos en caso de que haya puesto "3" sin querer no tenga que estar haciendo todo el proceso para salir o reintentar
            if opc not in ["1","2"]:
                print('la opcion es incorrecta, Ingrese "1" o "2"')
                continue # Si no agrego continue los inputs seguirian funcionando
            try:
                capital_inicial = float(input("Ingrese cantidad a invertir: $"))
                interes = float(input("Ingrese el interes anual en decimal (por ejemplo 0.05 para 5%): "))
                anios = int(input("Ingrese la cantidad de años:"))
                if opc == "1":
                    capital_final = capital_inicial + (capital_inicial * interes * anios)
                else:
                    capital_final = capital_inicial * (1 + interes) ** anios

                print(f"El capital obtenido de la inversion es de: ${capital_final:.2f}")
            except: 
                    print("La opcion elegida es incorrecta")


#Ejercicio 10
#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

    elif ejercicio == "10":
        payasos = int(input("Ingrese la cantidad de payasos vendidos:"))
        muniecas = int(input("Ingrese la cantidad de muñecas vendidas:"))
    #calcular precios
        peso_gm = (payasos * 112) + (muniecas * 75)
        peso_kg = peso_gm / 1000
    #preguntar si quiere precio del envio 
        seguir = input("Desea calcular la cantidad a pagar por el peso del paquete?: (y/n)")
        if seguir == "y":
            precio_por_kg = float(input("Ingrese el valor del peso: $"))
            total_pago = round(precio_por_kg * peso_kg, 2)
            if peso_kg < 1:
                print("El peso total es de: ", peso_gm, " gm y el precio a pagar es de: $", total_pago)
            else:
                print("El peso total es de: ", peso_kg, " kg y el precio a pagar es de: $", total_pago)
        elif seguir == "n":
            print("El peso total es de: ", peso_gm, " gm")
        else:
            print("La opcion elegida es incorrecta")

#Ejercicio 11
#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

    elif ejercicio == "11":
        monto_inicial = float(input("Ingrese el monto inicial: $"))
        for i in range (1, 4):
            monto_final = monto_inicial * (1 + 0.04) ** i
            print(f"El monto del anio {i} es de: ${monto_final:.2f}") #importante usar f-strings
#formato de impresión en Python que se usa para mostrar números flotantes con dos decimales,
#Formato           Descripción	                          Ejemplo
#:.2f	           Número con 2 decimales	              3.14159 → 3.14
#:.1f	           Número con 1 decimal	                  9.876 → 9.9
#:.0f	           Número sin decimales (redondeado)	  5.999 → 6
#:.2%	           Porcentaje con 2 decimales	          0.1234 → 12.34%
#:08.2f	           Número con ceros a la izquierda        45.6 → 00045.60
#:+.2f	           Siempre mostrar signo + o -	          5.2 → +5.20


#Ejercicio 12
#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

    elif ejercicio == "12":
        pan_de_ayer = int(input('Cuantas barras de pan "no frescas" se vendieron?: '))
        pan = 3.49
        pan_descuento = pan * 0.40
        print(f"El precio del pan es de: ${pan:.2f}")
        print(f"El descuento del pan de ayer es de: ${pan_descuento:.2f}")
        print(f"El coste final es de: ${pan_de_ayer * pan_descuento:.2}")
    
    else:
        print("El valor ingresado no es valido, intente nuevamente...")