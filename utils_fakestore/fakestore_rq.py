import requests as rq

BASE_URL = 'https://fakestoreapi.com'

# Prend un dictionnaire correspondant au produit à mettre à jour.
# Le paramètre id est optionnel SI le produit passé en paramètre contient une clef id.
# On peut donc passé le produit au complet mis à jour ou seulement les valeurs à mettre à jour.

def mettre_produit_a_jour(produit:dict,id:int=None):
    if id == None:
        id = produit.get("id")
    response = rq.patch(f"{BASE_URL}/products/{id}",json=produit)
    return response.json()

new_list = []
liste = []
dictio = []
def liste_produits():

    reponse = rq.get(f"{BASE_URL}/products")
    liste = reponse.json()
    new_list = []
    for produits in liste:
        id = produits['id']
        titre = produits['title']
        prix =  produits['price']
        new_dictio = {"id": id,
                      "titre": titre,
                       "prix": prix }
        new_list.append(new_dictio)
        print(new_list)
liste_produits()

