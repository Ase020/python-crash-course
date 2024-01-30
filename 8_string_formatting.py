name = "Felix"
age = 19

f"{name} is {age} years old"  # Felix is 19 years old
'Beyonce\'s lemonade stand'  # Beyonce's lemonade stand
r'Beyonce\'s lemonade stand'  # Beyonce\'s lemonade stand

raw_str = 'Beyonce Lemonade'
is_aplha = raw_str.isalpha()  # Returns True if the string consists of letters only and is not blank
is_alnum = raw_str.isalnum()  # Returns True if the string consists of numbers and letters and is not blank
is_digit = '123456'.isdigit()
is_space = raw_str.isspace()  # Returns True if the string contains only space, tabs, or new lines
is_title = raw_str.istitle()  # Returns True if the string contains words that start with uppercase letters
print(is_title)
