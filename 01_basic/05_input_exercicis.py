###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informacaió.

nomT, nomX = input("introdueix el nom d'un tecnic i d'una xarxa:\n" ).split()

print(f"el teu tecnoc es:{nomT} . i la teva xarxa es:{nomX} ")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.

Lfibra= float(input("introdueix a longitud d'un enllaç de fibra en quilòmetres:"))
velocitat= float(input("introdueix la velocitat de transmissió:"))

segons= 8/velocitat
print(f"es tarda {segons} segons")


# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.

hores=float(input("intro hores de feina"))
preu_hora=float(input("preu per hora:"))
preu_material=float(input("preu del material:"))
cost= (preu_hora*hores)+ preu_material
print(f"el cost total es de:{cost}")