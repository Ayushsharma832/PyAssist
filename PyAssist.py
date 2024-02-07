import pyttsx3    # used to creates a engine which helps us in text to voice convertion
import os
import datetime
import webbrowser
import wikipedia
import speech_recognition as sr
import pyaudio
import pywhatkit
import random
import pyjokes
import cv2
from requests import get
import smtplib
import time
import pyautogui
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)   #voices[0].id is a male voice if we do voices[1].id we get a female voice

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishme():
    hours = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hours>=0 and hours<12:
        speak(f"Good Morning Sir, it's {tt}")
    elif hours>=12 and hours<17:
        speak(f"Good Afternoon Sir, it's {tt}")
    elif hours>=17:
        speak(f"Good Evening Sir, it's {tt}") 
    speak("I am jarvis. How can i help you today")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: " + query)
    except:
        print("Say that again please")
        return "None"
    return query

def sendemail(to,content):
    server = smtplib.SMTP('smtp.google.com',587)
    server.ehlo()
    server.starttls()
    server.login('sharmaayush832@gmail.com','asmsksas')
    server.sendmail('sharmaayush832@gmail.com',to,content)
    server.close()

if __name__== "__main__":
   wishme()
   while True:
    query = takecommand().lower()

    if 'open youtube' in query:
        webbrowser.open("youtube.com")
    
    elif 'open google' in query:
        speak("What do you want me to search")
        command = takecommand().lower()
        webbrowser.open(f"{command}")
    
    elif 'open facebook' in query:
        webbrowser.open("facebook.com")

    elif 'open linkedin' in query:
        webbrowser.open("linkedin.com")

    elif 'open instagram' in query:
        webbrowser.open("instagram.com")

    elif 'wikipedia' in query:
        speak('searching wikipedia')
        query = query.replace('wikipedia','')
        results = wikipedia.summary(query,sentace = 2)
        speak(results)
    #will run music on youtube
    elif 'play music on youtube' in query:
        query = query.replace('play music on youtube','')
        speak(f'playing {query}')
        pywhatkit.playonyt(query)
    #will run music on device
    elif 'play music from laptop' in query:
        music_dir = 'D:\\Music\\Songs\\English God'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir,random.choice(music_dir)))

    elif "send message" in query:
        pywhatkit.sendwhatmsg("+918839561708","This is a Jarvis generated msg",18,33)
    #No need of this as included in wishme function
    elif 'the time' in query:
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir the time is {strtime}")

    elif 'open vs code' in query:
        codepath = "C:\\Users\\sharm\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        speak("Starting vs code")
        os.startfile(codepath)

    elif "close vs code" in query:
        speak("Closing vs code")
        os.system('taskkill /f /im Code.exe')
        
    elif 'open notepad' in query:
        codepath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2210.5.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad"
        speak("Starting nodepad")
        os.startfile(codepath)

    elif "close notepad" in query:
        speak("Closing notepad")
        os.system('taskkill /f /im Notepad.exe')

    elif 'open command prompt' in query:
        speak("Starting command prompt")
        os.system('start cmd')    
    
    elif "close command prompt" in query:
        speak("Closing command prompt")
        os.system('taskkill /f /im cmd.exe')

    elif 'joke' in query:  
        joke_1 = pyjokes.get_joke(language='en', category='neutral')
        speak(joke_1)
    #Giving error solve later
    elif "open camera" in query:
        cap  = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('webcam', frame)
            k = cv2.waitKey(50)
            if k == 27:
                break
            cap.release()
            cv2.destroyAllWindows()

    elif 'ip address' in query:
        ip = get('https://api.ipify.org').text
        speak(f"your ip address is {ip}")
    #not working as less secure app setting is not available on google anymore
    elif 'send email' in query:
        try:
            speak("what should i send")
            content = takecommand().lower()
            to = "wearwolf877@gmail.com"
            sendemail(to,content)
            speak("Email has been sent")
        except Exception as e:
            print(e)
            speak("Sorry sir, I am not able to send this email")
    #Not proper
    elif "set alarm" in query:
        '''tt = time.strftime("%I:%M %p")
        if tt == "01:29 PM":'''
        nn = int(datetime.datetime.now().hour)
        if nn == 13:
            speak("alarm set")
            music_dir = 'D:\\Music\\Songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

    elif "switch the window" in query:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        time.sleep(1)
        pyautogui.keyUp("alt")

    elif "go to sleep" in query:
        os.system("rundll32.exe powrprof.dll, SetSuspendState 0, 1,0")
    
    elif "restart the system" in query:
        os.system("shutdown /r /t 5")

    elif "shutdown the system" in query:
        os.system("shutdown /s /t 5")

    elif 'your master' in query or 'who made you' in query:
        speak("A Btech student named Ayush Sharma is the person who made me.")

    elif 'jesus' in query:
        speak("Jesus is always there for you") 
    
    elif 'fuck' in query or 'fucker' in query:
        speak("Sir did you forgot your resolve of not saying bad words anymore")

    elif 'quit' in query:
        break