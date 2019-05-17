class node:
  def __init__(self,x):
    self.data=x
    self.nextt=None

class sll:
  def __init__(self):
    self.head=None
  def insertAtBeg(self):
    v=int(input())
    new=node(v)
    new.nextt=self.head
    self.head=new
    
  def display(self):
    temp=self.head
    while temp!=None:
      print(temp.data,end="  ")
      temp=temp.nextt
    
  def deleB(self):
    temp=self.head
    self.head=temp.nextt
    temp.nextt=None

  def search(self):
    v=int(input())
    temp=self.head
    p=1
    while temp.data!=v and temp.nextt!=None:
      temp=temp.nextt
      p+=1
    if temp.data==v:
      print("found",p)
    else:
      print("not  found")
  
  def deleGiven(self):
    v=int(input())
    temp=self.head
    prev=temp
    if self.head.data==v:
      self.head=self.head.nextt
      temp.nextt=None
    while temp.data!=v and temp.nextt!=None:
      prev=temp
      temp=temp.nextt
    if temp.data==v :
      prev.nextt=temp.nextt
      temp.nextt=None
    
    else:
      print("not found")


    


sl=sll()
ch=0
while ch!=4:
  print("1.insertB 2.Delb 3.Display  4.search 5.DeleGiven")
  ch=int(input())
  if  ch==1:
    sl.insertAtBeg()
  elif ch==2:
    sl.deleB()
  elif  ch==3:
    sl.display()
  elif ch==4:
    sl.search()
  elif  ch==5:
    sl.deleGiven()

