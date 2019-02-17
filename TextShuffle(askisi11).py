#import random 
import random
#path for read the txt
text=open(r"c:\users\apros\Desktop\word.txt",'r')
#create var for keep information after close it
Maintext=text.read()
#close 
text.close() 
#seperated by ' '
SeperatedText=Maintext.split()
#new list for after use
StoredText=[]
#'for loop' in order to create triads
for i in range (len(SeperatedText)-2):
	A=SeperatedText[i]
	B=SeperatedText[i+1]
	C=SeperatedText[i+2]
	Triads=A,B,C
	StoredText.append(Triads)

#randomly appearance
random.shuffle(StoredText)
#new list for after use
FinalText=[]
#'for loop' in stored text for seperate triads from list
for i in StoredText:
	FinalText+=i
#'for loop' for readable results
for i in FinalText:
	print(i,' ',end='')









