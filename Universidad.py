i = 's'
estuAc = []
estuIn = []
cambio_estado = {}
while i.lower() == 's':
    print("Que desea realizar")
    menu = input("Digite: \n 1. Control de estudiantes \n 2. Control de becas de Estudiantes")

    if menu == '1':
        j = 's'
        while j.lower() == 's':
            print("Que desea realizar")
            submenu = input(
                "Digite: \n 1. Registro de un Estudiante \n 2. Listar estudiantes activos \n 3. cambiar estado de un "
                "estudiante")

            if submenu == '1':
                carne = input("Ingrese el numero de Carnet del estudiante que desee matricular: ")
                name = input("Ingrese el nombre del estudiante que desee matricular: ")
                carrera = input("Ingrese la carrera que el estudiante cursa: ")
                estado = input("Ingrese el estado del estudiante: (a/i)")
                anno = int(input("Digite el año de ingreso del estudiante"))
                lista = [carne, name, carrera, estado, anno]
                est = {}
                est[carne] = [name, carrera, estado, anno]
                print("El estudiante a registrar es: ", est)
                # if est[carne][2] == "a":
                estuAc.append(est)
                # if est[carne][2] == "i":
                #     estuIn.append(est)
                print(estuAc)

                # Submenu de impresion de datos
            if submenu == '2':
                for dic in estuAc:
                    for i in dic:
                        if dic[i][2] == "a":
                            print(dic)

            # SUBMENU DE CAMBIO DE ESTADO
            if submenu == '3':
                for dic2 in estuAc:
                    for i in dic2:
                        cambio_estado[i] = dic2

                carne_estado = input("Ingrese el numero de Carnet del estudiante que desee cambiar el estado")
                nuevo_estado = input("Ingrese el nuevo estado: ")
                
                #Test este metodo de conversion a minuscula
                carne_estado = carne_estado.lower()
                nuevo_estado = nuevo_estado.lower()
                #Manejo si el estudiante ya posee ese mismo estado
                if cambio_estado[carne_estado][carne_estado][2] == nuevo_estado:
                    print("No se puede cambiar el estado, ya que el estado deseado es que el ya "
                          "corresponde al estudiante")

                if cambio_estado[carne_estado][carne_estado][2] != nuevo_estado:


            j = input("Desea realizar otra tarea? S/N ")

    i = input("Desea continuar? S/N: ")
