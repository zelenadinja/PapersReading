import os 
from tqdm import tqdm 
import shutil


for img_class in tqdm(os.listdir('/content/drive/MyDrive/Papers/raw-img')):
    print(f'Class:{img_class}')

    img_ls = os.listdir('/content/drive/MyDrive/Papers/raw-img/' + img_class)
    print(f'Num Images:{len(img_ls)}')
    for img in img_ls[:int(len(img_ls) * 0.8)]:
        
        shutil.copy(
            '/content/drive/MyDrive/Papers/raw-img/' + img_class + '/' + img,
            '/content/drive/MyDrive/Papers/train/' + img_class + '/' + img
        )

for img_class in tqdm(os.listdir('/content/drive/MyDrive/Papers/raw-img')):
    print(f'Class:{img_class}')

    img_ls = os.listdir('/content/drive/MyDrive/Papers/raw-img/' + img_class)
    print(f'Num Images:{len(img_ls)}')
    for img in img_ls[int(len(img_ls) * 0.8):]:
        
        shutil.copy(
            '/content/drive/MyDrive/Papers/raw-img/' + img_class + '/' + img,
            '/content/drive/MyDrive/Papers/test/' + img_class + '/' + img
        )
