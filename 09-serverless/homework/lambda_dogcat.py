#!/usr/bin/env python
# coding: utf-8

# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# import tensorflow as tf
# import tensorflow.lite as tflite

import tflite_runtime.interpreter as tflite
import numpy as np

from io import BytesIO
from urllib import request

from PIL import Image

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img

def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def preprocess_input(x):
    x /= 255
    return x


interpreter = tflite.Interpreter(model_path='dogcat-model.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

# url = 'https://upload.wikimedia.org/wikipedia/commons/1/18/Vombatus_ursinus_-Maria_Island_National_Park.jpg'


def predict(url):
    img = download_image(url)
    img = prepare_image(img, (150, 150))

    x = np.array(img, dtype='float32')
    X = np.array([x])

    X = preprocess_input(X)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    prediction = preds[0][0].tolist()
    print("Predicted dog/vs_cat probability:", round(prediction, 5))

    return round(prediction, 5)


def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result

if __name__ == "__main__":
    predict(url)





