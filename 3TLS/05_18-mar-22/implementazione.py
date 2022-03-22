# Lista di prezzi
# Non abbiamo necessità di ternere traccia dei nomi dei prodotti, 
# bensì esclusivamente dei prezzi
prodotti = [ 3.50, 2.00, 1.70, 2.50, 3.00 ]

# N = 5 (numero di prodotti/prezzi)
N = len(prodotti)

# Variabile in cui verranno sommati i prezzi dei singoli prodotti
costo_totale = 0

# Variabile che si occupa di tenere traccia del prezzo massimo
prezzo_max = 0

# Variabile che si occupa di tenere traccia del numero di prodotti il 
# cui prezzo è > 2.50 euro
sup_250 = 0

# Variabile di controllo del processo iterativo (contatore)
counter = 0

# Qui ha inizio il processo iterativo (eseguito al più N volte)
while counter < N:
    # A ciascuna iterazione la variabile prezzo conterrà il prezzo alla posizione 
    # counter all'interno della lista prodotti
    prezzo = prodotti[counter]
    
    # A ciascuna iterazione viene aggiunto il prezzo al costo totale
    costo_totale = costo_totale + prezzo

    # Incremento la variabile sup_250 se il prezzo del prodotto è effettivamente
    # superiore a 2.50 euro
    if prezzo > 2.50:
        sup_250 = sup_250 + 1

    if prezzo > prezzo_max:
        prezzo_max = prezzo

    counter = counter + 1

### DA TERMINARE ###

























