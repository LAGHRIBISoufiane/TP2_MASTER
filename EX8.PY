class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.amis = []

    def ajouter_ami(self, ami):
        self.amis.append(ami)

    def afficher_amis(self):
        print("Liste des amis:")
        for ami in self.amis:
            print(f"{ami.prenom} {ami.nom}")

# Test
personne = Personne("Noubir", "Walid", 20)
ami1 = Personne("Rouddasse", "Hossam", 22)
ami2 = Personne("Laghribi", "Soufiane", 23)
personne.ajouter_ami(ami1)
personne.ajouter_ami(ami2)
personne.afficher_amis()
