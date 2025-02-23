
# DevOps CI/CD Demo

Простой проект для демонстрации навыков Docker и CI/CD.

## Технологии
- Docker
- Flask (Python)
- GitHub Actions (опционально)

## Как запустить
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-юзернейм/devops-demo.git

Соберите Docker-образ:
docker build -t my-app .
Запустите контейнер:
docker run -d -p 80:80 --name my-app my-app

