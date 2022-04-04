# Lista di voti (indicizzati da 0 a 4)
voti = [6, 5.5, 7.5, 4.5, 7.75]

# Inizializzazione delle variabili
suff = 0
insuff = 0
N = len(voti)
counter = 0
totale = 0


while counter < N:
    # Prelevo il voto in posizione counter dalla lista voti
    voto = voti[counter]

    if voto >= 6:
        # Qualora il voto sia >= 6, allora incremento la variabile suff
        suff = suff + 1
    else:
        # Alrimenti il voto è insufficiente
        insuff = insuff + 1

    # Man mano che procedo tra le varie iterazioni tengo traccia del valore totale:
    # servirà per il calcolo del voto medio
    totale = totale + voto

    # Incremento la variabile di controllo, necessaria per la corretta gestione del
    # processo iterativo
    counter = counter + 1
# Termina il ciclo


if insuff > N * 50 / 100:
    # I voti insufficienti sono superiori al 50% dei voti totali
    print('Attivazione corso di recupero')

# 1° modo per calcolare la media
media = sum(voti) / N
print('La media dei voti è', media)

# 2° modo per calcolare la media
media = totale / N
print('La media dei voti è', media)

print('Le sufficienze sono', suff)
print('Le insufficienze sono', insuff)
