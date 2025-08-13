def ReverseArray(brr):
   itemp = 0
   istart = 0
   iend = len(brr)-1

   while(istart < iend):
      itemp = brr[istart]
      brr[istart] = brr[iend]
      brr[iend] = itemp

      istart+=1
      iend-=1




def main():
  print("Enter Number")
  ilength = int(input())

  Arr = []

  print("Enter the Elements")
  for i in range(ilength):
      no = int(input())
      Arr.append(no)

  ReverseArray(Arr)
  print(Arr)

if __name__ == "__main__":
   main()