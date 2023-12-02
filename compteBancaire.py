class CompteBancaire:
    def __init__(self, nom, solde=0,taux_interet=0.18):
        self.nom = nom
        self.solde = solde
        self.taux_interet = taux_interet
        self.montant_pret = 0

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
        self.montant_pret = montant_pret * self.taux_interet
        print(f"Total de votre prét est: {self.montant_pret} ariary")








