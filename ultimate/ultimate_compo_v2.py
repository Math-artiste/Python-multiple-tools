import random 

team_leader_h = ["Adam", "Lyrian"]
team_leader_f = ["Fanny", "Méline"]
useful = ["Tymothé", "Radouane", "Mathis"]
Handler = ["Mathias", "Yanis", "Raphaël", "Adam", "Lyrian", "Fanny" ,"Méline"]
others = ["Isaac", "Noa"]
table_1 = [5,10,15,20,25,30]
table_2 = [2,4,6,8,10,12,14,16,18,20]


def selectRandom(x):
  return random.choice(x)


print("Logicielle de crétion d'équipe d'ultimate !")
print("...........................................")

team = input("Voulez-vous voir les catégories ? (oui ou non) ")
exec = "oui"

if team == "oui" :
    print(team_leader_h, "Leader d'équipe masculins, nom de ce groupe : team_leader_h")
    print(team_leader_f, "Leader d'équipe féminines, nom de ce groupe : team_leader_f")
    print(useful, "Défenseurs/attaquants utile, nom de ce groupe : useful ")
    print(Handler, "Lanceurs, nom de ce groupe : Handler")
    print(others, "Les autres, nom de ce groupe : others")
    print()
    modif = input("Voulez-vous modifier une des listes ci dessus ? (oui ou non) ")
    print("................................................................")
    
    reset = "oui"
    
    if modif == "oui" : 
    

        while reset == "oui" :
            What = input("Que voulez-vous faire ? (effacer/ajouter/rien) ")
            if What == "rien" :
                break


            if What == "ajouter" :
                which = input("Indiquer le nom de la liste que vous souhaitez modifier (merci d'être précis) : ")
                who = input("Qui voulez vous rajouter ? ")

                if which == "team_leader_h" :
                    team_leader_h.append(who)
                elif which == "team_leader_f" :
                    team_leader_f.append(who)
                elif which == "useful" :
                    useful.append(who)
                elif which == "Handler" :
                    Handler.append(who)
                elif which == "others" :
                    others.append(who)
                
            else :
                which = input("Indiquer le nom de la liste que vous souhaitez modifier (merci d'être précis) : ")
                who = input("Qui voulez vous enlever ? ")
            
                if which == "team_leader_h" :
                    team_leader_h.remove(who)
                elif which == "team_leader_f" :
                    team_leader_f.remove(who)
                elif which == "useful" :
                    useful.remove(who)
                elif which == "Handler" :
                    Handler.remove(who)
                elif which == "others" :
                    others.remove(who)
                
            reset = input("Voulez-vous visionner les nouvelles listes ? ")

            if reset == "oui" :
                print(team_leader_h, "Leader d'équipe masculins, nom de ce groupe : team_leader_h")
                print(team_leader_f, "Leader d'équipe féminines, nom de ce groupe : team_leader_f")
                print(useful, "Défenseurs/attaquants utile, nom de ce groupe : useful ")
                print(Handler, "Lanceurs, nom de ce groupe : Handler")
                print(others, "Les autres, nom de ce groupe : others")
        print(".......................................................................................................")

everybody = input("Y'a t'il tout les personnes cités dans les listes qui sont présentes ? (oui ou non) ")
    
if everybody == "non" :
    how_many = input("Quels sont le(s)/la personne(s) qui seront absente(s) ? (Nom propre) ")
    what = input("Quel était son rôle ? (mettre le nom de la variable) ")
    if which == "team_leader_h" :
        team_leader_h.remove(how_many)
    elif which == "team_leader_f" :
        team_leader_f.remove(how_many)
    elif which == "useful" :
        useful.remove(how_many)
    elif which == "Handler" :
        Handler.remove(how_many)
    elif which == "others" :
        others.remove(how_many)

