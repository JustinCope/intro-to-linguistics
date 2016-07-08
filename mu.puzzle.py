
import string
import re

axiom = "MI"

# input is axiom, stop is integer
def MU_Puzzle_Solver(input, stop):
    theorems = []
    stack = [input]
    while len(theorems) <= stop:
        top = stack[0]
        if top[-1] == "I":
            newSentence = top + "U"
            stack.append(newSentence)
            theorems.append(newSentence)
            print newSentence
        if top[0] == "M":
            newSentence = top + top[1:]
            stack.append(newSentence)
            theorems.append(newSentence)
            print newSentence
        indices = [m.start() for m in re.finditer('(?=III)', top)]
        for index in indices:
            newSentence = top[:index]+ "U" + top[index+3:]
            stack.append(newSentence)
            theorems.append(newSentence)
            print newSentence
        indices = [m.start() for m in re.finditer('(?=UU)', top)]
        for index in indices:
            newSentence = top[:index] + top[index+2:]
            stack.append(newSentence)
            theorems.append(newSentence)
            print newSentence
        stack.pop(0)
    if "MU" in set(theorems):
        print "We found MU!"
    else:
        print ":("
    return 

