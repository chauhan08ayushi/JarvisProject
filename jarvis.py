import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning mam")
        print("Good Morning mam")

    elif hour>=12 and hour<18:
        speak("Good Afternoon mam")

    else:
        speak("Good Evening mam")

    speak("I am Jarvis. How are you mam?")

def takeCommand():
    #It takes microphone input from the user and returns string output.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-us')
        print(f"You said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please.....")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

    #Logic for executing tasks based on query.
        if 'wikipedia' in query:
            speak("ok")
            speak('Searching wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'about you' in query:
            speak(f"I am good. Please tell me mam, how may I help you?")

        elif 'open youtube' in query:
            speak("ok")
            webbrowser.open("youtube.com")
            speak("done")

        elif 'open google' in query:
            speak("ok")
            webbrowser.open("google.com")
            speak("done")

        elif 'open gfg' in query:
            speak("ok")
            webbrowser.open("geeksforgeeks.org")
            speak("done")

        elif 'open stack overflow' in query:
            speak("ok")
            webbrowser.open("stackoverflow.com")
            speak("done")

        elif 'time' in query:
            speak("ok")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"the time is {strTime}")

        elif 'date' in query:
            speak("ok")
            strDate = datetime.datetime.now().strftime("%D")
            print(strDate)
            speak(f"the date is {strDate}")

        elif 'open vs code' in query:
            speak("ok")
            codePath = "C:\\Users\\MY PC\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("done")

        elif 'open whatsapp' in query:
            speak("ok")
            webbrowser.open("whatsapp.com")
            speak("done")

        elif 'open chrome' in query:
            speak("ok")
            webbrowser.open("chrome.com")
            speak("done")

        elif 'bye bye' in query:
            speak("Bye mam thank you")
            exit("Thank You!")
            