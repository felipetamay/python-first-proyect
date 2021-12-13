# Para ingreso inicial del correo
def ingrese():
    print("")
    print("Ingrese su correo electronico")
    correo = input("_____: ")
    return correo


# mensaje en ciclo repetitivo cuando el correo es incorrecto
def mens_corre_rep():
    print("No se a encontrado esa cuenta de correo")
    print("    \033[41m Ingrese su correo nuevamente\033[0m")
    print("")



# mensaje en ciclo repetitivo cuando la contraseña es incorrecta
def mens_contra_rep():
    print("Contraseña incorrecta intenete nuevamente")
    print("   \033[41m Ingrese su contraseña nuevamnete\033[0m")
    print("")



# siclo para validar correo y verificar que no este vacio.
def correo_val(correo):
    correo_valido = "usermaster@gmail.com"

    if not correo:
        print("       La entrada es vacia")

    while correo != correo_valido:
        mens_corre_rep()
        correo = input("_____:")
        if not correo:
            print("       La entrada es vacia")
    print("")
    print("     \033[44m CORREO VERIFICADO\033[0m")



#siclo validar contraseña y verificar que no este vacia.
def contraseña_val():
    contraseñavalida = "8hla907"

    print("Ingrese su contraseña")
    contraseña = input("_____:")
    if contar_contraseña(contraseña) < 8:
        print("***La contraseña tiene menos de 8 caracteres***")


    if not contraseña:
        print("          La entrada es vacia")

    while contraseña != contraseñavalida:

        mens_contra_rep()
        contraseña = input("_____:")
        if contar_contraseña(contraseña) < 8:
            print("***La contraseña tiene menos de 8 caracteres***")

        if not contraseña:
            print("          La entrada es vacia")




def contar_contraseña(contraseña):
    contar=0

    for i in contraseña:
        if i:
            contar+=1
    return contar
