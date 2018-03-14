
# coding: utf-8

# In[3]:


from glob import glob
for file in glob("416-ADH-*.seq"): # Any combination for the file names
    f= open(file,"r")  
    for lines in f.readlines():
        AllSeq= open("AllSeq.seq", "a")
        AllSeq.write(lines)
    f.close()
AllSeq.close()    

