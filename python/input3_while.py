print ("INPUTE THREE NUMBERS")
A = float(input("\tA : "))
B = float(input("\tB : "))
C = float(input("\tC : "))
x = -5
while True:
	y = A*(x*x) + B*x + C
	print (x,y)
	x = x + 1
	if(x > 5):
	    break
