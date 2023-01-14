import pyttsx3
import speech_recognition as sr
import pyfirmata


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

board = pyfirmata.Arduino('COM3')

board.digital[10].mode = pyfirmata.OUTPUT
board.digital[10].write(1)
board.digital[11].mode = pyfirmata.OUTPUT
board.digital[11].write(1)
board.digital[12].mode = pyfirmata.OUTPUT
board.digital[12].write(1)


while True:
    query = takecommand().lower()
    if 'on the light' in query:
        speak("Initiating your request")
        board.digital[10].write(0)
    elif 'off the light' in query:
        speak("Initiating your request")
        board.digital[10].write(1)