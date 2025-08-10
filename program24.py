def Countx(no):
  idigit = 0
  icount = 0

  while(no != 0):
    idigit = no % 10
    if(idigit == 5):
      icount = icount+1
    no = no//10

  return icount

def main():
  print("Enter Number:")
  value = int(input())

  iret = 0

  iret = Countx(value)
  print(f" frequency of 5 is:{iret}")

if __name__ == "__main__":
  main()      
    