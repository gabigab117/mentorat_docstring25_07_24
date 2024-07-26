# itérable en argument
# any retourne True si au moins un élément de l'itérable est vrai

# all retourne True si tous les éléments sont vrais, Si un élément est faux False
# all retourne True pour un itérable vide

print(any([0, 0, 0, 1]))
print(all([0, 0, 0, 1]))
print(all([1, 1, 1, 1]))
print(all(["", None, "salut", 1]))
print(any(["", None, "salut", 0]))
