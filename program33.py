
def main():
 print("Enter the number of elements")
 ilength = int(input())

 Arr = []

 print("Please enter the element:")

 for i in range(1,ilength+1):
  no = int(input())
  Arr.append(no)

  print(Arr)



if  __name__ == "__main__":
  main()