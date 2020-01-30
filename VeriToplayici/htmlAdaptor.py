
import re
from bs4 import BeautifulSoup


class HtmlGet:
    def getData(self,document):
        data = []
        documents = []
        soup = BeautifulSoup(document,features="html.parser")
        for script in soup("script"):
            script.extract()
        documents.append(soup)

        for soup in documents:
            for content in soup.find_all("p"):
                #print(content.text)
                data.append(content.text.replace("\n"," "))

        return data
