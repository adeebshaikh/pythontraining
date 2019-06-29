#!/usr/bin/env python
# coding: utf-8

# In[2]:


x=10;
if(x<15):
    print("the number is less than 15");


# In[1]:


print(3>=3)


# In[8]:


x=10;
if(x>15):
    print("hello good morning");
else:
    print("hello good afternoon");


# In[11]:


x=10
y=5
if(x<y):
    print(x,"is smallest number")
else:
    print(y,"is largest number")
    


# In[19]:


x=10
y=20
z=30
if(x>y and x>z):
    print("x is largest")
elif(y>z and y>x):
    print("y is largest")
else:
    print("z is largest")
    
  


# In[22]:


x=10
y=10
res=x*x
res1=x*y
if(x==y):
    print(res)
else:
    print(res1)


# In[24]:


x=10
if(x<0):
    print("nagative number")
elif(x>0):
    print(x,"positive")
elif(x==0):
    print("zero")


# In[2]:


n =1
while(n<=10):
    print(n)
    n=n+1


# In[1]:


n=10
while(n>=1):
    print(n)
    n=n-1


# In[1]:


x=-22
while(x>=-45):
    print(x)
    x=x-1


# In[5]:


x= int(input("enter lower limit"))
y= int(input("enter the upper limit"))
s=0
while(x<=y):
     if(x%2==0):
            s=s+x
     x=x+1
print(s)

    

    


# In[2]:


x=int(input("enter the number"))
r=0
while(x>0):
    r=x%10
    print(r)
    x=x//10
    
    


# In[ ]:




