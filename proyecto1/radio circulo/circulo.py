from math import pi
print("Aqui podra calcular el area de un circulo por su radio o diamentro")
radio_or_diametro = int(input("Ingrese una 1 si es radio o 2 si es radio:" ))
if radio_or_diametro==1:
    radio = int(input("Ingresa el radio del circulo:"))
    print("El area del circiulo  por medio del radio es:")
    area = pi * radio ** 2
    print(area)

if radio_or_diametro==2:
    diametro = int(input("Ingresa el diametro del circulo:"))
    print("El area del circiulo  por medio del diameatro es:")
    area =(1/4)* pi * diametro ** 2
    print(area)
