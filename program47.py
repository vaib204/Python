def CountSmall(data):
  icount = 0
  for ch in data:
    if(ch >= 'a' and ch <= 'z'):
      icount+=1

  return icount    


def main():
  print("Enter String")

  str = input()

  iret = 0

  iret = CountSmall(str)

  print(f"Small Charchter count is:{iret}")

if __name__ == "__main__":
  main()

