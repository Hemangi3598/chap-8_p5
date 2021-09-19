# intro to object oriented program
class student:
	def __init__(self, r, n):
		self.rno = r
		self.name = n
	def show(self):
		print(" my rno is ", self.rno)
		print(" my name is ", self.name)
s1 = student(10, "amit")
s1.show()

s2 = student(20, "sumit")
s2.show()

'''
note1:
init ke pehele two __ and init ke baad two __
note2:
self is not a keyword it is prefferd word
self will contain the address of the object

'''

