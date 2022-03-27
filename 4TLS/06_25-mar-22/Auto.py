# Classe: descrizione di una entità di realtà, un'Auto nel nostro semplice caso
class Auto:
    # Metodo costruttore: avviato in fase di creazione di un'oggetto,
    # ovvero di un'istanza della classe Auto, ovvero di un "esemplare" della classe Auto
    def __init__(self, marca, modello, targa, cilindrata, cavalli, colore):
    	# Attributi: caratteristiche descrittive e/o parametri di stato di uno oggetto
        self.marca = marca
        self.modello = modello
        self.targa = targa
        self.cilindrata = cilindrata
        self.cavalli = cavalli
        self.colore = colore

    # Metodi: comportamenti, funzionalità che un oggetto mette a disposizione        
    def accendi(self):
        print('Accensione dell\'auto')
        
    def spegni(self):
        print('Spegnimento dell\'auto')
        
    def sterza(self):
        print('L\'auto sterza')
        
    def frena(self):
        print('L\'auto frena')
        
    def ripara(self):
        print('L\'auto è in riparazione')

    def get_targa(self):
    	return self.targa



# Esternamente alla classe
# Creazione di un oggetto di tipo Auto (un'istanza della classe Auto, uno specifico "esemplare"):
# una Fiat Panda
pandino = Auto('Fiat', 'Panda', 'AA000BB', 1100, 85, 'bianco')

print('La targa dell\'auto è:', pandino.get_targa())
pandino.accendi()
pandino.spegni()
