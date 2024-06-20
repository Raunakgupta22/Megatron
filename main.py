import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import sys
import random
import threading

sys.path.append('/path/to/directory/containing/api.py')

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = r.listen(source)
        
    try:
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}")
        return query
    except Exception as e:
        print(e)
        say("Sorry, I couldn't understand. Please say that again.")
        return ""

def speak_async(text):
    thread = threading.Thread(target=say, args=(text,))
    thread.start()

if __name__ == "__main__":
    print("Hello")
    speak_async("Hello, I am Megatron A I Robot, how can i help you today")
    
    while True:
        text = takeCommand().lower()

        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.org"],
            ["google", "https://www.google.com"],
            ["instagram", "https://www.instagram.com"],
            ["amazon", "https://www.amazon.in"],
            ["github", "https://github.com/"],
            ["chat GPT", "https://www.facebook.com"],
        ]
        for site in sites:
            if f"open {site[0]}" in text:
                speak_async(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "open music" in text:
            musicPath = "C:/Users/Dell/Downloads/Shin-Chan-Title.mp3"
            os.startfile(musicPath)

        if "the time" in text:
            time_now = datetime.datetime.now().strftime("%H:%M")
            speak_async(f"Sir, the time is {time_now}")

        if "search in google" in text:
            query = text.replace("search in google", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")

        if "say" in text:
            say(text.replace("say", ""))

        if "stop" in text:
            say("I am stopping")
            break

        if "hello" in text:
            speak_async("hi sir")

        if "hi" in text:
            speak_async("hello sir")

        if "how are you" in text:
            speak_async("I am fine sir")
        
        if "name" in text:
            speak_async("my name is Megatron")
        

        if "who have created you" in text or "who has created you" in text:
            speak_async("Raunak Gupta has created me")

        if "thank" in text or "shukriya" in text:
            speak_async("You are welcome sir")

        if "random number" in text:
            rnum = random.randint(0, 999999)
            speak_async(f"Your random number is {rnum}")

        if "add" in text:
            speak_async("Type here the numbers you want to add")
            num1 = int(input("Enter your number 1: "))
            num2 = int(input("Enter your number 2: "))
            speak_async(f"Your answer is {num1 + num2}")

        if "subtract" in text:
            speak_async("Type here the numbers you want to subtract")
            num1 = int(input("Enter your number 1: "))
            num2 = int(input("Enter your number 2: "))
            speak_async(f"Your answer is {num1 - num2}")



