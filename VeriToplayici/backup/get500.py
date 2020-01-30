import re

def hasNumbers(text):
    return bool(re.search(r'\d',text))

fl = open("words.csv","r")
k = fl.read().split("\n")[:501]
fl.close()
fl = open("lik500.csv","w")
fl.write(k[0] + "\n")
for i in range(1, 501):
    if(hasNumbers(k[i].split(",")[0])):
        continue
    if(k[i][-1] == ","):
        k[i] += "0"
    fl.write(k[i] + "\n")

fl.close()



