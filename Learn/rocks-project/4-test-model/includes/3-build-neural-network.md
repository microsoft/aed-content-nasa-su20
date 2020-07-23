# Exercise - Build a Neural Network to Classify Space Rocks

Now lets Build a neural network / deep network to learn the associations between features (curves, edges, texture, ...) and each rock type.

A neural network is a computer system that is modeled after the human brain and nervous system. This is how we will teach the computer to recognize different features.

```python
# Determine if you are using a CPU or GPU for building the deep learning network
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.resnet50(pretrained=True)
```

```python
# Freeze parameters so we don't backprop through them
for param in model.parameters():
    param.requires_grad = False

# Parameters of our deep learning model
model.fc = nn.Sequential(nn.Linear(2048, 512),
                                 nn.ReLU(),
                                 nn.Dropout(0.2),
                                 nn.Linear(512, 2),
                                 nn.LogSoftmax(dim=1))
criterion = nn.NLLLoss()
optimizer = optim.Adam(model.fc.parameters(), lr=0.003)
model.to(device)
print('done')
```

The Neural Network goes back and forth many times till it learns the best associations between features and rock types.

<img src="Media/dl.gif" width="650" align="center">