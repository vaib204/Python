def Addition(brr):
 isum = 0

 for no in brr:
  isum += no

 return isum 

 
def main():
 print("Enter the number of elements")
 ilength = int(input())

 Arr = []

 print("Please enter the element:")

 for i in range(ilength+1):
  no = int(input())
  Arr.append(no)
  
 iret = Addition(Arr)
 print (f"Addition of all element:{iret}")



if  __name__ == "__main__":
  main()