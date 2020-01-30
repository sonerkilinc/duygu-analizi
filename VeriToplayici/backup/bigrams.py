import pandas as pd
import numpy as np

df = pd.read_csv("allComments_cleaned",names=["yorum","positivity"],encoding="iso-8859-9",sep="\n")


df["positivity"] = 1
df.to_csv(r'allComments_cleaned.csv')
print(df)

from sklearn.model_selection import train_test_split
X_train , X_test,y_train,y_test = train_test_split(df["yorum"],df["positivity"],random_state=0)



from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer(min_df=5,ngram_range = (1,2)).fit(X_train)
X_train_vectorized = vect.transform(X_train)

print(X_train_vectorized)



while(True):
    yorum=input("Yorumunuz Nedir?(Programdan çıkmak için \'F\' yazınız)")
    if(yorum == 'F' or yorum == 'f'):
        break
    else:
        print(vect.transform([yorum]))
