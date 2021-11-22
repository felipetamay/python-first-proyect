print("Aqui podrá evaluar cualquier numero entero y saber si es PAR o IMPAR ")
print()
numero=int(input("Ingrese el numero que el cual desea saber si es PAR o IMPAR: "))


if numero % 2 == 0:
    numero=str(numero)
    print("EL numero "+ numero+" es par ")
else:
    numero = str(numero)
    print("EL numero " + numero + " es impar")



