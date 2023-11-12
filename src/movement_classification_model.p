import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib  # Для сохранения модели

def load_data(data_path):
    """
    Загружает данные для обучения модели.
    """
    # Загрузка данных. Предполагается, что данные уже предобработаны
    data = pd.read_csv(data_path)
    return data

def preprocess_data(data):
    """
    Предобработка данных перед обучением модели.
    """
    # Разделите данные на признаки и метки
    X = data.drop('label', axis=1)
    y = data['label']
    return X, y

def train_model(X, y):
    """
    Обучает модель классификации на основе случайного леса.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Оценка модели
    y_pred = model.predict(X_test)
    print("Точность модели:", accuracy_score(y_test, y_pred))
    print("Отчет о классификации:\n", classification_report(y_test, y_pred))

    return model

def save_model(model, model_path):
    """
    Сохраняет обученную модель для последующего использования.
    """
    joblib.dump(model, model_path)

# Пример использования
data_path = 'path/to/your/preprocessed_data.csv'
model_path = 'saved_models/movement_classifier.pkl'

data = load_data(data_path)
X, y = preprocess_data(data)
model = train_model(X, y)
save_model(model, model_path)
