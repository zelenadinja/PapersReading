import os 



for img_class in os.listdir('/content/drive/MyDrive/Papers/raw-img'):

    total_images = len(os.listdir('/content/drive/MyDrive/Papers/raw-img/' + img_class + '/'))
    train_images = len(os.listdir('/content/drive/MyDrive/Papers/train/' + img_class + '/'))
    test_images = len(os.listdir('/content/drive/MyDrive/Papers/test/' + img_class + '/'))

    print(f'Class:{img_class} Total Images:{total_images} Train+Test:{train_images+test_images} Train Images:{train_images} Test Images:{test_images}')
