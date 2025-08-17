def Demo():
  def __init__(self):
   print("Inside constructor")

  def __del__(self):
    print("Inside destructor") 


def main():
  print("Inside main")
  obj1 = Demo()
  obj2 = Demo()

  del obj1
  del obj2

  print("End of main")

if __name__ == "__main__":
  main()  