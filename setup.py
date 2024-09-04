import os
import subprocess
import sys

def setup_environment():
    # Проверка наличия Python и pip
    if not (sys.version_info.major == 3 and sys.version_info.minor >= 6):
        raise EnvironmentError("Требуется Python версии 3.6 или выше.")

    # Создание виртуального окружения
    subprocess.check_call([sys.executable, '-m', 'venv', 'venv'])

    # Активация виртуального окружения и установка зависимостей
    subprocess.check_call(['venv/bin/pip', 'install', '--upgrade', 'pip'])
    subprocess.check_call(['venv/bin/pip', 'install', '-r', 'requirements.txt'])

    print("Настройка завершена. Активируйте виртуальное окружение с помощью 'source venv/bin/activate'.")

if __name__ == "__main__":
    setup_environment()
