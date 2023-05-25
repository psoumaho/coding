import random
 


def determine_gagnant(joueur, ordinateur):
    if joueur == ordinateur:
        return "Égalité"
    elif (joueur == "Pierre" and ordinateur == "Ciseaux") or (joueur == "Papier" and ordinateur == "Pierre") or (joueur == "Ciseaux" and ordinateur == "Papier"):
        return "Vous avez gagné !"
    else:
        return "L'ordinateur a gagné !"

def jouer():
    choix_possibles = ["Pierre", "Papier", "Ciseaux"]
    while True:
        joueur = input("Choisissez entre Pierre, Papier ou Ciseaux (ou tapez 'Q' pour quitter) : ").capitalize()
        if joueur == "Q":
            break
        if joueur not in choix_possibles:
            print("Choix invalide. Veuillez choisir entre Pierre, Papier ou Ciseaux.")
            continue

        ordinateur = random.choice(choix_possibles)
        print(f"Vous avez choisi {joueur}. L'ordinateur a choisi {ordinateur}.")
        resultat = determine_gagnant(joueur, ordinateur)
        print(resultat)


def jouer_devine_nombre():
    nombre_secret = random.randint(1, 100)
    nb_tentatives = 0

    print("Bienvenue ! Devinez le nombre secret entre 1 et 100.")
   

    while True:
  
        try:
            devine = int(input("Entrez votre estimation : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        nb_tentatives += 1

        if devine < nombre_secret:
            print("Le nombre secret est plus grand !")
        elif devine > nombre_secret:
            print("Le nombre secret est plus petit !")
        else:
            print(f"Félicitations ! Vous avez trouvé le nombre secret en {nb_tentatives} tentatives.")
            break

    print("Merci d'avoir joué !")

jouer_devine_nombre()
