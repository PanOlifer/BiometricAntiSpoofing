import cv2
import time
import os

def capture_images(output_dir, capture_duration=10, display_frames=False):
    """
    Захватывает изображения с веб-камеры и сохраняет их в указанную директорию.

    Args:
        output_dir (str): Путь к директории для сохранения изображений.
        capture_duration (int): Длительность захвата в секундах.
        display_frames (bool): Если True, показывает захватываемые кадры.
    """

    # Инициализация захвата видео с веб-камеры
    cap = cv2.VideoCapture(0)

    # Определение частоты кадров
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(fps * capture_duration)

    # Создание директории для вывода, если она не существует
    os.makedirs(output_dir, exist_ok=True)

    # Захват кадров
    for i in range(total_frames):
        ret, frame = cap.read()
        if ret:
            filename = f'frame_{i}.jpg'
            filepath = os.path.join(output_dir, filename)
            cv2.imwrite(filepath, frame)
            if display_frames:
                cv2.imshow('Video', frame)
                cv2.waitKey(1)
            print(f"Saved frame {i + 1} as {filepath}")
        time.sleep(1 / fps)

    # Освобождение захвата видео и закрытие окон
    cap.release()
    cv2.destroyAllWindows()

# Пример вызова функции
capture_images('C:/Users/User/Documents/GitHub/BiometricAntiSpoofing/src/pics/')
