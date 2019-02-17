#every numberword be a function an return an int
def zero():
	x=0
	return x
def one():
	x=1
	return x
def two():
	x=2
	return x
def three():
	x=3
	return x
def four():
	x=4
	return x
def five():
	x=5
	return x
def six():
	x=6
	return x
def seven():
	x=7
	return x
def eight():
	x=8
	return x
def nine():
	x=9
	return x
def plus(x,y):
	f=x+y
	return f
def minus(x,y):
	f=x-y
	return f 
def multi(x,y):
	f=x*y
	return f
def div(x,y):
	f=x//y
	return f

def Calculator():
	#list with words with 10 positions
	lst = ['zero','one','two','three','four','five','six','seven','eight','nine']
	#list with functions with the same number of pos the 'lst' for identify words<-->functions
	FunctionLst = [zero(),one(),two(),three(),four(),five(),six(),seven(),eight(),nine()]
	#input 
	userInput = str(input('Give your numberWords x(x(x())) : '))
	
	finalList=[]
	#seperate the input from user and create a new list with 4 positions wich i use only the first 3
	finalList=userInput.split('(')
	#look for the right numberword and identify the function list for first numberword
	for i in range(10):
		if lst[i] == finalList[0]:
			x=FunctionLst[i]
	#look for the right numberword and identify the function list for second numberword
	for i in range(10):
		if lst[i] == finalList[2]:
			y=FunctionLst[i]
	#if input word == choosenword call the right function 
	if finalList[1] == 'plus':
		print(plus(x,y))
		#restart the programm 
		Calculator()
	
	if finalList [1] == 'minus':
		print(minus(x,y))
		Calculator()
	
	if finalList [1] == 'multi':
		print(multi(x,y))
		Calculator()
	#div and 'try / except' for zero div 
	try:
		if finalList[1] == 'div':
			print(div(x,y))
			Calculator()
	except:
		print('invalid INPUT,Division with zero')
		Calculator()
		
Calculator()

	


