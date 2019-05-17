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

  def  insertAtEnd(self):
    v=int(input())
    new=node(v)
    temp=self.head
    while temp.nextt!=None:
      temp=temp.nextt
    if temp.nextt==None:
      temp.nextt=new
  
  def delEnd(self):
    temp=self.head
    prev=temp
    while temp.nextt!=None:
      prev=temp
      temp=temp.nextt
    if  temp.nextt==None:
      prev.nextt=None
    
  def insertM(self):
    v=int(input())
    temp=self.head
    pos=1
    while pos<v:
      temp=temp.nextt
      pos+=1
    if v==pos:
      val=int(input())
      new=node(val)
      
      new.nextt=temp.nextt
      temp.nextt=new

sl=sll()
ch=0
while ch>9:
  print("1.insertB 2.DelBeg 3.Display  4.search 5.DeleGiven  6.insertAtEnd 7.DelEnd 8.InsertMid")
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
  elif  ch==6:
    sl.insertAtEnd()
  elif ch==7:
    sl.delEnd()
  elif ch==8:
    sl.insertM()

