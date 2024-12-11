class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.prenom} {self.nom}, j'ai {self.age} ans.")

class Etudiant(Personne):
    def __init__(self, nom, prenom, age, matricule):
        super().__init__(nom, prenom, age)
        self.matricule = matricule

    def etudier(self):
        print(f"L'étudiant {self.prenom} étudie.")

# Test
etudiant = Etudiant("LAGHRIBI", "Soufiane", 23, "AE298296")
etudiant.se_presenter()
etudiant.etudier()
