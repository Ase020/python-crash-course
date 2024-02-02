
handle = open('test.txt', 'r')

data = handle.read()  #  returns the contents of the file
# data = handle.readline()  #  returns the first line of the file
# data = handle.readlines()  #  returns a list of all the lines in the file separated by \n tags. []

counter = 0
for word in data.split():
    if word == 'Python':
        counter += 1

print(counter)

# handle.close()
