import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests
from bs4 import BeautifulSoup


engine = pyttsx3.init('sapi5')#sapi5 is a microsoft api
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    """
    Wishing us Good morning/Afternoon/night

    """
    hour = int(datetime.datetime.now().hour)
    if hour >0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("This is your assistant, Jarvis sir. Please Tell me how can I help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    #speak("Good Morning! amit")
    wishme()
    while True:
        query = takeCommand().lower()

        #Making queries and getting results
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            print(results)
            speak("According to wikipedia...")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            print("Please tell me which channel you want to surf..")
            speak("Please tell me which channel you want to surf..")
            channel_name= takeCommand().lower()
            webbrowser.open(f"youtube.com/resullts?serach_query ={channel_name}")

        elif "ok google" in query:
            webbrowser.open("google.com")

        elif "play music" in query:
            music_dir= "#give dir here you have saved the music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))#use random module

        elif "the time " in query:
            stime = datetime.datetime.now().strftime("%H:%M:%S")#use specifiers
            speak(f"Sir The time is {stime}")

        elif "Open code" in query:
            codepath = "C:\\Users\\AMIT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email' in query:
            #to be completed
            try:
                speak("What should I say?")
                content = takeCommand()
                to ="required email"
                send_email(to, content)

                #make a dictionary of names and email
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")



