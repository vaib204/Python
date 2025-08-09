def Display(ino):
   i =0

   while(i<ino):
     print("*",end="\t")
     i = i+1

  

def main():
  print("Enter the Number")
  value1 = int(input())

  Display(value1)

if __name__ == "__main__":
  main()  
