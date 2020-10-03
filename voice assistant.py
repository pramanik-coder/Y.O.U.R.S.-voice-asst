import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import subprocess
from selenium import webdriver

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am YOURS. How may I help you today?")      

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print('e')    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")   


        elif 'play songs' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)    
            os.startfile(os.path.join(music_dir, songs[43]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'your name' in query:
            speak('I am YOURS. It means Your Own Ultimate Retainer Service.')
        
        elif 'search google'in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak('What do you want to search?')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                        # print("You said : {}".format(text))
                    driver = webdriver.Chrome('C:\\Users\\Ankan-HP\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\chromedriver.exe')
                    driver.get("https://google.co.in/search?q="+text) 

                except:
                    print("Sorry could not recognize what you said")
        
        elif 'search music'in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak('What do you want to listen?')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                        # print("You said : {}".format(text))
                    driver = webdriver.Chrome('C:\\Users\\Ankan-HP\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\chromedriver.exe')
                    driver.get("https://www.youtube.com/results?search_query="+text) 

                except:
                    print("Sorry could not recognize what you said")
                    
        elif 'open calculator' in query:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        
        elif 'open notepad' in query:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
        
        elif 'open wordpad' in query:
            subprocess.Popen('C:\\Windows\\System32\\write.exe')
        
        

        

        
