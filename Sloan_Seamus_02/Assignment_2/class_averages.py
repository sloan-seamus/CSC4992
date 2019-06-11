#!/usr/bin/env python3
import statistics

"""Global Variables + Dictionary"""
dictionary = {"10": "A", "9": "A", "8": "B", "7": "C", "6": "D"}
class_scores = []
class_minimum = 100
class_maximum = 0
test_count = 0
maximum_scoring_student = ""
minimum_scoring_student = ""
maximum_scored_test = 0
minimum_scored_test = 0


def get_name(line):
    line = line.split(":")
    return line[0]


def get_scores(line):
    global test_count
    line = line.split(":")
    line = line[1]
    line = line.replace(",", "")
    line = line.split()
    test_count = len(line)
    return line


def get_average(scores, name):
    sum = 0
    for score in scores:
        if int(score) > int(class_maximum):
            update_class_stats(scores.index(score), name, score, 1)
        if int(score) < int(class_minimum):
            update_class_stats(scores.index(score), name, score, 0)
        sum += int(score)
    return sum / len(scores)


def get_grade(average):
    average = int(average / 10)
    return dictionary.get(str(average), "F")


def get_class_average():
    average = 0
    for score in class_scores:
        average += int(score)
    return average / len(class_scores)


def update_class_stats(index, name, score, max):
    global class_maximum, class_minimum
    global maximum_scoring_student, minimum_scoring_student
    global maximum_scored_test, minimum_scored_test
    """Update based on 'max' value"""
    if max == 1:
        class_maximum = score
        maximum_scoring_student = name
        maximum_scored_test = index
    else:
        class_minimum = score
        minimum_scoring_student = name
        minimum_scored_test = index


infile = open("input.txt", "r")
outfile = open("output.txt", "w+")
lines = infile.readlines()
for i in lines:
    if i == "\n":
        continue
    name = get_name(i)
    scores = get_scores(i)
    average = get_average(scores, name)
    letter = get_grade(average)
    class_scores.extend(scores)
    print("Name: {}".format(name))
    outfile.write("Name: {}\n".format(name))

    print("Scores: {}".format(scores))
    outfile.write("Scores: {}\n".format(scores))

    print("Student Average: {}".format(average))
    outfile.write("Student Average: {}\n".format(average))

    print("Student's Grade: {}\n".format(letter))
    outfile.write("Student's Grade: {}\n\n".format(letter))


print("\nTotal Students: {}".format(len(lines)))
outfile.write("\nTotal Students: {}\n".format(len(lines)))

print("Class Average: {}".format(get_class_average()))
outfile.write("Class Average: {}\n".format(get_class_average()))

class_scores = list(map(int, class_scores))
print("Standard Deviation: {}".format(statistics.stdev(class_scores)))
outfile.write("Standard Deviation: {}\n\n".format(statistics.stdev(class_scores)))

print("Class's Lowest Score: {}\n\tScored by: {}\n\tScored on Test {}\n"
      .format(class_minimum, minimum_scoring_student, minimum_scored_test + 1))
outfile.write("Class's Lowest Score: {}\n\tScored by: {}\n\tScored on Test {}\n\n"
              .format(class_minimum, minimum_scoring_student, minimum_scored_test + 1))

print("Class's Highest Score: {}\n\tScored by: {}\n\tScored on Test {}\n"
      .format(class_maximum, maximum_scoring_student, maximum_scored_test + 1))
outfile.write("Class's Highest Score: {}\n\tScored by: {}\n\tScored on Test {}\n"
              .format(class_maximum, maximum_scoring_student, maximum_scored_test + 1))
