import pandas as pd
import numpy as np
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import nbformat

def extract_data_from_notebook(notebook_path):
    try:
        with open(notebook_path, 'r', encoding='utf-8') as file:
            nb = nbformat.read(file, as_version=4)

        data = {}
        for cell in nb.cells:
            if cell.cell_type == 'code':
                if 'extracted_data' in cell['source']:
                    exec(cell['source'])
                    data['extracted_data'] = extracted_data

    except Exception as e:
        print(f"Ошибка при извлечении данных из ноутбука: {e}")
        data = None

    return data

def preprocess_image(image, target_size=(224, 224)):
    image = cv2.resize(image, target_size)
    image = image / 255.0
    return image

def prepare_data_generator(data, batch_size=32):
    try:
        datagen = ImageDataGenerator(rescale=1./255)
        generator = datagen.flow_from_dataframe(
            dataframe=data,
            x_col='file_path',
            y_col='label',
            class_mode='raw',
            batch_size=batch_size,
            shuffle=True,
            target_size=(224, 224))
    except Exception as e:
        print(f"Ошибка при создании генератора данных: {e}")
        generator = None

    return generator

# Пример использования
notebook_path = 'notebooks/webcam_pics_getting.ipynb'
data = extract_data_from_notebook(notebook_path)
if data is not None:
    data_generator = prepare_data_generator(data)
