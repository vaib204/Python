def Maximum(brr):
 iMax = 0

 for no in brr:
  if(no > iMax):
   iMax = no

 return iMax

 
def main():
 print("Enter the number of elements")
 ilength = int(input())

 Arr = []

 print("Please enter the element:")

 for i in range(ilength+1):
  no = int(input())
  Arr.append(no)
  
 iret = Maximum(Arr)
 print (f"Maximum element is:{iret}")



if  __name__ == "__main__":
  main()