import pandas as pd


dataset = pd.read_csv('lik500.csv',names = ["kelimeler","maz"])

dataset["kelimeler"] = dataset["kelimeler"].str.split("")

kelimeler = []
for i in range(1,len(dataset["kelimeler"])):
    size = len(dataset["kelimeler"][i])
    kelimeler.append(dataset["kelimeler"][i][1:size-1] + (22- size)*["\0"])

fl = open("lanetdosya.csv","w")
for i in range(-1,len(kelimeler)):
    for j in range(20):
        if(i == -1):
            fl.write("in"+str(j)+ ",")
        else:
            fl.write(str(ord(kelimeler[i][j])) + (","))
    if(i == -1):
        fl.write("out\n")
        continue
    if(i == len(kelimeler)): continue
    fl.write(str(dataset["maz"][i+1]) + "\n")
fl.close()
