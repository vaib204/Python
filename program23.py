def reverse(no):
  idigit = 0
  irev = 0

  while(no != 0):
    idigit = no % 10
    irev = irev * 10 + idigit
    no = no//10

  return irev

def main():
  print("Enter Number:")
  value = int(input())

  iret = 0

  iret = reverse(value)
  print(f" reverse elements are:{iret}")

if __name__ == "__main__":
  main()      
    