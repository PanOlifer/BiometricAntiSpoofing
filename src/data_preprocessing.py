import pandas as pd
import numpy as np
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import nbformat

def extract_data_from_notebook(notebook_path):
    """
    Извлекает данные из Jupyter ноутбука.
    """
    with open(notebook_path, 'r', encoding='utf-8') as file:
        nb = nbformat.read(file, as_version=4)

    # Пример кода для извлечения данных из ноутбука
    # Это нужно доработать в зависимости от структуры и содержания ноутбука
    data = None
    for cell in nb.cells:
        if cell.cell_type == 'code':
            # Пример: поиск и извлечение определенных данных из кодовых ячеек
            # ...
            pass

    return data

def preprocess_image(image, target_size=(224, 224)):
    """
    Преобразует изображение: изменяет размер и нормализует.
    """
    image = cv2.resize(image, target_size)
    image = image / 255.0  # Нормализация
    return image

def prepare_data_generator(data, batch_size=32):
    """
    Подготавливает генератор данных для модели.
    """
    datagen = ImageDataGenerator(rescale=1./255)
    generator = datagen.flow_from_dataframe(
        dataframe=data,
        x_col='file_path',  # Название столбца с путями к файлам
        y_col='label',      # Метки
        class_mode='raw',   # Тип меток
        batch_size=batch_size,
        shuffle=True,       # Перемешивание данных
        target_size=(224, 224))  # Размер изображений
    return generator

# Пример использования
notebook_path = 'data/age_recognitionV1.ipynb'
data = extract_data_from_notebook(notebook_path)

data_generator = prepare_data_generator(data)
