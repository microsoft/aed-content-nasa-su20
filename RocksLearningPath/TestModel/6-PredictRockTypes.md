# Predict Rock Types

Lets predict the rock types
To predict the type of a new rock image, we need to the following:

1. Convert the new image into numbers
2. Transform it (Crop and resize to 224*224)
3. Extract features and characteristics of the image
4. Predict its type using the associations we have learned in step 2.

```python
#transform the new image into numbers and resize it
test_transforms = transforms.Compose([transforms.RandomResizedCrop(224),
                                      transforms.Resize(224),
                                      transforms.ToTensor(),
                                      #transforms.Normalize([0.485, 0.456, 0.406],
                                      #                     [0.229, 0.224, 0.225])
                                     ])
```

```python
# Load the neural network we built in previous step
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model=torch.load('aerialmodel.pth')
#model.eval()
```

```python
# Predict the image type
def predict_image(image):
    image_tensor = test_transforms(image).float()
    image_tensor = image_tensor.unsqueeze_(0)
    input = Variable(image_tensor)
    input = input.to(device)
    output = model(input)
    index = output.data.cpu().numpy().argmax()
    return index  
```
