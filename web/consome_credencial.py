def exporta_credencial():
    
    path = "./venv/credencial.txt"

    lista = []

    with open (path, "r") as file:
        file1 = file.read()
        for linha in file1:
            lista.append(linha)
    return lista


