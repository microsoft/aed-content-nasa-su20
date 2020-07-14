# Import the Libraries we Need

Now that we have all of the libraries downloaded, we can begin importing them into our Jupyter Notebooks file.

```python
import matplotlib.pyplot as plt
import numpy as np
import torch
from torch import nn
from torch import optim
import torch.nn.functional as F
from torchvision import datasets, transforms, models
import torchvision
from PIL import Image
from torch.autograd import Variable
%matplotlib inline
%config InlineBackend.figure_format = 'retina'
```
