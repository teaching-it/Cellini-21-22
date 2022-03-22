"""
Esercizio n. 1
Dati i voti di 3 prove di uno studente, calcolare la media aritmetica.
"""

# Definizione di una costante
# Nb. in Python per convenzione le costanti sono definite in uppercase
N_VOTI = 3

print('hello')

# Dati in input
voto1 = float(input('Voto n. 1: '))
voto2 = float(input('Voto n. 2: '))
voto3 = float(input('Voto n. 3: '))

# Calcolo della media aritmetica
media = (voto1 + voto2 + voto3) / N_VOTI

# Output a video del risultato
print('La media aritmetica è:', media)

# Arrotondamento alla seconda cifra decimale; si presti attenzione all'utilizzo di .format()
print('La media aritmetica è: {0:.2f}'.format(media))



"""
Esercizio n. 2
Data la media dei voti precedentemente calcolata, stampare a video quanto segue:
    - 'Sufficiente', qualora la media sia >= 6
    - 'Insufficiente', altrimenti 
"""
