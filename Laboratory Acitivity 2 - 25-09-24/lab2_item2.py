while True:
    purchase = int(input("Enter the total purchase amount: "))

    initialPurchase = float(purchase)
    print("Initial Purchase Amount: %.2f" % initialPurchase)

    if initialPurchase > 5000:
        discount = (initialPurchase / 100) * 10
        print("Discount: %.2f" % discount)
    else:
        discount = initialPurchase * 0.05
        print("Discount: %.2f" % discount)

    finalPrice = initialPurchase - discount
    print("Final price: %.2f" % finalPrice)

    purchase_2 = input("Do you want to try again? (yes/no): ")
    if purchase_2 != "yes":
        print("Thank you!")
        break
