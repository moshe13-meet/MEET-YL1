import random
def pali():
	x=raw_input("write n: ")
	while x!="n" :
		x=raw_input("try again: ")
	z=raw_input("probabilliy for heads: ")
	z=int(z)

	while int(z) >= 101:
		z=raw_input("don't insert more than 100,try again: ")
	ht=random.randint(0,100)
	if ht >= (100-z):
		print "H"
	else:
		print "T"

def etz():
	z=raw_input("probabilliy for heads: ")
	z=int(z)
	while int(z) >= 101:
		z=raw_input("don't insert more than 100,try again: ")
	x=raw_input("write n: ")
	while x!="n" :
		x=raw_input("try again: ")
	
	
pali()

