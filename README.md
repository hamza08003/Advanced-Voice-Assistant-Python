# Semester Project: Voice Assistant

## Overview

This is my personal semester project that implements a voice assistant using Python, allowing users to perform various tasks through voice commands. The assistant can open applications, fetch information from the internet, send emails and messages, and much more. It uses several libraries including `pyttsx3` for text-to-speech, `speech_recognition` for voice input, and external APIs for various functionalities.

## Features

- **Voice Commands**: Recognizes voice commands to perform tasks.
- **Text-to-Speech**: Converts text responses into spoken words.
- **Application Control**: Opens applications like Calculator, VS Code, Google Chrome, etc.
- **Web Searches**: Performs searches on Google and Wikipedia.
- **Entertainment**: Tells jokes, provides advice, and fetches trending movies.
- **Communication**: Sends emails and WhatsApp messages.
- **Weather Reports**: Provides current weather updates.
- **Screenshots**: Takes screenshots of the desktop.

## Libraries Used
- `time`: For handling time-related tasks.
- `pyttsx3`: A text-to-speech conversion library.
- `speech_recognition`: For converting speech into text.
- `decouple`: For managing environment variables.
- `datetime`: For handling date and time.
- `random`: For selecting random advice or jokes.
- `default_opening_txt`: A module containing default opening texts.
- `Functions.os_methods`: A module containing functions to open various applications.
- `Functions.online_methods`: A module containing functions for online tasks such as fetching IP, searching, sending emails, etc.

## Requirements

- Python 3.x
- Required Python libraries:
  - `pyttsx3`
  - `SpeechRecognition`
  - `python-decouple`
  - Additional libraries for online methods (refer to the Functions directory)
  
