from typing import List, Dict, Union

def analyze_final_results(texture_features: List[float], device_boundaries: List[bool], movements_detected: List[bool]) -> Dict[str, Union[float, bool, str]]:
    """
    Анализирует и синтезирует результаты от различных модулей.

    Args:
        texture_features (List[float]): Результаты анализа текстуры.
        device_boundaries (List[bool]): Результаты обнаружения границ устройств.
        movements_detected (List[bool]): Результаты обнаружения микродвижений.

    Returns:
        Dict[str, Union[float, bool, str]]: Словарь с окончательными выводами и рекомендациями.
    """
    try:
        if not texture_features or not device_boundaries or not movements_detected:
            raise ValueError("Входные данные не должны быть пустыми.")

        final_conclusions = {
            'texture_analysis': sum(texture_features) / len(texture_features),
            'device_boundary_detection': any(device_boundaries),
            'micro_movement_detection': any(movements_detected)
        }

        if all(final_conclusions.values()):
            final_conclusions['action'] = 'Suspicious activity detected'
        else:
            final_conclusions['action'] = 'Activity seems normal'

        return final_conclusions
    except Exception as e:
        print(f"Ошибка при анализе результатов: {e}")
        return {}

texture_features = [0.2, 0.3, 0.4]
device_boundaries = [False, False, True]
movements_detected = [False, False, True]

final_results = analyze_final_results(texture_features, device_boundaries, movements_detected)
print(final_results)
