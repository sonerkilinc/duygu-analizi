import re

punc = "!'^+%&/()=?_.,;:\'\"";


tr_Characters = [["\u00E7","c"],["\u011F","g"],
                 ["\u0131","i"],["\u015F","s"],
                 ["\u00F6","o"],["\u00FC","u"],
                 ["\u00C7","c"],["\u011E","g"],
                 ["\u0130","i"],["\u015E","s"],
                 ["\u00D6","o"],["\u00DC","u"]]


def deleteStopWords(data):
    stopwords = read("stopwords").split()
    for word in stopwords:
        data = re.sub(r"(\^|\s)"+word+r"[\s|&]"," ",data)
    return data

def deletePunctation(data):
    for char in punc:
        data = data.replace(char," ")
    return data

def deleateAdditional(data):
    pre = data[0]
    counter = 0
    content = pre
    for i in range(1,len(data)):
        if(pre == data[i]):
            counter += 1
        else:
            if(counter == 1):
                if(pre != " "):
                    content += pre
            counter = 0
            pre = data[i]
        if(counter == 0):
            content += data[i]
    return content

def read(path):
    file_ = open(path,"r")
    content = file_.read()
    file_.close()
    return content


def write(path,content):
    file_ = open(path,"w")
    file_.write(content)
    file_.close()

def deleteTurkishCharacters(content):
    for char in tr_Characters:
        content = content.replace(char[0],char[1])
    return content

path = input("Temizlenecek dosya Path:")

data = read(path)
data = deletePunctation(data)
data = deleteTurkishCharacters(data)
data = data.lower()
data = deleteStopWords(data)
data = deleateAdditional(data)

data = data.replace("\n ","\n")
path += "_cleaned"
write(path+"",data)
