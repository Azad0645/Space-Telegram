# Space Telegram

Описание проекта:
- Этот бот автоматически публикует фотографии из NASA, SpaceX и EPIC в ваш Telegram канал с заданным интервалом. 

## Как установить 

Создайте бота в Telegram:
- Перейдите в Telegram и напишите боту @BotFather.
- Получите TOKEN — он понадобится для работы бота.
- Добавьте бота в свой канал и дайте ему права администратора.
- Узнайте CHAT_ID канала

Создайте файл .env в корневой папке проекта и добавьте туда ваш токен и ID канала:
- TOKEN=ваш токен
- CHAT_ID=имя канала

Установка зависимостей:
- Python 3 должен быть уже установлен.
- `pip install -r requirements.txt`

## Примеры запуска всех скриптов

Автоматическая публикация фото раз в 4 часа:
-  `python photo_publisher.py`

Отправка одного фото (указанного или случайного):
- `python send_photo.py --photo "epic_images/epic_1.jpg"`
- `python send_photo.py`

Загрузка фото с NASA APOD:
- `python fetch_nasa_apod.py`

Загрузка фото EPIC:
- `python fetch_nasa_epic.py`

Загрузка фото SpaceX:
- `python fetch_spacex_images.py`

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).