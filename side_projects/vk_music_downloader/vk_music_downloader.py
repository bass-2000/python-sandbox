import os
from time import time

import requests
import vk_api
from vk_api import audio

REQUEST_STATUS_CODE = 200
name_dir = 'music_vk'
path = r'music' + name_dir
login = ''  # tel number
password = ''  # pwd
my_id = ''  # your id vk

if not os.path.exists(path):
    os.makedirs(path)


def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция.
    """

    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device


vk_session = vk_api.VkApi(login=login, password=password, auth_handler=auth_handler)
vk_session.auth()
vk = vk_session.get_api()
vk_audio = audio.VkAudio(vk_session)
os.chdir(path)

time_start = time()
for i in vk_audio.get_iter(owner_id=my_id):
    print(i)
    try:
        r = requests.get(i["url"])
        print(r)
        if r.status_code == REQUEST_STATUS_CODE:
            with open(i["title"] + '.mp3', 'wb') as output_file:
                output_file.write(r.content)
    except OSError:
        print(i["artist"] + '_' + i["title"])
time_finish = time()
print("Time seconds:", time_finish - time_start)
