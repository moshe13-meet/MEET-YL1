class Integer(object):
	def __init__(self, number,negative):
		self.num=number
		self.negative=negative
	def display(self):
		if self.negative=="negative":
			print "-" + str(self.num)
		else:
			print self.num
class NegativeInteger(Integer):
	def __init__(self, number):
		super(NegativeInteger, self).__init__(number, "negative")
	def display(self):
		Integer.display(self)
		print "This is an object of the NegativeInteger class"
		


if __name__=="__main__":
	#9:
	#test2 = Integer(30,"positive")
	#test1 = NegativeInteger(50)
	#list12 = [test2,test1]
	#for x in list12:
	#	x.display()
	#10:
	#pos=raw_input("please insert positive number: ")
	#neg=raw_input("please insert negative number: ")
	#posi=Integer(pos,"positive")
	#negi=NegativeInteger(neg)
	#posi.display()
	#negi.display()
	lis=[]
	a=raw_input("how many numbers: ")
	for x in range(int(a)):
		por=raw_input("positive or negative: ")
		num=raw_input("what is the number: ")
		if por == "negative":
			y=NegativeInteger(num)
		else:
			y=Integer(num,"positive")
		lis.append(y)
	for x in lis:
		x.display()



 
