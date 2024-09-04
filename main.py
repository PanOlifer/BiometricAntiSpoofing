from src.data_preprocessing import preprocess_data
from src.device_boundary_detection import detect_device_boundaries
from src.face_micro_movements_detector import FaceMicroMovementsDetector
from src.texture_analysis import analyze_texture
from src.image_preprocessing import preprocess_image
from src.pictures_getting import load_images_from_directory
import argparse
import sys
import os

def load_your_data(directory_path: str):
    """
    Загружает изображения из указанной директории.
    
    Args:
        directory_path (str): Путь к директории с данными.
        
    Returns:
        list: Список загруженных изображений.
    """
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Директория {directory_path} не найдена.")
        
        images = load_images_from_directory(directory_path)
        if not images:
            raise ValueError("Не удалось загрузить изображения или директория пуста.")
        
        print(f"Успешно загружено {len(images)} изображений.")
        return images
    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

def process_image(image, detector: FaceMicroMovementsDetector):
    """
    Обрабатывает одно изображение: предобработка, анализ текстуры, обнаружение границ устройства и микродвижений.
    
    Args:
        image: Входное изображение для обработки.
        detector (FaceMicroMovementsDetector): Объект детектора микродвижений.
    
    Returns:
        dict: Результаты анализа изображения.
    """
    try:
        print("Предобработка изображения...")
        processed_image = preprocess_image(image)
        
        print("Анализ текстуры изображения...")
        texture_features = analyze_texture(processed_image)
        
        print("Обнаружение границ устройства...")
        device_boundaries = detect_device_boundaries(processed_image)
        
        print("Обнаружение микродвижений...")
        movements_detected = detector.detect_micro_movements(processed_image)
        
        results = {
            "texture_features": texture_features,
            "device_boundaries": device_boundaries,
            "movements_detected": movements_detected
        }
        
        return results
    except Exception as e:
        print(f"Ошибка при обработке изображения: {e}")
        return {}

def main():
    parser = argparse.ArgumentParser(description="Biometric Anti-Spoofing Tool")
    parser.add_argument('--data-dir', type=str, required=True, help="Путь к директории с данными")
    parser.add_argument('--model-path', type=str, required=True, help="Путь к файлу модели")
    args = parser.parse_args()

    print("Загрузка и предобработка данных...")
    data = load_your_data(args.data_dir)
    
    print("Инициализация модели для обнаружения микродвижений...")
    detector = FaceMicroMovementsDetector(model_path=args.model_path)

    print("Начало обработки изображений...")
    for idx, image in enumerate(data):
        print(f"\nОбработка изображения {idx + 1} из {len(data)}")
        results = process_image(image, detector)
        
        print(f"Результаты анализа: {results}")

    print("Обработка завершена. Все изображения обработаны.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nПроцесс был прерван пользователем.")
        sys.exit(0)
