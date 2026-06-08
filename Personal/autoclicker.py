#!/usr/bin/env python3

import threading
import time
import tkinter as tk
from tkinter import ttk
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, Key

class AutoClicker:
    def __init__(self):
        self.running = False
        self.program_running = True
        self.mouse = Controller()
        self.delay = 0.1
        self.click_limit = 0  # 0 means infinite
        self.clicks_done = 0
        self.button = Button.left

        # Start the clicking thread
        self.click_thread = threading.Thread(target=self.clicking_logic)
        self.click_thread.start()

        # Start the keyboard listener thread for the shortcut (F6)
        self.listener_thread = threading.Thread(target=self.start_listener)
        self.listener_thread.start()

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def toggle(self):
        if self.running:
            self.stop_clicking()
        else:
            self.start_clicking()

    def set_config(self, delay, limit):
        self.delay = delay
        self.click_limit = int(limit)
        # Reset counter if we restart
        if not self.running:
            self.clicks_done = 0

    def clicking_logic(self):
        while self.program_running:
            if self.running:
                # Check for finite clicking
                if self.click_limit > 0 and self.clicks_done >= self.click_limit:
                    self.stop_clicking()
                    continue

                # Perform the click
                self.mouse.click(self.button)
                self.clicks_done += 1
                time.sleep(self.delay)
            else:
                # Sleep briefly to avoid consuming 100% CPU when idle
                time.sleep(0.01)

    def start_listener(self):
        # Hotkey listener: Toggle on F6
        with Listener(on_press=self.on_press) as listener:
            listener.join()

    def on_press(self, key):
        if key == Key.f6:
            self.toggle()
            # Update GUI variable via callback if needed (omitted for simplicity)

    def exit(self):
        self.stop_clicking()
        self.program_running = False

# --- GUI Setup ---
def update_status(app, status_label):
    # Polling loop to update the status text
    if app.running:
        status_label.config(text=f"Status: RUNNING ({app.clicks_done})", foreground="green")
    else:
        status_label.config(text=f"Status: STOPPED ({app.clicks_done})", foreground="red")
    root.after(100, update_status, app, status_label)

def apply_settings():
    try:
        delay = float(delay_entry.get())
        limit = int(limit_entry.get())
        clicker.set_config(delay, limit)
    except ValueError:
        pass # Handle invalid input gracefully

root = tk.Tk()
root.title("Manjaro Autoclicker")
root.geometry("300x250")

clicker = AutoClicker()

# UI Elements
ttk.Label(root, text="Click Interval (seconds):").pack(pady=5)
delay_entry = ttk.Entry(root)
delay_entry.insert(0, "0.1")
delay_entry.pack()

ttk.Label(root, text="Click Limit (0 = Infinite):").pack(pady=5)
limit_entry = ttk.Entry(root)
limit_entry.insert(0, "0")
limit_entry.pack()

status_label = ttk.Label(root, text="Status: STOPPED", font=("Helvetica", 10, "bold"))
status_label.pack(pady=15)

btn_frame = ttk.Frame(root)
btn_frame.pack(pady=5)

apply_btn = ttk.Button(btn_frame, text="Apply Settings", command=apply_settings)
apply_btn.pack(side=tk.LEFT, padx=5)

# Hotkey Info
ttk.Label(root, text="Hotkey: Press F6 to Start/Stop").pack(side=tk.BOTTOM, pady=10)

# Start the GUI update loop
update_status(clicker, status_label)

# Handle window close
def on_closing():
    clicker.exit()
    root.destroy()
    exit()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
