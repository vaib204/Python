def DisplayDigit(no):
  idigit = 0

  while(no != 0):
    idigit = no % 10
    no = no//10
    print(idigit)

def main():
  print("Enter Number:")
  value = int(input())

  DisplayDigit(value)

if __name__ == "__main__":
  main()      
    