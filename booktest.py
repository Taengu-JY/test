from gensim.summarization.summarizer import  summarize
import pandas as pd
import  numpy as np

df = pd.read_csv('Book_test.csv')
df = df.iloc[0:100]
df.reset_index(inplace=True)

