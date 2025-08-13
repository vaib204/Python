def CountVowel(data):
  icount = 0
  for ch in data:
    if ch in 'aeiouAEIOU':
      icount+=1

  return icount    


def main():
  print("Enter String")

  str = input()

  iret = 0

  iret = CountVowel(str)

  print(f"vowel count is:{iret}")

if __name__ == "__main__":
  main()

