import cv2
import numpy as np

def load_image(image_path):
    """
    Загружает изображение из файла.
    """
    return cv2.imread(image_path, cv2.IMREAD_COLOR)

def convert_to_grayscale(image):
    """
    Преобразует изображение в градации серого.
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def gaussian_blur(image, kernel_size=5):
    """
    Применяет Гауссово размытие для уменьшения шума.
    """
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

def detect_edges(image, sigma=0.33):
    """
    Адаптивное обнаружение краев с использованием алгоритма Кэнни.
    """
    v = np.median(image)
    lower = int(max(0, (1.0 - sigma) * v))
    higher = int(min(255, (1.0 + sigma) * v))
    return cv2.Canny(image, lower, higher)

def is_rectangular(contour, aspect_ratio_range=(0.8, 1.2), area_threshold=500):
    """
    Определяет, является ли контур прямоугольником на основе пропорций и площади.
    """
    x, y, w, h = cv2.boundingRect(contour)
    aspect_ratio = w / float(h)
    area = cv2.contourArea(contour)
    return aspect_ratio_range[0] <= aspect_ratio <= aspect_ratio_range[1] and area > area_threshold

def find_rectangular_contours(edges):
    """
    Находит контуры, которые могут быть прямоугольниками (границами устройств).
    """
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    rectangular_contours = []
    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
        if len(approx) == 4 and is_rectangular(approx):  # Прямоугольники имеют 4 угла
            rectangular_contours.append(approx)
    return rectangular_contours

# Пример использования
image_path = 'path/to/your/image.jpg'
image = load_image(image_path)
gray_image = convert_to_grayscale(image)
blurred_image = gaussian_blur(gray_image)
edges = detect_edges(blurred_image)
rectangular_contours = find_rectangular_contours(edges)

# Визуализация
for contour in rectangular_contours:
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 3)
cv2.imshow('Detected Device Boundaries', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
