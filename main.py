import time
import pyttsx3
import speech_recognition as sr
from decouple import config
from datetime import datetime, date
from random import choice
from default_opening_txt import opening_text
from Functions.os_methods import open_calculator, open_chrome, open_cmd, open_camera, open_vscode, open_ms_word, take_ss
from Functions.online_methods import get_my_ip, search_on_wikipedia, play_on_youtube, search_on_google, get_random_advice,\
    get_random_joke, send_email, send_whatsapp_message, get_trending_movies, get_weather_report, openaiGPT3


USER_NAME = config('USER')
BOT_NAME = config('BOT_NAME')

# Object Creation - getting a reference to pyttsx3
engine = pyttsx3.init('sapi5')
# Set the Rate
# Here 'rate' is an Integer speech rate in words per minute. Defaults to 200 words per minute.
engine.setProperty('rate', 150)
# Set the Volume
# Here 'volume' is the floating point volume in the range of 0.0 to 1.0. Defaults to 1.0.
engine.setProperty('volume', 1.0)


# Set Voice Type
# Getting the current value of an engine property
# Here voices is the String identifier of the active voice.
voices = engine.getProperty('voices')
# Here you can switch between different voices installed on your system.
engine.setProperty('voice', voices[3].id)


# Text to Speech Conversion
def speak(text) -> None:
    """This function Speaks whatever text is passed to it"""

    # Queues a command to speak an utterance.
    engine.say(text)
    # Blocks while processing all currently queued commands,
    # Returns when all commands queued before this call are emptied from the queue.
    engine.runAndWait()


# Greeting Function
def greet() -> None:
    """Greets the user according to the current hour"""

    # Get the current hour
    cur_hour = int(datetime.now().hour)
    # Get the current time
    cur_time = time.strftime("%I:%M %p")
    # Get the current Day
    current_day = date.today().strftime("%A")

    # If the time is between 6AM - 12PM, then says 'Good Morning' to the user.
    if (cur_hour >= 6) and (cur_hour < 12):
        print(
            f"\033[1m\033[91mGood Morning {USER_NAME}, Its {current_day} {cur_time}\033[0m")
        speak(f"Good Morning {USER_NAME}, Its {current_day} {cur_time}")

    # If the time is between 12PM - 4PM, then says 'Good afternoon' to the user.
    elif (cur_hour >= 12) and (cur_hour < 16):
        print(
            f"\033[1m\033[91mGood Afternoon {USER_NAME}, Its {current_day} {cur_time}\033[0m")
        speak(f"Good afternoon {USER_NAME}, Its {current_day} {cur_time}")

    # If the time is between 4PM -  7PM, then says 'Good Morning' to the user.
    elif (cur_hour >= 16) and (cur_hour < 19):
        print(
            f"\033[1m\033[91mGood Evening {USER_NAME}, Its {current_day} {cur_time}\033[0m")
        speak(f"Good Evening {USER_NAME}, Its {current_day} {cur_time}")

    print(
        f"\033[3m\033[1m\033[91m\nI am {BOT_NAME}. How may I assist you?\033[0m")
    speak(f"I am {BOT_NAME}. How may I assist you?")


# Speech to text
def take_user_input() -> str or Exception:
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""

    # Initialize the Recognizer, i-e create an instance of the Recognizer Class
    a = sr.Recognizer()
    # Using the microphone as a source for input.
    with sr.Microphone() as source:
        print('\033[3m\033[1m\033[92m\nListening.... \033[0m')
        a.adjust_for_ambient_noise(source)
        # Represents the minimum length of silence (in seconds) that will be considered as the end of a phrase.
        a.pause_threshold = 1
        # Listens for the user's input.
        audio = a.listen(source)

    try:
        print('\033[3m\033[1m\033[92mRecognizing...\033[0m')
        # Using google to recognize the audio to transcribe the speech using Google Web API
        command = a.recognize_google(audio, language='en-PK')
        print(f"\033[1m\033[93mUser Said: {command} \n\033[0m")

        # If the user says 'exit' or 'stop', we will greet him again according
        # to the time and then the program will exit.
        if 'exit' in command or 'stop' in command:
            hour = datetime.now().hour
            if (hour >= 21) and (hour < 6):
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
        else:
            speak(choice(opening_text))

    # If the TTS engine doesn't recognizes the audio then it will say for the input again.
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        command = 'None'
    return command


# Main Function
def main():

    # Calling the greet() function
    greet()

    # Loop till user doesn't says 'exit' or 'stop'.
    while True:

        # Take the input (voice command) from the user.
        command = take_user_input().lower()

        if 'open calculator' in command:
            open_calculator()

        elif 'open camera' in command:
            open_camera()

        elif 'open command prompt' in command:
            open_cmd()

        elif 'open vs code' in command:
            open_vscode()

        elif 'open google chrome' in command:
            open_chrome()

        elif 'open ms word' in command:
            open_ms_word()

        elif 'get my ip' in command:
            ip_address = get_my_ip()
            speak(
                f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in command:
            speak('What do you want to search on Wikipedia, sir?')
            search_command = take_user_input().lower()
            results = search_on_wikipedia(search_command)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'youtube' in command:
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'google search' in command:
            speak("What do you want to search on google, sir?")
            search = take_user_input().lower()
            search_on_google(search)

        elif "give me some advice" in command:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            print(advice)

        elif 'tell me a joke' in command:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            print(joke)

        elif "send an email" in command:
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            speak("What is the message sir?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak(
                    "Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif "send whatsapp message" in command:
            speak(
                'On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        elif 'get weather report' in command:
            city = 'Taxila, Punjab, Pakistan'
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(
                f"The current temperature of your city is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(
                f"City:{city}\nDescription: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

        elif "trending movies" in command:
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_trending_movies(), sep='\n')

        elif "take screenshot" in command:
            take_ss()
            speak("Screen Shot Taken")

        else:
            speak("I am searching for the question you asked ! Please Hold on ...")
            f_answer = openaiGPT3(command)
            speak("Here is your answer....")
            speak(f_answer)
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"\033[92m{f_answer}\033[0m")


if __name__ == "__main__":
    main()
