# Exercise - Test a Neural Network that Classifies Images of Space Rocks

Lets pick 5 random images and see if our model can tell what type of rock it is:

```python
# Set to 5 but can be adjusted to any number- for example if you want to test if for 10 rock images, use 10 in the code line below
images, labels = get_random_images(5)
```

```python
# code to visualize the new new images and add captions for image types
to_pil = transforms.ToPILImage()
images, labels = get_random_images(5)
fig=plt.figure(figsize=(20,10))

classes=trainloader.dataset.classes
for ii in range(len(images)):
    image = to_pil(images[ii])
    index = predict_image(image)
    sub = fig.add_subplot(1, len(images), ii+1)
    res = int(labels[ii]) == index
    sub.set_title(str(classes[index]) + ":" + str(res))
    plt.axis('off')
    plt.imshow(image)
plt.show()
```

The example images above are labeled as
Actual Rock Type : True / False

Where True and False show if our AI system correctly classified it or not.
