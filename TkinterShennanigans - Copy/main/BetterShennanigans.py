import random
import pynput
import pyautogui

class AntiClick:
    def __init__(self):
        self.last_mouse_position = (0, 0)
        self.if_click = False

        self.keyboard_listener = pynput.keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.mouse_listener = pynput.mouse.Listener(on_click=self.on_click, on_move=self.on_move)

        self.keyboard_listener.start()
        self.mouse_listener.start()

        with self.mouse_listener as pynput.mouse.Listener:
            with self.keyboard_listener as pynput.keyboard.Listener:
                self.listener.join()

    def on_click(self, x, y, button, pressed):
        decide = random.randint(1,3)
        if pressed:
            self.if_click = True
            ran_num_x = random.randint(-100, 100)
            ran_num_y = random.randint(-100, 100)
            pyautogui.moveTo(x + ran_num_x, y + ran_num_y, duration=0.1)
        else:
            self.if_click = False

    def on_move(self, x, y):
        self.last_mouse_position = (x, y)

    def on_press(self, key):
        pyautogui.press('backspace')

    def on_release(self, key):
        if key == pynput.keyboard.Key.caps_lock:
            self.mouse_listener.stop()
            return False

    def get_last_mouse_position(self):
        return self.last_mouse_position

    def not_click(self):
        return self.if_click

    def destroy(self):
        self.keyboard_listener.stop()
        self.mouse_listener.stop()