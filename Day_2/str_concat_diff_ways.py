"""
🚀 Day 2 - Problem 2: String Concatenation & Formatting
👉 Problem Statement:

Take two strings as input.
Concatenate them using:
+ operator
format() method
f"" (f-string)
Print the concatenated result in each case.

"""
from functools import reduce
from itertools import chain

str_1 = input("enter first str ").strip()
str_2 = input("enter second str ").strip()
from io import StringIO

conc_1 = str_1 + " " + str_2

conc_2 = "{} {}".format(str_1, str_2)

conc_3 = f"{str_1} {str_2}"

conc_4 = ' '.join([str_1, str_2])

conc_5 = reduce(lambda x, y: x + ' ' + y, [str_1, str_2])

conc_6 = " ".join(chain(str_1, str_2))

buffer = StringIO()
buffer.write(str_1)
buffer.write(' ')
buffer.write(str_2)

print(buffer.getvalue())
buffer.close()


print(conc_6)

print(conc_5)

print(conc_4)

print(conc_3)

print(conc_2)

print(conc_1)