Agenda ={}
Id = 0
def Add():
    global Id
    while True:
        Id += 1
        while True:
            Nombre = input("\nIngrese un nombre: ")
            if Nombre.replace(" ", "").isalpha():
                var = any(Nombre.lower() == nom["Nombre"] for nom in Agenda.values())
                if not var:
                    break
                else:
                    print("\nIngrese un nombre que no exista")
            else:
                print("\nIngrese solo letras")
            
        while True:
            Telefono = input("\nIngrese un Telefono: ")
            if Telefono.isdigit():
                Telefono = int(Telefono)
                break
            else:
                print("\nIngrese solo numeros")
        while True:
            Email = input("\nIngrese un email: ")
            if Email.isalpha():
                break
            else:
                print("\nIngrese solo letras")
        data = {"Nombre" : Nombre, "Telefono" : Telefono, "Email" : Email}
        Agenda[Id] = data
        while True:
            opcion = input("\nDesea ingresar otro contacto? (1. si ó 2. no): ")
            if opcion.isdigit():
                opcion = int(opcion)
                if opcion == 1:
                    print("\nAgregado correctamente")
                    break
                elif opcion == 2:
                    print("\nAgregado correctamente")
                    return
                else:
                    print("\nIngrese una opcion valida")
            else:
                print("\nAgregue solo numeros")
                
def lista():
    print(f"\nLista: {Agenda}")
    
def buscar():
    while True:
        nom = input("\nIngrese un nombre a buscar: ")
        if nom.isalpha():
            for Id, data in Agenda.items():
                if data["Nombre"] == nom:
                    print(Id, data)
                    return
            else:
                print("\nUsuario no encontrado")
        else:
            print("\nIngrese solo letras")
            
def actualizar():
    while True:
        nom = input("\nIngrese un nombre a buscar: ")
        if nom.isalpha():
            opcion = input("\nQue desea actualizar? (1. Telefono ó 2. Email): ")
            if opcion.isdigit():
                opcion = int(opcion)
                if opcion == 1:
                    for Id, data in Agenda.items():
                        if data["Nombre"] == nom:
                            while True:
                                tel = input("\nIngrese el nuevo telefono: ")
                                if tel.isdigit():
                                    tel = int(tel)
                                    data["Telefono"] = tel
                                    print(Id, data)
                                    return
                                else:
                                    print("\nsolo ingrese numeros")
                    else:
                        print("\nUsuario no encontrado")
                elif opcion == 2:
                        for Id, data in Agenda.items():
                            if data["Nombre"] == nom:
                                while True:
                                    email = input("\nIngrese el nuevo email: ")
                                    if email.isalpha():
                                        data["Email"] = email
                                        print(Id, data)
                                        return
                                    else:
                                        print("\nsolo ingrese numeros")
                        else:
                            print("\nUsuario no encontrado")
                else:
                    print("\nOpcion no valida")
                        
            else:
                print("\nIngrese solo numeros")
            
def eliminar():
    while True:
        eli = input("\nIngrese un nombre a eliminar:")
        if eli.isalpha():
            for Id, data in Agenda.items():
                if data["Nombre"] == eli:
                    del Agenda[Id]
                    return
            else:
                print("\nUsuario no encontrado")
        else:
            print("\nIngrese solo letras ")
                
def menu():
    
    while True:
    
        print("\n---Bienvenido a la biblioteca Riwi, elija una opcion---")
        print("1: Crear libro")
        print("2: Lista de libros")
        print("3: Buscar un libro")
        print("4: Modificar libros")
        print("5: Eliminacion de libros")
        print("6: Salir")
            
            
        opcion = int(input("\nIngrese una opcion: "))
                
        if opcion == 1:
            Add()
        elif opcion == 2:
            lista()
        elif opcion == 3:
            buscar()
        elif opcion == 4:
            actualizar()
        elif opcion == 5:
            eliminar()
        elif opcion == 6:
                print("\n---Gracias por visitarnos---")
                break
        else:
                print("\n###Error, Ingrese una opcion valida###")
                             
menu()