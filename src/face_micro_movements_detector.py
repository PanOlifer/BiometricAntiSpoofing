import cv2
import numpy as np
from tensorflow.keras.models import load_model
from typing import Optional

class FaceMicroMovementsDetector:
    def __init__(self, model_path: str):
        """
        Инициализация детектора микродвижений лица.

        Args:
            model_path (str): Путь к файлу модели машинного обучения.
        """
        self.model = self.load_model(model_path)

    def load_model(self, model_path: str) -> Optional[load_model]:
        """
        Загрузка модели машинного обучения.

        Args:
            model_path (str): Путь к файлу модели.

        Returns:
            Optional[load_model]: Загруженная модель или None в случае ошибки.
        """
        try:
            model = load_model(model_path)
            return model
        except Exception as e:
            print(f"Ошибка при загрузке модели: {e}")
            return None

    def preprocess_frame(self, frame: np.ndarray) -> np.ndarray:
        """
        Предобработка кадра перед анализом микродвижений.

        Args:
            frame (np.ndarray): Входной кадр.

        Returns:
            np.ndarray: Предобработанный кадр.
        """
        try:
            frame_resized = cv2.resize(frame, (224, 224))
            frame_normalized = frame_resized / 255.0
            return frame_normalized
        except Exception as e:
            print(f"Ошибка при предобработке кадра: {e}")
            return np.zeros((224, 224, 3))

    def detect_micro_movements(self, frame: np.ndarray) -> bool:
        """
        Обнаружение микродвижений на кадре.

        Args:
            frame (np.ndarray): Входной кадр.

        Returns:
            bool: True, если обнаружены микродвижения, иначе False.
        """
        try:
            processed_frame = self.preprocess_frame(frame)
            prediction = self.model.predict(np.expand_dims(processed_frame, axis=0))
            return prediction[0][0] > 0.5  # Используем порог 0.5 для бинарной классификации
        except Exception as e:
            print(f"Ошибка при детекции микродвижений: {e}")
            return False

    def process_video_stream(self, video_path: str):
        """
        Обработка видеопотока и обнаружение микродвижений.

        Args:
            video_path (str): Путь к видеофайлу.
        """
        try:
            cap = cv2.VideoCapture(video_path)
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                movements_detected = self.detect_micro_movements(frame)

                if movements_detected:
                    print("Обнаружены микродвижения")
                else:
                    print("Микродвижения не обнаружены")

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            print(f"Ошибка при обработке видеопотока: {e}")

detector = FaceMicroMovementsDetector(model_path='path/to/model.h5')
detector.process_video_stream(video_path='path/to/video.mp4')
