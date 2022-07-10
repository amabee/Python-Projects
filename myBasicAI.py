
import pyttsx3
import datetime
import speech_recognition as speech_recog
import webbrowser
import os
import wikipedia
import pyjokes, random
import cv2

_Master = "Paul"

#"VOICE"
voice_engine = pyttsx3.init('sapi5')
voices = voice_engine.getProperty('voices')
voice_engine.setProperty('voice', voices[1].id)
#"RATE"
voice_engine.getProperty('rate')
voice_engine.setProperty('rate', 125)
#"VOLUME"
voice_engine.getProperty('volume')
voice_engine.setProperty('volume', 50)

def speak(text):
    voice_engine.say(text)
    voice_engine.runAndWait()

def wishMe():
    time = int(datetime.datetime.now().hour)

    if time >= 0 and time < 12:
        speak("Good Morning Sire")
    elif time >=12 and time < 18:
        speak("Good Afternon Sir")
    else:
        speak("Good Evening Sir")

def _takeCommands():
    recog = speech_recog.Recognizer()
    with speech_recog.Microphone() as source:
        recog.adjust_for_ambient_noise(source, duration = 1)
        print("Listening...")
        audio = recog.listen(source)

    try:
        print("Thinking...")
        query = recog.recognize_google(audio, language = 'en-us')
        print(f"taken command is: {query}\n")

    except Exception as ex:
        print("Sorry something went wrong. Please try again.")

        query = None
    return query

def startup():
    speak("Alice at your service Sir")

def main():
    startup()
    wishMe()
    query = _takeCommands()

    if 'wikipedia' in query.lower():
        speak('searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 3)
        print(results)
        speak(results)

    elif 'open google' in query.lower():
            url = "google.com"
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

    elif 'open facebook' in query.lower():
            url = "facebook.com"
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

    elif 'open instagram' in query.lower():
            url = "instagram.com"
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

    elif 'open twitter' in query.lower():
            url = "twitter.com"
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

    elif 'open netflix' in query.lower():
            url = "netflix.com"
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        songs_dir =  "C:\\Users\\63956\\Music\\Musics"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'time and date today' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S %p")
        date =  datetime.datetime.now().strftime("%m %d %Y")
        speak(f"{_Master} the time is {strTime}")
        speak(f"{_Master} and the date is {date}")

    elif 'open visual code' in query.lower():
        codePath = "D:\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'joke' in query.lower():
        jokes = pyjokes.get_jokes()
        joke = random.choice(jokes)
        print(joke)
        speak(joke)

main()