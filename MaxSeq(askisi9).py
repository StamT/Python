#convert str list to int list 
def Str_Int():
	InputByUser=input('Give me your list : ')
	strL=InputByUser.strip('[]')
	aList=strL.split(',')
	bList=[]
	for i in aList:
			bList.append(int(i))
	MaxSeq(bList)	
#Max Seq list function
def MaxSeq(lista):
	a=len(lista)
	store2=[]
	for i in range (0,a-3):
		a=(lista[i])
		b=(lista[i+1])
		c=(lista[i+2])
		d=(lista[i+3])
		new=[a,b,c,d]
		store2.append(new)
	print("The result is:",sum(max(store2)),':',max(store2))

Str_Int()



	