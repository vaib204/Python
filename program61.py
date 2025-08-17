class Demo():
  def __init__(self,A = 0,B = 0):
   print("Inside constructor")
   self.No1 = A
   self.No2 = B

  def Addition(self):
      return  self.No1 + self.No2

  def sub(self):
      return self.No1 - self.No2



def main():
 obj1 = Demo(11,10)

 iret = obj1.Addition()
 print(f"Addition is :{iret}")

 iret = obj1.sub()
 print(f"sub is:{iret}")

if __name__ == "__main__":
  main()  