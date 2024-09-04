import cv2
import time
import os
from typing import Optional

def capture_images(output_dir: str, capture_duration: int = 10, display_frames: bool = False) -> None:
    """
    Захватывает изображения с веб-камеры и сохраняет их в указанную директорию.

    Args:
        output_dir (str): Путь к директории для сохранения изображений.
        capture_duration (int): Длительность захвата в секундах.
        display_frames (bool): Если True, показывает захватываемые кадры.
    """
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise RuntimeError("Не удалось открыть веб-камеру.")

        fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
        total_frames = int(fps * capture_duration)

        os.makedirs(output_dir, exist_ok=True)

        for i in range(total_frames):
            ret, frame = cap.read()
            if not ret:
                print(f"Ошибка при захвате кадра {i}.")
                continue

            filename = f'frame_{i}.jpg'
            filepath = os.path.join(output_dir, filename)
            cv2.imwrite(filepath, frame)

            if display_frames:
                cv2.imshow('Video', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            print(f"Сохранен кадр {i + 1} как {filepath}")
            time.sleep(1 / fps)

        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"Ошибка при захвате изображений: {e}")

capture_images('C:/Users/User/Documents/GitHub/BiometricAntiSpoofing/src/pics/')
