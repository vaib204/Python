def displayCheckPerfect(no):
  isum = 0

  for i in range(1,(no//2)+1):
    if(no % i == 0):
      isum += i
  return (isum == no)
 

def main():
  print("Enter  NUmber")
  value  = int(input())

  
  bret = displayCheckPerfect(value)

  if(bret):
   print(f"{value}: is perfect")
  else:
   print(f"{value}: is not perfect")
  
if __name__  == "__main__":
  main()


  