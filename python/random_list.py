from random import randint
def randlist(r, usedlist, done):
	alpha = ["a", "b", "c", "d", "e", "f"]
	usedlist[r] = 1
	c = alpha[r]
	sum = 0
	for i in range(len(usedlist)):
		sum = sum + usedlist[i]
	done = True
	return c, usedlist,# this is belongs to ranlist(r)
	
def main():
	used = [0,0,0,0,0,0]
	done = False
	while True:
		r = randint(0, 5)# make a random number
		done = 0
		c,used = randlist(r,used,done)
		print (used)
main ()
