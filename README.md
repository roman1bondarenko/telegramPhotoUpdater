# Telegram Photo Updater

It update telegram user's photo by o'clock time

## Getting Started

### Installing

Go to https://my.telegram.org/auth and create app. Save api_id and api_hash. Replace it on app.py.

Install libraries

```
pip3 install -r requirements.txt
```

run app.py

```
python3 app.py
```
Than enter phone number like - '380994567321' and 2fa code from telegram.

NOTE: use phone number whith code of your country.

## Deployment

Before deploy it on server, to not auth on server, by first run, you can auth on your local machine first time
and then just copy telegramPhotoUpdater.session where save you sessions.

Like that :
![github-small](https://user-images.githubusercontent.com/17086715/61576433-be16b200-aae2-11e9-9965-b6db354ef665.png)

## Built With

* [telethon](https://github.com/LonamiWebs/Telethon) - MTProto API Telegram client library
* [pillow](https://pillow.readthedocs.io/) - Python Imaging Library
