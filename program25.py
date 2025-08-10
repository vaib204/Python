def displayfactor(no):
  print(f"factors of {no}are:")

  for i in range(1,no):
    if(no % i == 0):
      print(i)

def main():
  print("Enter  NUmber")
  value  = int(input())

  displayfactor(value)
  
if __name__  == "__main__":
  main()


  