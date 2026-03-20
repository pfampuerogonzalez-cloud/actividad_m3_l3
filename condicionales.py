#1. DECISIÓN SIMPLE

edad_usuario = int(input("Ingresar edad: "))

if edad_usuario >18:
    print("Eres mayor de edad")

else:
    print("Eres menor de edad")




#2. DECISIÓN MÚLTIPLE CON ELIF

calificacion_alumno = float(input("Ingrese calificación de 1 a 7: "))

if calificacion_alumno == 7:
    print("Excelente")

elif calificacion_alumno == 6:
    print("Muy bien")

elif calificacion_alumno == 5:
    print ("Bien")
    
elif calificacion_alumno == 4:
    print("Suficiente")

else:
    print("Insuficiente")
 

#3.CONDICIONES ANIDADAS

numero_entero = int(input("Ingrese un número entero: "))

if numero_entero !=0:
    
    if numero_entero >0:
        print("Número positivo")

    else:
        print("Número negativo")
        
else:
    print("Es cero")



#4.CONDICIÓN DE BORDE

valor_rango = int(input("Ingresa un número entre 1 y 100: "))

if valor_rango == 1 or valor_rango ==100:
   print("Estás en un límite permitido")

elif 1< valor_rango <100:
    print ("Dentro del rango")

else:
    print("Fuera del rango")


