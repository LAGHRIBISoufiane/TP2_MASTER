class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant
        else:
            print("Solde insuffisant.")

    def afficher_solde(self):
        print(f"Solde actuel: {self.solde} DH")

# Test
compte = CompteBancaire("LAGHRIBI Soufiane", 100)
compte.deposer(50)
compte.retirer(30)
compte.afficher_solde()
