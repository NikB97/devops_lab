def selfDividingNumbers(left, right):
	def self_dividing(n):
		for d in str(n):
			if d == '0' or n % int(d) > 0:
				return False
		return True
	ans = []
	for n in range(left, right + 1):
		if self_dividing(n):
			ans.append(n)
	return ans 

print ("enter left and right borders of list:") 
a=(int(input()))  
b=(int(input()))  
print(selfDividingNumbers(a,b))

