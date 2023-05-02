#!/usr/bin/env python
# coding: utf-8

# # printing hello world

# ## printing hello world

# ### Printing Hello World

# #### printing hello world

# ##### printing hello world

# ###### printing hello world

# In[ ]:


# shortcut key
run->shift + enter
insert cell above->press a
insert cell below->press b
markdown->press m+shift+enter



# In[9]:


print("hello world")


# In[10]:


print("hello saurav")


# ## datatypes

# In[11]:


x=100
x


# In[12]:


print(x)


# In[13]:


type(x)


# In[14]:


x=10.6
type(x)


# In[15]:


y="saurav"
type(y)


# In[16]:


course="ai"
print(type(course))
print(course)


# In[17]:


type(course),course


# ### rules for naming variables

# In[19]:


book_name=["python","ai","ds"]
book_name


# In[20]:


book names=["python","ds","ai"]
book names


# In[21]:


3book_name=["ai","ds","dm"]
3book_name


# In[23]:


booknames=["python","ai","ds"]
booknames


# ### space is not allowed in python
# ### only special character allowed is underscore
# ### variable name should  not start with a number
# ### variable name should start with A-Z,a-z,or underscore
# ### green colour words appearing are keywords
# 

# ## Data Structures

# ## LISTS
# #### square brackets
# #### we can retrieve elements using index and index start from 0
# #### mutable->we can make the changes

# In[24]:


sample_list=[1,2,3,4,5,"hi"]
sample_list


# In[26]:


type(sample_list)


# In[27]:


sample_list[3]


# In[28]:


sample_list[10]
sample_list


# In[29]:


sample_list[0]=10
sample_list


# ## TUPLES
# #### paranthesis
# #### immutable->we cannot make the changes
# #### we can retrieve elements using index and index start from 0

# In[30]:


sample_tuple=(10, 2, 3, 4, 5, 'hi')
sample_tuple


# In[31]:


type(sample_tuple)


# In[32]:


sample_tuple[0]


# In[33]:


sample_tuple[10]


# In[34]:


sample_tuple[0]=100
sample_tuple


# In[37]:


sample_set={1,2,3,4,5,6,8,45,3,4,6,'hi'}
sample_set


# ### SETS
# #### square brackets
# #### duplicates are not allowed
# #### arranged according to first place
# #### cannot access using index
# #### set is mutable

# In[38]:


sample_set[0]


# In[40]:


sample_set.add(25)
sample_set


# In[41]:


sample_set.remove(45)
sample_set


# ## dictionary
# ####  it has key value pair data structure
# #### key is unique
# #### values can be duplicacted
# #### values can be retrieved using key
# #### key cannot be retrieved using value

# In[1]:


sample_dict={1:"apple",2:35.4,3:'data',2:"every",6:35.4,7:35.4,2:"hi"}
sample_dict


# In[2]:


sample_dict[3]


# In[3]:


sample_dict["apple"]


# In[4]:


sample_dict[7]=100


# In[5]:


sample_dict


# In[ ]:




