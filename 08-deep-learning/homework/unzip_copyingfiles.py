# unzip the downloaded dataset
import zipfile
with zipfile.ZipFile('train.zip', 'r') as zip_ref:
    zip_ref.extractall('.')

import os

#create folders
os.makedirs('train/dogs')
os.makedirs('train/cats')
os.makedirs('val/dogs')
os.makedirs('val/cats')


# move the images
for i in range(0, 10000):
    os.rename(f'train/dog.{i}.jpg', f'train/dogs/dog.{i}.jpg')
    os.rename(f'train/cat.{i}.jpg', f'train/cats/cat.{i}.jpg')

for i in range(10000, 12500):
    os.rename(f'train/dog.{i}.jpg', f'val/dogs/dog.{i}.jpg')
    os.rename(f'train/cat.{i}.jpg', f'val/cats/cat.{i}.jpg')

