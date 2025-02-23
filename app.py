# Импортируем Flask
from flask import Flask

# Создаем экземпляр приложения
app = Flask(__name__)

# Определяем маршрут для главной страницы
@app.route('/')
def hello():
    return """
    <h1>Hello DevOps!</h1>
    <p>This is my first CI/CD project.</p>
    <p>I'm learning Docker, CI/CD, and more!</p>
    """

# Запускаем приложение, если файл выполняется напрямую
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
