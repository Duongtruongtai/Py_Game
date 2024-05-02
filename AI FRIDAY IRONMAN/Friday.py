# import thư viện
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
friday = pyttsx3.init()

vocie = friday.getProperty("voice")
friday.setProperty('vocie',vocie[1])
# Hàm để phát tiếng nói 
def speak(audio):
    print('F.I.R.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)
def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak('GOOD MORNING SIR')
    elif hour >= 12 and hour <18:
        speak('GOOD AFTERNOON SIR')
    elif hour >= 18 and hour <24:
        speak('GOOD NIGHT SIR')
    speak ('How can i help you ?')
def command():
    c =sr.Recognizer()
    with sr.Microphone() as source :
        c.pause_threshold=2
        audio = c.listen(source)
    try :
        query = c.recognize_google(audio,language='en')
        print("Sếp :" + query)
    except sr.UnknownValueError:
        print('Please repeat or typing the command')
        query = str(input('Your order is: '))
    return query
if __name__ == "__main__":
    welcome()
    while True :
        query = command().lower()
        if "google" in query:
           speak ('What shoul I Search BOSS ?')
           search = command().lower()
           url = f"https://www.google.com/?q={search}"
           wb.get().open(url)
           speak(f'Here is your {search} on google')
        query = command().lower()
        if "youtube" in query:
           speak ('What shoul I Search BOSS ?')
           search = command().lower()
           url = f"https://www.youtube.com/?q={search}"
           wb.get().open(url)
           speak(f'Here is your {search} on youtube')
        elif 'open video' in query :
            meme = r'C:\Users\Admin\Desktop\AI FRIDAY\meme.mp4'
            os.startfile(meme)
        elif 'time' in query:
            time()
        elif 'quit' in query:
            speak('Friday is quitting sir.GOODBYE BOSS')
            quit()