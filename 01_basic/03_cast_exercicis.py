###
# Exercicis - conversió de tipus (casting)
# Completa els exercicis següents convertint dades entre tipus.
###

# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.

paquets_rebuts= int(input("quants paquets ha rebut un encaminador?"))
total_paquets= paquets_rebuts+ 1200
print(total_paquets)

# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.
velocitat= float(input("quina és la velocitat de la connexió en Mbps?"))
velocitat_eq= velocitat/8
print(velocitat_eq)