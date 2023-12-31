![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

# Сервис Афиша на карте

Онлайн сервис Афиши. 

## Установка.
- Python 3.10 должен быть уже установлен.
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

[Сайт на удаленном сервере](https://vladpap.pythonanywhere.com/), и [Административная часть удаленного сайта](https://vladpap.pythonanywhere.com/admin/) (логин: admin пароль: kliekl)

## Добавление локации с помощью команды
```console
$ python3 manage.py load_place url_json_position
```
где `url_json_position` url json файла

пример
```console
$ python3 manage.py https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json
```

## Образец json файла
```console
{
    "title": "Смотровая площадка «Выше Только Любовь»",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/907b9e406d19964cf15dd0e5968f6411.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f33c9a13a204b27cfe1e52ad6d33e746.JPG"
    ],
    "description_short": "В одном из небоскрёбов бизнес-центра расположена уникальная смотровая площадка — «Выше Только Любовь», романтичное место и самая высокая точка в Европе, открытая для туристов. Здесь можно полюбоваться круговой панорамой города с высоты 354 метра, увидеть знакомые места с необычного ракурса и получить незабываемые эмоции.",
    "description_long": "<p>Согласно Книге рекордов России, «Выше Только Любовь» является самой высокой открытой смотровой площадкой — а это значит, что она точно поразит вас неповторимой панорамой. Вместе с тем площадка в самом сердце столицы полностью безопасна и имеет всё необходимое для приятного отдыха. Для посетителей играет музыка.</p><p>На небоскрёбе проводят бесплатные экскурсии (они входят в стоимость посещения), работает фотограф, бар и сувенирная лавка. Место понравится как коренным москвичам, так и туристам. Здесь каждый сможет сделать отличные фотографии на фоне столицы: так как на площадке отсутствует остекление, панорама будет видна без искажения. </p><p>Пространство «Выше Только Любовь» по праву можно считать одним из самых романтичных мест в Москве. На площадке установлен огромный одноимённый хештег: сюда регулярно приходят на свидания и ежедневно делают предложения руки и сердца.</p><p>С декабря до конца зимы на площадке функционирует ледяной городок с фигурами изо льда, горками и лабиринтом. Каждому гостю полагается вкусный комплимент! Подробности узнавайте на официальном<a class=\"external-link\" href=\"https://www.smotrovaya.com/\" target=\"_blank\"> сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/354oko/\" rel=\"nofollow\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.53484000000032",
        "lat": "55.74998119999979"
    }
}
```

## Цели проекта

Код написан в учебных целях — это командный проект на курсе по Python [Devman](https://dvmn.org).


<img src="https://dvmn.org/assets/img/logo.8d8f24edbb5f.svg" alt= “” width="102" height="25">