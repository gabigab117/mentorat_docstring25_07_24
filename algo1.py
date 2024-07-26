# Dans cet exercice, vous allez travailler avec une liste de nombres et de chaînes de caractères. 
# Votre tâche est d’écrire une fonction find_number qui parcourt la liste et renvoie le premier 
# élément qui est une chaîne de caractères ainsi que sa position dans la liste.

# La fonction find_number prend en entrée une liste numbers_with_string qui contient des nombres et
#  des chaînes de caractères. Elle doit renvoyer un tuple contenant deux éléments : 
# l’indice du premier élément qui est une chaîne de caractères et la chaîne de caractères elle-même.

# Par exemple, si la liste est [1, 2, 3, 4, 5, 6, "fizz", 8, "buzz"], la fonction doit renvoyer (7, "fizz") 
# car “fizz” est la première chaîne de caractères dans la liste et elle se trouve à l’indice 7.

def find_number(numbers_with_string: list):
    for i, el in enumerate(numbers_with_string, 1):
        if isinstance(el, str):
            return i, el


ex1 = [1, 2, 3, 4, 5, 6, "fizz", 8, "buzz"]
ex2 = [1, 2, "buzz", 4, 5, 6]

print(find_number(ex1))
print(find_number(ex2))
