import cv2
import numpy as np
from typing import Tuple

def load_image(image_path: str) -> np.ndarray:
    """
    Загружает изображение из файла.

    Args:
        image_path (str): Путь к изображению.

    Returns:
        np.ndarray: Загруженное изображение.
    """
    try:
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        if image is None:
            raise FileNotFoundError(f"Не удалось загрузить изображение по пути: {image_path}")
        return image
    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return np.array([])

def normalize_image(image: np.ndarray, target_size: Tuple[int, int] = (256, 256)) -> np.ndarray:
    """
    Нормализует размер изображения.

    Args:
        image (np.ndarray): Входное изображение.
        target_size (Tuple[int, int]): Целевой размер изображения.

    Returns:
        np.ndarray: Нормализованное изображение.
    """
    try:
        image_resized = cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)
        return image_resized
    except Exception as e:
        print(f"Ошибка при нормализации изображения: {e}")
        return np.zeros(target_size)

def adjust_brightness_contrast(image: np.ndarray, brightness: int = 0, contrast: int = 0) -> np.ndarray:
    """
    Корректирует яркость и контраст изображения.

    Args:
        image (np.ndarray): Входное изображение.
        brightness (int): Уровень яркости.
        contrast (int): Уровень контраста.

    Returns:
        np.ndarray: Изображение с скорректированными яркостью и контрастом.
    """
    try:
        beta = brightness
        alpha = contrast / 127 + 1
        adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
        return adjusted
    except Exception as e:
        print(f"Ошибка при корректировке яркости и контраста: {e}")
        return np.array([])

def correct_color_balance(image: np.ndarray, alpha: float = 1.0, beta: float = 1.0, gamma: float = 0.0) -> np.ndarray:
    """
    Корректирует цветовой баланс изображения.

    Args:
        image (np.ndarray): Входное изображение.
        alpha (float): Масштабный коэффициент.
        beta (float): Коэффициент смещения.
        gamma (float): Гамма-коррекция.

    Returns:
        np.ndarray: Изображение с скорректированным цветовым балансом.
    """
    try:
        adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
        adjusted_image = cv2.addWeighted(adjusted_image, alpha, np.zeros_like(image), 0, gamma)
        return adjusted_image
    except Exception as e:
        print(f"Ошибка при коррекции цветового баланса: {e}")
        return np.array([])

def reduce_noise(image: np.ndarray) -> np.ndarray:
    """
    Уменьшает шум на изображении.

    Args:
        image (np.ndarray): Входное изображение.

    Returns:
        np.ndarray: Изображение с уменьшенным шумом.
    """
    try:
        return cv2.GaussianBlur(image, (5, 5), 0)
    except Exception as e:
        print(f"Ошибка при уменьшении шума: {e}")
        return np.array([])

image_path = 'path/to/your/image.jpg'
image = load_image(image_path)
if image.size > 0:
    normalized_image = normalize_image(image)
    adjusted_image = adjust_brightness_contrast(normalized_image, brightness=30, contrast=30)
    color_corrected_image = correct_color_balance(adjusted_image, alpha=1.2, beta=1.2)
    noise_reduced_image = reduce_noise(color_corrected_image)

    cv2.imshow('Processed Image', noise_reduced_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