while exec == "oui" :
    print("...........Début...........")
    print("...........................")

    group_1 = len(team_leader_h)
    group_2 = len(team_leader_f)
    group_3 = len(useful)
    group_4 = len(Handler)
    group_5 = len(others)
    result = group_1 + group_2 + group_3 + group_4 + group_5
    result = int(result)
    print("Il y a actuellemnt",result,"joueurs")
    
    number = int(input("Voulez vous une équipe de 5 ou de 6 ? (5 ou 6) "))
    number_1 = int(input("Combien voulez-vous d'équipes ? "))
   
    
    if number == 5 :
        for k in range(number_1) :
            if number_1 == 3 :
                mixte = team_leader_f + team_leader_h
                print("Les chefs d'équipes seront mixtes")
                print(".................................")
                print("Le chef d'équipe est : ", selectRandom(mixte))

                if selectRandom(Handler) == "Adam" :
                    try_1 = selectRandom(Handler)
                    print("Le lanceur est : ", try_1)
                elif selectRandom(Handler) == "Lyrian" :
                    try_2 = selectRandom(Handler)
                    print("Le lanceur est : ", try_2)
                else :
                    print("Le lanceur est : ", selectRandom(Handler))

                print("Les deux pivot sont : ", selectRandom(useful), end = " ")

                if random.choice(useful) == "Mathias" :
                    try_1 = selectRandom(useful)
                    print(try_1)
                elif random.choice(useful) == "Tymothé" :
                    try_2 = selectRandom(useful)
                    print( try_2)
                if random.choice(useful) == "Mathis" :
                    try_1 = selectRandom(useful)
                    print( try_1)
                elif random.choice(useful) == "Radouanne" :
                    try_2 = selectRandom(useful)
                    print( try_2)
                else :
                    print(selectRandom(useful))
                            
                print("Le bouche-trou est : ", selectRandom(others))
                print(".....................................")
            else :
                choice = input("Voulez-vous un ou une chef d'équipe ? (fille ou garçon) ")

                if choice == "fille" :
                    print("Le chef d'équipe est : ", selectRandom(team_leader_f))

                    if selectRandom(Handler) == "Fanny" :
                        try_1 = selectRandom(Handler)
                        print("Le lanceur est : ", try_1)
                    elif selectRandom(Handler) == "Méline" :
                        try_2 = selectRandom(Handler)
                        print("Le lanceur est : ", try_2)
                    else :
                        print("Le lanceur est : ", selectRandom(Handler))
                    
                    print("Les deux pivot sont : ", selectRandom(useful), end = " ")

                if random.choice(useful) == "Mathias" :
                    try_a = selectRandom(useful)
                    print(try_1)
                elif random.choice(useful) == "Tymothé" :
                    try_2 = selectRandom(useful)
                    print( try_2)
                if random.choice(useful) == "Mathis" :
                    try_1 = selectRandom(useful)
                    print( try_1)
                elif random.choice(useful) == "Radouanne" :
                    try_2 = selectRandom(useful)
                    print( try_2)
                else :
                    print(selectRandom(useful))
                            
                print("Le bouche-trou est : ", selectRandom(others))
                        
                if choice == "garçon" :
                    print("Le chef d'équipe est : ", selectRandom(team_leader_h))

                    if selectRandom(Handler) == "Adam" :
                        try_1 = selectRandom(Handler)
                        print("Le lanceur est : ", try_1)
                    elif selectRandom(Handler) == "Lyrian" :
                        try_2 = selectRandom(Handler)
                        print("Le lanceur est : ", try_2)
                    else :
                            print("Le lanceur est : ", selectRandom(Handler))
                    print("Les deux pivot sont : ", selectRandom(useful), end = " ")
                    print(selectRandom(useful))
                                
                    print("Le bouche-trou est : ", selectRandom(others))
                    print(".....................................")

                
    
    if number == 6 :

        for k in range(number_1) :

           if number_1 == 3 :
                mixte = team_leader_f + team_leader_h
                print("Les chefs d'équipes seront mixtes")
                print(".................................")
                print("Le chef d'équipe est : ", selectRandom(mixte))

                if selectRandom(Handler) == "Adam" :
                    try_1 = selectRandom(Handler)
                    print("Le lanceur est : ", try_1)
                elif selectRandom(Handler) == "Lyrian" :
                    try_2 = selectRandom(Handler)
                    print("Le lanceur est : ", try_2)
                if selectRandom(Handler) == "Fanny" :
                    try_1 = selectRandom(Handler)
                    print("Le lanceur est : ", try_1)
                elif selectRandom(Handler) == "Méline" :
                    try_2 = selectRandom(Handler)
                    print("Le lanceur est : ", try_2)
                else :
                    print("Le lanceur est : ", selectRandom(Handler))

                print("Les deux pivot sont : ", selectRandom(useful), end = " ")

                if random.choice(useful) == "Mathias" :
                    try_a = selectRandom(useful)
                    print(try_1)
                elif random.choice(useful) == "Tymothé" :
                    try_2 = selectRandom(useful)
                    print( try_2)
                if random.choice(useful) == "Mathis" :
                    try_1 = selectRandom(useful)
                    print( try_1)
                elif random.choice(useful) == "Radouanne" :
                    try_2 = selectRandom(useful)
                    print( try_2)
                else :
                    print(selectRandom(useful))
                            
                
                            
                print("Le bouche-trou est : ", selectRandom(others))
                print(".....................................")
        else :
                
            choice = input("Voulez-vous un ou une chef d'équipe ? (fille ou garçon) ")

            if choice == "fille" :
                print("Le chef d'équipe est : ", selectRandom(team_leader_f))

                if selectRandom(Handler) == "Fanny" :
                    try_1 = selectRandom(Handler)
                    print("Le lanceur est : ", try_1)
                elif selectRandom(Handler) == "Méline" :
                    try_2 = selectRandom(Handler)
                    print("Le lanceur est : ", try_2)
                else :
                    print("Le lanceur est : ", selectRandom(Handler))
                            
                print("Les deux pivot sont : ", selectRandom(useful), end = " ")

                if random.choice(useful) == "Mathias" :
                    try_a = selectRandom(useful)
                    print(try_1)
                elif random.choice(useful) == "Tymothé" :
                    try_2 = selectRandom(useful)
                    print( try_2)
                if random.choice(useful) == "Mathis" :
                    try_1 = selectRandom(useful)
                    print( try_1)
                elif random.choice(useful) == "Radouanne" :
                    try_2 = selectRandom(useful)
                    print( try_2)
                else :
                    print(selectRandom(useful))
                                
                
                print("Le bouche-trou est : ", selectRandom(others))
                        
                if choice == "garçon" :
                    print("Le chef d'équipe est : ", selectRandom(team_leader_h))

                    if selectRandom(Handler) == "Adam" :
                        try_1 = selectRandom(Handler)
                        print("Le lanceur est : ", try_1)
                    elif selectRandom(Handler) == "Lyrian" :
                        try_2 = selectRandom(Handler)
                        print("Le lanceur est : ", try_2)
                    else :
                        print("Le lanceur est : ", selectRandom(Handler))
                                
                    print("Les deux pivot sont : ", selectRandom(useful), end = " ")

                if random.choice(useful) == "Mathias" :
                    try_a = selectRandom(useful)
                    print(try_1)
                elif random.choice(useful) == "Tymothé" :
                    try_2 = selectRandom(useful)
                    print( try_2)
                if random.choice(useful) == "Mathis" :
                    try_1 = selectRandom(useful)
                    print( try_1)
                elif random.choice(useful) == "Radouanne" :
                    try_2 = selectRandom(useful)
                    print( try_2)
                else :
                    print(selectRandom(useful))
                                
                    
                    print("Le bouche-trou est : ", selectRandom(others))
                    print(".....................................")
    exec = input("Voulez-vous recommencer ? ")

if exec == "non" :
    print("Au revoir")