#!/usr/bin/env python3
import random
import tkinter
from breezypythongui import EasyFrame


infile = open("words.txt", "r")
lines = infile.readlines()


def __init__(self):
    """Sets up the window and the widgets."""
    EasyFrame.__init__(self, title="Tax Calculator")

    # Label and field for the income
    self.addLabel(text="Income", row=0, column=0)
    self.incomeField = self.addFloatField(value=0.0, row=0, column=1)

    # Label and field for the number of dependents
    self.addLabel(text="Dependents", row=1, column=0)
    self.depField = self.addIntegerField(value=0, row=1, column=1)

    # Label and field for the exemption amount
    self.addLabel(text="Exemption amount", row=2, column=0)
    self.exeField = self.addFloatField(value=0.0, row=2, column=1)
    # The command button
    self.addButton(text="Compute", row=3, column=0,
                   columnspan=2, command=self.computeTax)

    # Label and field for the tax
    self.addLabel(text="Total tax",
                  row=4, column=0)
    self.taxField = self.addFloatField(value=0.0,
                                       row=4,
                                       column=1,
                                       precision=2)