import pandas as pd
import numpy as np
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import nbformat
from typing import Optional, Dict

def extract_data_from_notebook(notebook_path: str) -> Optional[Dict[str, np.ndarray]]:
    """
    Извлекает данные из Jupyter Notebook, если они определены в переменной 'extracted_data'.

    Args:
        notebook_path (str): Путь к файлу Jupyter Notebook.

    Returns:
        Optional[Dict[str, np.ndarray]]: Извлеченные данные или None в случае ошибки.
    """
    try:
        with open(notebook_path, 'r', encoding='utf-8') as file:
            nb = nbformat.read(file, as_version=4)

        data = {}
        for cell in nb.cells:
            if cell.cell_type == 'code' and 'extracted_data' in cell['source']:
                exec(cell['source'])
                data['extracted_data'] = locals().get('extracted_data', None)

        return data if data else None

    except Exception as e:
        print(f"Ошибка при извлечении данных из ноутбука: {e}")
        return None

def preprocess_image(image: np.ndarray, target_size: tuple = (224, 224)) -> np.ndarray:
    """
    Предобрабатывает изображение: изменение размера и нормализация.

    Args:
        image (np.ndarray): Входное изображение.
        target_size (tuple): Размер выходного изображения.

    Returns:
        np.ndarray: Предобработанное изображение.
    """
    try:
        image = cv2.resize(image, target_size)
        image = image / 255.0
        return image
    except Exception as e:
        print(f"Ошибка при предобработке изображения: {e}")
        return np.zeros(target_size)

def prepare_data_generator(data: pd.DataFrame, batch_size: int = 32) -> Optional[ImageDataGenerator]:
    """
    Создает генератор данных для обучения моделей.

    Args:
        data (pd.DataFrame): Данные с путями к изображениям и метками.
        batch_size (int): Размер батча.

    Returns:
        Optional[ImageDataGenerator]: Генератор данных или None в случае ошибки.
    """
    try:
        datagen = ImageDataGenerator(rescale=1./255)
        generator = datagen.flow_from_dataframe(
            dataframe=data,
            x_col='file_path',
            y_col='label',
            class_mode='raw',
            batch_size=batch_size,
            shuffle=True,
            target_size=(224, 224)
        )
        return generator
    except Exception as e:
        print(f"Ошибка при создании генератора данных: {e}")
        return None


notebook_path = 'notebooks/webcam_pics_getting.ipynb'
data = extract_data_from_notebook(notebook_path)
if data is not None:
    data_generator = prepare_data_generator(pd.DataFrame(data))
