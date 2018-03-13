"""hw2_t4"""
# pylint: disable=invalid-name
dicte = {}

print("enter number of distinct words:")
number = int(input())

print("enter words:")
for i in range(number):
    key = input()
    if key not in dicte.keys():
        dicte.update({key: 1})
        continue
    dicte[key] += 1

print(len(dicte.keys()))
print(*dicte.values())
