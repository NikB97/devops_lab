from collections import OrderedDict
dict = OrderedDict()

print("enter number of distinct words:")
number=int(input())

print("enter words:")
for i in range(number):
	key = input()
	if not key in dict.keys():
		dict.update({key : 1})
		continue
	dict[key] += 1

print(len(dict.keys()))
print(*dict.values())
