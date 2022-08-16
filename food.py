

# instancier une classe Food disposant des propriétés suivantes:
#   . name
#   . calories
#   . fat (lipides)
#   . carbs (glucides)
#   . protein (protéines)

class Food :
    """ classe food"""
     # propriétés (variables définies dans une classe)
    name = ''
    calories = ''
    fat = ''
    carb = ''
    protein = ''


    # méthodes (fonctions définies dans une classe)
    def __init__(self, name, calories, fat, carb, protein):
        """ def init"""
        
        self.name = name
        self.calories = calories
        self.fat = fat
        self.carb = carb
        self.protein = protein

    # accesseurs (getters)

    def get_name(self):
        """ get_name"""
        return self.name

    def get_calories(self):
        """ get_calories"""
        return self.calories

    def get_fat(self):
        """ get_fat"""
        return self.fat

    def get_carb(self):
        """ get_carb"""
        return self.fat

    def get_protein(self):
        """ get_protein"""
        return self.protein

    # mutateurs (setters)
    
    def set_name(self, name):
        """ set_name"""
        self.name = name

    def set_calories(self, calories):
        """ set_calories"""
        self.calories = calories

    def set_fat(self, fat ):
        """ set_fat"""
        self.fat = fat

    # def set_carb(self, carb):
    #     """ set_carb"""
    #     self.carb = carb


    


