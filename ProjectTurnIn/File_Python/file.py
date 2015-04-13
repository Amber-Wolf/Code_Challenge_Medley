class Split:
	def __init__(self, t, h, p, c):
		self.time = int(t)
		self.heart = int(h)
		self.cadence = int(c)
		x = p.split(":")
		self.pace = int(x[0]) * 60 + int(x[1])



def rFile(file):
	f = open(file,"r")
	global splits
	splits = []
	for line in f:
		pieces = line.split()
		splits.append(Split(pieces[0],pieces[1],pieces[2],pieces[3]))
		#print(pieces[2])



def helpTime(time1, time2, x):
	while x < len(splits) and splits[x].pace < time2 and splits[x].pace > time1:
		x = x + 1
	return x

def findTime(time1,time2):
	x = 0
	a = 0
	b = 0
	c = 0
	ta = 0;
	tb = 0;
	while x < len(splits):
		if splits[x].pace < time2 and splits[x].pace > time1:
			tempA = x
			tempB = helpTime(time1,time2,x)
			x = tempB
			timeA, timeB, ttA, ttB = splits[a].time,splits[b].time,splits[tempA].time,splits[tempB].time
			tt, time = ttB - ttA, timeB - timeA
			if tt >  time:
				a, b, ta, tb = tempA , tempB, ttA, ttB
		else:
			x = x + 1
	c = tb - ta
	return [ta, tb, c]

if __name__ == "__main__":
	import sys
	rFile("run.txt")
	res1 = findTime(390,420)
	res2 = findTime(420,450)
	res3 = findTime(450,480)
	print("The longest time between 390 and 420 seconds are " + str(res1[0]) + " and " + str(res1[1]) )
	print("The longest time between 420 and 450 seconds are " + str(res2[0]) + " and " + str(res2[1]) )
	print("The longest time between 450 and 480 seconds are " + str(res3[0]) + " and " + str(res3[1]) )


