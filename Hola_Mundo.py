# Escriba un programa que muestre " Hola Mundo".
#print("Hola Mundo")
# 1) Forma número 1 de hacerlo
#print("Hola Mundo")
# --------------------------------------------
# 2) Forma número 2.
#saludo = "Hola Mundo"
#print(saludo)
# --------------------------------------------
# 3) Forma de hacerlo concatenando
#saludo = " Hola Mundo"
#print("Tu primer programa es: " +  saludo)
# --------------------------------------------
# 4) El usuario ingresa el saludo para ejecutarlo
# para ello se utiliza el input para escribir datos
# desde el teclado.
saludo = input("Mi primer saludo: ")
print(saludo)
# y para concatenarlo.
print("El saludo que escribi es: " + saludo)
# --------------------------------------------
# Quieres utilizar la concatenación en formato.
nombre = input("Ingresa tu nombre: ")
# Utilizando está estructura podemos concatenar n cantidad de variables.
print(f"Tu nombre es: {nombre}")