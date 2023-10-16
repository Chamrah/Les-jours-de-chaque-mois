#Programme qui donne le jour de chaque mois
m=input("Entrer le mois : ")
nj=0
if(m=="fevrier"):
    print(f"Le nombre de jour de {m} est 28 ou 29 jours")
elif(m=="avril" or m=="juin" or m=="septembre" or m=="novembre"):
    nj=30
    print(f"Le nombre de jours est {nj} jours")
elif(m=="janvier" or m=="mars" or m=="juillet" or m=="aout" or m=="octobre" or  m=="decembre"):
    nj=30
    print(f"Le nombre de jours est {nj} jours")
else:
    print("Error")