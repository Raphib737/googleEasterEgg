def answer(str):
	numQueue=[]
	multList=[]
	addList=[]
	numSeq=""
	finString=""

	for x in str:
		numSeq+=x
		print (x,numSeq,finString)
		if x == "+":
			numSeq = numSeq[:-1]
			numQueue.append(numSeq)
			numSeq=""
			addList.append("+")
			for z in numQueue:
				finString += z
			while len(numQueue) >0 : numQueue.pop()
			for y in multList:
				finString += y
			while len(multList) >0 : multList.pop()

		elif x == "*":
			numSeq = numSeq[:-1]
			multList.append("*")
			numQueue.append(numSeq)
			numSeq=""

	for x in numQueue:
		finString += x
	finString+=numSeq
	for x in multList:
		finString += x
	for x in addList:
		finString += x

	return finString


str = "2*4*3+9*3+5"
print(answer(str))
