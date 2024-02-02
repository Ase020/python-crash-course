# Create a program where you prompt a user for their age and return the year they were born.
# After that, return the year they will turn 80.

import datetime


def calculate_birthyear(age):
    current_year = datetime.datetime.now().year
    birth_year = current_year - age
    return birth_year


def main():
    try:
        age = int(input("Enter your age: "))
        birth_year = calculate_birthyear(age)
        age_at_80 = birth_year + 80
        print(f"Your birth year is {birth_year}, and you'll turn 80 in {age_at_80}.")
    except:
        print("Invalid input entered")



main()


