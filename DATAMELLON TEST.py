#!/usr/bin/env python
# coding: utf-8

# In[45]:


import json 
import re


#store the filepath
path = "C:\\Users\\HP\\Downloads\\"

#store the data to be read in a variable 'filename'
filename = "datamellon data.txt"

# Opening JSON file 
f = open(path+filename,'r',encoding='utf-8') 
  
data = f.read()

# def jsonReadPrint():
    


# In[ ]:





# In[48]:




newdata = re.sub(r"(\\n)|(\\)",'',data)
newdata = re.sub(r"(\"\")",'',newdata)
newdata = re.sub(r"(\"{)",'{',newdata)
newdata = re.sub(r"(}\")",'}',newdata)
newdata = re.sub(r"(\"string_value:)","", newdata)


# print(newdata)


# In[49]:


newfile =open(path+"datamellon_new_data.json","w+",encoding='utf-8')


# In[50]:


newfile.write(newdata)
newfile.close()


# In[51]:


f = open(path+'datamellon_new_data.json',encoding='utf-8') 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 


# In[52]:


data['Records'][0]['Sns']['Message']['Records'][0]['body']


# In[59]:


category = data['Records'][0]['Sns']['Message']['Records'][0]['body']['category']
print(category)


# In[60]:


violation_data = data['Records'][0]['Sns']['Message']['Records'][0]['body']['violation_data']
print(violation_data)


# In[61]:


recommended_actions = data['Records'][0]['Sns']['Message']['Records'][0]['body']['violation_data']['recommended_actions']
print(recommended_actions)


# In[ ]:




