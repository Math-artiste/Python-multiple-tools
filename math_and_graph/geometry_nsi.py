# programme utilitaire de calcul de forme géométrique


"""
création d'une interface visuelle agréable
"""

end = "oui"

while end == "oui" or end == "o"  :
    print("Logiciele de calcul géomètrique")
    print("...............................")
    print("Quelle forme géométrique souhaitez-vous analysez ? ")
    print("-Tapez 1 pour un carrÃ© ")
    print("-Tapez 2 pour un rectangle")
    print("-Tapez 3 pour un cercle")
    choice = input()

    """
    création des questions nécessaires au variables pour la suite
    """

    if choice == "1" :
        square = float(input("Quelle est la longueur, en mètre, d'un côté du carré ? "))

    if choice == "2":
        longueur = float(input("Quelle est la longueur, en mètre, du grand côté du rectangle ? "))
        largeur = float(input("Quelle est la longueur, en mètre, du petit côté du rectangle ? "))

    if choice == "3" :
        circle = float(input("Quelle est la longueur, en mètre, du rayon du cercle ? "))
    
    """
    création des diffèrentes variables

    """

    if choice == "1" :
        perimeter_1 = square * 4
        area_1 = square * square
        area_1 = round(area_1, 2)
        perimeter_1 = round(perimeter_1, 2)
        print("Le périmètre du carré vaut : ", perimeter_1 , "m")
        print("L'aire du carré vaut : ", area_1, "m2")

    if choice == "2" :
        area_2 = longueur * largeur
        perimeter_2 = (longueur + largeur) * 2
        area_2 = round(area_2, 2)
        perimeter_2 = round(perimeter_2, 2)
        print("Le périmètre du rectangle vaut : ", perimeter_2, "m")
        print("L'aire du rectangle vaut : ", area_2, "m2")

    if choice == "3" :
        area_3 = circle * circle * 3.14
        perimeter_3 = 2 * 3.14 * circle
        area_3 = round(area_3, 2)
        perimeter_3 = round(perimeter_3, 2)
        print("Le périmètre du cercle vaut : ", perimeter_3, "m")
        print("L'aire du cercle vaut : ", area_3, "m2")

    end = input("Voulez vous continuer ? ")

"""
Fin de programme bienveillante
"""

if end == "non" or end == "n":
    print("Au revoir")
    
    