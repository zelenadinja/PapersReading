import os 

if __name__ == '__main__':
#Train Folder
    os.mkdir('/content/drive/MyDrive/Papers/train')
    for img_class in os.listdir('/content/drive/MyDrive/Papers/raw-img'):
        print(img_class)
        os.mkdir('/content/drive/MyDrive/Papers/train/' + img_class + '/')

#Test Folder
    os.mkdir('/content/drive/MyDrive/Papers/test')
    for img_class in os.listdir('/content/drive/MyDrive/Papers/raw-img'):
        os.mkdir('/content/drive/MyDrive/Papers/test/' + img_class + '/')


