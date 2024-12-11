class Chien:
    def __init__(self, nom, race, age):
        self.nom = nom
        self.race = race
        self.age = age

    def aboyer(self):
        print("Woof!")

# Test
mon_chien = Chien("Dolf", "Golden retriever", 5)
mon_chien.aboyer()
