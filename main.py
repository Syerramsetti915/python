
# # # # # s1=input("enter s1")
# # # # # s3= input ("enter s3")
# # # # # def s(s1,s3):
# # # # #   print("output "+ s1 + "  input. " + s3)


# # # # # s(s1,s3)


# # # # # s={'a':'b1', 'a2':'b2'}
# # # # # b= input('enter key')
# # # # # z= input('enter value')
# # # # # s[b]=z

# # # # # print (s)


# # # # s =['s','sw','se']
# # # # b='zzzzzz'
# # # # s[0]=b

# # # # print (s)

# # # for i in range(10):
# # #   try: 
# # #     if 10 / i == 2.0:
# # #       break
# # #   except ZeroDivisionError:
# # #     print(1)
# # #   else:
# # #     print(2)

# # # # for i in count (3):
# # # #     print (i)
# # # #     if i >=11:
# # # #       break


# # # # a={1, 2}
# # # # print(len(list(product(range(3), a))))



# # # try:
# # #   z=open('tests.txt','a')
# # #   z.write(' test ')
# # #   z.close()
# # #   bz=open('tests.txt','r')
# # #   a= bz.read()
# # #   print (a)
# # # except FileNotFoundError :
# # #   print('yes')

# # #print ('hi')

# # # else:
# # #   print("no")

# # # z.close()

# # #print(z)



# # class PythonTraining :

# #     def bookwriting(self): #========> Instance method is defined under class
# #         print ('book writing code')

# # @staticmethod #=======> this decorator is used to mark method as StaticMethod
# # def boardreading(): #========> static method
# #     print ('book writing code')

# # @classmethod #========> this decorator is used to mark method as ClassMethod
# # def boardreading(cls): #========> class method
# #     print ('book writing code')


# # class PythonTraining :
# # 	board = 'White Bloard'  #========> class variables are declared under class

# # 	def bookwriting(self,name):  #========> Instance method
# # 		print ("I am writing by booke at"+ str(name))

# # 	def listning(self,name): #========> Instance method
# # 		print ("I am listeneing perfectly"+ str(name))

# # 	def understanding(self, percentage): #========>Instance method
# # 		print ("I understood the class :" + str(percentage))


# # 	@staticmethod # decorator used to mark method as static or classic method
# # 	def boardreading(): 
# # 		print ("I understood the class :")

# # @classmethod
# # def boardreading(cls): 
# # 	print ("I understood the class :")

# # x=PythonTraining() #========>object x created so it can use all the methods defined in the class  


# # # Defining instance variables for object X
# # x.pen='Parker' #========>Instance variables are declared under object (object is an instance of a class)
# # x.book='Rule' 

# # # Calling instance variables for object X
# # x.bookwriting(x.pen)
# # x.understanding ('90% : X') #========> calling class method
# # # Creation of object for class
# # y = PythonTraining() #========>object Y created 

# # # Defining instance variables for object Y 
# # y.pen='Reynolds'
# # y.book='White Note Book'

# # # Calling instance variables for object Y
# # y.bookwriting(y.pen)
# # y.understanding('80% : Y')


# # print (PythonTraining.board)

# # PythonTraining.boardreading()




# class PythonTraining:
#     def __init__(self, a, b):
#         print("iam a constructor method")
#         self.book = b
#         self.pen = a

#     def display(self):
#         print ('my book is '+self.book)
#         print ('my pen is '+self.pen)

# # object creation
# x = PythonTraining('Parker', 'White Notebook')
# x.display()  # calling method from the class pythonTraining
# # new object created
# y = PythonTraining('Reynolds', 'Rule Notebook')
# y.display()


# for i in range(4):
#     print(i)

# li = ["dog", "cat", "mouse"]
# for animal in li:
#     # You can use format() to interpolate formatted strings
#   print(animal)
# #print (li)
# x = input("enter")
# li.append(x)
# s= li.sort()
# print(li)
