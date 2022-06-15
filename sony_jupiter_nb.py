#!/usr/bin/env python
# coding: utf-8

# 

# In[250]:


import pandas as pd
import numpy as np
df=pd.read_csv('example.csv')
df.columns


# In[254]:


#selecting reuired asset_type_or_class
clas=['archive',
'Audio Stem',
'Dubbed Audio',
'OV Audio',
'package',
'Restored Audio']
df = df.loc[df['asset_type_or_class'].isin(clas)]


# In[256]:


#Exclude files that match: folder_names:"Trailer"
df = df.loc[~df['folder_names'].str.contains("Trailer")]


# In[ ]:





# In[274]:


def task3(df):
    df['meta_discrepancy'] =''
    for index,row in df.iterrows():
        l =[]
        if pd.isnull(row['title_gpms_ids']) or row['title_gpms_ids'] == " ":
        #print("ss")
            l.append(''.join("title_gpms_ids"))
        if(pd.isnull(row['custom_metadata.content_details.language_dubbed']) or row['custom_metadata.content_details.language_dubbed']== " "):
            l.append(''.join("custom_metadata.content_details.language_dubbed"))
        if(pd.isnull(row['custom_metadata.dcs.dcs_vendor'] ) or row['custom_metadata.dcs.dcs_vendor']== " "):
            l.append(''.join("custom_metadata.dcs.dcs_vendor"))
        if(pd.isnull(row['custom_metadata.format_details.audio_configuration']) or row['custom_metadata.format_details.audio_configuration']== " " ):
            l.append(''.join("custom_metadata.format_details.audio_configuration"))
        if(pd.isnull(row['custom_metadata.format_details.audio_element'])  or row['custom_metadata.format_details.audio_element'] == " "):
            l.append(''.join("custom_metadata.format_details.audio_element"))
        df.at[index,'meta_discrepancy'] = l
    return(df)


# In[279]:


df=task3(df)

#writing into new file csv
df.to_csv("newfile.csv",index=False)


# In[278]:





# In[ ]:




