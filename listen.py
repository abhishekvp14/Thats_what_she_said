from twss import *
from sentences import *



import speech_recognition as sr

sample_rate = 48000

chunk_size = 2048

r = sr.Recognizer()

text = ''
while text.lower() != 'stop':
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something: ")
        audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio)
            #print("You said: " + text)
            
        except sr.UnknownValueError:
            print("Didnt get you.")
        except sr.RequestError as e:
            print("Could not request results from Google SRS; {0}".format(e))
            
    if(search(text)):
        michael()
    else:
        okay()