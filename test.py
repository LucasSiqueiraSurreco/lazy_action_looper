from pynput import mouse, keyboard
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener, Key
import time
import json

events = []
recording = True

def on_move(x, y):
    if recording:
        events.append(("mouse_move", time.time(), x, y))

def on_click(x, y, button, pressed):
    if recording:
        events.append(("mouse_click", time.time(), x, y, button.name, pressed))

def on_scroll(x, y, dx, dy):
    if recording:
        events.append(("mouse_scroll", time.time(), x, y, dx, dy))

def on_press(key):
    global recording
    if recording:
        events.append(("key_press", time.time(), key.name if hasattr(key, "name") else key.char))
    if key == Key.esc:
        print("Stopping recording...")
        return False

def on_release(key):
    if recording:
        events.append(("key_release", time.time(), key.name if hasattr(key, "name") else key.char))

def start_recording():
    global recording
    recording = True
    print("Recording started. Press ESC to stop.")
    with MouseListener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as mouse_listener, \
            KeyboardListener(on_press=on_press, on_release=on_release) as keyboard_listener:
        keyboard_listener.join()

    print("Recording stopped.")
    print(f"Captured events: {len(events)}")
    save_events()

def save_events():
    with open("events_log.json", "w") as file:
        json.dump(events, file, indent=4)
    print("Events saved in 'events_log.json'.")

if __name__ == "__main__":
    start_recording()
