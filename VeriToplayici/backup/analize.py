import sys
def sortSecond(val): 
    return val[1]  

def read(path):
    file_ = open(path,'r')
    content = file_.read()
    file_.close()
    return content


path = sys.argv[1]
reversed_ = sys.argv[2]
size = 10
if(len(sys.argv) > 3):
    size = int(sys.argv[3])
if(path == ""):
    print("Please pass a file argument")
data = read(path).split()

word_dict = dict()

for word in data:
    try:
        a = word_dict[word]
        word_dict[word] = a + 1
    except KeyError:
        word_dict[word] = 1
items = word_dict.items()
items2 = []

for item in items:
    items2.append(list(item))

items2.sort(key= sortSecond, reverse = (True if reversed_ =="1" else False))

for item in items2[:size]:
    print(item)
