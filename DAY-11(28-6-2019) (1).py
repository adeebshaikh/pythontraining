#!/usr/bin/env python
# coding: utf-8

# # INTRODUCTION TO OBJECT OREINTED PROGRAMMING LANGUAGE IN PYHTON
# ## 1.STRUCTURE ORIENTED PROGRAMMING--C
# ## 2. OBJECT ORIENTED LANGUAGE PROGRAMMING--C++,JAVA,C#,PYHTON
#    ### THE EXCHANGES OF DATA HAPPENS THROUGH SINGLE OBJECT IS CALLED OBJECT OREINTED LANGUAGE
#    #### ONE OF THE POPULAR APPROACH TO SOLVE A PROGRAMME PROBLEM BY CREATING AN OBJECTS.THIS IS CALLED OBJECT ORIENTED PROGRAMMING LANGUAGE
#    #### AN OBJECT HAS TO CHARACTERSTICS
#    ##### 1. ATTRIBUTES(NAME,AGE,COLOR)
#    ##### 2. BEHAVIOUR(LEARN,STUDY,SINGING,DANCE)
#    
#    
# ## IN PYTHON THE CONCEPT OOP FOLLOW THESE THINGS
# #### >1.INHERITANCE
# ##### >2.ENCAPSULATION
# ##### >3.POLYMORPHISM
# 
# 
# ## CLASS:IT IS A BLUE PRINT OF THE OBJECT
# ## functions:used to write to perform the specific task
# ## methods:used to write a logic
# ## object:blue print of class or instance of the class or physical entity
# ## methods:part of a class and can be called with object
# ## constructors;part of a class  and can be called automatically when an object is created

# In[ ]:


class ClassName:
    # some functions and variables
    # function--used to perform the specific activity
    #variables---data memory


# In[ ]:


class Demo:
    def test():
        print("test() for the class and method")
        return


# In[ ]:


def test():
    print("  test for a function    ")
    return
test()


# In[ ]:


class Demo:
    def test(self):
        print("this is called a method")
        return
obj=Demo() #object creation
obj.test() #call for the method in a class


# In[ ]:


class Demo1:
    def fact(self,n):
        fact=1
        while(n!=0):
            fact=fact * n
            n=n-1
        return fact
obj=Demo1()
print(obj.fact(5))


# In[ ]:


# method
# def tast(self,para1,para2):


# In[1]:


class Demo2:
    def accept(self,p1,p2):
        self.p1=p1
        self.p2=p2
        return
    def disply(self):
        print("p1=",p1)
        print("p2=",p2)
c1=Demo2()
c1.accept(10,20)
c1.display()


# In[2]:


class Demo2:
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
    def add(self):
        return self.p1+self.p2
c1=Demo2(100,200)
print(c1.add())


# In[ ]:


class person(object):
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self.name
    def isemp(self):
        return False
class empl(person):
    def isemp(self):
        return True
emp=person('Jotaro')
print(emp.getname(),emp.isemp())
emp1=empl('Jonathan')
print(emp1.getname(),emp1.isemp())


# In[ ]:


import numpy as np
l=[1,2,3,4]
array=np.array(l)
print(array)
print(array.shape)
print(array.dtype)


# In[ ]:


a1=np.array([(1,2,3),(4,5,6)])
print(a1)
a1.reshape(3,2)


# In[ ]:


#APPEND SOME DATA ----HORIZONTALLY
#HSTACK(ARRAY1,ARRAY2)-- will be automatically arrange
import numpy as np
a1=np.array([1,2,3])
a2=np.array([4,5,6])
print(np.hstack((a1,a2)))


# In[ ]:


import numpy as np
a1=np.array([1,2,3])
a2=np.array([4,5,6])
print(np.vstack((a1,a2)))


# In[ ]:


# Generate random number from np
a1=np.random.normal(5,0.5,10)
print(a1)


# In[ ]:


# numpy.zeroes() and numpy.one()
np.zeros((2,2))


