def lista_inversa(lista):
    if not lista:
        return[]
    else:
        return lista_inversa(lista[1:]) + [lista[0]]

lista1 = [4, 505, 20, 109, 21, 94]
print(lista_inversa(lista1))