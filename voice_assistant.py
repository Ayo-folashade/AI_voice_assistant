import datetime
import webbrowser
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import wikipedia
from pyjokes import pyjokes
from speech_recognition import Recognizer

listener: Recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

to_do_list = []
grocery_list = []


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jezz' in command:
                command = command.replace('jezz', '')
                print(command)
    except sr.RequestError:
        print('Speech Recognition service is unavailable.')
    except sr.UnknownValueError:
        print("I didn't understand what you said.")
    return command


def run_jezz():
    command = take_command()
    print(command)
    if 'to do' in command:
        task = command.replace('add to do', '')
        to_do_list.append(task)
        talk('added ' + task + ' to the to do list')
    elif 'show my list' in command:
        if len(to_do_list) == 0:
            talk('Your to-do list is empty.')
        else:
            talk('Here is your to-do list:')
            for i, task in enumerate(to_do_list):
                talk(str(i + 1) + ': ' + task)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'date' in command:
        talk('Sorry, I have a headache')
    elif 'are you in a relationship' in command:
        talk('No am not, but i do have a secret crush')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open google' in command:
        webbrowser.open_new_tab("https://www.google.com")
        talk("Google chrome is open now")
    elif 'search' in command:
        command = command.replace("search", "")
        webbrowser.open_new_tab(command)
        talk("Your search has finished loading")
    elif 'open gmail' in command:
        webbrowser.open_new_tab("gmail.com")
        talk("Google Mail open now")
    elif 'news' in command:
        webbrowser.open_new_tab("https://guardian.ng/")
        talk('Here are some headlines from The Guardian, Happy reading')
    elif 'tell me about yourself' in command:
        talk('My name is Jezz, your favourite talk buddy. I have been programmed to help you with tasks like:'
             'checking the time, opening youtube, google chrome and gmail, search the internet, take a photo, '
             'search wikipedia, predict weather in different cities,'
             'and give you latest headline news too!')
    elif "weather" in command:
        api_key = "styu7654566890ijhgfgsdf"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        talk("what city")
        city_name = take_command()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            talk(" Temperature in kelvin unit is " +
                 str(current_temperature) +
                 "\n humidity in percentage is " +
                 str(current_humidiy) +
                 "\n description  " +
                 str(weather_description))
            print(" Temperature in kelvin unit = " +
                  str(current_temperature) +
                  "\n humidity (in percentage) = " +
                  str(current_humidiy) +
                  "\n description = " +
                  str(weather_description))
    else:
        talk('Did not catch that.')


while True:
    run_jezz()
