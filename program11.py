def Division(No1,No2):
  Ans = 0
  Ans = No1 // No2   # we use floar division

  return Ans

def main():
   print("Enter first Number")
   value1 = int(input())

   print("Enter first Number")
   value2 = int(input())

   iret = Division(value1,value1)

   print(f"Division is :{iret}")

if __name__ == "__main__":
   main()