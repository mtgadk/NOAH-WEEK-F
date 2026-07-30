print ("ENTER A NUMBER")

userinput=input()
userinput=int(userinput)

prime=True

for i in range (3, int(1/2 * userinput) ,2):
    if userinput%i==0:
        prime=False


if userinput%2==0:
    prime=False


if prime:
    print ("Prime")


else:
    print ("Not prime")