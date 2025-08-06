def Addition(No1, No2):
    Sum = No1 + No2
    return Sum

def main():
    print("Enter first Number:")
    value1 = int(input())

    print("Enter second Number:")
    value2 = int(input())

    Ans = Addition(value1, value2)

    print(f"Addition of {value1} & {value2} is: {Ans}")

if __name__ == "__main__":
    main()