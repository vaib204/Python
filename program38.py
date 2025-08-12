def CountEvenOdd(brr):
 ieven = 0
 icount = 0
 for no in brr:
  if(no % 2 == 0):
    ieven+=1

 return ieven,len(brr)-ieven

 
def main():
 print("Enter the number of elements")
 ilength = int(input())

 Arr = []

 print("Please enter the element:")

 for i in range(1,ilength+1):
  no = int(input())
  Arr.append(no)
  
 iret1,iret2 = CountEvenOdd(Arr)
 print(f"even count are:{iret1} odd count Are:{iret2}")
 

if  __name__ == "__main__":
  main()