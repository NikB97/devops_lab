list="qwertyuiopasdfghjklzxcvbnm"
print("enter keyboard letter")
letter=str(input())	
if letter=="m":
	print(list[0]) 
else:
	index=list.find(letter)
	print(list[index+1])

