# Écrivez une fonction nommée 'matrix' qui prend en entrée une matrice de booléens (True/False).
# La fonction doit
# retourner une nouvelle liste de listes, où chaque sous-liste contient les indices des valeurs True
# dans la ligne correspondante de la matrice d'entrée.
# Par exemple, pour la matrice d'entrée :
# [[False, True, True], [True, False, False], [True, True, False]]
# La fonction devrait retourner :
# [[1, 2], [0], [0, 1]]


def matrix(m):
    result = []
    for element in m:
        sub_list = []
        for i, e in enumerate(element):
            if e:
                sub_list.append(i)
        result.append(sub_list)
    return result


ex = [[False, True], [False, False, False], [True, True, False, True]]
print(matrix(ex))
