#!/usr/bin/env python3

animals = ['Bird', 'Cat', 'Dog', 'Donkey', 'Monkey']
testScores = [54, 67, 89, 93, 92, 87, 89, 78, 75, 73, 98, 68]

print("\n\n Midterm Review\n")
print("List the Seamus1 scores in descending order")
print(", ".join(map(str, testScores))[0:])

print("\n")
print("Print only commas from the Seamus1 scores list")
listComp = [comma for comma in str(testScores) if comma == ","]
print(str(listComp)[0::])


print("\n")
print("Print only the words with 'o' in the animals list")
listComp2 = [animal for animal in animals for char in animal if char == 'o']
print(listComp2)

print("\n")
print("Print the odd numbers in the Seamus1 scores list")
listComp3 = [score for score in testScores if score % 2 == 1]
print(listComp3)

print(88 in testScores)

a = [(1, 2)]
b = [3, 4]
b = b + a
b = b + a
a.append(3)
print(b)

for x in [1, 2, 3]:
    for y in [3, x]:
        print(x, y)


y = []
w = 10
while w > 0:
    y += [[w]]
    w /= 2
print(y)




print("\n")
