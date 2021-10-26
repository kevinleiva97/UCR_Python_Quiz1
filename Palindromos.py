i = 's'
while i.lower() == 's':
    miCadenaDeTexto = input(
        "\n Digite una palabra, para saber si es palindroma: ")
    if str(miCadenaDeTexto) == str(miCadenaDeTexto)[::-1]:
        print("Es palindroma")
    else:
        print("No es palindroma")
    i = input("Desea probar otra palabra s/n: ")
