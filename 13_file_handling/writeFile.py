"""writing a file"""

# handle = open('test-write.txt', 'w')
# handle.write("Hello world")
# handle.close()

"""With operator"""
with open('test.txt', 'r') as handle:
    data = handle.read()
    print(data)