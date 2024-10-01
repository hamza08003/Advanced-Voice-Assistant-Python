import requests
import openai
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

# Adding Necessary Credentials from our .env file
USER_EMAIL = config('EMAIL')
USER_PASS = config('PASSWORD')
TMDB_API_KEY = config("TMDB_API_KEY")
OPENAIGPT3_API_KEY = config('openai_API_KEY')
OPEN_WEATHER_API_KEY = config('Open_Weather_MAP_API_KEY')


# Function to get the IP Adress.
# ipify provides a simple public IP address API. We just need to make a GET request on this URL:
# https://api64.ipify.org/?format=json. It returns JSON data as def get_my_ip():
def get_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]


# Function to make search call on wikipedia, we are using the 'wikipedia' module for that.
def search_on_wikipedia(query):
    # Inside the wikipedia module, we have a summary() method that accepts a query as an argument,
    # Additionally, we can also pass the number of sentences required. Then we simply return the result.
    results = wikipedia.summary(query, sentences=2)
    return results


# For playing videos on YouTube, we are using 'PyWhatKit' for that. We have already imported it as kit.
def play_on_youtube(video):
    # PyWhatKit has a playonyt() method that accepts a topic as an argument,
    # It then searches the topic on YouTube and plays the most appropriate video. It uses PyAutoGUI under the hood.
    kit.playonyt(video)


# Again we will be using 'PyWhatKit' for searching on Google.
def search_on_google(query):
    # It has a method search() that helps us search on Google instantly.
    kit.search(query)


# Function to get random advice
def get_random_advice():
    # To get a random advice, we're using the 'Advice Slip API' and making a GET request on this API.
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']


# Function to get randon joke
def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    # To get a random joke, we just need to make a GET request on this URL: https://icanhazdadjoke.com/.
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


# For sending emails, we are using the built-in 'smtplib' module from Python.
# The method accepts receiver_address, subject, and message as arguments.
# Also, We've made sure that we have added EMAIL and PASSWORD in the .env file.
def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = USER_EMAIL
        email.set_content(message)
        # We create an object of the SMTP class from the smtplib module. It takes host and port number as the parameters.
        s = smtplib.SMTP("smtp.gmail.com", 587)
        # We then start a session and login with the email address and password and send the email.
        s.starttls()
        s.login(USER_EMAIL, USER_PASS)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False


# We'll be using PyWhatKit once again for sending WhatsApp messages,
# Our method accepts two arguments – the phone number number and the message.
def send_whatsapp_message(number, message):
    # It then calls the sendwhatmsg_instantly() method, to send a WhatsApp message.
    # Also, We've made sure that we are already logged in into our WhatsApp account on WhatsApp for Web.
    kit.sendwhatmsg_instantly(f"+92{number}", message)


# To get the trending movies, we'll be using The Movie Database (TMDB) API.
# We have added the TMDB_API_KEY in the .env file.
def get_trending_movies():
    trending_movies = []
    # As per the TMDB API Documentation, we're making a GET request. The Response will be a JSON file.
    res = requests.get(
        f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = res["results"]
    # From the JSON response we just need the title of the movie. We get the results which is a list and then iterate over it,
    # to get the movie title and append it to the trending_movies list. In the end, we return the first five elements of the list.
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5]


# To get the weather report, we're using the OpenWeatherMap API. Signup for a free account and get the APP ID.
# We have made sure to add the OPENWEATHER_APP_ID in the .env file.
def get_weather_report(city):
    # As per the OpenWeatherMap API, we need to make a GET request on the above-mentioned URL with the city name.
    # We'll get a JSON response
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPEN_WEATHER_API_KEY}&units=metric").json()
    try:
        weather = res["weather"][0]["main"]
    except KeyError:
        weather = "Not available"
    # We'll just need the weather, temperature, and feels_like from the above JSON response.
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"


# Function to answer almost every question asked by the user using GPT-3
def openaiGPT3(query):
    # set the API key for OpenAI's GPT-3 API
    openai.api_key = OPENAIGPT3_API_KEY
    # create a completion request using the GPT-3 API
    response = openai.Completion.create(
        # specify the engine to use
        engine="text-davinci-002",
        # The prompt to generate a response for
        prompt=query,
        # set the temperature to control the randomness of the response
        temperature=0.1,
        # set the maximum number of tokens to generate, , By setting max_tokens to a certain value, you can limit the length of the generated text.
        # Here we set it to 256 that means the API will return a maximum of 256 tokens in its response.
        max_tokens=256,
        # set the top-p value to control the proportion of the response that comes from the model
        top_p=1,
        # set the number of different completions to generate
        best_of=2,
        # set the frequency penalty to control the balance between generating novel words and using common words
        frequency_penalty=0.4,
        # set the presence penalty to encourage the model to generate words that were in the prompt
        presence_penalty=0.3)
    # get the text of the first choice
    answer = response['choices'][0]['text']
    # return the answer
    return answer
