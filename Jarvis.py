import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as web 
import os
import smtplib
from win10toast import ToastNotifier
import playsound
import pyfirmata


engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#os.startfile("C:\\Program Files\\Rainmeter\\Rainmeter.exe")
#playsound.playsound("C:\\Users\\kn392\\PycharmProjects\\Jarvis\\.idea\\inspectionProfiles\\jarvis\\power up.mp3")
#playsound.playsound("C:\\Users\\kn392\\PycharmProjects\\Jarvis\\.idea\\inspectionProfiles\\jarvis\\Jarvis.mp3")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak("Hi sir i am Jarvis . how may i help you")

def takecommand():
    r = sr.Recognizer()


    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        # print(e) 
        print("say that again please...")
        return "none"        
    return query

#board = pyfirmata.Arduino('COM3')

#board.digital[10].mode = pyfirmata.OUTPUT
#board.digital[10].write(1)
#board.digital[11].mode = pyfirmata.OUTPUT
#board.digital[11].write(1)
#board.digital[12].mode = pyfirmata.OUTPUT
#board.digital[12].write(1)

toast = ToastNotifier()
toast.show_toast("Jarvis","the Jarvis is now activated",duration=3)

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('nabeelakmal007@gmail.com','khan86250')
    server.sendmail('nabeelakmal007@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    wishMe()

def taskexe():

    while True:
        query = takecommand().lower()

        
        if 'wikipedia' in query:
           speak('searching wikipedia...')
           query = query.replace("wikipedia", "")
           reasults = wikipedia.summary(query, sentences=2)
           speak("according to wikipedia")
           speak(reasults)

        elif 'Wake up ' in query:
            os.startfile("C:\\Users\\kn392\\PycharmProjects\\Jarvis\\.idea\\inspectionProfiles\\jarvis")

        elif 'hello how are you' in query:
            speak("i am fine sir")
            break

        elif 'you need a break' in query:
            speak("ok sir, you can call me anytime !")
            speak("just say wake up jarvis !")
            break

        elif 'open youtube' in query:
           web.open("youtube.com") 

        elif 'instagram' in query:
            web.open("instagram.com")

        elif 'facebook' in query:
            web.open("facebook.com")

        elif 'open google'in query:
           web.open("google.com")

        elif 'open stackoverflow'in query:
            web.open("stackoverflow.com")

        elif 'play music'in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is{strtime}")
            print(strtime)    

        elif 'open code' in query:
            codepath ="C:\\Users\\kn392\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codepath)  

        elif 'email to nabeel' in query:
            try:
                speak("what should i send?")
                content = takecommand()
                to = "nabeelakmal007@gmail.com"
                sendemail(to,content)
                speak("email has been sent!")
            except Exception as e:
                # print(e)
                speak("sorry sir.i am not able to send this email")

        elif 'whatsapp message' in query:

            name = query.replace("whatsapp message", "")
            name = name.replace("send","")
            name = name.replace("to","")
            Name = str(name)
            speak(f"whats the message for {Name}")
            MSG = takecommand()
            from automation import WhatsappMsg
            WhatsappMsg(Name,MSG)

        elif 'call' in query:
            from automation import WhatsappCall
            name = query.replace("call","")
            name = name.replace("jarvis","")
            Name = str(name)
            WhatsappCall(Name)

        elif 'Show Chat' in query:
            speak("with whom ?")
            name = takecommand()
            from automation import WhatsappChat
            WhatsappChat(name)

        elif 'whatsapp Status' in query:
            speak("whose ?")
            name = takecommand()
            from automation import WhatsappStatus
            WhatsappStatus(name)

        elif 'videocall' in query:
            from automation import WhatsappVideocall
            name = query.replace("videocall", "")
            name = name.replace("jarvis", "")
            Name = str(name)
            WhatsappVideocall(Name)

        elif 'turn on the light' in query:
            speak("Initiating your request")
            board.digital[10].write(0)
        
        elif 'turn off the light' in query:
            speak("Initiating your request")
            board.digital[10].write(1)

        elif 'turn on the fan' in query:
            speak("Initiating your request")
            board.digital[11].write(0)
        
        elif 'turn off the fan' in query:
            speak("Initiating your request")
            board.digital[11].write(1)   

        elif 'turn on the charger' in query:
            speak("Initiating your request")
            board.digital[12].write(0)
        
        elif 'turn off the charger' in query:
            speak("Initiating your request")
            board.digital[12].write(1)   

taskexe()    

               
