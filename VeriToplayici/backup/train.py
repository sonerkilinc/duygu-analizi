import pandas as pd
import numpy as np
import torch
import pickle


dataset = pd.read_csv('lanetdosya.csv')
dataset = dataset.sample(frac=1,random_state = 1234)
print(dataset.values.shape)
train_input = dataset.values[:300,:20]
train_target = dataset.values[:300,20]

test_input = dataset.values[300:,:20][:]
test_target = dataset.values[300:,20]

torch.manual_seed(1234)

hidden_units = 5
fc1 = torch.nn.Linear(20,hidden_units)
fc2 = torch.nn.Linear(hidden_units,2)
net = torch.nn.Sequential(fc1,
        torch.nn.ReLU(),
        fc2)

criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(net.parameters(),lr=0.1,momentum=0.9)

epochs = 50

for epoch in range(epochs):
    inputs = torch.autograd.Variable(torch.Tensor(train_input).float())
    target = torch.autograd.Variable(torch.Tensor(train_target).long())

    optimizer.zero_grad()
    out = net(inputs)

    loss = criterion(out,target)
    loss.backward()

    optimizer.step()

    if(epoch == 0 or (epoch + 1)% 10 == 0):
        print("epoch %d Loss: %.4f" % (epoch+1,loss.item()))


inputs = torch.autograd.Variable(torch.Tensor(test_input).float())
targets = torch.autograd.Variable(torch.Tensor(test_target).long())
print(inputs)
optimizer.zero_grad()
out = net(inputs)
print(out.data)
_,predicted = torch.max(out.data,1)
print(_)
print(predicted)
error_count = test_target.size - np.count_nonzero((targets == predicted).numpy())
print('Errors: %d; Accuracy %d%%' % (error_count,100*torch.sum(targets == predicted) / test_target.size))

fl = open("net","wb")
pickle.dump(net,fl)
fl.close()

fl = open("optimezer","wb")
pickle.dump(optimizer,fl)
fl.close()
