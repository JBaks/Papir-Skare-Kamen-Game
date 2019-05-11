import time
from random import choice # random.choice znaci da ce izabrat random string.

# Ovde smo deklarirali 3 najvaznije varijable:"Comp,Player te niz iz kojeg ce Comp izabrat svoj random odgovor!

comp=0
player=0
niz=["papir","skare","kamen"]
print("""Papir:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
Skare:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
Kamen:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)\n""")

# Sve smo stavili u for petlju koja se vrsi 3 puta,sto znaci da se igra 3 puta.

for i in range(3):
    print("Runda: "+str(i+1))
    print("=============================")
    odgovor=str(input("""Upisite papir,skare ili kamen.\nPlayer: """))

    # Dok god ne upisete nesto sto nije u varijabli "niz",ponov ce vas pitat da upisete.
    while (odgovor not in niz):
        odgovor=str(input("Upisite jedno od 3 ponudjena odgovora.\n"))
        
    # Ovde smo stavili da je odgovor kompjutera "random.choice",izabrat ce random string iz niza.
    computer=choice(niz) 
    print("Comp:",computer)
    
    # Ako je odgovor jednak kompu onda poen dobivaju i igrac i komp.
    if odgovor==computer:
        comp+=1
        player+=1
        print("""=====================
| Comp: """+str(comp)+" Player: "+str(player),"""|
=====================""")
    # Ovo je elif koji govori sta ce bit ako igrac dobije,player ce se uvecati.
    elif (odgovor=="papir"and computer=="kamen")or(odgovor=="skare"and computer=="papir")or(odgovor=="kamen"and computer=="skare"):
        player+=1
        print("""============
| Player: """+str(player),"""|
============""")
    # Ovo je ako kompjuter dobije,komp ce se uvecati.
    elif (odgovor=="papir"and computer=="skare")or(odgovor=="skare"and computer=="kamen")or(odgovor=="kamen"and computer=="papir"):
        comp+=1
        print("""==========
| Comp: """+str(comp),"""|
==========""")
    print("")

# Na kraju ispisemo sta ce bit ako je nerjeseno,ako dobije i ako izgubi.
print("Rezultat je: Player:"+str(player)+" Comp:"+str(comp))
if(player==comp):
    print("Nerjeseno.")
elif(player>comp):
    print("Dobili ste!")
elif(player<comp):
    print("Izgubili ste!")
time.sleep(10)

    
