# Cuadrado 0.2

print("Bienvenido\n")

c = 0

while c < 100:
	num = int(input("Ingresa la base del cuadrado: "))
	num2 = int(input("ingresa la su altura: "))
	print("resultado: ", num*num2,"\nquieres volver a calcular?")
	resp = input()
	
	if resp == "si":
		c +=1
	else:
		break
