num = int(input("Enter an integer: "))

numValue = str(num)

if numValue == numValue[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
