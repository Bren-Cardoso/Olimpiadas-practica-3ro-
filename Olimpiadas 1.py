import math

n = int(input("Ingrese la cantidad de litros en el tanque: "))
m = int(input("Ingrese la cantidad de kilómetros a recorrer: "))

consumo_por_km = 3 / 13  #Consumo por km recorrido
capacidad_tanque = 70.0

#Verificar si la cantidad de litros es válida
if (n <= 0 or n > capacidad_tanque):
    print("Cantidad de litros inválida")
    n = int(input("Ingrese la cantidad de litros en el tanque: "))


#Calcular cuántos km puede recorrer con los litros actuales
km_con_litros_actuales = (n / consumo_por_km)

#Verificar si puede llegar
if (km_con_litros_actuales >= m):
    print("Llego" )
 
else:
    #Calcular cuántos tanques completos necesita
    km_con_un_tanque_lleno = capacidad_tanque / consumo_por_km
    recargas_necesarias = (m - km_con_litros_actuales) / km_con_un_tanque_lleno;
    recargas_necesarias = recargas_necesarias + 1
    
    redondeo = math.floor(recargas_necesarias)
    
    print(redondeo)

#en 299 (casi 300) km se usan 69L (casi 70L)
#dividido por 23 (aprox)
#70L --> 300km                    