#!/usr/bin/env python3
import random
from breezypythongui import EasyFrame

count = 0
word = ""
points = 0


class WordGuesser(EasyFrame):
    def __init__(self):

        EasyFrame.__init__(self, title="Word Guesser 1.0")

        self.addLabel(text="Word: ", row=0, column=0)
        self.actualWordField = self.addTextField(text="", row=0, column=1)

        self.addLabel(text="Guess: ", row=1, column=0)
        self.guessField = self.addTextField(text="", row=1, column=1)

        self.addButton(text="Guess It!", row=2, column=0, columnspan=2, command=self.checkWord)

        self.addLabel(text="Points: ", row=4, column=0)
        self.pointField = self.addIntegerField(value=0, row=4, column=1)

    def checkWord(self):
        if count == 0:
            self.changeWord()

        elif self.guessField.getText().upper() == word.upper():
            self.changeWord()
            self.addPoints()
            self.guessField.option_clear()
            self.messageBox(title="Correct!", message="You got it!\n\n+1 Points")
        else:
            self.messageBox(title="Incorrect", message="Incorrect Guess, Try Again!")

    def changeWord(self):
        global word
        word = self.getWord()
        shuffled = list(str(word))
        random.shuffle(shuffled)
        shuffled = ''.join(shuffled)
        self.actualWordField.setText(shuffled)

    def addPoints(self):
        global points
        points += 1
        self.pointField.setNumber(points)

    def getWord(self):
        global count
        words = open("words.txt")
        lines = words.readlines()
        print(len(lines))
        count += 1
        if (count - 1) >= len(lines):
            self.messageBox(title="Complete!", message="You have successfully completed all words!\n\n"
                                                       "Game will exit now.")
            exit()
        else:
            return lines[count - 1].strip()


WordGuesser().mainloop()
