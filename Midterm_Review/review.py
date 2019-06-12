#!/usr/bin/env python3

animals = ['Bird', 'Cat', 'Dog', 'Donkey', 'Monkey']
testScores = [54, 67, 89, 93, 92, 87, 89, 78, 75, 73, 98, 68]

print("\n\n Midterm Review\n")
print("List the test scores in descending order")
print(", ".join(map(str, testScores))[0:])

print("\n")
print("Print only commas from the test scores list")
listComp = [comma for comma in str(testScores) if comma == ","]
print(str(listComp)[0::])


print("\n")
print("Print only the words with 'o' in the animals list")
listComp2 = [animal for animal in animals for char in animal if char == 'o']
print(listComp2)

print("\n")
print("Print the odd numbers in the test scores list")
listComp3 = [score for score in testScores if score % 2 == 1]
print(listComp3)





print("\n")
