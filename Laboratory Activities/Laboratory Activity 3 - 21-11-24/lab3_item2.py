def perfectNum(num):
    if num <= 0:
        return False
    
    divisors = [divisor for divisor in range(1, num) if num % divisor == 0]
    return sum(divisors) == num

while True:
    InputNum = input("Enter a number: ")
    try:
        num = int(InputNum)
        if perfectNum(num):
            print(f"{num} is a perfect number.")
        else:
            print(f"{num} is not a perfect number.")
    except ValueError:
        print("Please enter a valid integer.")
