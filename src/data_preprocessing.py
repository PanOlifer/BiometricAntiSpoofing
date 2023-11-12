import numpy as np
import pandas as pd
import cv2
import nbformat
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def read_notebook(notebook_path):
    """
    Читает Jupyter ноутбук и возвращает его содержимое.
    """
    with open(notebook_path, 'r', encoding='utf-8') as file:
        nb = nbformat.read(file, as_version=4)
    return nb

def extract_data_from_notebook(notebook, data_path):
    """
    Извлекает данные из Jupyter ноутбука и сохраняет их в указанном пути.
    """
    # Здесь должен быть код для извлечения данных из ячеек ноутбука
    # Например, если данные находятся в определенной ячейке, извлеките их и сохраните
    # ...

def preprocess_image(image, target_size=(224, 224)):
    """
    Преобразует изображение: изменяет размер и нормализует.
    """
    image = cv2.resize(image, target_size)
    image = image / 255.0  # Нормализация
    return image

def prepare_data_generator(data_frame, image_column, label_column, batch_size=32):
    """
    Подготавливает генератор данных для модели.
    """
    datagen = ImageDataGenerator(rescale=1./255)
    generator = datagen.flow_from_dataframe(
        dataframe=data_frame,
        x_col=image_column,    # Название столбца с путями к файлам
        y_col=label_column,    # Название столбца с метками
        class_mode='raw',      # Тип меток
        batch_size=batch_size,
        shuffle=True,          # Перемешивание данных
        target_size=(224, 224)) # Размер изображений
    return generator

# Пример использования
notebook_path = 'data/age_recognitionV1.ipynb'
data_path = 'processed_data/data.csv'  # Путь для сохранения извлеченных данных
notebook = read_notebook(notebook_path)
extract_data_from_notebook(notebook, data_path)

