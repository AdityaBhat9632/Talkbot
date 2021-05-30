from chatterbot import ChatBot
import speech_recognition as sr
import pyttsx3
from chatterbot.trainers import ChatterBotCorpusTrainer
bot = ChatBot('Aditya')
bot.set_trainer(ChatterBotCorpusTrainer)



while(True):
    r = sr.Recognizer()
    print("Could nor Recognize Plz Reply ")
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source, duration=3)
        print("recognise")
       answer = r.recognize_google(audio)
        print(answer)

    msg = answer
    if((msg == 'bye') or (msg == 'Bye')):
        reply = 'Nice to talk to you.'
        print('{} : {}'.format(bot.name, reply))
        break
    else:
        con = pyttsx3.init()
        print(type(msg))
        print(msg)
        reply = bot.get_response(msg)
        con.say(reply)
        con.runAndWait()
        print('{} : {}'.format(bot.name, reply))
