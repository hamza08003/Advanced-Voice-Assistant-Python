import os
import subprocess as sp
import pyautogui
import tkinter as tk
from tkinter import filedialog

# Software Paths Installed on PC
paths = {
    'google_chrome': "C:\\Program Files\\Google\Chrome\\Application\\chrome.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'VS_Code': "C:\\Users\\hamza\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe",
    'Ms_Word': "C:\\Program Files\\Microsoft Office\\root\Office16\\WINWORD.exe"
}

# Function to open 'Google Chrome'


def open_chrome():
    sp.Popen(paths['google_chrome'])


# Function to open 'Calculator'
def open_calculator():
    sp.Popen(paths['calculator'])


# Function to open 'VS Code'
def open_vscode():
    sp.Popen(paths['VS_Code'])


# Function to open 'Microsoft Word'
def open_ms_word():
    sp.Popen(paths['Ms_Word'])


# Function to open 'Command Prompt'
def open_cmd():
    os.system('start cmd')


# Function to open 'Camera'
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


# Function to take screenshot using pyautogui and save it specifed location through tkinter
def take_ss():
    # Take the screenshot
    screenshot = pyautogui.screenshot()
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()
    # Ask the user for the save location
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png", initialfile="screenshot.png")
    # Save the screenshot
    screenshot.save(file_path)
