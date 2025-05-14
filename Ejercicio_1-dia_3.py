Biblioteca = {
    1 : {'ID': 1,'Titulo': 'Cien años de soledad', 'Autor': 'Gabriel García Márquez', 'Año': 1967},
    2 : {'ID': 2,'Titulo': '1984', 'Autor': 'George Orwell', 'Año': 1949},
    3: {'ID': 3,'Titulo': 'Orgullo y prejuicio', 'Autor': 'Jane Austen', 'Año': 1813},
    4: {'ID': 4,'Titulo': 'Don Quijote de la Mancha', 'Autor': 'Miguel de Cervantes', 'Año': 1605},
    5: {'ID': 5,'Titulo': 'El nombre de la rosa', 'Autor': 'Umberto Eco', 'Año': 1980}
}

Id = 5

def Add():
    global Id
    while True:
        Id += 1
        while True:
            Titulo = input("\nIngrese un Titulo a agregar: ")
            if Titulo.replace(" ","").isalpha():
                data = any(Titulo.lower() == tite["Titulo"] for tite in Biblioteca.values())
                if not data:
                    break
                else:
                    print("\nYa esxiste")
            else: print("\nIngrese solo letras")
        while True:
            Autor = input("\nIngrese el autor del libro: ")
            if Autor.replace(" ", "").isalpha():
                break
            else:
                print("\nIngrese solo letras")
        while True:
            Year = input("\nIngrese el año del libro : ")
            if Year.isdigit():
                Year = int(Year)
                break
            else:
                print("Ingrese solo numeros")
        Data = {'ID' : Id, 'Titulo' : Titulo, 'Autor' : Autor, 'Año' : Year }
        Biblioteca[Id] = Data
        while True:
            try:
                opcion = int(input("\nDesea agregar otro libro? (1. Si ó 2. No): "))
                if opcion == 1:
                        print("\nLibro agregado")
                        break
                elif opcion == 2:
                        print("\nLibro agregado")
                        return
                else:
                        print("\nOpcion no valida")
            except ValueError:
                print("\nIngrese solo numeros ")
                
def Lista():
    print("\n----- Lista de libros -----")
    print(f"{Biblioteca}")
    
def Buscar():
    while True:
        print("\n----- Buscar libro -----")
        opcion = input("\nDesea buscar por: (1. Titulo ó 2. ID)?: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion == 1:
                titulo = input("\nIngrese un titulo a buscar: ")
                for Id, data in Biblioteca.items():
                    if data['Titulo'] == titulo:
                        print(Id, data)
                        return
                else:
                    print("\nNo se encuentra el titulo")
            elif opcion == 2:
                id = input("\nIngrese un ID a buscar: ")
                if id.isdigit():
                    id = int(id)
                    if id in Biblioteca:
                        print(Biblioteca[id])
                        return
                else:
                    print("\nNo se encuentra el Id")
            else:
                print("\nOpcion no valida")
        else:
            ("\nIngrese solo numeros")
            
def Actualizar():
    while True:
        id = input("\nIngrese el ID a actualizar: ")
        if id.isdigit():
            id = int(id)
            cambio = input("\nDesea cambiar (1. el autor ó 2. año de publicacion)?: ")
            if cambio.isdigit():
                cambio = int(cambio)
                if cambio == 1:
                    if id in Biblioteca:
                        ingre = input("\nIngrese el nuevo autor: ")
                        if ingre.isalpha():
                            Biblioteca[id]["Autor"] = ingre
                            print(Biblioteca[id])
                            break
                        else:
                            print("\nIngrese solo letras")
                elif cambio == 2:
                    if id in Biblioteca:
                        ingre = input("\nIngrese el nuevo año: ")
                        if ingre.isdigit():
                            Biblioteca[id]["Año"] = ingre
                            print(Biblioteca[id])
                            break
                        else:
                            print("\nIngrese solo numeros")
                else:
                    print("\nOpcion no valida")
            else:
                print("\nOpcion no valida")
        else:
            print("\nOpcion no valida")
            
def Eliminar():
    while True:
        id = input("\nIngrese el id a eliminar:")
        if id.isdigit():
            id = int(id)
            if id in Biblioteca:
                del (Biblioteca[id])
                print("\nEliminado correctamente")
                break
            else:
                print("\nId no encontrado")
        else:
            print("\nIngrese solo numeros")
                
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
            Lista()
        elif opcion == 3:
            Buscar()
        elif opcion == 4:
            Actualizar()
        elif opcion == 5:
            Eliminar()
        elif opcion == 6:
                print("\n---Gracias por visitarnos---")
                break
        else:
                print("\n###Error, Ingrese una opcion valida###")
                             
menu()
    
        



    
    
    
             
             
         



