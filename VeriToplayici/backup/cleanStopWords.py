import re
path = input("Temizlenecek belgenin adi:")

fl = open(path,"r")

data = fl.read()

fl.close()

fl = open("stopwords_cleaned2","r")
stopwords = fl.read().split()
fl.close()

for word in stopwords:
    data = re.sub(r"\b"+word+r"\b","",data)

fl = open(path+"_cleanedFromStopwords","w")

fl.write(data)
fl.close()
