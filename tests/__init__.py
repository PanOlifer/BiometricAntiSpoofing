import unittest
from src import device_boundary_detection, face_micro_movements_detector, image_preprocessing, texture_analysis

class TestDeviceBoundaryDetection(unittest.TestCase):
    def test_detect_device_boundary(self):
        # функция detect возвращает True, если граница устройства обнаружена
        result = device_boundary_detection.detect('test_image.jpg')
        self.assertTrue(result, "Device boundary should be detected correctly.")

class TestFaceMicroMovementsDetector(unittest.TestCase):
    def test_detect_face_micro_movements(self):
        # функция detect возвращает число, соответствующее количеству обнаруженных микродвижений
        result = face_micro_movements_detector.detect('test_video.mp4')
        self.assertGreater(result, 0, "Micro movements should be detected in the video.")

class TestImagePreprocessing(unittest.TestCase):
    def test_preprocess_image(self):
        # функция preprocess возвращает обработанное изображение в виде массива
        processed_image = image_preprocessing.preprocess('raw_image.jpg')
        self.assertIsNotNone(processed_image, "Processed image should not be None.")
        self.assertIsInstance(processed_image, list, "Processed image should be a list.")

class TestTextureAnalysis(unittest.TestCase):
    def test_analyze_texture(self):
        # функция analyze возвращает индекс текстуры (число)
        texture_index = texture_analysis.analyze('test_image.jpg')
        self.assertGreaterEqual(texture_index, 0, "Texture index should be a non-negative number.")

if __name__ == "__main__":
    unittest.main()
