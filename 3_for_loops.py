numbers = [1,2,3,4,5]

for number in numbers:
     print(number)

list_a = list(range(0,10))
print(list_a)

for i in range(1,len(list_a)):
    print(f"I would love {i} cookies")

for i in list_a:
    if i % 2 != 0:
        print(i)