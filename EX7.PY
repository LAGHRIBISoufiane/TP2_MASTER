class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def afficher_livres(self):
        for livre in self.livres:
            print(f"Titre: {livre.titre}, Auteur: {livre.auteur}, Année: {livre.annee_publication}")

# Test
bibliotheque = Bibliotheque()
livre1 = Livre("Harry Potter and the Philosopher's Stone", "Joanne Rowling", 1997)
livre2 = Livre("The wheel of time", "Robert Jordan", 1990)
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.afficher_livres()
