def Uperx(data):
  Output = ""
  for ch in data:
    if(ch >= 'a'and ch<= 'z'):
      Output = Output+chr(ord(ch)-32)
      

  return Output   


def main():
  print("Enter String")

  str = input()

  str =  Uperx(str)

  print(f"updated string is:{str}")

  

if __name__ == "__main__":
  main()

