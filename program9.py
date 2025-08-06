def CheckMaximum(No1,No2,No3):
    if(No1 > No2 and No1 > No3):
        return No1
    elif(No2 > No1 and No2 >No3 ):
        return No2
    else:
        return No3
    
def main():
    print("Enter first Number:")
    value1 = int(input())

    print("Enter second Number:")
    value2 = int(input())

    print("Enter third Number:")
    value3 = int(input())

    bret = CheckMaximum(value1,value2,value3)

    print(f"Maximum value is :",bret)   

    
if __name__ == "__main__":
    main()