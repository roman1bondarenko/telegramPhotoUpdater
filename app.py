from datetime import datetime
import time
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from imageGenerator import generate_images
from telethon.sync import TelegramClient

# !!! EXAMPLE !!!
# You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 32143245
api_hash = 'ajhfiuewhjr32orqdoiqjreqjpoiqjqorj'


def is_time_changed(prev_converted_time):
    return convert_time(datetime.now()) != prev_converted_time


def convert_time(date_time):
    result = '0' + str(date_time.hour) + ':' if date_time.hour < 10 else str(date_time.hour) + ':'
    result += '0' + str(date_time.minute) if date_time.minute < 10 else str(date_time.minute)
    return result


def start_update_photo():
    prev_time = datetime.now()
    while True:
        if is_time_changed(convert_time(prev_time)):
            prev_time = datetime.now()
            print(prev_time)
            client(DeletePhotosRequest(client.get_profile_photos('me')))
            file = client.upload_file('./images/' + convert_time(prev_time) + '.png')
            client(UploadProfilePhotoRequest(file))
            print(file)
            time.sleep(59)


with TelegramClient('telegramPhotoUpdater', api_id, api_hash) as client:
    generate_images()
    client.start()
    client.send_message('me', 'Hello, i login successful')
    print('login success... start work')
    start_update_photo()
