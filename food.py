""" instancier une classe Food disposant des propriétés suivantes:
   . name
   . calories
   . fat (lipides)
   . carbss (glucides)
   . protein (protéines)
   les valeurs associées à ces propriétés se feront sur une base de 100 grammes
**Projet réalisé par Phuc PHAM NGOC et Fanjavola RAHANTAHARIMANANA
"""

import os
import csv

TABLE_LINE = "-------------------------------------------------------------------------"
CSV_FILE = "foods_calories.csv"

class Food :
    """ classe food"""
     # propriétés (variables définies dans une classe)
    name = ''
    calories = 0
    fat = 0.0
    carbs = 0.0
    protein = 0.0

    # méthodes (fonctions définies dans une classe)
    def __init__(self, name) -> None:
        """Constructor for new food"""
        # Création d'une nouvelle instance avec un nom
        self.name = name

    # accesseurs (getters)
    def get_name(self) -> str:
        """ get_name"""
        return self.name

    def get_calories(self) -> int:
        """ get_calories"""
        return self.calories

    def get_fat(self) -> float:
        """ get_fat"""
        return self.fat

    def get_carbs(self) -> float:
        """ get_carbs"""
        return self.fat

    def get_protein(self) -> float:
        """ get_protein"""
        return self.protein

    # mutateurs (setters)
    def set_name(self, name: str):
        """ set_name"""
        self.name = name

    def set_calories(self, calories: int):
        """ set_calories"""
        self.calories = calories

    def set_fat(self, fat: float):
        """ set_fat"""
        self.fat = fat

    def set_carbs(self, carbs: float):
        """ set_carbs"""
        self.carbs = carbs

    def set_protein(self, protein: float):
        """ set_protein"""
        self.protein = protein

    def show_calories_full(self):
        """show all calories infos of the food in terminal"""
        # Pour utiliser ljust() il faut convertir les valeurs en str
        calories = str(self.calories)
        fat = str(self.fat)
        carbs = str(self.carbs)
        protein = str(self.protein)
        print(TABLE_LINE)
        print("name".ljust(30)+
            "calories(KCal)".ljust(15)+
            "fat".ljust(10)+
            "carbs".ljust(10)+
            "protein".ljust(10))
        print(self.name.ljust(30)+
            calories.ljust(15)+
            fat.ljust(10)+
            carbs.ljust(10)+
            protein.ljust(10))
        print(TABLE_LINE)

    def check_fat(self) -> bool:
        """check if the food is too fat or not"""
        is_fat = False
        if self.fat > 0.2:
            is_fat = True
        return is_fat

    def save_to_csv(self):
        """save calories food infos in the csv file"""
        header = ["'Name'", "'Calories(Kcal)'", "'Fat(g)'", "'Carbs(g)'", "'Protein(g)'"]
        row = [f"{self.name}", self.calories, self.fat, self.carbs, self.protein]
        if os.path.exists(CSV_FILE):
            # Cas où le fichier est déjà généré, on ajoute nouvelle ligne
            with open (CSV_FILE,'a',newline = '',encoding='UTF8') as csvfile:
                my_writer = csv.writer(csvfile, delimiter = ';')
                my_writer.writerow(row)
        else:
            # Cas où le fichier n'est pas encore créé
            with open (CSV_FILE,'w',newline = '',encoding='UTF8') as csvfile:
                my_writer = csv.writer(csvfile, delimiter = ';')
                my_writer.writerow(header)
                my_writer.writerow(row)
