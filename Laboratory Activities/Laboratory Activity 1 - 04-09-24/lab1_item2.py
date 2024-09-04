var1, var2 = input ("Enter two space-separated characters: ").split()

greaterVal = ''
if var1 > var2 :
    greaterVal = var1
else:
    greaterVal = var2

print ("------------------------------------------")
print ("The character with greater value is :", greaterVal)
print ("------------------------------------------")

asciiVal1 = ord(var1)
asciiVal2 = ord (var2)
print ("Showing ASCII Values:")
print (var1, ":", asciiVal1)
print (var2, ":", asciiVal2)