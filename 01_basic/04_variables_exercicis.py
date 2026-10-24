###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.

nom= ""
ubicacio= ""
num_ports= 0
esta_ences= True
print(f"el nom del encaminador es: {nom} , la seva ubicacio es a {ubicacio}: te un numero de ports de {num_ports} : , i esta: {esta_ences} ")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.


GBpla=200
GBcons=100
GBrestants= GBpla-GBcons

print(f"aquests son els GB restants: {GBrestants}")
GBcons= 150
GBrestants= GBpla-GBcons
print(f"aquests son els GB restants: {GBrestants}")