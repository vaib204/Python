class Node:
    def __init__(self,No):
        self.Data = No
        self.next = None

class SinglyLL:
    def __init__(self):
       self.first = None
       self.icount = 0
  ############################################################################
    def InsertFirst(self,No):
        newn = Node(No)

        if(self.first == None):     # ll  is empty
            self.first = newn
        else:
            newn.next = self.first
            self.first = newn                       #ll contain atleast one node
        self.icount = self.icount+1

    #####################################################################      
    def Display(self,No):
        pass
       
    def Count(self):
        return self.icount   


    
def main():
    print("Demonstartion of singly linear linked list")
    sobj =  SinglyLL()

    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)
   
    iret = sobj.Count()
    print(f"number of ll are:{iret}")
   
      
if __name__ == "__main__":
    main()