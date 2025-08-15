def Display(row,col):
  for i in range(1,row+1,1):
    for j in range(1,col+1,1):
      print("*",end="\t")
    print()  


def main():
  print("Enter row")
  value1= int(input())

  print("Enter col")
  value2= int(input())

  Display(value1,value2)

if  __name__ == "__main__":
  main()


