class BandMatrix:
	def __init__(self, s):
		self.mainDiagnol = s
		self.mIndices = s+2 * (s - 1)
		self.band = [0] * (s + 2 * (s - 1))

	def setVal(self,r,c,v):
		mIndex = self.convertHelp(r,c)
		if(mIndex != -1):
			self.band[mIndex] = v
			
	def getVal(self,r,c):
		mIndex = self.convertHelp(r,c)
		if(mIndex != -1):
			return self.band[mIndex]
		else:
			return 0
			
	def convertHelp(self,r,c):
		val = -1
		shift = r - c
		if(self.mainDiagnol <= r) or (self.mainDiagnol <= c):
			return -1
		else:
			shift2 = r
			if((shift > 1) or (shift < -1)):
				return -1
			if(-shift + r >= self.mainDiagnol):
				return -1
			if(shift == -1):
				val = r
			elif shift == 0:
				val = self.mainDiagnol - 1 + r
			elif shift == 1:
				val = self.mainDiagnol * 2 - 2 + r
		#print(val)
		return val
		
	def addBand(b1,b2):
		newBand = BandMatrix(b1.mainDiagnol)
		if(b1.mainDiagnol == b2.mainDiagnol):
			x = 0
			while x < (b1.mainDiagnol + 2 * (b1.mainDiagnol - 1)):
				newBand.band[x] = b1.band[x] + b2.band[x]
				x = x + 1
		else:
			print("Non-compatable matrices")
		return newBand
		
	def printRaw(self):
		for x in self.band:
			print(x)
			
if __name__ == "__main__":
	bm1 = BandMatrix(10)
	bm2 = BandMatrix(10)
	bm1.setVal(2,2,7)
	bm1.setVal(4,5,2.7)
	bm1.setVal(2,3,9)
	bm1.setVal(0,1,29)
	bm1.setVal(8,9,30)
	bm1.setVal(0,0,31)
	bm1.setVal(9,9,32)	
	bm1.setVal(7,9,99)  #will not appear in metadata
	bm1.setVal(9,7,99)  #will not appear in metadata
	bm1.setVal(9,8,33)
	#print("printing values before addition")
	#bm1.printRaw()
	bm2.setVal(9,9,100)
	#print("after addition of another matrix")
	#(bm1.addBand(bm2)).printRaw()
	print("This is the data at 2,2 :" + str(bm1.getVal(2,2)))
	print("This is the data at 9,7 :" + str(bm1.getVal(9,7)))