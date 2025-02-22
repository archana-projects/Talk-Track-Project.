import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk
listening = sr.Recognizer()
engine = pt.init('dummy')

def speak(text):
    engine.say(text)
    engine.runAndWait()
def hear():
    cmd = ""  # Initialize cmd to an empty string
    try:
        with sr.Microphone() as mic:
            print('listening....')
            voice = listening.listen(mic)
            cmd = listening.recognize_google(voice)
            cmd = cmd.lower()
            if 'archana' in cmd:
                cmd = cmd.replace('archana', '')
                print(cmd)
    except Exception as e:
        print("Error:", e)  # Print the error for debugging
    return cmd
    
'''def hear():
    try:
        with sr.Microphone() as mic:
            print('listening....')
            voice = listening.listen(mic)
            cmd = listening.recognize_google(voice)
            cmd = cmd.lower()
            if 'archana' in cmd:
                cmd = cmd.replace('archana','')
                print(cmd)
    except:
        pass
    return cmd'''
def run():
    cmd = hear()
    print(cmd)
    if 'play' in cmd:
        song = cmd.replace('play', '')
        speak('playing' + song)
        pk.playonyt('Playing...' + song)

run()