# In[ ]:


np.zeros((2,2),dtype=np.int64)


# In[ ]:


# np.ones(shape,dtype=float,order='c')
np.ones((4,3),dtype=np.int64)


# In[ ]:


A=np.matrix(np.ones((4,4),dtype=np.int64))
print(A)


# In[ ]:


A=np.matrix(np.ones((4,4),dtype=np.int64))
np.asarray(A)[2] = 5
print(A)


# In[ ]:


A=np.matrix(np.ones((4,4),dtype=np.int64))
np.asarray(A)[1][3]=9
np.asarray(A)[3][3]=18
print(A)


# In[ ]:


# arrange()---particular()
# numpy.arrange(start,end,step)
#start---value
#end--value
# step gap between 1 value to another value
import numpy as np
np.arange(1,10)


# In[ ]:


np.arange(1,100,8)


# In[ ]:


np.arange(2,20,2)
np.arange(1,25,2)


# In[ ]:


# Indexing and Slicing7 of numpy
a1 = np.array([(1,2,3),(4,5,6)])
print(a1)


# In[ ]:


a1 = np.array([(1,2,3),(4,5,6)])
print("first row :",a1[0])


# In[ ]:


a1 = np.array([(1,2,3),(4,5,6)])
print("second row",a1[1])


# In[ ]:


a1 = np.array([(1,2,3),(4,5,6)])
print("row and column",a1[1,:2])


# In[ ]:


a1 = np.array([(1,2,3),(4,5,6)])
print(a1[:])


# In[ ]:


a1 = np.array([(1,2,3),(4,5,6)])
print(a1[:1])


# In[ ]:


a1 = np.array([(1,2,3),(4,5,6)])
print(a1[0:,1])


# In[ ]:


a1 = np.array([(1,2,3),(4,5,6)])
print(a1[:,2])


# In[ ]:


a1 = np.array([(1,2,3),(4,5,6)])
print(a1[:,0])


# In[ ]:


a1 = np.array([(1,2,3),(4,5,6)])
print(a1[1:,2])


# In[ ]:


a1 = np.array([(1,2,3),(4,5,6)])
print(a1[1:,1])


# In[ ]:





# In[ ]:


# some math operations given rsndom numbers
#min    ---returns the smallest number
#max   -----returns the largest number
#mean -- mean
# median --- median
#gausian algorithm
a1=np.random.normal(5,1,10)
print(a1)
print(np.min(a1))
print(np.max(a1))
print(np.mean(a1))
print(np.median(a1))


# In[ ]:


# multiply of 1d arrays
#numpy.dot(x,y)
c1=np.array([1,2])
c2=np.array([4,5])
np.dot(c1,c2)


# In[ ]:


c1=np.array([(1,2),(3,4)])
c2=np.array([(3,4),(1,2)])
np.dot(c1,c2)


# In[ ]:


a1 = np.array([(1,5),(6,9)])
a2 = np.array([(1,2),(4,5)])
np.matmul(a1,a2)


# # Pandas Basics
# ## pandas data frames
#       # data analysis with python
#    
# # python is offering the lib function called pandas used for importing and analysing pretty much faster and easier also

# In[ ]:


import pandas as pd
dict={"name":["anil",'akhil','dinesh','harsha','ajay','kranth'],'emailid':['anil@gmail.com','akhil@gmail.com','dinesh@gmail.com','ajay@gmail.com','harsha@gmail.com',"kranth@gmail.com"],'mobilenumber':[143,4565,265,763567,6748878,3567567],'address':['hyd','agra','chennai','delhi','mumbai','kolkata']}
b=pd.DataFrame(dict)
print(b)


# In[ ]:


b.index=["01","02","03","04","05","06"]
print(b)


# In[ ]:


# super market.csv-analyse(which product having higher % of selling)
# which products having least selling%
import pandas as pd
products=pd.read_csv('filename.csv')
print(products)


# In[ ]:




