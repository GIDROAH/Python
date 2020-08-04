# Solving simple question v.1.0
import os 
import sys

x = int(input("Pop = "))
y = int(input("Sib = "))

z = x % y
print(z)

if z == 0:
	print("give away")
else:
	print("eat them yourself")
	
#restart session
os.execl(sys.executable, sys.executable, *sys.argv)