# ✨**Laboratory Activities** ✨
## **_CS 121: Advanced Computer Programming_** 

### 🗃️ **About**
- This readme provides an overview, purpose, and instructions for reviewers in CS 121.
- Every lab activity shows practical applications of Python concepts to enhance programming skills.

---

## 🐍 **Laboratory Activity 1: Introduction to Python** 🐍
### 🎶 **Item 1: Song Details**
- This python script collects and displays song details provided by the user.
- **Purpose**: It demonstrates basic input handling and formatted output.
- **Instructions to Reviewers**: The user inputs the year, genre, album, song title, and artist, and the program displays the song details based on the provided information. This serves as valuable practice for developing basic Python skills.

### 🔢 **Item 2: Character and ASCII Values** 
- It allows users to input two space-separated characters, prints the one with the greater value, and displays the ASCII value of the character.
- **Purpose**: Demonstrates basic string comparison, conditional logic, and the use of ASCII values to compare characters.
- Example of ASCII Values (A-65; a-97)
- **Instructions for Reviewers**: The user inputs two space-separated characters, then the program determines which has a greater value and prints the ASCII values of the characters. This can be a good start in exploring the ASCII values.

---

## 🗂️ **Laboratory Activity 2: Libraries and Control Flow** 🗂️
### ✅ **Item 1: Integer Palindrome Checker** 
- It checks whether the entered integer is a palindrome.
- **_What is a Palindrome?_** It is a number that reads the same forward and backward when its digits are reversed.
- **Purpose**: Demonstrates the basic concepts of string manipulation and conditional logic.
- **Palindrome example**: 989 (Palindrome); 183 (Not a Palindrome).
- **Instructions for Reviewers**: The user inputs an integer, and the program checks if it is a palindrome by comparing the string version of the number with its reversed version.

### 💸 **Item 2: Discount Calculator** 
- It calculates the final purchase price after applying a discount based on the total purchase amount.
- **Purpose**: Demonstrate the use of loops, conditional statements, and basic arithmetic operations for calculating discounts.
- **_The amount prints in two decimal places_** 
- **Instructions for Reviewers**: The user inputs their total purchase amount, and then the program prints the initial purchase amount, the discount, and the total price. The program then asks the user if they want to make another transaction.
---

## 📜 **Laboratory Activity 3: Dictionaries and Lists** 📜
### 📚 **Item 1: Roman to Integer** 
- This function converts a Roman numeral to its integer equivalent. It uses a dictionary to map Roman numeral characters to their values and processes the input to calculate the total integer value based on Roman numeral rules.
- **Purpose**: Demonstrates how to convert Roman numerals to integers using dictionaries and conditional checks.
- **How is dictionary applied**: `roman_values = {'I': 1, 'V':5, 'X':10, 'L':50, etc.}`
- **Instructions for Reviewers**: The user will enter a Roman numeral, and it will be processed from right to left. The program should accept input in either lowercase or uppercase letters.

### 👌 **Item 2: Perfect Numbers** 
- It defines a function `perfectNum` that checks if a given number is a perfect number.
- **What is a Perfect Number?** A positive integer that is equal to the sum of its proper divisors (excluding the number itself; 28: 1+2+4+7+14).
- **Purpose**: Demonstrates how to find perfect numbers and handle user input with exception handling.
- **Instructions for Reviewers**: The user will enter a number, and the program will check if the input is a perfect number or not. It also includes error handling for invalid inputs.

---

## 💌 **Laboratory Activity 4: Object-Oriented Programming in Python** 💌
### 🦫 **Item 1: Meeting a Capybara** 
- It defines a `Capybara` class in `capybara.py` with attributes for name, gender, and age.
- The `test_capybara_class` function demonstrates instantiation of `Capybara` objects and selects a specific capybara based on user input to test its attributes.
- **Purpose**: How to apply object-oriented programming in Python with classes and instances, and how to interact with user input to select and manipulate class objects.
- **Instructions for Reviewers**: In the program, there is a `Capybara` class and a constructor. Then, in the script, the `Capybara` was imported to have access, and it shows the predefined values of capybaras. The user will enter a test case to print and then select a specific capybara based on user input to show its attributes.

### 😓 **Item 2: Exception Handling** 
- It allows the user to input the size of an array and its elements, and then retrieves and prints an element at a specified index.
- **Purpose**: Demonstrates basic array handling, input validation, and error handling in Python.
- **`arr = [0.0] * size`** (length will be determined by the size inputted by the user).
- **Instructions for Reviewers**: The user will enter the size of the array and then inputs the elements of the array based on its length. Then, the user will be asked to enter the index of the element to print in two decimal places. The `except IndexError` is used to catch the error.

---

💌 **Thank You!**  💌
### print("Keep on Coding!")
