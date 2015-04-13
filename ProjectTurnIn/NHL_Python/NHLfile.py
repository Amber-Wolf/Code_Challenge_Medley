class Data:
	def __init__(self, t, l, d):
		self.time = t
		self.location = l
		self.data = d.split()

def rFile(file):
	f = open(file,"r")
	global datas
	datas = []
	for line in f:
		if line.find("\t") > -1:
			pieces = line.split('\t')
			datas.append(Data(pieces[0],pieces[1],pieces[2]))

def cGoals(fN,lN):
	count = 0
	for d in datas:
		if d.data.count(fN) > 0 and (d.data.count("scored") > 0 or d.data.count("Scored") > 0):
			a = d.data.index(fN)
			b = d.data.index("by")
			c = 0;
			if d.data.count("scored") > 0:
				c = d.data.index("scored")
			else:
				c = d.data.index("Scored")
			if c == a -2:
				count = count + 1
			#else:
				#print("scored name fail")
	return count

if __name__ == "__main__":
	import sys
	rFile("NHL.txt")
	print("Goals by Travis Zajac: " + str(cGoals("Travis","Zajac")))
	print("Goals by Jaromir Jagr: " + str(cGoals("Jaromir","Jagr")))
	print("Goals by Dmitry Kulikov: " + str(cGoals("Dmitry","Kulikov")))
	print("Goals by Dan Ellis: " + str(cGoals("Dan","Ellis")))