def EvenOdd(brr):
 ieven = 0
 iodd = 0
 for no in brr:
  if(no % 2 == 0):
    ieven+=1
  else:
    iodd+=1 

 return ieven,iodd

 
def main():
 print("Enter the number of elements")
 ilength = int(input())

 Arr = []

 print("Please enter the element:")

 for i in range(1,ilength+1):
  no = int(input())
  Arr.append(no)
  
 iret1,iret2 = EvenOdd(Arr)
 print(f"even count are:{iret1} odd count Are:{iret2}")
 

if  __name__ == "__main__":
  main()