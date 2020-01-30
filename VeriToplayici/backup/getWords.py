
fl = open("allComments_cleaned","r")
k = fl.read()
fl.close()


k = k.replace(" ","\n")
k = k.replace("\n\n","\n")

word_dict = dict()
data = k.split("\n")
for word in data:
    try:
        if(len(word) < 3):
            continue
        a = word_dict[word]
        word_dict[word] = a + 1
    except KeyError:
        word_dict[word] = 1

items = word_dict.items()
items2 = []


fl = open("words","w")
for word in items:
    fl.write(word[0] + ","+str(word[1])+"\n")
fl.close()

