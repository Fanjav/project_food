"""check_calories_food.py
Cette application python permet la collecte des données nutritionnelles
obtenues depuis une source Internet publique.
Source: https://www.infocalories.fr/
Projet réalisé par Phuc PHAM NGOC et Fanjavola RAHANTAHARIMANANA
"""
import argparse
from bs4 import BeautifulSoup
import requests
from food import Food

URL_PREFIX = "https://www.infocalories.fr/calories/calories-"

def extract_data_from_html(html_page) -> dict:
    """extract data from html page"""
    soup = BeautifulSoup(html_page, 'html.parser')
    try:
        div_block = soup.find("div", attrs={'id': 'diva'})
        b_block = div_block.find_all("b")
        values = []
        for val in b_block:
            val = str(val).strip("<b></b>") # pylint: disable=bad-str-strip-call
            if "g" in val:
                val = val.strip("g").replace(',','.')
            if " Kcal" in val:
                val = val.strip(" Kcal").replace(',','.')
            values.append(val)
        # On retourne les valeurs extraites sous forme d'un dictionnaire Python
        food_dict = {'calories':values[0], 'protein':values[1], 'carbs': values[2], 'fat':values[3]}
        return food_dict
    except: # pylint: disable=bare-except
        print("[-] Extraction error")
        return -1

def check_food_page(food_name: str) -> str:
    """check calories food"""
    req_food = requests.get(f"{URL_PREFIX}{food_name}.php")
    if req_food.status_code == 404:
        # si return code 404 de la requete GET
        raise ValueError("Food not found in database")
    return req_food.text

def main():
    """main program"""
    parser = argparse.ArgumentParser("Vérifier les infos nutritionnelles d'un aliment")
    # les paramètres -f et -l doivent s'exclure mutuellement
    group = parser.add_mutually_exclusive_group(required=True)
    # nargs='*' permet de prendre en compte plusieurs string pour un seul argument sous form list
    group.add_argument('-f', '--foodname', dest="foodname", nargs='*',
        help="Nom de l'aliment à vérifier")
    group.add_argument('-l', '--foods_file', dest="foods_file",
        help="Fichier contenant la liste de plusieurs aliments à vérifier (Optionnel)")
    args = parser.parse_args()

    try:
        if args.foodname:
            # cas de Fruit de la passion
            if len(args.foodname) > 1:
                food_alias = '-'.join(args.foodname).casefold()
            # cas général: nom en un seul string
            else:
                food_alias = args.foodname[0].casefold()
        food_name = food_alias.replace('-',' ')
        page_html = check_food_page(food_alias)
        food_dict = extract_data_from_html(page_html)
    except ValueError:
        print(f"[-] Aliment {food_name} n'est pas trouvé dans notre base de données")
        exit(2) # pylint: disable=consider-using-sys-exit

    try:
        food_object = Food(food_name)
        food_object.set_calories(int(food_dict["calories"]))
        food_object.set_protein(float(food_dict["protein"]))
        food_object.set_carbs(float(food_dict["carbs"]))
        food_object.set_fat(float(food_dict["fat"]))
        food_object.show_calories_full()
        food_object.save_to_csv()
    except:  # pylint: disable=bare-except
        print("[-] Erreur générique")
        exit(3) # pylint: disable=consider-using-sys-exit

main()
