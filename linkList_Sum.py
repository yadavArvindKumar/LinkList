#!/usr/bin/env python
# coding: utf-8

# In[24]:


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


# In[25]:


class SLinkedList:
    def __init__(self):
        self.headval = None
    
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
            
    def addNode(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode


# In[33]:


linkList = SLinkedList()
linkList.addNode(2)
linkList.addNode(4)
linkList.addNode(3)


linkList2 = SLinkedList()
linkList2.addNode(5)
linkList2.addNode(6)
linkList2.addNode(8)


# In[34]:


linkList.listprint()


# In[35]:


linkList2.listprint()


# In[19]:





# In[20]:





# In[ ]:




