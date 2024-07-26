# Modes d'ouverture de fichiers
with open("file.txt", "r") as f:  # "r" : lecture seule (par défaut)
# with open("file.txt", "w") as f:  # "w" : écriture (écrase le contenu existant)
# with open("file.txt", "a") as f:  # "a" : ajout à la fin du fichier
# with open("file.txt", "r+") as f:  # "r+" : lecture et écriture

    # Méthodes de lecture
    contenu = f.read()  # Lit tout le contenu du fichier en une seule chaîne
    # ligne = f.readline()  # Lit une seule ligne du fichier
    # lignes = f.readlines()  # Lit toutes les lignes et les retourne dans une liste

    print(contenu)


# Utilisation de readline()
with open("file.txt", "r") as f:
    ligne = f.readline()  # Lit une seule ligne du fichier
    print(ligne)  # Affiche la première ligne, y compris le caractère de nouvelle ligne

    # Lecture de toutes les lignes avec readline()
    while True:
        ligne = f.readline()
        if not ligne:  # Si ligne est vide, on a atteint la fin du fichier
            break
        print(ligne)


# Autre façon similaire à readline
with open("file.txt", "r") as f:
    for ligne in f:
        print(ligne)


# Avec readlines
with open("file.txt", "r") as f:
    contenu = f.readlines()
    print(contenu)


# Écriture dans un fichier avec "w" (écrase le contenu existant)
with open("file.txt", "w") as f:
    f.write("Première ligne\n")
    f.write("Deuxième ligne\n")
    # Écriture de plusieurs lignes à la fois
    lignes = ["Troisième ligne\n", "Quatrième ligne\n"]
    f.writelines(lignes)

# Ajout à un fichier avec "a" (ajoute à la fin du fichier)
with open("file.txt", "a") as f:
    f.write("Cinquième ligne (ajoutée)\n")
    f.write("Sixième ligne (ajoutée)\n")
    # Ajout de plusieurs lignes à la fois
    lignes = ["Septième ligne (ajoutée)\n", "Huitième ligne (ajoutée)\n"]
    f.writelines(lignes)
