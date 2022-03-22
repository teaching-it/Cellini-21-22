"""
Il listato seguente si riferisce all'esercizio reperibile all'url:
https://github.com/teaching-it/Cellini-21-22/tree/main/3TLS/10-dic

Struttura dati:
indice_0 | prezzo_1
indice_1 | prezzo_2
..		   ..
indice_x | prezzo_y
"""

# vettore (lista)
           # 0     1     2     3     4
prodotti = [ 2.60, 2.00, 1.70, 2.50, 3.00 ]    

# N = 5
N = len(prodotti)

costo_totale = 0
prezzo_max = 0
sup_250 = 0
counter = 0

while counter < N:
	prezzo = prodotti[counter]
	costo_totale = costo_totale + prezzo

	if prezzo > 2.50:
		# sup_250 = sup_250 + 1
		sup_250 += 1

	if prezzo > prezzo_max:
		prezzo_max = prezzo

	counter = counter + 1

print('Il costo totale è pari a', costo_totale)

if costo_totale > 10:
	print('Applico uno sconto del 10%')
	costo_totale = costo_totale - (costo_totale * 0.1)
	# print('Il costo totale è pari a', costo_totale)

if sup_250 >= 2:
	print('Applico uno sconto del 5%')
	costo_totale = costo_totale - (costo_totale * 0.05)
	# print('Il costo totale è pari a', costo_totale)

print('Il costo totale è pari a', costo_totale)
