class CompteBancaire:
    def __init__(self, nom, solde=0,taux_interet=0.18):
        self.nom = nom
        self.solde = solde
        self.taux_interet = taux_interet

    def deposer(self, montant):
        self.solde += montant
        print(f"{montant} ariary déposés. Nouveau solde : {self.solde} ariary")

    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant
            print(f"{montant} ariary retirés. Nouveau solde : {self.solde} ariary")
        else:
            print("Solde insuffisant.")

    def consulter_solde(self):
        print(f"Solde du compte {self.nom} : {self.solde} ariary")

    def demande_pret(self,montant_pret):
        self.montant_pret = self.montant_pret * self.taux_interet





def menu():
    print("1. Créer un compte")
    print("2. Déposer de l'argent")
    print("3. Retirer de l'argent")
    print("4. Consulter le solde")
    print("5. Quitter")
    choix = input("Veuillez choisir une option (1-5) : ")
    return choix



