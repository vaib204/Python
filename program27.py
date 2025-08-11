def displaySumfactor(no):
  isum = 0
  print(f"factors of {no}are:")

  for i in range(1,(no//2)+1):
    if(no % i == 0):
      isum = isum + i
  return isum

def main():
  print("Enter  NUmber")
  value  = int(input())

  iret = 0
  iret = displaySumfactor(value)
  print(f"Summesion is:{iret}")
  
if __name__  == "__main__":
  main()


  