class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_surface(self):
        return self.largeur * self.hauteur

    def calculer_perimetre(self):
        return 2 * (self.largeur + self.hauteur)

# Test
rectangle = Rectangle(10, 5)
print("Surface :", rectangle.calculer_surface())
print("Périmètre :", rectangle.calculer_perimetre())
