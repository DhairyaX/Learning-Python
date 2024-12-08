from tkinter.messagebox import showinfo
from tkinter import *
import os
from gtts import gTTS
import speech_recognition as sr

mainwindow= Tk()
mainwindow.title(' Text-To-Speech and Speech-To-Text Converter')
mainwindow.configure(bg='#A2F3E6')
mainwindow.geometry('500x500')
mainwindow.resizable(0, 0)

def say(text1):
     language = 'en'
     speech = gTTS(text = text1, lang = language, slow = False)
     speech.save("text.mp3")
     os.system("start text.mp3")
 
def recordvoice():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            try:    
                text1 = r.recognize_google(audio,language="en-IN")
            except:
                pass
            return text1
        
        
def TextToSpeech():
    texttospeechwindow = Toplevel(mainwindow)
    texttospeechwindow.title('Text-to-Speech Converter')
    texttospeechwindow.geometry("500x500")
    texttospeechwindow.configure(bg='Blue')
 
    Label(texttospeechwindow, text='Text-to-Speech Converter', font=("Times New Roman", 15), bg='white').place(x=145,y=10)
 
    text = Text(texttospeechwindow, height=5, width=30, font=12)
    text.place(x=85, y=60)
   
    speakbutton = Button(texttospeechwindow, text='listen', bg='white', command=lambda: say(str(text.get(1.0, END))))
    speakbutton.place(x=240, y=200)
 
def SpeechToText():
    speechtotextwindow = Toplevel(mainwindow)
    speechtotextwindow.title('Speech-to-Text Converter')
    speechtotextwindow.geometry("500x500")
    speechtotextwindow.configure(bg='pink')
 
    Label(speechtotextwindow, text='Speech-to-Text Converter', font=("Times New Roman", 15), bg='white').place(x=145,y=10)
 
    text = Text(speechtotextwindow, font=12, height=3, width=30)
    text.place(x=85, y=100)
   
    recordbutton = Button(speechtotextwindow, text='Record', bg='Sienna', command=lambda: text.insert(END, recordvoice()))
    recordbutton.place(x=220, y=50)
 
Label(mainwindow, text='Text-To-Speech and Speech-To-Text Converter',
     font=('Times New Roman', 16), bg='#4995FF', wrap=True, wraplength=450).place(x=50, y=10)
 
texttospeechbutton = Button(mainwindow, text='Text-To-Speech', font=('Times New Roman', 16), bg='white', command=TextToSpeech)
texttospeechbutton.place(x=180, y=150)
 
speechtotextbutton = Button(mainwindow, text='Speech-To-Text', font=('Times New Roman', 16), bg='white', command=SpeechToText)
speechtotextbutton.place(x=180, y=250)
 
mainwindow.update()
mainwindow.mainloop()