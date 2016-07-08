boy = ('boi', "boy")
house = ('haus', "house")
believe = ('bəliv', "believe")
start = ('stɑɹt', "start")
meet = ('mit', "meet")
short = ('ʃɔrt', "short")
happy = ('hapi', "happy")


N = set([boy,house])
V = set([believe,start,meet])
A = set([short,happy])

def PL(input):
	if input in N:
		return (input[0] + '-z', input[1] + "-PL")
	return

def PST(input):
	if input in V:
		return (input[0] + '-d', input[1] + "-PST")
	return

def CMPR(input):
	if input in A:
		return (input[0] + '@r', input[1] + "-CMPR")
	return


