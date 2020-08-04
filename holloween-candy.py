# Programe Name "Halloween Candy"
# Deepak Jaiswar with Help.

#Programe Name
print("Helloween Candy?")

#visited house amount.
print("Give the input of number of houses you visited? ")
house = int(input("House = "))

a = 200 / house
b = int(a)
c = a - b

#
print("")
if c > 0:
	print("Ans = ", b+1)
else:
    print(b)