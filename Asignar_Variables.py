# algoritmo de asignacion de variables
# nombre, edad, direccion, DUI, dia, mes, sueldo, comision, verdadero o falso

nombre = "Lionel Andrés Messi"
edad = 33  
direccion = "Rosario, Argentina"
DUI = "06538266-1"
dia = "Martes"
mes = "Mayo"
Sueldo = 500.000
comision = 4.500
#Inicialiación
#Datos de la persona
print("-----------------")
print("Escriba su nombre: ",nombre)
print("Su edad es: ", edad,"años")
print("Su direccción es: ", direccion)
print("Su número de identidad es: ", DUI)
print("-----------------")

#Sueldo de la persona
print("-----------------")
deuda = 1000 + 300 + 200
gastos = 1000 + 200
Sueldo = 40000
salario = Sueldo - (deuda + gastos)
print("Ingrese el sueldo del mes: $",Sueldo," euros")
print("El total de deudas es de: $",deuda," euros")
print("El total de gastos es de: $",gastos," euros")
print("El sueldo del trabajador es de: $",salario," euros")
print("-----------------")

#Comisión de ZapatosAdidas_f50
print("-------------------------")
f_50 = 300
f_30 = 150
f_10 = 75

cantf_50 = int(input("ingrese la cantidad de zapatos tipo F_50 vendidos: "))
cantf_30 = int(input("ingrese la cantidad de zapatos tipo F_30 vendidos: "))
cantf_10 = int(input("ingrese la cantidad de zapatos tipo F_10 vendidos: "))

comision = cantf_50 * f_50 + cantf_30 * f_30 + cantf_10 * f_10

print("La comisión a pagar es: $", comision," euros")
print("-------------------------")

#Condición Verdadero o Falso
#Verdadero
print("-------------------------")
bool = 500.00 < 4000
print(bool)
print("-------------------------")

#Falso
print("-------------------------")
bool = 4000 > 400000
print(bool)
print("-------------------------")

print("Fin del Ejercicio 1")