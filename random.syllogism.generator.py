import random

Major = "wugs"
Minor = "modis"
Middle = "blebus"

def A(x,y):
    return("All " + x + " are " + y + ".")

def E(x,y):
    return("No " + x + " are " + y + ".")

def I(x,y):
    return("Some " + x + " are " + y + ".")

def O(x,y):
    return("Some " + x + " are not " + y + ".")


def Fig1(major, minor, middle, a, b, c):
    print a(middle,major)
    print b(minor,middle)
    print("Therefore: " + c(minor,major))

def Fig2(major, minor, middle, a, b, c):
    print a(major,middle)
    print b(minor,middle)
    print("Therefore: " + c(minor,major))

def Fig3(major, minor, middle, a, b, c):
    print a(middle,major)
    print b(middle,minor)
    print("Therefore: " + c(minor,major))

def Fig4(major, minor, middle, a, b, c):
    print a(major,middle)
    print b(middle,minor)
    print("Therefore: " + c(minor,major))

def syllogism(figure, major, minor, middle, a, b, c):
    return figure(major, minor, middle, a, b, c)

def randomSyllogism(major,minor,middle):
    figures = [Fig1, Fig2, Fig3, Fig4]
    figureNames = ["Fig1", "Fig2", "Fig3", "Fig4"]
    frames = [A, E, I, O]
    frameNames = ["A", "E", "I", "O"]
    figVar = random.randint(0,3)
    a = random.randint(0,3)
    b = random.randint(0,3)
    c = random.randint(0,3)
    syllogism(figures[figVar], major, minor, middle, frames[a], frames[b], frames[c])
    return figureNames[figVar] + ":" + frameNames[a] + frameNames[b] + frameNames[c]


valid = set(["Fig1:AAA", "Fig1:AAI", "Fig1:AII", "Fig1:EAE", "Fig1:EAO", "Fig1:EIO", "Fig2:AEE", "Fig2:AEO", "Fig2:AOO", "Fig2:EAE", "Fig2:EAO", "Fig2:EIO", "Fig3:AAI", "Fig3:AII", "Fig3:EAO", "Fig3:EIO", "Fig3:IAI", "Fig3:OAO", "Fig4:AAI", "Fig4:AEE", "Fig4:AEO", "Fig4:EAO", "Fig4:EIO", "Fig4:IAI"])



