import cv2
import numpy as np
from typing import List

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
            raise FileNotFoundError(f"Изображение не найдено по пути: {image_path}")
        return image
    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return np.array([])

def convert_to_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Преобразует изображение в градации серого.

    Args:
        image (np.ndarray): Входное изображение.

    Returns:
        np.ndarray: Изображение в градациях серого.
    """
    try:
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except Exception as e:
        print(f"Ошибка при преобразовании изображения в градации серого: {e}")
        return np.array([])

def gaussian_blur(image: np.ndarray, kernel_size: int = 5) -> np.ndarray:
    """
    Применяет Гауссово размытие для уменьшения шума.

    Args:
        image (np.ndarray): Входное изображение.
        kernel_size (int): Размер ядра размытия.

    Returns:
        np.ndarray: Размытое изображение.
    """
    try:
        return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    except Exception as e:
        print(f"Ошибка при применении размытия: {e}")
        return np.array([])

def detect_edges(image: np.ndarray, sigma: float = 0.33) -> np.ndarray:
    """
    Адаптивное обнаружение краев с использованием алгоритма Кэнни.

    Args:
        image (np.ndarray): Входное изображение.
        sigma (float): Параметр для определения пороговых значений.

    Returns:
        np.ndarray: Изображение с обнаруженными краями.
    """
    try:
        v = np.median(image)
        lower = int(max(0, (1.0 - sigma) * v))
        higher = int(min(255, (1.0 + sigma) * v))
        return cv2.Canny(image, lower, higher)
    except Exception as e:
        print(f"Ошибка при обнаружении краев: {e}")
        return np.array([])

def is_rectangular(contour: np.ndarray, aspect_ratio_range: tuple = (0.8, 1.2), area_threshold: int = 500) -> bool:
    """
    Определяет, является ли контур прямоугольником на основе пропорций и площади.

    Args:
        contour (np.ndarray): Контур.
        aspect_ratio_range (tuple): Допустимый диапазон пропорций.
        area_threshold (int): Минимальная площадь для прямоугольника.

    Returns:
        bool: True, если контур является прямоугольником, иначе False.
    """
    x, y, w, h = cv2.boundingRect(contour)
    aspect_ratio = w / float(h)
    area = cv2.contourArea(contour)
    return aspect_ratio_range[0] <= aspect_ratio <= aspect_ratio_range[1] and area > area_threshold

def find_rectangular_contours(edges: np.ndarray) -> List[np.ndarray]:
    """
    Находит контуры, которые могут быть прямоугольниками (границами устройств).

    Args:
        edges (np.ndarray): Изображение с обнаруженными краями.

    Returns:
        List[np.ndarray]: Список контуров, которые являются прямоугольниками.
    """
    try:
        contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        rectangular_contours = []
        for contour in contours:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
            if len(approx) == 4 and is_rectangular(approx):
                rectangular_contours.append(approx)
        return rectangular_contours
    except Exception as e:
        print(f"Ошибка при нахождении прямоугольных контуров: {e}")
        return []

image_path = 'pdata/pics/frame_5.jpg'
image = load_image(image_path)
if image.size > 0:
    gray_image = convert_to_grayscale(image)
    blurred_image = gaussian_blur(gray_image)
    edges = detect_edges(blurred_image)
    rectangular_contours = find_rectangular_contours(edges)

    for contour in rectangular_contours:
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 3)
    cv2.imshow('Detected Device Boundaries', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
