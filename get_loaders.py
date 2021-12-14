import torch
import torchvision
from torch.utils import data
from torchvision import transforms



TRAIN_DATA_PATH = '/content/drive/MyDrive/Papers/train/'
TEST_DATA_PATH = '/content/drive/MyDrive/Papers/test/'

transforms = transforms.Compose([
    transforms.Resize((64,64)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                    std=[0.229, 0.224, 0.225] )
    ])


train_data = torchvision.datasets.ImageFolder(root=TRAIN_DATA_PATH,
                                              transform=transforms)

test_data = torchvision.datasets.ImageFolder(root=TEST_DATA_PATH,
                                             transform=transforms)


BATCH_SIZE = 32

trainloader = data.DataLoader(
    train_data, batch_size=BATCH_SIZE, shuffle=True
)
testloader = data.DataLoader(
    test_data, batch_size=BATCH_SIZE, shuffle=True
)

def loaders():
    return trainloader, testloader
