import sys
input_str = ""
for line in sys.stdin:

    if line.rstrip() == "q":
        break
    input_str = input_str + line

print(input_str)
print("Exit")
