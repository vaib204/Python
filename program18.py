def Factorial(no):
  ifact = 1

  for i in range(1,no+1):
    ifact = ifact * i

    return ifact

def main():
  print("Enter number")
  value = int(input())

  iret = Factorial(value)
  print(f"Factorial is :{iret}")  

if __name__ == "__main__":
  main()
  