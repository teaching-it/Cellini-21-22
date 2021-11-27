# Rispetto all'esercizio svolto il 19 novembre, supponiamo che la media aritmetica sia:
media = 5
# (modificare all'occorrenza)



"""
Esercizio n. 1
Data la media dei voti precedentemente calcolata, stampare a video quanto segue:
    - 'Sufficiente', qualora la media sia >= 6
    - 'Insufficiente', altrimenti
    
Il linguaggio Python usa l'indentazione significativa per raggruppare un blocco di istruzioni.
"""

if media >= 6:
    print('Sufficiente')
else:
    print('Insufficiente')



"""
Esercizio n. 2
Data la media dei voti precedentemente calcolata, stampare a video quanto segue:
    - 'Gravemente insufficiente', qualora la media sia compresa nell'intervallo [0,3[
    - 'Insufficiente: [3,5[
    - 'Mediocre': [5,6[
    - 'Sufficiente: [6,7[
    - 'Buono': [7,8[
    - 'Molto buono': [8,9[
    - 'Ottimo': [9,10]

Tabella della verità AND
    T AND T -> T
    T AND F -> F 
    F AND T -> F
    F AND F -> F
"""

"""
Possibilità n. 1
(inefficiente, da non usare)
"""
if media >= 3 and media < 5:
    print('Gravemente insufficiente')
if media >= 5 and media < 6:
    print('Insufficiente')
# Piuttosto che concatenare le due espressioni con una congiunzione logica AND, è possibile impiegare una differente notazione.
if 5 <= media < 6:
    print('Mediocre')
# Proseguire con gli intervalli residui

"""
Possibilità n. 2
Corretto.
"""
if 3 <= media < 4:
    print('Gravemente insufficiente')
elif 4 <= media < 5:
    print('Insufficiente')
elif 5 <= media < 6:
    print('Mediocre')

# Proseguire con gli intervalli residui

# Altrimenti, in tutti gli altri casi:
else: 
    print('Ottimo')