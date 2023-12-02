from compteBancaire import CompteBancaire

def menu():
    print("1. Créer un compte")
    print("2. Déposer de l'argent")
    print("3. Retirer de l'argent")
    print("4. Consulter le solde")
    print("5. demande de prêt")
    print("6. Quitter")
    choix = input("Veuillez choisir une option (1-5) : ")
    return choix

def main():
    comptes = {}

    while True:
        choix = menu()

        if choix == "1":
            nom = input("Entrez le nom du titulaire du compte : ")
            compte = CompteBancaire(nom)
            comptes[nom] = compte
            print(f"Compte créé pour {nom}.")

        elif choix == "2":
            nom = input("Entrez le nom du titulaire du compte : ")
            montant = float(input("Entrez le montant à déposer : "))
            comptes[nom].deposer(montant)

        elif choix == "3":
            nom = input("Entrez le nom du titulaire du compte : ")
            montant = float(input("Entrez le montant à retirer : "))
            comptes[nom].retirer(montant)

        elif choix == "4":
            nom = input("Entrez le nom du titulaire du compte : ")
            comptes[nom].consulter_solde()

        elif choix == "5":
            montant_pret = input("Taper votre montant de prêt : ")
            break
        
        elif choix == "6":
            print("Merci d'avoir utilisé notre application. Au revoir!")
            break

        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()