repetidos = []
agregar = " "
cartas = 0
aux = 0
aux2 = 0

while agregar == "si":
    x = int(input("Ingrese nuemros de cartas"))
    agregar = print ("¿Quiere seguir agregando?")
    cartas.append(x)


for i in cartas:
    aux = i
    aux2 = i=i+1
    
if aux == aux2:
    repetidos.append(aux2)
    print("Los numeros repetidos son: ", repetidos)
