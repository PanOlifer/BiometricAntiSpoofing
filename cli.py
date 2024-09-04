import argparse
from src import (
    image_preprocessing,
    device_boundary_detection,
    face_micro_movements_detector,
    texture_analysis,
    results_analysis
)

def preprocess_image(image_path: str):
    """
    Предобработка изображения.
    """
    try:
        image = image_preprocessing.load_image(image_path)
        preprocessed_image = image_preprocessing.normalize_image(image)
        print("Image preprocessed successfully.")
    except Exception as e:
        print(f"Ошибка при предобработке изображения: {e}")

def detect_device_boundaries(image_path: str):
    """
    Обнаружение границ устройства на изображении.
    """
    try:
        image = device_boundary_detection.load_image(image_path)
        if image.size == 0:
            raise ValueError("Не удалось загрузить изображение или изображение пустое.")
        edges = device_boundary_detection.detect_edges(image)
        boundaries = device_boundary_detection.find_rectangular_contours(edges)
        print(f"Detected {len(boundaries)} device boundaries.")
    except Exception as e:
        print(f"Ошибка при обнаружении границ устройства: {e}")

def detect_micro_movements(video_path: str, model_path: str):
    """
    Обнаружение микродвижений лица в видео.
    """
    try:
        detector = face_micro_movements_detector.FaceMicroMovementsDetector(model_path)
        detector.process_video_stream(video_path)
        print("Micro-movement detection completed successfully.")
    except Exception as e:
        print(f"Ошибка при обнаружении микродвижений: {e}")

def analyze_image_texture(image_path: str):
    """
    Анализ текстуры на изображении.
    """
    try:
        image = texture_analysis.load_image(image_path)
        if image.size == 0:
            raise ValueError("Не удалось загрузить изображение или изображение пустое.")
        texture_score = texture_analysis.analyze_texture(image)
        print(f"Texture score: {texture_score}")
    except Exception as e:
        print(f"Ошибка при анализе текстуры: {e}")

def main():
    parser = argparse.ArgumentParser(description="Biometric Anti-Spoofing CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    preprocess_parser = subparsers.add_parser("preprocess", help="Preprocess an image")
    preprocess_parser.add_argument("image_path", help="Path to the image to preprocess")

    detect_device_parser = subparsers.add_parser("detect_device", help="Detect device boundaries in an image")
    detect_device_parser.add_argument("image_path", help="Path to the image for device boundary detection")

    detect_movement_parser = subparsers.add_parser("detect_movement", help="Detect facial micro-movements in a video")
    detect_movement_parser.add_argument("video_path", help="Path to the video for micro-movement detection")
    detect_movement_parser.add_argument("model_path", help="Path to the model file for detection")

    analyze_texture_parser = subparsers.add_parser("analyze_texture", help="Analyze texture in an image")
    analyze_texture_parser.add_argument("image_path", help="Path to the image for texture analysis")

    args = parser.parse_args()

    if args.command == "preprocess":
        preprocess_image(args.image_path)

    elif args.command == "detect_device":
        detect_device_boundaries(args.image_path)

    elif args.command == "detect_movement":
        detect_micro_movements(args.video_path, args.model_path)

    elif args.command == "analyze_texture":
        analyze_image_texture(args.image_path)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
