# Créer une fonction pour retourner une valeur d'un objet JSON
# https://www.docstring.fr/formations/exercices/179

# À l'aide de la bibliothèque standard, écrivez une fonction read_object qui lit un objet JSON contenu dans
# une chaîne de caractères et retourne la valeur associée à la clé donnée en 2e argument,
# sous la forme d'un objet Python.


import json


def read_object(json_str, k):
    data = json.loads(json_str)
    return data.get(k)


print(read_object('{"x" : [3, "A"], "a" : [1, 2, null]}', "a"))  # On a bien une chaine de caractères


# Rappel sur la manipulation de fichiers json
# Json
# La différence avec la fonction ci-dessus, c'est qu'ici on ouvre un fichier .json
def read_json_file(file, k):
    with open(file, "r") as f:
        data = json.load(f)
    return data.get(k)


print(read_json_file("data.json", "a"))  # fichier data.json