# weather-bot
https://t.me/fakin_weather_bot
### Умный сервис прогноза погоды.

## Описание сервиса

Язык программирования `python`, библиотека `aiogram` для создания бота и `aiohttp` для запросов к внешнему сервису.

Реализована модель long polling бот - боту не требуется внешний IP и какой-либо деплой - можно запускать на любой машине, имеющей доступ к `api.telegram.org`.

Формат ответа: текстовый шаблон вида `{локация}: {температура}, {погодный статус}`.

## Процесс работы

- Пользователь отправляет боту название города или геолокацию.
- Из этих данных формируется запрос к [https://openweathermap.org/](openweathermap) и из полученного ответа получаются данные о температуре и погодном статусе (e.g. переменная облачность).
- Данные постобрабатываются для получения совета об одежде на основе правил на температуру и погодный статус.
- Результат отправляется пользователю текстовым сообщением.

## Как запустить

Добавить в переменные окружения ключ API Telegram (получается у [@BotFather](https://telegram.me/botfather) при создании нового бота командой /newbot) и ключ API [OpenWeatherMap](https://openweathermap.org/). 

Создать файл с переменными окружения (.env):
```
TELEGRAM_API_TOKEN=...
WEATHER_SERVICE_API_KEY=...
```

Для запуска необходим Python версии 3.7 и выше.

Создать и активировать виртуальное окружение(опционально):
```python
python -m venv venv
```
Windows:
```python
venv/scripts/activate
```
Unix:
```python
venv/bin/activate
```

Установить зависимости:
```python
pip install -r requirements.txt
```

Запустить
```python
python3 weather_bot.py
```
