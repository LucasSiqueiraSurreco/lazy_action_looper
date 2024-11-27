import time
import json
from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key

mouse = MouseController()
keyboard = KeyboardController()

SPECIAL_KEYS = {
    "space": Key.space,
    "enter": Key.enter,
    "backspace": Key.backspace,
    "tab": Key.tab,
    "shift": Key.shift,
    "ctrl": Key.ctrl,
    "alt": Key.alt,
    "esc": Key.esc,
    "up": Key.up,
    "down": Key.down,
    "left": Key.left,
    "right": Key.right,
    "caps_lock": Key.caps_lock,
    "delete": Key.delete,
}

def play_events(file_name="events_log.json", loops=1):
    try:
        with open(file_name, "r") as file:
            events = json.load(file)

        for loop in range(loops):
            print(f"Starting loop {loop + 1} of {loops}...")
            start_time = None
            for event in events:
                event_type, timestamp, *args = event

                if start_time is None:
                    start_time = timestamp
                time.sleep(timestamp - start_time)
                start_time = timestamp

                if event_type == "mouse_move":
                    x, y = args
                    mouse.position = (x, y)
                elif event_type == "mouse_click":
                    x, y, button, pressed = args
                    mouse.position = (x, y)
                    if pressed:
                        mouse.press(Button[button])
                    else:
                        mouse.release(Button[button])
                elif event_type == "mouse_scroll":
                    x, y, dx, dy = args
                    mouse.scroll(dx, dy)
                elif event_type == "key_press":
                    key = args[0]
                    if key == "esc":
                        continue
                    if key in SPECIAL_KEYS:
                        keyboard.press(SPECIAL_KEYS[key])
                    else:
                        keyboard.press(key)
                elif event_type == "key_release":
                    key = args[0]
                    if key == "esc":
                        continue
                    if key in SPECIAL_KEYS:
                        keyboard.release(SPECIAL_KEYS[key])
                    else:
                        keyboard.release(key)

            print(f"Loop {loop + 1} completed.")

        print("Playback completed!")

    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except Exception as e:
        print(f"Error during playback: {e}")


if __name__ == "__main__":
    try:
        loops = int(input("How many times do you want to repeat the events? "))
        if loops < 1:
            print("The number of loops must be at least 1.")
        else:
            play_events(loops=loops)
    except ValueError:
        print("Please enter a valid number for the loops.")
