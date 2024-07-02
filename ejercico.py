

def mayor_edad():
    edad=int(input("que edad tienes: "))

    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("No eres mayor de edad")

def Inicio_sesion():
    users_nom=str(input("Usuario: "))
    users_con=str(input("Contraseña: "))
    usuario_validar(users_nom,users_con)

def usuario_validar(users_nom,users_con):
    users=[["karol","1234"],["shaky","a4s1"]]
 
    
    for columna in range(len(users[0])):
        if users[columna][0]==users_nom:
            print("bienvenido ",users[columna][0])
            if users[columna][1]==users_con:
                print("Inicio seccion exitosa")
                input("press")
            else:
                print("contraseña incorrecta")
        elif len(users[0])==columna+1:
            print("inicio de seccion errada")

    

  

resp=10
while resp!=0:
    print("_________________")
    print("1.ejercicio 1")
    print("2.ejercicio 2")
    print("")
    print("0.salir")
    print("_________________")
    resp=int(input("Respu: "))


    if resp==1:
        mayor_edad()
    elif resp==2:
        Inicio_sesion()
    elif resp==0:
        print("se cerro el programa")
        input() 
    else:
        print("no existe esa alternativa")
