# Create a program that lets the user input their total bill at a restaurant, and returns the total cost of the bill including
# a tip. Use 15% of the total bill calculation.
# Once you're finished, take this a step further and let the user enter their level of satisfaction with their service and factor
# that value into the tip percentage. For example, if they received good service, the tip is 15%; great service is 20%; terrible service is 0%


def bill_calculator(tip, bill):
    tip_percent = tip / 100
    total = bill + (bill * tip_percent)
    return total


def main():
    try:
        bill = int(input("Enter your bill amount: "))
        satisfaction = input("What's your level of satisfaction?: ")
        if satisfaction == "good service":
            tip = 15
        elif satisfaction == "great service":
            tip = 20
        else:
            tip = 0
        total = bill_calculator(tip, bill)
        print(f"Your total bill is Ksh {total}")
    except:
        print("Invalid input format")


main()
