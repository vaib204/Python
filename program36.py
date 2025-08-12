def Minimum(brr):
 iMin = 0 = brr[0]

 for no in brr:
  if(no < iMin):
   iMin = no

 return iMin

 
def main():
 print("Enter the number of elements")
 ilength = int(input())

 Arr = []

 print("Please enter the element:")

 for i in range(ilength+1):
  no = int(input())
  Arr.append(no)
  
 iret = Minimum(Arr)
 print (f"Minimum element is:{iret}")



if  __name__ == "__main__":
  main()