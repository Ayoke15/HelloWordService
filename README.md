# My Django App

## Описание
Это инструкция по сборке и запуску приложения Django с использованием Docker.

## Установка и запуск

### Шаг 1: Сборка образа Docker
1. Откройте терминал и перейдите в каталог с вашим Dockerfile.
2. Запустите команду для сборки образа:
   ```docker build -t my-django-app .```

### Шаг 2: Запуск контейнера
1. Запустите контейнер с помощью следующей команды:
```docker run -d -p 8003:8003 my-django-app```
2. Приложение теперь доступно по адресу `http://localhost:8003/`.

## Примечания
- Флаг `-d` запускает контейнер в фоновом режиме.
- Опция `-p` используется для проброса портов.
