from PIL import Image, ImageDraw, ImageFont
import os

IMAGE_W, IMAGE_H = (600, 400)
TEXT_SIZE = 200


def generate_image(time):
    img = Image.new('RGB', (IMAGE_W, IMAGE_H), color=(0, 0, 0))
    font = ImageFont.truetype('./font/digital-7.ttf', TEXT_SIZE)
    d = ImageDraw.Draw(img)
    text_w, text_h = d.textsize()
    d.text(((IMAGE_W - text_w) / 2, (IMAGE_H - text_h) / 2), time, font=font, fill=(255, 255, 0))
    img.save('./images/' + time + '.png')


def generate_images():
    if not os.path.exists('./images'):
        print('start generating images...')
        os.mkdir('./images')
        for hour in range(0, 24):
            for minute in range(0, 60):
                time = '0' + str(hour) + ':' if hour < 10 else str(hour) + ':'
                time += '0' + str(minute) if minute < 10 else str(minute)
                generate_image(time)
        print('end generating images')


generate_images()
