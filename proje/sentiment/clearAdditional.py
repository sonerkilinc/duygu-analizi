# -*- coding: latin1 -*- 
import re,os,sys,codecs
class DataCleaner:
    def __init__(self):
        self.punc = "!'^+%&/()=?_.,;:\'\"";
        self.tr_Characters = [["\u00E7","c"],["\u011F","g"],
                                                                 ["\u0131","i"],["\u015F","s"],
                                                                 ["\u00F6","o"],["\u00FC","u"],
                                                                 ["\u00C7","c"],["\u011E","g"],
                                                                 ["\u0130","i"],["\u015E","s"],
                                                                 ["\u00D6","o"],["\u00DC","u"]]
    def deleteStopWords(self,data):
        stopwords = DataCleaner.read("/var/www/html/proje/sentiment/tsw").split()
        for word in stopwords:
            data = re.sub(r"(\^|\s)"+word+r"(\s|&)"," ",data)
        return data
    def deletePunctation(self,data):
        for char in self.punc:
            data = data.replace(char," ")
        return data

    def deleteAdditional(self,data):
        if(len(data) == 0):
            return ""
        pre = data[0]
        counter = 0
        content = pre
        for i in range(1,len(data)):
            now = data[i]
            if(pre != now):
                if(counter == 1):
                    content += pre
                content += data[i]
                pre = data[i]
                counter = 0
            else:
                counter += 1
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
    def deleteTurkishCharacters(self,content):
        for char in self.tr_Characters:
            content = content.replace(char[0],char[1])
        return content

    def deleteUnascii(self,content):
        tempS = ""
        for char in content:
            if(char == " "):
                tempS += " "
                continue
            elif(char == "\n"):
                tempS += "\n"
                continue
            if(ord(char) > 95 and ord(char) < 123):
                tempS += char
        return tempS

    def Clear(self,data):
        try:
            data = self.deletePunctation(data)
            data = self.deleteTurkishCharacters(data)
            data = data.lower()
            data = self.deleteUnascii(data)
            data = self.deleteAdditional(data)
            data = self.deleteStopWords(data)
            data = data.replace("\n ","\n")
            data = data.replace("\n\n","\n")
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            raise Exception(str(exc_type) +  str(fname) +  str(exc_tb.tb_lineno)+str(e))
        return data
