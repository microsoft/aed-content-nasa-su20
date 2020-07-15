# Importing Data

Now that we know about cleaning and separating the data, we can actually apply these principles to our rock classification project.

Since the the rock images come in different sizes (small, medium, large), we will crop all images to transform them into the same size (224*224 pixels).

Additionally, at the bottom of this code block you can see that are separating the data into a training variable and a testing variable.

```python
# telling the machine what folder contains the image data
data_dir = './data'

# function to read the data, crop and resize the images and then split it into test and train chunks
def load_split_train_test(datadir, valid_size = .2):
    # this line of code transforms the images
    train_transforms = transforms.Compose([
                                       transforms.RandomResizedCrop(224),
                                       transforms.Resize(224),
                                       transforms.ToTensor(),
                                       ])

    test_transforms = transforms.Compose([transforms.RandomResizedCrop(224),
                                          transforms.Resize(224),
                                          transforms.ToTensor(),
                                      ])

    train_data = datasets.ImageFolder(datadir, transform=train_transforms)
    test_data = datasets.ImageFolder(datadir, transform=test_transforms)

    num_train = len(train_data)
    indices = list(range(num_train))
    split = int(np.floor(valid_size * num_train))
    np.random.shuffle(indices)
    from torch.utils.data.sampler import SubsetRandomSampler
    train_idx, test_idx = indices[split:], indices[:split]
    train_sampler = SubsetRandomSampler(train_idx)
    test_sampler = SubsetRandomSampler(test_idx)
    trainloader = torch.utils.data.DataLoader(train_data, sampler=train_sampler, batch_size=16)
    testloader = torch.utils.data.DataLoader(test_data, sampler=test_sampler, batch_size=16)
    return trainloader, testloader

# Using 20% of data for testingS
trainloader, testloader = load_split_train_test(data_dir, .2)
print(trainloader.dataset.classes)
```
