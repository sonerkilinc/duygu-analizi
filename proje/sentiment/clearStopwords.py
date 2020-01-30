from myTools import CleanData
path = input("path:")


fl = open(path,"r")
content = fl.read()
fl.close()

content = CleanData.deleteStopWords(content)
print(content)
content = CleanData.deleteUnascii(content)

print(content)
fl = open(path+".cleaned","w")
fl.write(content)
fl.close()

