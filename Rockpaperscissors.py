
from random import randint
cpuChoice = randint(0, 2)
if cpuChoice==0:
    cpuChoice= ("rock")
if cpuChoice==1:
    cpuChoice= ("paper")
if cpuChoice==2:
   cpuChoice= ("scissors")
print ("Rock paper or sciccors")
x=input ()
if x==0:
    print ("rock")
if x==1:
    print ("paper")
if x==2:
    print ("scissors")
print (cpuChoice)
if  x==("rock") and cpuChoice==("paper"):
    print ("You lose")
if x==("paper") and cpuChoice==("paper"):
    print ("tie")
if x==("scissors") and cpuChoice==("paper"):
    print ("you win")
if x==("rock") and cpuChoice==("rock"):
    print ("tie")
if x==("paper") and cpuChoice==("rock"):
    print ("you win")
if x==("scissors") and cpuChoice==("rock"):
    print ("you lose")
if x== ("rock") and cpuChoice== ("scissors"):
    print ("you win")
if x== ("paper") and cpuChoice== ("scissors"):
    print ("you lose")
if x== ("scissors") and cpuChoice== ("scissors"):
    print ("tie")


