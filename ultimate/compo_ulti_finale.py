import random

def letter_range(start, stop="{", step=1):
    """Yield a range of lowercase letters.""" 
    for ord_ in range(ord(start.upper()), ord(stop.upper()), step):
        yield chr(ord_)

print("Logicielle de crétion d'équipe d'ultimate !")
print("...........................................")

TEAMS = ()  # Replaced mutable list with immutable tuple.

                    # Names of constants should be in all-caps.
PLAYERS = ()

PLAYERS_2 = ()

CLUB = ['Adam', 'Lyrian', 'Fanny', 'Méline', 'Tymothé',
           'Elyes', 'Mathis', 'Mathias', 'Yanis', 
           'Isaac', 'Coralie']

AS = ['Adam', 'Lyrian', 'Fanny', 'Méline', 'Tymothé',
           'Shannah', 'Mathis', 'Mathias', 'Yanis', 
           'Isaac', 'Noa']

team = input("Voulez-vous voir les catégories ? (oui/non) ")
exec = "oui"

if team == "oui" :
    print(CLUB, "Joueurs dans la liste")
    print()
    modif = input("Voulez-vous modifier la listes ci dessus ? (oui/non) ")
    print("......................................................")
    
    reset = "oui"
    
    if modif == "oui" : 
    

        while reset == "oui" :
            What = input("Que voulez-vous faire ? (effacer/ajouter/rien) ")
            if What == "rien" :
                break


            if What == "ajouter" :
                who = input("Qui voulez vous rajouter ? ")
                CLUB.append(who)


                
            else :
                who = input("Qui voulez vous enlever ? ")
                CLUB.remove(who)

                
            reset = input("Voulez-vous visionner les nouvelles listes ? ")

            if reset == "oui" :
               print(CLUB, "Joueurs dans la liste")
        print(".......................................................................................................")

everybody = input("Y'a t'il tout les personnes cités dans les listes qui sont présentes ? (oui/non) ")
print(".......................................................................................")
    
if everybody == "non" :
        who = input("Citez la/les personnes absentes ? ")
        CLUB.remove(who)
else : 
    PLAYERS = (CLUB)
    PLAYERS_2 = (AS)


again = "oui"

while again == "oui" :
    number_of_team = input("Combien voulez-vous d'équipes ? (2= C / 3= D, etc....) ")
    TEAMS = list(letter_range("A", number_of_team))

    which = input("Voulez-vous une équipe pour l'as ou pour le club ? ")

    class TeamAssigner:
        def assign_players_to_teams(teams, players):
            players_on_teams = dict()
            randomized_players = random.sample(players, len(players))  # changed to .sample because .shuffle doesn't work on tuples / immutable sequences
            for i, team in enumerate(teams):
                players_on_teams[team] = randomized_players[i::len(teams)]
            return players_on_teams

    if which == "club" :
        my_teams = TeamAssigner.assign_players_to_teams(TEAMS, PLAYERS)
        for team, name in my_teams.items():
            print(team, name)
            print(".......................................")
    else :
        my_teams = TeamAssigner.assign_players_to_teams(TEAMS, PLAYERS_2)
        for team, name in my_teams.items():
            print(team, name)
            print(".......................................")
    again = input("Voulez-vous recommencer ? (oui/non) ")

if again == "non" :
    print("Au revoir")