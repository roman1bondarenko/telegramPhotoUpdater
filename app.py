from datetime import datetime
from datetime import timedelta
import time
import os
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from imageGenerator import generate_images
from telethon.sync import TelegramClient

# !!! EXAMPLE !!!
# You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = os.environ['API_ID']
api_hash = os.environ['API_HASH']


TIME_DIFF = int(os.environ['TIME_DIFF'])


def is_time_changed(prev_converted_time):
    return convert_time(datetime.now() + timedelta(hours=TIME_DIFF)) != prev_converted_time


def convert_time(date_time):
    result = '0' + str(date_time.hour) + ':' if date_time.hour < 10 else str(date_time.hour) + ':'
    result += '0' + str(date_time.minute) if date_time.minute < 10 else str(date_time.minute)
    return result


def start_update_photo():
    prev_time = datetime.now() + timedelta(hours=TIME_DIFF)
    while True:
        if is_time_changed(convert_time(prev_time)):
            prev_time = datetime.now() + timedelta(hours=TIME_DIFF)
#            print(prev_time)
            client(DeletePhotosRequest(client.get_profile_photos('me')))
            file = client.upload_file('./images/' + convert_time(prev_time) + '.png')
            client(UploadProfilePhotoRequest(file))
#            print(file)
            time.sleep(59)


with TelegramClient('telegramPhotoUpdater', api_id, api_hash) as client:
    if len(os.listdir('./images/') ) == 0:
        generate_images()
    client.start()
    print('login success... start work')
    start_update_photo()
