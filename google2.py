#Challenge 1
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


#Challenge 2
def answers(names):
	finList=[];
	dictionary = {}

	for i in range(len(names)):
		names[i]=[getValue(names[i]),names[i]]

	names = reversed(sorted(names,key=lambda x: (x[0],x[1])))

	for x in names:
		finList.append(x[1])
	return finList


def getValue(name):
	alphaDict={}
	alphabet="abcdefghijklmnopqrstuvwxyz"
	let_value=1

	for x in alphabet:
		alphaDict[x] = let_value
		let_value+=1

	total = 0
	for x in name:
		total+=alphaDict[x]

	return total

print answers(["al", "cj"])
