def printVals():
	print(tree)
	#print(tree.values())
	#print("stage final clear")

def startLine():
	global CHECKSEMICOLON, FORGOSEMICOLON, loopMode, loopCounter, loopMax, buffer, forBuffer, END, bufferCounter
	iLine = interpretLine()
	if iLine == END:
		printVals()
	elif iLine == CHECKSEMICOLON:
		try:
			getWord()
			if loopMode and (len(buffer) <= bufferCounter):
				loopCounter = loopCounter + 1
				if loopCounter < loopMax:
					buffer = list(forBuffer)
					bufferCounter = 0
				else:
					loopMode = False
			startLine()
		except NameError:
			x = 0
	elif iLine == FORGOSEMICOLON:
		if loopMode and (len(buffer) <= bufferCounter):
			loopCounter = loopCounter + 1
			if loopCounter < loopMax:
				buffer = list(forBuffer)
				bufferCounter = 0
			else:
				loopMode = False
		startLine()
	else:
		print("Major ERROR")
		print("Code is: " + str(iLine))


def interpretLine():
	global CHECKSEMICOLON, FORGOSEMICOLON, DEF, FOR, loopCounter, loopMax, forBuffer, bufferCounter, loopMode, buffer
	codeVal = 100
	try:
		key = getWord()
		if key != '':
			kWord = findKeyword(key)
			if kWord == -1:
				interpretOperator(key)
				codeVal = CHECKSEMICOLON
			elif kWord == DEF:
				tree[getWord()] = 0 
				codeVal = CHECKSEMICOLON
			elif kWord == FOR:
				loopCounter = 0
				loopMax = int(getWord())
				set = getWord()
				holder = ""
				while set != "ENDFOR":
					holder += set + " "
					set = getWord()
				forBuffer = holder.split()
				buffer = list(forBuffer)
				bufferCounter = 0
				loopMode = True
				codeVal = FORGOSEMICOLON
		else:
			codeVal = END
	except NameError:
		codeVal = END
	return codeVal

def interpretOperator(key):
	global PLUS, tree, TIMES, EQUALS
	op = findOperator(getWord())
	operand = getWord()
	opVal1 = 0
	opVal2 = 0
	if(operand in tree):
		opVal2 = tree[operand]
	else:
		opVal2 = int(operand)
	if op == PLUS:
		opVal1 = tree[key]
		tree[key] = opVal1 + opVal2
		#print("plus performed")
	elif op == TIMES:
		opVal1 = tree[key]
		tree[key] = opVal1 * opVal2
	elif op == EQUALS:
		tree[key] = opVal2
	else:
		print("major error in operators")
		
		
def getWord():
	global buffer, bufferCounter
	#print("stage 2 reached ")
	#print("stage 2 reached " + str(len(buffer)))
	if buffer is None:
		buffer = []
	if ( buffer is None or ( len(buffer) <= bufferCounter)):
		rawString = myReadLine()
		if(rawString == "\n"):
			return getWord()
		buffer = rawString.split()
		bufferCounter = 0
		return getWord()
	else:
		returnVal = buffer[bufferCounter]
		bufferCounter = bufferCounter + 1
		if returnVal == "":
			return getWord()
		return returnVal

def findKeyword(term):
	global keyWords
	val = -1
	x = 0
	while x < len(keyWords):
		if term == keyWords[x]:
			val = x 
			x = len(keyWords)
		x = x + 1
	return val
	
def findOperator(op):
	global operators
	val = -1
	x = 0
	while x < len(operators):
		if op == operators[x]:
			val = x 
			x = len(operators)
		x = x + 1
	return val
		
def myReadLine():
	global f
	ret = f.readline()
	#print("line is " + ret)
	if ret == "":
		raise NameError('HiThere')
	return ret
	
if __name__ == "__main__":
	global DEF
	global FOR
	global ENDFOR
	global PLUS 
	global TIMES 
	global EQUALS 
	global END 
	global CHECKSEMICOLON 
	global FORGOSEMICOLON 
	global keyWords 
	global operators 
	global tree 
	global buffer 
	global forBuffer 
	global bufferCounter 
	DEF = 0
	FOR = 1 
	ENDFOR = 2
	PLUS = 0
	TIMES = 1
	EQUALS = 2
	END = -1
	CHECKSEMICOLON = 0
	FORGOSEMICOLON = 1
	keyWords = ["DEF","FOR","ENDFOR"]
	operators = ["+=","*=","="]
	tree = {}
	buffer = []
	forBuffer = []
	bufferCounter = 0
	global loopMode 
	global valueKey
	global loopCounter
	global loopMax
	global readerVal
	#print("stage 1 clear")
	global f
	import sys
	fileToOpen = str(sys.argv[1])
	print("Opening file " + fileToOpen)
	f = open(fileToOpen,"r")
	loopMode = False
	startLine()