# Écrivez une fonction nommée lists_sum qui prend en paramètre une liste de listes 
# d'entiers et renvoie la somme du nombre d'éléments dans chaque sous-liste.


def lists_sum(numbers_lists: list[list[int]]):
    number = 0
    for el in numbers_lists:
        number += len(el)
    return number


# Version élégante :)


def lists_sum2(numbers_lists: list[list[int]]):
    return sum(len(el) for el in numbers_lists)


ex1 = [[1, 2, 3], [4, 5, 7, 8], [1, 2, 7]]

print(lists_sum(ex1))
print(lists_sum2(ex1))
