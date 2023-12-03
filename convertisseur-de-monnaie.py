
from forex_python.converter import CurrencyRates

c = CurrencyRates()
3
montant = float(input("Entrez le montant à convertir : "))
devise_source = input("Entrez la devise source : ").upper()
devise_cible = input("Entrez la devise cible : ").upper()

taux_de_change = c.get_rate(devise_source, devise_cible)


valeur_convertie = montant * taux_de_change


print(f"{montant} {devise_source} équivaut à {valeur_convertie} {devise_cible} avec un taux de change de {taux_de_change}")

