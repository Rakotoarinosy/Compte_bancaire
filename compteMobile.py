from compteBancaire import CompteBancaire

class CompteMobile(CompteBancaire):
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