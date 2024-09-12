#!/usr/bin/python3

# Create the formatted output for numbers 0 to 99 in hexadecimal
output = "\n".join("{} = {}".format(i, hex(i)) for i in range(100))

# Print the result in one go to avoid extra newlines
print(output)
