"""hw2_t5"""
# pylint: disable=invalid-name
liste = "qwertyuiopasdfghjklzxcvbnm"
print("enter keyboard letter")
letter = str(input())
if letter == "m":
    print(liste[0])
else:
    index = liste.find(letter)
print(liste[index+1])
