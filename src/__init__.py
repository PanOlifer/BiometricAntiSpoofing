# __init__.py
# Инициализация пакета BiometricAntiSpoofing

from .data_preprocessing import extract_data_from_notebook, preprocess_image, prepare_data_generator
from .device_boundary_detection import load_image, convert_to_grayscale, gaussian_blur, detect_edges
from .face_micro_movements_detector import FaceMicroMovementsDetector
from .image_preprocessing import load_image, normalize_image, adjust_brightness_contrast
from .results_analysis import analyze_final_results
from .texture_analysis import analyze_texture, texture_analysis_using_lbp
