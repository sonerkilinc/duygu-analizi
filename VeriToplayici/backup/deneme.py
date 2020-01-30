import pandas as pd
import numpy as np
import torch
import pickle

fl = open("net","rb")
net = pickle.load(fl)
fl.close()

word = input("Kelimeyi giriniz: ")

word_inp = []
for i in word:
    word_inp.append(ord(i))

word_inp += (20 - len(word))*[0]

print(word_inp)

inp = np.array(word_inp)

inputs = torch.autograd.Variable(torch.Tensor(inp).float())

out = net(inputs)
print(out.data)
_,predicted = torch.max(out.data,1)
print(predicted)

