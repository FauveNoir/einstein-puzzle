#!/usr/bin/env python
# -*- coding: utf-8 -*-
# frdepartment : mainfile
#!/usr/bin/python

import random
import sys
from tabulate import tabulate
from optparse import OptionParser

usage = "usage: %prog [ --lvl [0-5] | ]"
parser = OptionParser(usage=usage, version="%prog 0.1")

parser.add_option("--lvl",              help="set a level from 0 to 5",              default=0, action="store", dest="lvlchoosen")
(options, args) = parser.parse_args()

if not options.lvlchoosen:
    options.lvlchoosen = 0



#latn = ["A", "B", "C", "D", "E", "F"]
#grek = ["Σ", "Ω", "Π", "Γ", "Δ", "Ψ"]
#arab = ["ﻃ", "ﺱ", "ﺭ", "ﺝ", "ﺏ", "ﺃ"]
#cyrl = ["Д", "Ж", "И", "Л", "Ш", "Ы"]
#hebr = ["א", "ב", "ה", "ע", "ש", "פ"]
#armn = ["Ե", "Ձ", "Թ", "Ս", "Խ", "Գ"]
#
#canonicalTable = [latn, grek, arab, cyrl, hebr, armn]
#
#
#i = 0
#while i < 6:
#    # Adding to each language group 5 letters
#    items = [[0,""], [1,""], [2,""], [3,""], [4,""], [5,""]]
#    random.shuffle(items)
#    solution.append(items)
#    i+=1
#
#
#for row in solution[0]:
#    row[1] = latn[row[0]]
#
#for row in solution[1]:
#    row[1] = grek[row[0]]
#
#for row in solution[2]:
#    row[1] = arab[row[0]]
#
#for row in solution[3]:
#    row[1] = cyrl[row[0]]
#
#for row in solution[4]:
#    row[1] = hebr[row[0]]
#
#for row in solution[5]:
#    row[1] = armn[row[0]]
#
#presentablesolution = []
#for line in solution:
#    line2 = []
#    for row in line:
#        row = row[1].decode('utf-8')
#        line2.append(row)
#    presentablesolution.append(line2)
#
##print(presentablesolution)
#print tabulate(presentablesolution, headers=[0, 1, 2, 3, 4, 5])
#
#
#
#
#obfuscated = solution
#
#presentablesolution = []
#for line in obfuscated:
#    line2 = []
#    for row in line:
#        row = row[1].decode('utf-8')
#        line2.append(row)
#    presentablesolution.append(line2)
#print tabulate(presentablesolution, headers=[0, 1, 2, 3, 4, 5])
#



##reduce possibilities
#numberOfCaseShowen=random.randint(numberOfCaseShowenRange[0], numberOfCaseShowenRange[1])
#
#showenRows=sorted(random.sample(range(0, 35),  numberOfCaseShowen))
#print(showenRows)
#
#tempRowFullRange=0
#tempLine=0
#showenRow = range(0,6)
#for line in obfuscated:
#    rowNumber=0
#    for row in line:
#        if tempRowFullRange not in showenRows:
#            row = canonicalTable[tempLine]
#            obfuscated[tempLine][rowNumber] = canonicalTable[tempLine]
#        tempRowFullRange+=1
#        rowNumber+=1
#    tempLine+=1
#
#print(obfuscated)
#
#
#
##TODO###################################################
##for line in obfuscated:
##    line2 = []
##    for row in line:
##        if isinstance(row , list):
###            print("yata")
##            print(row)
###            row = "-".join(row)
##           # print(row)
##        row = row[1].decode('utf-8')
##        line2.append(row)
##    presentablesolution.append(line2)
##print tabulate(presentablesolution, headers=[0, 1, 2, 3, 4, 5])
#
########################################################################
########################################################################
########################################################################

maxLines = 6
maxColumns = 6

class Row:
    def __init__(self, realValue): 
        self.realValue = ""
        self.seenValues = range(0,maxColumns)
        if isinstance(self.seenValues, list):
            self.isReduced = False
        else:
            self.isReduced = True
        def reduceit():
            if self.realValue != "":
                self.seenValues = self.realValue


def generateNewTable():
    tempTable = []
    i = 0
    while i < maxLines:

        tempTable.append([])
        items = range(0,maxColumns)
        random.shuffle(items)
        j = 0
        while j < maxColumns:
            tempRow = Row(items[j])
            tempTable[i].append(tempRow)
            j+=1
        i+=1

    return tempTable

table = generateNewTable()

# Obfuscation



print "You choose level", options.lvlchoosen
if options.lvlchoosen:
    if options.lvlchoosen not in ["0", "1", "2", "3", "4"]:
        print("You have to chose a level from 0 to 4")
    else:
        if options.lvlchoosen == "0":
            numberOfCaseShowenRange   = (0,1)
            numberOfTipsBeforeSolving = (5,7)
        if options.lvlchoosen == "1":
            numberOfCaseShowenRange   = (2,3)
            numberOfTipsBeforeSolving = (4,6)
        if options.lvlchoosen == "2":
            numberOfCaseShowenRange   = (4,5)
            numberOfTipsBeforeSolving = (3,5)
        if options.lvlchoosen == "3":
            numberOfCaseShowenRange   = (5,6)
            numberOfTipsBeforeSolving = (2,4)
        if options.lvlchoosen == "4":
            numberOfCaseShowenRange   = (7,8)
            numberOfTipsBeforeSolving = (1,3)

random.randint(numberOfCaseShowenRange[0], numberOfCaseShowenRange[1])
numberOfCaseShowen = random.randint(numberOfCaseShowenRange[0], numberOfCaseShowenRange[1])


i=0
for i in xrange(0, numberOfCaseShowen):
    randomrow = [random.randint(0,maxLines-1),random.randint(0,maxColumns-1)]
    if not table[randomrow[0]][randomrow[1]].isReduced :
        table[randomrow[0]][randomrow[1]].reduceit
        i+=1

print(table)
