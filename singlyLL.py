class Node:
  def __init__(self,no):
    self.data = no
    self.next = None
##################################################################################################3
class SinglyLL:
  def __init__(self):
    self.first = None
    self.icount = 0
##########################################################################################
  def InsertFirst(self,no):
    newn = Node(no)
  
    if(self.first == None):
     self.first = newn
    else:
     newn.next = self.first
     self.first  = newn

    self.icount = self.icount + 1
 
##############################################################################################3
  def Display(self):
    temp = self.first

    while(temp != None):
     print(f"|{temp.data}| -> ",end = "")
     temp = temp.next

    print(None)        
#####################################################################################################
  def InsertLast(self,no):
    newn = Node(no)
    
    if (self.first == None):
      self.first = newn
    else:
      temp = self.first

      while(temp.next != None):
        temp = temp.next

      temp.next = newn  

    self.icount = self.icount + 1

##################################################################################################
  def DeleteFirst(self):
   if(self.first == None):
    return
   else:
    temp = self.first
    self.first = self.first.next
    del temp

   self.icount = self.icount + 1
 
 ################################################################################################
  def DeleteLast(self):
    if(self.first == None):
      return
    elif(self.first.next == None):
      del self.first
      self.first = None
    else:
      temp = self.first

      while(temp.next.next != None):
        temp = temp.next

      del temp.next

      temp.next = None 

    self.icount = self.icount + 1
   
#################################################################################################
  def InsertAtPos(self ,no,pos):
    if(pos == 1):
      self.InsertFirst(no)
    elif(pos == self.icount+1):
      self.InsertLast(no)
    else:
      newn = Node(no)

      temp = self.first

      for i in range(1,pos-1):
        temp = temp.next

      newn.next = temp.next
      temp.next = newn     

      self.icount = self.icount + 1
      
##################################################################################################
  def DeleteAtPos(self,pos):
    if(pos == 1):
      self.DeleteFirst()
    elif(pos == self.icount):
      self.DeleteLast()
    else:
      
      temp = self.first

      for i in range(1,pos-1,1):
        temp = temp.next

      target = temp.next

      temp.next = target.next

      del target

      self.icount = self.icount - 1
            

##################################################################################################

  def Count(self):
     return self.icount

def main():
    obj = SinglyLL()

    print("\n=============================================================")
    print("                    Singly Linear Linked List                 ")
    print("=============================================================")

    while True:
        print("\n-------------------------------------------------------------")
        print(" Please select an option:")
        print("-------------------------------------------------------------")
        print("1. Insert new node at first position")
        print("2. Insert new node at last position")
        print("3. Insert new node at given position")
        print("4. Delete the node at first position")
        print("5. Delete the node at last position")
        print("6. Delete the node at given position")
        print("7. Display all elements of LinkedList")
        print("8. Count all elements of LinkedList")
        print("0. Terminate the application")
        print("-------------------------------------------------------------")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            no = int(input("Enter the data you want to insert : "))
            obj.InsertFirst(no)

        elif choice == 2:
            no = int(input("Enter the data you want to insert : "))
            obj.InsertLast(no)

        elif choice == 3:
            no = int(input("Enter the data you want to insert : "))
            pos = int(input("Enter the position at which you want to insert new node : "))
            obj.InsertAtPos(no, pos)

        elif choice == 4:
            print("Deleting the first element form LinkedList")

            obj.DeleteFirst()

        elif choice == 5:
            print("Deleting the last element form LinkedList")

            obj.DeleteLast()

        elif choice == 6:
            print("Deleting the element from given position form Linked List")

            pos = int(input("Enter the position at which you want to delete the node : "))
            obj.DeleteAtPos(pos)

        elif choice == 7:
            print("Elements of the Linked List are : ")

            obj.Display()

        elif choice == 8:
            print(f"Number of elements in the Linked List are : {obj.Count()}")

        elif choice == 0:
            print("Thank you for using our application")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()