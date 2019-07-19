from setuptools import setup

setup(
    name='telegramPhotoUpdater',
    version='1.0',
    description='App for updating telegram profile photo by clock time',
    author='Roman Bondarenko',
    author_email='romanbondarenko14@gmail.com',
    packages=['telegramPhotoUpdater'],  #same as name
    install_requires=['PIL', 'telethon'], #external packages as dependencies
)