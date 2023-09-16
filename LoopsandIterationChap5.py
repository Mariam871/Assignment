#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=5
while n>0:
    print(n)
    n=n-1
print('Blastoff!')
print(n)


# In[2]:


n=0
while n>0:
    print('Lather')
    print('Rinse')
print('Dry Off!')    


# In[ ]:


while True:
    line=input('>')
    if line=='done':
        break
    print(line)
    print('Done!')


# In[ ]:


while True:
    line =input('> ')
    if line[0]=='#':
        continue
    if line=='done':
        break
    print(line) 
print('Done!')    


# In[ ]:


for i in[5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')    


# In[ ]:


friends=['joseph','Glenn','Sally']
for friend in friends:
    print('Happy New Year:',friend)
print('Done!')    


# In[ ]:





# In[ ]:




