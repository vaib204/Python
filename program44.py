def CountChar(data):
  icount = 0
  for ch in data:
    if(ch == 'a'):
      icount+=1

  return icount    


def main():
  print("Enter String")

  str = input()

  iret = 0

  iret = CountChar(str)

  print(f"count is:{iret}")

if __name__ == "__main__":
  main()

