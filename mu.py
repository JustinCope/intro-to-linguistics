import re
import time

rule1 = re.compile(r"(.*I)$")
rule2 = re.compile(r"^(M)(.+)")
rule3 = re.compile(r"(.*)III(.*)")
rule4 = re.compile(r"(.*)UU(.*)")

queue = ["MI"]

while queue[0] != "MU":
	x = queue.pop(0)
	print x
	time.sleep(1)
	r1 = rule1.search(x)
	r2 = rule2.search(x)
	if r1 != None:
		queue.append(r1.expand(r'\1U'))	
			
	if r2 != None:
		queue.append(r2.expand(r'\1\2\2'))	
			
	if rule3.search(x) != None:
		for n in re.finditer(rule3,x):
			queue.append(n.expand(r'\1U\2'))		
				
	if rule4.search(x) != None:
		for n in re.finditer(rule4,x):
			queue.append(n.expand(r'\1\2'))
			

	


 