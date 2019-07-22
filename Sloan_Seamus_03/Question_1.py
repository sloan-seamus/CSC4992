#!/usr/bin/env python3
import math

string1 = "WAYNE STATE UNIVERSITY"
string8 = "This is a list comprehension example"
sublist3 = ['pen', 'staple', 'ruler', 'pencil', 'eraser']
outfile = open("output.txt", "w+")

list1 = [char for char in string1 if char in 'AEIOU']
list2 = [x for x in range(0, 50) if x == 0 or float(x) % math.sqrt(x) == 0]
list3 = [word for word in sublist3 if word[-2:len(word)] == "er"]
list4 = [(c * 1.8) + 32 for c in [39.2, 36.5, 37.3, 37.8]]
list5 = [(x, y) for x in range(1, 100) for y in range (1, 100) if (x + y) % 2 == 0]
list6 = [x for x in range(1, 100) if x % 7 == 0]
list7 = [x for x in range(1, 100) if str(x).find('3') == 1 or x == 3]
list8 = [word for word in string8.split() if len(word) <= 5]

print("\n\nQuestion One\n\n")
print("Part 1: \n{}\n\n".format(list1))
print("Part 2: \n{}\n\n".format(list2))
print("Part 3: \n{}\n\n".format(list3))
print("Part 4: \n{}\n\n".format(list4))
print("Part 5: \n PLEASE SEE THE 'Output(1-5).txt' FILE\n\n")
outfile.write("Part 5\n{}\n".format(list5, end="\n"))
print("Part 6: \n{}\n\n".format(list6))
print("Part 7: \n{}\n\n".format(list7))
print("Part 8: \n{}\n\n".format(list8))





## Equivalence classes, Seamus1 cases, boundary testing, requirement writing,
## white/gray/black box testing, invalid/valid Seamus1 case, corner, base, edge case scenarios
## good vs bad requirement, function vs non func requirements
