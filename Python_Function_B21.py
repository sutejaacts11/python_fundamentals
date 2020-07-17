#!/usr/bin/env python
# coding: utf-8

# In[1]:


#How to define function.

def greet_user():
    """Display a simple greeting"""     #Used for giving comments in functions
    print("Hello I am going to start Python")


# In[8]:


greet_user()


# In[11]:


#Passing Information to function

def greet_user(username):
    """Display a simple greeting"""
    
    print(f"Hello, {username.title()}")
    
    


# In[12]:


greet_user('Suteja')


# In[13]:




# Introduction to Parameters and arguments:

def describe_pet(Animal_type,pet_name):
    """Display information about pet"""
    print(f"\n I have a {Animal_type}")
    print(f"\n My {Animal_type}'s name is {pet_name.title()}'")
    
    
    


# In[15]:


describe_pet('Dog','Bruno')


# In[16]:


# Mutiple Function call:

describe_pet('Dog','Bruno')
describe_pet('Cat','Snowbell')


# In[ ]:




