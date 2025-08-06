def CheckDivision(No):
   if(No % 2 == 0):
       return True
   else:
       return False

def main():
    print("Enter first Number:")
    value1 = int(input())

    bret = CheckDivision(value1)

    if(bret == True):
        print(f"{value1} is even number")
    else:
        print(f"{value1} is not even number")    

    
if __name__ == "__main__":
    main()