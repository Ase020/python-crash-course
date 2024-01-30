players = 11

while players >= 5:
    print("The remaining players are: ", players)
    players -= 1

numTaken = [3,5,7,11,13]

print("Available numbers: ")

for i in range(1,21):
    if i in numTaken:
        continue
    print(i)