import random

class LEXEME:
    def __init__(self,orthography="",pf="",lf=""):
        self.orthography = orthography
        # self.pf = pf # phonological form
        # self.lf = lf # logical form


class YEAR(LEXEME):
    def __init__(self):
        epoch = [" BC"]*2 + [" BCE"]*1 + [" AD"]*3 + [" CE"]*2 + [""]*4 # Weighted to make these epochal designations less probable
        LEXEME.__init__(self,str(random.randint(0,2100)) + epoch[random.randint(0,len(epoch)-1)])


class MONTH(LEXEME):
    def __init__(self):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        month = months[random.randint(0,len(months)-1)]
        LEXEME.__init__(self,month)


dates = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

def ordinal(i):
    x = str(i)[-1]
    if i > 9:
        y = str(i)[-2:]
    else:
        y = None
    if x == "1" and not y == "11":
        return str(i) + "st"
    elif x == "2" and not y == "12":
        return str(i) + "nd"
    elif x == "3" and not y == "13":
        return str(i) + "rd"
    else:
        return str(i) + "th"

class DATE(LEXEME):
    def __init__(self):
        m = MONTH()
        y = YEAR()
        d = str(random.randint(1,dates[m.orthography]))
        x = random.randint(0,2)
        if x == 0:
            a = m.orthography + " " + d
        elif x == 1:
            a = d + m.orthography
        else:
            a = "the " + ordinal(d) + " of " + m.orthography
        x = random.randint(0,1)
        if x == 0:
            b = a + ", " + y.orthography
        else:
            b = a


class SEASON(LEXEME):
    def __init__(self):
        seasons = ["spring", "summer", "fall", "autumn", "winter"]
        season = seasons[random.randint(0,len(seasons)-1)]
        LEXEME.__init__(self,season)


class WEEKDAY(LEXEME):
    def __init__(self):
        weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        weekday = weekdays[random.randint(0,len(weekdays)-1)]
        LEXEME.__init__(self,weekday)


class TIME(LEXEME):
    def __init__(self):
        n = random.randint(0,9) % 8
        if n == 0:
            x = YEAR()
            LEXEME.__init__(self,x.orthography,x.pf,x.lf)
        elif n == 1:
            x = MONTH()
            LEXEME.__init__(self,x.orthography,x.pf,x.lf)
        elif n == 2:
            x = MONTH()
            y = YEAR()
            LEXEME.__init__(self,x.orthography + " " + y.orthography, x.pf + " " + y.pf, x.lf + " " + y.lf)        
        elif n == 3:
            x = DATE()
            LEXEME.__init__(self,x.orthography,x.pf,x.lf)
        elif n == 4:
            x = SEASON()
            LEXEME.__init__(self,x.orthography,x.pf,x.lf)
        elif n == 5:
            x = SEASON()
            y = YEAR()
            LEXEME.__init__(self,x.orthography + " " + y.orthography, x.pf + " " + y.pf, x.lf + " " + y.lf)
        elif n == 6:
            x = WEEKDAY()
            LEXEME.__init__(self,x.orthography,x.pf,x.lf)
        elif n == 7:
            x = WEEKDAY()
            y = DATE()
            LEXEME.__init__(self,x.orthography + ", " + y.orthography, x.pf + " " + y.pf, x.lf + " " + y.lf)
        else:
            LEXEME.__init__(self,"")


# holidays ::= Christmas, Easter, New Year, ...
