def Display(no):
  for i in range(no,0,-1):
    print(i,end="\t")


def main():
  print("Enter Number")
  value = int(input())

  Display(value)

if __name__ == "__main__":
  main()  