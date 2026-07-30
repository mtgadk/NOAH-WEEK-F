print ("Say a word now")

userinput=input ()
x=""
for i in range (len (userinput) -1 ,-1,-1):
    x = x + userinput[i]
print (x)
if userinput==x:
    print ("palindrome")
else:
    print ("Not a palindrome")
    
    