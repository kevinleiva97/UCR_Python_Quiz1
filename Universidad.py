i = 's'
estu = []
estuIn = []
cambio_estado = {}
carnets = '0'
becas = [] # estructura es: Becas['Carnet', 'Numero de beca', 'Porcentaje de beca']
becas1 = '0'
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
            # submeno de registro de estudiantes
            if submenu == '1':
                carne = input("Ingrese el numero de Carnet del estudiante que desee matricular: ")
                name = input("Ingrese el nombre del estudiante que desee matricular: ")
                carrera = input("Ingrese la carrera que el estudiante cursa: ")
                estado = input("Ingrese el estado del estudiante: (a/i)")
                anno = int(input("Digite el año de ingreso del estudiante"))
                lista = [carne, name, carrera, estado, anno]
                est = {}
                for carnet1 in estu:
                    carnets1 = carnet1.keys()
                    for i1 in carnets1:
                        carnets = i1
                if lista[0] == carnets:
                    print("No se puede agregar el estudiante, ya que este existe anteriormente en el sistema")
                if lista[0] != carnets:
                    est[carne] = [name, carrera, estado, anno]
                    print("El estudiante a registrar es: ", est)
                    estu.append(est)

                # Submenu de impresion de datos
            # SubMenu de listado de estudiantes activos
            if submenu == '2':
                for dic in estu:
                    for i in dic:
                        if dic[i][2] == "a":
                            print(dic)
            # SUBMENU DE CAMBIO DE ESTADO
            if submenu == '3':
                for dic2 in estu:
                    for i in dic2:
                        cambio_estado[i] = dic2

                carne_estado = input("Ingrese el numero de Carnet del estudiante que desee cambiar el estado")
                nuevo_estado = input("Ingrese el nuevo estado: ")

                # Test este metodo de conversion a minuscula
                carne_estado = carne_estado.lower()
                nuevo_estado = nuevo_estado.lower()
                # Manejo si el estudiante ya posee ese mismo estado
                if cambio_estado[carne_estado][carne_estado][2] == nuevo_estado:
                    print("No se puede cambiar el estado, ya que el estado deseado es que el ya "
                          "corresponde al estudiante")

                if cambio_estado[carne_estado][carne_estado][2] != nuevo_estado:
                    cambio_estado[carne_estado][carne_estado][2] = nuevo_estado
                    print("Se cambió satisfactoriamente el estado")
            j = input("Desea mantenerse en este menu S/N")
    if menu == '2':
        k = 's'
        while k == 's':
            print("Que desea realizar?: ")
            submenu_becas = input("Digite: \n 1. Registro de becas \n 2. Listar estudiantes becados")
            if submenu_becas == '1':
                carnet_estudiante = input("Digite el carnet del estudiante que desee Becar: ")
                num_beca = input("Digite el numero de beca correspondiente: ")
                desc = input("digite el descuento a aplicar: ")
                for carnet1 in estu:
                    carnets1 = carnet1.keys()
                    for i1 in carnets1:
                        carnets = i1
                    if carnet_estudiante != carnets:
                        print("El estudiante no existe, por favor registrelo")
                    if carnet_estudiante == carnets:
                        for becas2 in becas:
                            becas2 = becas.keys()
                            for i1 in becas2:
                                becas1 = i1
                        if becas1 == carnet_estudiante:
                            print("El estudiante ya posee una beca")
                            k = input("Desea continuar con el menu de becas? S/N")
                        if becas1 != carnet_estudiante:
                            becasDic = {carnet_estudiante:[num_beca, desc]}
                            becas.append(becasDic)
                            k = input("Desea continuar con el menu de becas? S/N")
            if submenu_becas == '2':
                for i in becas:
                    print("La lista de estudiantes becados es: ",i)
                    k = input("Desea continuar con el menu de becas? S/N")
    i = input("Desea continuar? S/N: ")
