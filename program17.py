def Addition(no):
  isum = 0

  for i in range(1,no+1):
    isum = isum + i

    return isum

def main():
  print("Enter number")
  value = int(input())

  iret = Addition(value)
  print(f"Addition is :{iret}")  

if __name__ == "__main__":
  main()
  