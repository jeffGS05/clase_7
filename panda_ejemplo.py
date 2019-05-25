
# coding: utf-8

# In[14]:


import pandas as pd
notas_juan = {'Español':90,'Mate': 80, 'Sociales': 85, 'Ciencias': 95}
notas_juan =pd.Series(notas_juan)
notas_juan


# In[17]:


notas_juan.mean()


# In[18]:


notas_juan.min()


# In[19]:


notas_juan.max()


# In[20]:


notas_juan[notas_juan >= 90]

