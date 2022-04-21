import random 

pazienti=[]
n_pazienti=20
count=0

while count==0:
    
    while count < n_pazienti:
        
        pazienti.append(int(random.random()*100))
        count += 1
        
    print ("pazienti: ", len(pazienti), pazienti)
    
    gruppo_a=[]
    gruppo_b=[]
    
    for num in pazienti:
        
        if num % 2 == 0:
            gruppo_a.append(num)
        else:
            gruppo_b.append(num)
            
    print("\ngruppo A: ",len(gruppo_a),gruppo_a,"\ngruppo B: ",len(gruppo_b), gruppo_b)

    risposta_immunitaria=[]

    for num in gruppo_a:
        
        risposta_immunitaria.append(int(random.random()*250))

    print("\nrisposta immunitaria: ", len(risposta_immunitaria), risposta_immunitaria)

    mediocre=[]
    sufficiente=[]
    ottima=[]

    for num in risposta_immunitaria:
        
        if num < 50:
            mediocre.append(num)
        elif num >= 50 and num < 99:
            sufficiente.append(num)
        else:
            ottima.append(num)
            
    print("\nottimi: ",len(ottima),ottima)
    print("sufficient1: ",len(sufficiente), sufficiente)
    print("mediocri: ",len(mediocre), mediocre)
    print("----------------------------------------------------------------------------------")

    count=0
    pazienti=[]
    gruppo_a=[]
    gruppo_b=[]
    mediocre=[]
    sufficiente=[]
    ottima=[]
    
    input()
    
        

    
