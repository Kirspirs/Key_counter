import keyboard

def count_keys():

    key_count = 0

    while True:

        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_UP:

            key_count += 1
            print(f"count:{key_count}")

        if event.name == 'l':
            print(f"Programm stop. You pressed: {key_count}")
            break
def on_release(key):
    print(f"Name of the key pressed - {key.name}")
keyboard.on_release(on_release)


if __name__ == "__main__":    count_keys()

