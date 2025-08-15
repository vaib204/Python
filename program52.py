def Display(data):
  for ch in data:
    print(ch,end="\t")

def main():
  print("Enter String")
  str = input()

  Display(str)

if  __name__ == "__main__":
  main()


