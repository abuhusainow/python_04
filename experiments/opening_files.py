import sys

file = open(sys.argv[1])
content = file.read()
print(content)
file.close()

if file.closed == True:
    print("is closed")