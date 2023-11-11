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
    Нормализует размер изображения и преобразует его в градации серого.
    """
    image = cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)
    return image

def adjust_brightness_contrast(image, brightness=0, contrast=0):
    """
    Корректирует яркость и контраст изображения.
    """
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow) / 255
        gamma_b = shadow

        buf = cv2.addWeighted(image, alpha_b, image, 0, gamma_b)
    else:
        buf = image.copy()

    if contrast != 0:
        f = 131 * (contrast + 127) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127 * (1 - f)

        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    return buf

# Пример использования
image_path = 'path/to/your/image.jpg'
image = load_image(image_path)
normalized_image = normalize_image(image)
adjusted_image = adjust_brightness_contrast(normalized_image, brightness=30, contrast=30)

# Показать изображение
cv2.imshow('Processed Image', adjusted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
