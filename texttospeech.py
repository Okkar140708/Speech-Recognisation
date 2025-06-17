import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour) #to determine the time of the day
    """
    
    """
    if hour >= 0 and hour <= 12:
        speak("Guten Morgen")
    elif hour >= 12 and hour < 18:
        speak("Guten Tag")
    else:
        speak("Guten Abend")
    speak("Lassen Sie mich wissen, wie ich Ihnen helfen kann, was suchen Sie nach?")

def takecommend(): #when a person say unclearly, this will ask again
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you.........")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing your voice.....")
        query = r.recognize_google(audio, language='de-DE')
        print(f"Sie haben gesagt : {query}\n")
    
    except Exception as e:
        print("Können Sie bitte wiederholen")
        return "None"
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('okkaraung1407@gmail.com','opks414221')
    server.sendmail('okkaraung1407@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishme()

    while True:
        query = takecommend().lower()

        if 'öffnen sie Wikipedia' in query:
            speak('Searching wikipedia ......')
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query, sentence=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            break

        if 'öffnen sie discord' in query:  # Added missing 'in query'
            npath = r"C:\Users\User\AppData\Local\Discord\Update.exe --processStart Discord.exe"
            os.startfile(npath)
            break

        elif 'öffnen sie whatsapp' in query:  # Added missing 'in query'
            npath = r"C:\Users\User\AppData\Roaming\Telegram Desktop\Telegram.exe"
            os.startfile(npath)
            break

        elif 'öffnen sie youtube' in query:
            webbrowser.open('youtube.com')
            break

        elif 'die zeit' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Jetzt ist es {strTime}")
            break