###############
# Classe Auto #
###############
class Auto():
	# Metodo costruttore: avviato in fase di creazione di un'oggetto,
    # ovvero di un'istanza della classe Auto, ovvero di un "esemplare" della classe Auto
	def __init__(self, targa, modello, ora_entrata):
		self.targa = targa
		self.modello = modello
		self.ora_entrata = ora_entrata
	
	def get_targa(self):
		return self.targa
		
	def get_modello(self):
		return self.modello
	
	def get_ora_entrata(self):
		return self.ora_entrata
		
#################
# Classe Garage #
#################
class Garage():
	def __init__(self, capienza):
		self.capienza = capienza
		# Creo una lista di auto vuota (di oggetti di tipo Auto)
		self.auto_list = []
	
	def add_auto(self, auto):
		# Se i posti disponibili sono sufficienti: aggiungo un auto alla lista delle auto
		if len(self.auto_list) <= self.capienza:
			self.auto_list.append(auto)
			
	def get_last_auto(self):
		# Restituisco l'ultima auto entrata nel garage
		return self.auto_list[-1]
		
########
# Main #
########
# Creazione di un oggetto di tipo Garage (un'istanza della classe Garage, uno specifico "esemplare"), avente 10 posti:
garage = Garage(10)

auto_1 = Auto('BX123AH', 'Panda', '10:30')
garage.add_auto(auto_1)
auto_2 = Auto('AH567BJ', 'Logan', '11.30')
garage.add_auto(auto_2)

# Ottengo l'ultima auto entrata nel garage (un oggetto di tipo Auto)
ultima_auto = garage.get_last_auto()
# Stampa a video la targa
print(ultima_auto.get_targa())