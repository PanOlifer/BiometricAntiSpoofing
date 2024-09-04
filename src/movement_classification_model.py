import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib  
from typing import Tuple

def load_data(data_path: str) -> pd.DataFrame:
    """
    Загружает данные для обучения модели.

    Args:
        data_path (str): Путь к файлу с данными.

    Returns:
        pd.DataFrame: Загруженные данные.
    """
    try:
        data = pd.read_csv(data_path)
        return data
    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")
        return pd.DataFrame()

def preprocess_data(data: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Предобработка данных перед обучением модели.

    Args:
        data (pd.DataFrame): Данные для предобработки.

    Returns:
        Tuple[pd.DataFrame, pd.Series]: Признаки и метки.
    """
    try:
        X = data.drop('label', axis=1)
        y = data['label']
        return X, y
    except Exception as e:
        print(f"Ошибка при предобработке данных: {e}")
        return pd.DataFrame(), pd.Series()

def train_model(X: pd.DataFrame, y: pd.Series) -> RandomForestClassifier:
    """
    Обучает модель классификации на основе случайного леса.

    Args:
        X (pd.DataFrame): Признаки.
        y (pd.Series): Метки.

    Returns:
        RandomForestClassifier: Обученная модель.
    """
    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Оценка модели
        y_pred = model.predict(X_test)
        print("Точность модели:", accuracy_score(y_test, y_pred))
        print("Отчет о классификации:\n", classification_report(y_test, y_pred))

        return model
    except Exception as e:
        print(f"Ошибка при обучении модели: {e}")
        return RandomForestClassifier()

def save_model(model: RandomForestClassifier, model_path: str) -> None:
    """
    Сохраняет обученную модель для последующего использования.

    Args:
        model (RandomForestClassifier): Модель для сохранения.
        model_path (str): Путь для сохранения модели.
    """
    try:
        joblib.dump(model, model_path)
        print(f"Модель сохранена по пути: {model_path}")
    except Exception as e:
        print(f"Ошибка при сохранении модели: {e}")

data_path = 'path/to/your/preprocessed_data.csv'
model_path = 'saved_models/movement_classifier.pkl'

data = load_data(data_path)
if not data.empty:
    X, y = preprocess_data(data)
    if not X.empty and not y.empty:
        model = train_model(X, y)
        save_model(model, model_path)
