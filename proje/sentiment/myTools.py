
charset = list("qwertyuioplkjhgfdsazxcvbnm, 1234567890\n")

class CleanData:

  def deleteUnascii(content):
    tempS = ""
    for char in content:
      if char in charset:
        tempS += char
    return tempS

  def deleteStopWords(data):
    fl_ = open("/var/www/html/proje/sentiment/turkce-stop-words","r")
    stopwords = fl_.read().split()
    fl_.close()
    for word in stopwords:
      data = data.replace(" "+word+" "," ")
      data = data.replace(""+word+",",",")
      data = data.replace(","+word+" ",",")
    return data
