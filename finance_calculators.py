import math

print('''
    Welcome to the Finance Calculator.
    Here you can provide us with details
    of a bond or investment you are wanting
    to make and we will tell you your interest
''')

valid_choices = ["bond", "investment"]

while True:
    choice = input("Enter Bond or Investment: ").lower()
    if choice in valid_choices:
        break
    else:
        print("Invalid choice - Please select either Bond or Investment")

if choice == "investment":
    while True:
        try:
            total = float(input("Please tell us the total you would like to invest: "))
            adjusted_rate = float(input("And at what interest rate is that? "))
            rate = adjusted_rate / 100
            time = int(input("And over how many years? "))
            if total <= 0 or rate <= 0 or time <= 0:
                print("Error - Please enter numerical value above 0")
            else:
                break
        except ValueError:
            print("Error - Only numerical values can be entered. Please try again")

    valid_choices = ["simple", "compound"]

    while True:
        user_input = input("Now please tell us if\
 you would like to see that with simple or compound interest: ").lower()
        if user_input in valid_choices:
            break
        else:
            print("Invalid choice - Please select either simple or compound interest")

    # calculations for specified rates
    if user_input == "simple":
        simple = total * (1 + rate * time)
        print(f"£{simple:.2f} is the total after\
 {time} years with a simple interest rate of {adjusted_rate}%")
                  
    elif user_input == "compound":
        compound_interest = total * (math.pow((1 + rate), time))
        print(f"£{compound_interest:.2f} is the total\
 after {time} years with a compound interest rate of {adjusted_rate}%")

elif choice == "bond":
    while True:
        try:
            value = float(input("Please tell us the current value of the house: "))
            adjusted_rate = float(input("What is the monthly interest rate? "))
            rate = adjusted_rate / 100 / 12
            months = int(input("And over how many months will the bond be repaid? "))
            if value <= 0 or rate <= 0 or months <= 0:
                print("Error - Please enter numerical values above 0")
            else:
                break
        except ValueError:
            print("Error - Only numerical values can be entered - Please try again")

    repayment = (rate * value) / (1 - (1 + rate) ** -months)
    print(f"You will pay £{repayment:.2f} per\
 month based on the value of £{value} and interest rate of {adjusted_rate}%")
