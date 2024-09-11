str_input =(input("Enter a string: "))

vowel ='AaEeIiOoUu'
vowelList = []
 
for char in str_input:
    if char in vowel:
        vowelList.append(char)

print(vowelList)