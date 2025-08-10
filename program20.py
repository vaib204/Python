def DisplaySumDigit(no):
  idigit = 0
  isum = 0

  while(no != 0):
    idigit = no % 10
    isum = isum + idigit
    no = no//10

  return isum

def main():
  print("Enter Number:")
  value = int(input())

  iret = DisplaySumDigit(value)
  print(f"addition is:{iret}")

if __name__ == "__main__":
  main()      
    