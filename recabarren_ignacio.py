import os
def menu():
    print("""
    BIENVENIDO A MASCOTA SEGURA
    menú 
    1.grabar
    2.buscar
    3.retirarse
    4.salir""")
while True:
    try:
            opcion =  int(input("indique el numero del menú"))
            if opcion in (1,2,3,4):
                break
            else:
                print("debes seleccionar un numero (1,2,3,4)")
    except: 
        print("debes seleccionar un numero (1,2,3,4)")
    if opcion==1:
        def validar_rut():
            while True:
                try:
                    rut = int(input("Ingrese RUT del dueño de la mascota sin puntos ni dígito verificador: "))
                    if rut >= 1000000 and rut <= 99999999:
                        return rut
                    else:
                        print("¡ERROR! ¡INGRESE UN RUT VÁLIDO!")
                except:
                    print("¡ERROR! ¡DEBE INGRESAR UN NÚMERO ENTERO!")
        def validar_nombre():
            while True:
                nombre = input("Ingrese nombre del dueño de la mascota: ")
                if len(nombre.strip()) >= 3 and nombre.isalpha() and not nombre.isspace():
                    return nombre
                else:
                    print("El Nombre ingresado es muy corto (minimo debe tener 3 letras) o contiene caracteres no validos!")
        def validar_nombre():
            while True:
                nombre = input("Ingrese nombre de la mascota: ")
                if len(nombre.strip()) >= 3 and nombre.isalpha() and not nombre.isspace():
                    return nombre
                else:
                    print("El Nombre ingresado es muy corto (minimo debe tener 3 letras) o contiene caracteres no validos!")
        def validar_mascota(min:int,max:int):
            while True:
                try:
                    dias_perm = int(input(f"Ingrese cantidad de dias que permanecerá su mascota (entre {min} y {max}): "))
                    if dias_perm >= min and dias_perm <= max:
                        return dias_perm
                    else:
                        print(f"¡ERROR! ¡DEBE INGRESAR UN NÚMERO ENTRE ({min}) HASTA ({max})!")
                except:
                    print("¡ERROR! ¡DEBE INGRESAR UN NÚMERO ENTERO!")
        def validar_fila(min:int,max:int):
            while True:
                try:
                    fila = int(input(f"Ingrese número de fila ({min},{max}):"))
                    if fila >= min and fila <= max:
                        return fila
                    else:
                        print("ERROR! FILA INCORRECTA")
                except:
                    print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO POSITIVO!")
        def validar_columna(min:int,max:int):
            while True:
                try:
                    columna = int(input(f"Ingrese número de columna ({min},{max}):"))
                    if columna >= min and columna <= max:
                        return columna
                    else:
                        print("ERROR! COLUMNA INCORRECTA")
                except:
                    print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO POSITIVO!")
    elif opcion == 2:
        pass
    elif opcion== 3:
        pass
    break