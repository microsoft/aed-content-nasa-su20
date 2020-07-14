# Showing images we've imported

Now that we have read the images let's check out a few of them. Copy the following code into a cell and run it. This will show you five images from the data set.

```python
def get_random_images(num):
    data = datasets.ImageFolder(data_dir, transform=test_transforms)
    classes = data.classes
    indices = list(range(len(data)))
    np.random.shuffle(indices)
    idx = indices[:num]
    from torch.utils.data.sampler import SubsetRandomSampler
    sampler = SubsetRandomSampler(idx)
    loader = torch.utils.data.DataLoader(data, sampler=sampler, batch_size=num)
    dataiter = iter(loader)
    images, labels = dataiter.next()
    return images, labels

to_pil = transforms.ToPILImage()
# how many images you want to see? set to 5 but can be changed 
images, labels = get_random_images(5)
fig=plt.figure(figsize=(20,20))

classes=trainloader.dataset.classes
for ii in range(len(images)):
    image = to_pil(images[ii])
    sub = fig.add_subplot(1, len(images), ii+1)
    sub.set_title(str(classes[index]))
    plt.axis('off')
    plt.imshow(image)
plt.show()
```
