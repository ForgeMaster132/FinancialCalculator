import math

# Initial Output
print("Choose either \"investment\" or \"bond\" from the menu below to proceed:")
print("investment       - to calculate the amount of interest you'll earn on intrest")
print("bond             - to calculate the amount you'll have to pay on a home loan")

# Calculator Selection and Calculations
selection = input()

while True:
    if selection.lower() != "investment" and selection.lower() != "bond":
        selection = input("You have not entered a valid choice. Please try again: ")

    elif selection.lower() == "investment":
        deposit_amount = float(input("How much are you depositing? "))
        interest_rate = float(input("What is the percentage yearly interest rate? "))
        num_years = float(input("How many years will you be investing for? "))
        interest = input("Is it going to be \"simple\" or \"compound\" interest? ")
        while interest.lower() != "simple" and interest.lower() != "compound":
            interest = input("You have not entered a valid choice. Please try again: ")

        if interest.lower() == "simple":
            total = deposit_amount + (deposit_amount / 100* interest_rate) * num_years
            total_interest = total - deposit_amount
            print("Your total is: {} with a total interest of {}".format(round(total,2),round(total_interest,2)))
        else:
            total = deposit_amount * math.pow((1 + (interest_rate / 100)),num_years)
            total_interest = total - deposit_amount
            print("Your total is: {} with a total interest of {}".format(round(total,2),round(total_interest)))
        break

    else:
        house_value = float(input("What is the current value of the house? "))
        interest_rate = float(input("What is the percentage yearly interest rate? "))
        num_months = float(input("Over how many months are you planning to repay the bond? "))
        month_interest_rate = interest_rate / 12
        month_interest_rate = month_interest_rate / 100

        repayment = house_value * month_interest_rate * math.pow(1 + month_interest_rate,
            num_months)/(math.pow(1 + month_interest_rate,num_months) - 1)

        print("Your monthly repayment is: {}".format(round(repayment,2)))
        break