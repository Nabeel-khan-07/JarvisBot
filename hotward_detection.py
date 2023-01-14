import os
import speech_recognition as sr

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
        print("say that again please...")
        return "none"
        
    return query.lower()

while True:

    Wake_up = takecommand()

    if 'wake up' in Wake_up:

        os.startfile("C:\\Users\\kn392\\PycharmProjects\\Jarvis\\.idea\\inspectionProfiles\\Jarvis\\Jarvis.py")

    else:

        print("Nohing...")