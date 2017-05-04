import numpy as np
import pandas as pd
import json

df = pd.read_csv("Desktop/final.csv")
ff1=pd.DataFrame(df)    

#list1=[]
#list1=df.author.unique()
value=''
value2=''
count=0

for line1,line in df.iterrows():
    
    if (line['author']==value)& (line['subreddit_id']==value2):
            count=count+1
            value=line['author']
            value2=line['subreddit_id']
            df.loc[(df['author'] == value) & (df['subreddit_id'] == value2),value2] = count

            
    else:
        value=line['author']
        value2=line['subreddit_id']
        count=1
        df.loc[(df['author'] == value) & (df['subreddit_id'] == value2),value2] = count

df.to_csv("lo1.csv")

df2 = pd.read_csv("lo1.csv")

df2=df2.drop_duplicates(subset=['author', 'subreddit_id'])

df2.to_csv("lo3.csv")
grouped = ff1.groupby('author')
grouped.aggregate(np.sum)