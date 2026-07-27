from random import randint

looping = True
games=0
playerscore=0
cpuscore=0
while looping == True: 
    cpuChoice = randint(0, 2)
    if cpuChoice==0:
        cpuChoice= ("rock")
    if cpuChoice==1:
        cpuChoice= ("paper")
    if cpuChoice==2:
        cpuChoice= ("scissors")
    print ("Rock paper sciccors or quit")
    x=input ()
    if x==0:
        print ("rock")
    if x==1:
        print ("paper")
    if x==2:
        print ("scissors")
    if x==("quit"):
        looping=False
    print (cpuChoice)

    if  x==("rock") and cpuChoice==("paper"):
        print ("You lose haha")
        cpuscore=cpuscore+1
    if x==("paper") and cpuChoice==("paper"):
        print ("tie")
    if x==("scissors") and cpuChoice==("paper"):
        print ("you win")
        playerscore=playerscore+1
    if x==("rock") and cpuChoice==("rock"):
        print ("tie")
    if x==("paper") and cpuChoice==("rock"):
        print ("you win")
        playerscore=playerscore+1
    if x==("scissors") and cpuChoice==("rock"):
        print ("you lose haha")
        cpuscore=cpuscore+1
    if x== ("rock") and cpuChoice== ("scissors"):
        print ("you win")
        playerscore=playerscore+1
    if x== ("paper") and cpuChoice== ("scissors"):
        print ("you LOSE haha")
        cpuscore=cpuscore+1
    if x== ("scissors") and cpuChoice== ("scissors"):
        print ("tie")
    games=games+1
    print (games)
    print (cpuscore)
    print (playerscore)
    