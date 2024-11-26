from capybara import Capybara

def test_capybara_class():
    capybara1 = Capybara("Coffee-bara", "M", 4)
    capybara2 = Capybara("Choco", "F", 3)
    capybara3 = Capybara("Barbara", "F", 6)

    try:
        test_case = int(input("Enter the test case number: "))
    except ValueError:
        print("Invalid input. Please enter a number: ")
        return

    if test_case == 1:
        selected_capybara = capybara1
    elif test_case == 2:
        selected_capybara = capybara2
    elif test_case == 3:
        selected_capybara = capybara3
    else:
        print("Invalid test case number. Please enter a number: ")
        return

    print(f"Test Case {test_case}: Name: {selected_capybara.name}, Gender: {selected_capybara.gender}, Age: {selected_capybara.age} years old")

test_capybara_class()
