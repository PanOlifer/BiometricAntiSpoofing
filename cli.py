import argparse
from src import device_boundary_detection, face_micro_movements_detector, image_preprocessing, texture_analysis

def main():
    parser = argparse.ArgumentParser(description="Biometric Anti-Spoofing CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
  
    subparsers.add_parser("detect_device_boundary", help="Detect boundaries of the device in the input images.")
    subparsers.add_parser("detect_face_micro_movements", help="Detect micro movements of faces to identify spoofing.")
    subparsers.add_parser("preprocess_image", help="Preprocess images for further analysis.")
    subparsers.add_parser("analyze_texture", help="Analyze texture to detect spoofing attempts.")

    args = parser.parse_args()

    if args.command == "detect_device_boundary":
        device_boundary_detection.detect()  
    elif args.command == "detect_face_micro_movements":
        face_micro_movements_detector.detect()  
    elif args.command == "preprocess_image":
        image_preprocessing.preprocess()  
    elif args.command == "analyze_texture":
        texture_analysis.analyze() 
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
