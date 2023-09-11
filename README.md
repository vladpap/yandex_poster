![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

# Сервис Афиша на карте

Онлайн сервис Афиши. 

## Установка.
- Python3 должен быть уже установлен.
- Рекомендуется использовать среду окружения [venv](https://docs.python.org/3/library/venv.html) 
для изоляции проекта.
 - Используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей
```console
$ pip install -r requirements.txt
```

### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

- `DEBUG=True` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.

- `SECRET_KEY=My Secret Key` — секретный ключ проекта

- `ALLOWED_HOSTS=localhost,127.0.0.1` - Список строк, представляющих имена хоста / домена, которые может обслуживать этот сайт

## Запуск

```console
$ python3 manage.py migrate
$ python3 manage.py createsuperuser
$ python3 manage.py runserver
```
[Локальный сайт](http://127.0.0.1:8000/), и [Административная часть сайта](http://127.0.0.1:8000/admin/)

## Цели проекта

Код написан в учебных целях — это командный проект на курсе по Python [Devman](https://dvmn.org).


<img src="https://dvmn.org/assets/img/logo.8d8f24edbb5f.svg" alt= “” width="102" height="25">