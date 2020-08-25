import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')

#returns a list with two objects one for male and the other fo female
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id) #use voices[0] for male voice and [1] for female

#Initilisation of speech recogniser
r = sr.Recognizer()
with sr.Microphone() as source:
    #adjust for noise where microphone is placed
    r.adjust_for_ambient_noise(source, duration = 0.2)

    print("Listening...")
    audio = r.listen(source)

print("Recognising...")
#Convert audio to text
voice = r.recognize_google(audio, language = 'en-in')

print(f"You said {voice}.")
engine.say(voice) #speak out the text
engine.runAndWait() #Wait till speech is finished.
