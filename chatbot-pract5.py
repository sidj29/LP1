print("Welcome to our virtual cake shop!")
print("Please select a category from the following options:")
print("1. Birthday cakes")
print("2. Wedding cakes")
print("3. Custom cakes")

category = int(input("Enter Your Choice:"))

if category == 1:
    print("Great! You've selected the Birthday cake category.")
    print("Here are your options for birthday cakes:")
    print("1. Chocolate cake - $25")
    print("2. Vanilla cake - $20")
    print("3. Strawberry cake - $30")

    option = int(input("Choose one of the above cake:"))
    print("What color would you like your cake to be?")
    color = input()
    print("What Additional flavor would you want to add in your cake?")
    flavor = input()

    if option == 1:
        print("You've selected the Chocolate cake with", color, "color and", flavor, "flavor.")
        print("Your total amount is $25. Thank you for ordering!")
    elif option == 2:
        print("You've selected the Vanilla cake with", color, "color and", flavor, "flavor.")
        print("Your total amount is $20. Thank you for ordering!")
    elif option == 3:
        print("You've selected the Strawberry cake with", color, "color and", flavor, "flavor.")
        print("Your total amount is $30. Thank you for ordering!")
    else:
        print("Invalid option selected. Please try again.")

elif category == 2:
    print("Great! You've selected the Wedding cake category.")
    print("Here are your options for wedding cakes:")
    print("1. Vanilla and raspberry cake - $50")
    print("2. Lemon and blueberry cake - $60")
    print("3. Red velvet cake - $75")
    option = int(input())
    print("What color would you like your cake to be?")
    color = input()
    print("What Additional flavor would you want to add in your cake?")
    flavor = input()

    if option == 1:
        print("You've selected the Vanilla and Raspberry cake with", color, "color and", flavor, "flavor.")
        print("Your total amount is $50. Thank you for ordering!")
    elif option == 2:
        print("You've selected the Lemon and Blueberry cake with", color, "color and", flavor, "flavor.")
        print("Your total amount is $60. Thank you for ordering!")
    elif option == 3:
        print("You've selected the Red Velvet cake with", color, "color and", flavor, "flavor.")
        print("Your total amount is $75. Thank you for ordering!")
    else:
        print("Invalid option selected. Please try again.")

elif category == 3:
    print("Great! You've selected the Custom cake category.")
    print("What color would you like your cake to be?")
    color = input()

    print("What flavor would you like your cake to be?")
    flavor = input()

    print("What type of custom cake would you like to order?")
    type = input()

    print("What size of cake would you like to order?")
    size = input()

    print("What design or theme would you like for your cake?")
    design = input()

    print("What is your budget for the cake?")
    budget = float(input())

    print("Thank you for your order! We will contact you soon for your custom cake.")

else:
    print("Invalid category selected. Please try again.")