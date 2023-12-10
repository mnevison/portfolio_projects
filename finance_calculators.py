import math

# outputting user friendly information about the program

print('''

    Welcome to the Finance Calculator.
      
   Here you can provide us with details
  of a bond or investment you are wanting
 to make and we will tell you your interest


''')

# getting information on the initial query 
# adding safeguards with a while loop and booleans

valid_choices = ["bond", "investment"]

while True:
    choice = input("Enter Bond or Investment: ").lower()
    if choice in valid_choices:
        break
    else:
        print("Invalid choice - Please select either Bond or Investnemt")

# gathering the information needed for the investment calculations

if choice == "investment":
    total = float(input("Please tell us the total you would like to invest: "))
    # using float allows the use of decimals in the rates added
    rate = float(input("And at what interest rate is that? "))
    time = int(input("And over how many years? "))

# adding more safeguards

    valid_choices = ["simple", "compound"]

    while True:
        user_input = input("Now please tell us if you would like to see\
that with simple or compound interest: ").lower()
        if user_input in valid_choices:
            break
        else:
            print("Invalid choice - Please select either simple or compound interest")

# calculations for specified rates

    if user_input == "simple":
        simple = (total * rate * time) / 100
        print(f"£{simple} is the total after {time} years\
with a simple interest rate of {rate}%")
              
    elif user_input == "compound":
        compound_interest = total * (math.pow((1 + rate / 100), time))
        print(f"£{compound_interest:.2f} is the total after {time} years\
with a compound interest rate of {rate}%")

# data and calculations for the bond selection

elif choice == "bond":
    value = float(input("Please tell us the current value of the house: "))
    # Using float allows the use of decimals in the rates added
    rate = float(input("What is the monthly interest rate? ")) 
    months = int(input("And over how many months will the bond be repaid? "))

    monthly_rate = rate / 100 / 12  # Converting annual rate to monthly rate
    repayment = (monthly_rate * value) / (1 - (1 + monthly_rate) ** -months)
    print(f"You will pay £{repayment:.2f} per month based on the\
value of £{value} and interest rate of {rate}%")