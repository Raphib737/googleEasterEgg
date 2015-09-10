import requests
import re

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
def fib_seq(value):
	total = 0
	if value == 0:
		return 0
	elif value ==1:
		return 1
	else: 
		num1 = 1
		num2 = 0
		for x in range(2,value+1):
			temp_var = total
			total = num1 + num2
			num2 = num1
			num1 = total
		return total


url = 'https://www.find.foo/api/challenge'
token='uwKdi9DgBHeFiYTTKCSy6X'
r = requests.get(url, headers={"token":token})
data = r.content.split("\n")[1].split("\"")[3].split(" ")
sign = True
counter = 0
value = 0
for x in data:
	try:
		x = int(x)
		if sign ==True:
			value = value + x
		else :
			value = value - x
	except ValueError:
		if x == "+":
			sign = True
		else:
			sign = False 

d = requests.post(url,data={'answer':value,'token':token})
data = d.content.split("\n")[1].split("\"")[3].split(" ")
print(data)
list1 = []
for x in data:
	try:
		x = int(x.strip(','))
		list1.append(x)
	except ValueError:
		pass

x=min(list1)
y=max(list1)
list1.remove(x)
list1.remove(y)

maxGCD = gcd(x,y)
for x in list1 :
	if maxGCD == gcd(maxGCD,x):
		maxGCD = gcd(maxGCD,x)

p = requests.post(url,data={'answer':maxGCD,'token':token})
print p.content
data = p.content.split("\n")[1].split('\"')[3].split(" ")
data[0] = data[0].replace("("," ")
data[0] = data[0].replace(")"," ")
answer = fib_seq(int(data[0].split(" ")[1]))


