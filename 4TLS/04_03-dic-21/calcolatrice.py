"""
Calcolatrice
Prendere in input due valori da tastiera (operandi), selezionare l'operatore (addizione, sottrazione, moltiplicazione,
divisione, elevazione a potenza), restituire il risultato a video.

EXTRA.
Qualora i 
Qualora i due valori siano uguali, stampare a video:

"""

print('Benvenuti nella PythonCalc!')

value1 = float(input('Operando 1: '))
value2 = float(input('Operando 2: '))

print('Seleziona l\'operatore:')

print()

summary = """	1. addizione
	2. sottrazione
	3. moltiplicazione
	4. divisione
	5. elevazione a potenza"""

print(summary)

op = int(input('Operazione: '))

assert 1 <= op <= 5, 'Operatore errato!'

