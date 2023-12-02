from compteBancaire import CompteBancaire

def menu():
    print("1. Créer un compte")
    print("2. Déposer de l'argent")
    print("3. Retirer de l'argent")
    print("4. Consulter le solde")
    print("5. Demande de prêt")
    print("6. Quitter")
    choix = input("Veuillez choisir une option (1-6) : ")
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
            if nom in comptes:
                comptes[nom].deposer(montant)
            else:
                print(f"Compte pour {nom} non trouvé.")

        elif choix == "3":
            nom = input("Entrez le nom du titulaire du compte : ")
            montant = float(input("Entrez le montant à retirer : "))
            if nom in comptes:
                comptes[nom].retirer(montant)
            else:
                print(f"Compte pour {nom} non trouvé.")

        elif choix == "4":
            nom = input("Entrez le nom du titulaire du compte : ")
            if nom in comptes:
                comptes[nom].consulter_solde()
            else:
                print(f"Compte pour {nom} non trouvé.")

        elif choix == "5":
            nom = input("Entrez le nom du titulaire du compte : ")
            montant_pret = float(input("Entrez le montant du prêt : "))
            if nom in comptes:
                comptes[nom].demande_pret(montant_pret)
            else:
                print(f"Compte pour {nom} non trouvé.")

        elif choix == "6":
            print("Merci d'avoir utilisé notre application. Au revoir!")
            break

        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()