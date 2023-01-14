import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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

def Pass(pass_inp):

    password = "ironman"

    passs = str(password)

    if passs==str(pass_inp):

          speak("access granted .")
         
          print('access granted')

          import Jarvis
        
    else:

        speak("access not granted")

if __name__ == "__main__" :

    speak("this particular file is password protected .")
    
    speak("kindly provide the password to access .")
    
    passssss = input(":Enter the password :")

    Pass(passssss)