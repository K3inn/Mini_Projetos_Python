import pyttsx3
import time

engine = pyttsx3.init()
engine.setProperty('rate', 125)

def falar(frase):
	print("Falando...")
	time.sleep(5)
	engine.say(frase)
	engine.runAndWait()
