import requests
import time

TOKEN = '5549505301:AAF2_wuBZBMQY5EOaqfbtnptY8rVQo_wzMU'
URL = 'https://api.telegram.org/bot'

def get_updates(offset=0):
    result = requests.get(f'{URL}{TOKEN}/getUpdates?offset={offset}').json()
    return result['result']

def send_message(chat_id, text):
    requests.get(f'{URL}{TOKEN}/sendMessage?chat_id={chat_id}&text={text}')

def send_photo_url(chat_id, img_url):
    requests.get(f'{URL}{TOKEN}/sendPhoto?chat_id={chat_id}&photo={img_url}')

def send_photo_file(chat_id, img):
    files = {'photo': open(img, 'rb')}
    requests.post(f'{URL}{TOKEN}/sendPhoto?chat_id={chat_id}', files=files)

def send_photo_file_id(chat_id, file_id):
    requests.get(f'{URL}{TOKEN}/sendPhoto?chat_id={chat_id}&photo={file_id}')

def check_message(chat_id, message):
    if message.lower() in ['привет', 'hello']:
        send_message(chat_id, 'Привет :)')
    elif message.lower() in 'фото по url':
        # Отправить URL-адрес картинки (телеграм скачает его и отправит)
        send_photo_url(chat_id, 'https://ramziv.com/static/assets/img/home-bg.jpg')
    elif message.lower() in 'фото с компьютера':
        # Отправить файл с компьютера
        send_photo_file(chat_id, 'info/start.ogg')
    elif message.lower() in 'фото с сервера телеграм':
        # Отправить id файла (файл уже хранится где-то на серверах Telegram)
        send_photo_file_id(chat_id, 'AgACAgIAAxkBAAMqYVGBbdbivL53IzKLfUKUClBnB0cAApy0MRtfMZBKHL0tNw9aITwBAAMCAAN4AAMhBA')


def run():
    update_id = get_updates()[-1]['update_id'] # Присваиваем ID последнего отправленного сообщения боту
    while True:
        time.sleep(2)
        messages = get_updates(update_id) # Получаем обновления
        for message in messages:
            # Если в обновлении есть ID больше чем ID последнего сообщения, значит пришло новое сообщение
            if update_id < message['update_id']:
                update_id = message['update_id'] # Присваиваем ID последнего отправленного сообщения боту
                # Отвечаем тому кто прислал сообщение боту
                check_message(message['message']['chat']['id'], message['message']['text'])

if __name__ == '__main__':
    run()