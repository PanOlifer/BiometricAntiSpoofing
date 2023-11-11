pip install opencv-python

import cv2
import numpy as np

def load_image(image_path):
    """
    Загружает изображение из файла.
    """
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError(f"Не удалось загрузить изображение по пути: {image_path}")
    return image

def normalize_image(image, target_size=(256, 256)):
    """
    Нормализует размер изображения.
    """
    image = cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)
    return image

def adjust_brightness_contrast(image, brightness=0, contrast=0):
    """
    Корректирует яркость и контраст изображения.
    """
    # ... (предыдущий код коррекции яркости и контраста)

def correct_color_balance(image, alpha=1.0, beta=1.0, gamma=0.0):
    """
    Корректирует цветовой баланс изображения.
    """
    image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    image = cv2.addWeighted(image, alpha, np.zeros_like(image), 0, gamma)
    return image

def reduce_noise(image):
    """
    Уменьшает шум на изображении.
    """
    return cv2.GaussianBlur(image, (5, 5), 0)

# Пример использования
image_path = 'path/to/your/image.jpg'
image = load_image(image_path)
normalized_image = normalize_image(image)
adjusted_image = adjust_brightness_contrast(normalized_image, brightness=30, contrast=30)
color_corrected_image = correct_color_balance(adjusted_image, alpha=1.2, beta=1.2)
noise_reduced_image = reduce_noise(color_corrected_image)

# Показать изображение
cv2.imshow('Processed Image', noise_reduced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

