size = 7
output = "\n"
for row in range(size, 0, -1):

    for column in range(row):

        output += "* "

    output += "\n"
print(output)