
# coding: utf-8

# In[2]:


print('hello world')


# In[3]:


a=21


# In[4]:


b=11


# In[5]:


a+b


# In[9]:


import numpy as np


# In[10]:


my_list = [-17, 0, 4, 5, 9]
my_array_from_list = np.array(my_list)
my_array_from_list


# In[14]:


my_array_from_list * 10 + 1


# In[15]:


my_vector = np.array ([-17, -4, 0, 2, 21, 37, 105])


# In[16]:


my_vector


# In[17]:


my_vector[0]


# In[18]:


my_array= np.arange(35)
my_array.shape = (7,5)# esto indica la cantida de filas y columnas del array
my_array


# In[19]:


my_array[2]


# In[20]:


my_array[5,2] # muestra el elemento en fila 5 columna 2


# In[25]:


x= np.arange(4)
y= (2,3,4,5)


# In[30]:


x,y


# In[31]:


x*y


# In[32]:


x.sum()


# In[48]:


n = x.size
nvector = (x*y).sum()
suma_x = x.sum()
suma_y = y.sum()
raiz_x = (x**2).sum()


# In[49]:


import matplotlib.pyplot as plt


# In[ ]:


plt.scater

