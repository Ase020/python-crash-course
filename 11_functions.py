def get_age():
    try:
        age = int(input("What is your age? "))
        return age
    except ValueError:
        return "That was not an integer"


print(get_age())
