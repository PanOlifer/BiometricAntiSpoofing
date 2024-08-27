import argparse
from src import (
    image_preprocessing,
    device_boundary_detection,
    face_micro_movements_detector,
    texture_analysis,
    results_analysis
)

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
        image = image_preprocessing.load_image(args.image_path)
        preprocessed_image = image_preprocessing.normalize_image(image)
        print("Image preprocessed successfully.")

    elif args.command == "detect_device":
        image = device_boundary_detection.load_image(args.image_path)
        edges = device_boundary_detection.detect_edges(image)
        boundaries = device_boundary_detection.find_rectangular_contours(edges)
        print(f"Detected {len(boundaries)} device boundaries.")

    elif args.command == "detect_movement":
        detector = face_micro_movements_detector.FaceMicroMovementsDetector(args.model_path)
        detector.process_video_stream(args.video_path)

    elif args.command == "analyze_texture":
        image = texture_analysis.load_image(args.image_path)
        texture_score = texture_analysis.analyze_texture(image)
        print(f"Texture score: {texture_score}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
