from gtts import gTTS
import time
import playsound
import pyaudio
import speech_recognition as sr
import os
import random
import webbrowser
import subprocess
from time import localtime, strftime
import time
from googletrans import Translator
import mysql.connector
import wikipedia


i=0
n=0

print('=================================================================================================')
print('')
print('                        _____   ___    ___                                    ')
print('                           |   |   |  /     |   |                             ')
print('                           |   |---|  ----, |---|                             ')
print('                         __/   |   |  ___/  |   |                             ')
print('')
print('')
print('=================================================================================================')
print('')
print('')
print('')




mydb=mysql.connector.connect(host='localhost',database='nearbyloc',user='root',passwd='sample')                
mycursor=mydb.cursor()

#HOSPITALS
mycursor.execute("SELECT * FROM hos where Area='ARUMBAKKAM'")
hosar=mycursor.fetchall()

mycursor.execute("SELECT * FROM hos where Area='ANNA NAGAR'")
hosan=mycursor.fetchall()

mycursor.execute("SELECT * FROM hos where Area='VADAPALANI'")
hosvd=mycursor.fetchall()

#RESTAURANTS
mycursor.execute("SELECT * FROM res where Area='ARUMBAKKAM'")
resar=mycursor.fetchall()

mycursor.execute("SELECT * FROM res where Area='ANNA NAGAR'")
resan=mycursor.fetchall()

mycursor.execute("SELECT * FROM res where Area='VADAPALANI'")
resvd=mycursor.fetchall()

#FUEL
mycursor.execute("SELECT * FROM fuel where Area='ARUMBAKKAM'")
flsar=mycursor.fetchall()

mycursor.execute("SELECT * FROM fuel where Area='ANNA NAGAR'")
flsan=mycursor.fetchall()

mycursor.execute("SELECT * FROM fuel where Area='VADAPALANI'")
flvd=mycursor.fetchall()


def displayhos(are):
        if are=='ARUMBAKKAM':
            for i in hosar:
                print(i)
        elif are=='ANNA NAGAR' or are=='ANNANAGAR':
            for i in hosan:
                print(i)
        elif are=='VADAPALANI':
            for i in hosvd:
                print(i)
        
def displayres(are):
        if are=='ARUMBAKKAM':
            for i in resar:
                print(i)
        elif are=='ANNA NAGAR':
            for i in resan:
                print(i)
        elif are=='VADAPALANI':
            for i in resvd:
                print(i)

def displayfuel(are):
        if are=='ARUMBAKKAM':
            for i in flsar:
                print(i)
        elif are=='ANNA NAGAR' or are=='ANNANAGAR':
            for i in flsan:
                print(i)
        elif are=='VADAPALANI':
            for i in flvd:
                print(i)

    



def speak(audio):
    tts = gTTS(text=rand,lang='en')
    filename ='speech'+str(random.randint(1,1000))+'.mp3'
    tts.save(filename)
    print('Jash  : ',rand)
    playsound.playsound(filename)


def translate():
    ip=input('Enter the statement you want to translate : ')
    languages={'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu', 'fil': 'Filipino', 'he': 'Hebrew'}
    print(languages)
    print('You can use the above code for your own language!')
    lang=input('Enter the language-code you want this to be translated : ')
    translator=Translator()
    k=translator.translate(ip,dest=lang)
    print(k)
    
def wiki(s):
    print(wikipedia.summary(s,sentences=2))
            
        

    
    

                                                   # obtain audio
while (i<1):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.adjust_for_ambient_noise(source)
        n=(n+1)     
        print("LISTENING....")
        audio = r.listen(source)
                                                   # interprete audio (Google Speech Recognition)
    try:
        s = r.recognize_google(audio)
        message = (s.lower())
        print ('User       : ',message)        
        
        if 'goodbye' in message or ('power off') in message or ('stop') in message:                          
            rand ='Goodbye Sir. Jash powering off in 3.. 2.. 1.. 0'
            speak(audio)
            break
        if 'translator' in message:
            translate()
        if 'tell me about' in message:
            se=message[14::]
            rand=str(wikipedia.summary(se,sentences=2))
            speak(audio)
        elif ('hello') in message or ('hi') in message:
            rand ="Hello Sir. I'm Jash - Your Assistant . At Your Service Sir. "
            speak(audio)

        elif ('thanks') in message or ('tanks') in message or ('thank you') in message:
            l1=['You are welcome','You are Extremely Welcome !','Always a pleasure ! ','You are welcome,I was literally made for this thing..!']
            rand =random.choice(l1)
            speak(audio)

        elif ('jash') in message:
            rand ='Yes Sir . Waiting for your command!..'
            speak(audio)


        elif  ('how are you') in message or ('and you') in message or ('are you okay') in message:
            rand ="I'm fine! What can I do for you??"
            speak(audio)

        elif  ('f***') in message or ('a******') in message:
            rand ='Be polite please'
            speak(audio)

        elif ('your name') in message:
            rand ="I'm Jash. At your service dude!"
            speak(audio)


        elif ('wi-fi') in message:  
            REMOTE_SERVER = "www.google.com"
            rand ='We are connected'
            speak(audio)


        elif ('.com') in message :                                                        #VersatileBrowsing
            rand = 'Opening' + message[5:]         
            speak(audio)
            mess=message[5:-1]+'m'
            webbrowser.open('http://www.'+mess)
            print ('')
            

        elif ('google maps') in message:                                                  #Maps
            query = message
            stopwords = ['google', 'maps']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            webbrowser.open("https://www.google.com/maps/place/"+result+"/")
            rand = 'Results shown!'
            tts = gTTS(text=rand,lang='en')
            filename ='speech13.mp3'
            tts.save(filename)
            print('Jash : ',rand)
            playsound.playsound(filename)


        if ('nearby') in message:
            
            choice=int(input('Enter [1] for HOSPITALS and [2] for RESTAURANTS AND [3] FOR FUEL PUMPS: '))
            area=input('Enter your area : ')
            are=area.upper()
            if choice==1:
                displayhos(are)
            elif choice==2:
                displayres(are)
            elif choice==3:
                displayfuel(are)
            else:
                print('INVALID CHOICE!')
        





        if ('sleep mode') in message:
            rand = ['good night']
            speakmodule.speak(rand,n,mixer)
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        if ('time') in message:
            tim = strftime("%X", localtime())
            rand = tim
            speak(audio)

        if ('joke') in message:
            ques=['What’s the best thing about Switzerland?','Hear about the new restaurant called Karma?']
            ans=['I don’t know, but the flag is a big plus.','There’s no menu: You get what you deserve.' ]
            k=random.randint(0,len(ques)-1)
            rand=ques[k]
            speak(audio)
            time.sleep(1)
            rand=ans[k]
            speak(audio)


        if ('system information') in message :
            rand='Your system information will be shown in a Command Window!'
            speak(audio)
            os.system('cmd /k "systeminfo"')

        if ('games')in message or ('game') in message:
            rand="I can help you to play the following games.."
            speak(audio)
            print('Ant, Bagels, Bounce, Cannon, Connect, Crypto, Fidget, Flappy, Guess, Life, Maze, Memory, Minesweeper, Pacman, Paint, Pong, Simonsays, Snake, Tictactoetiles, Tron')
            rand='Please enter your choice..'
            speak(audio)
            choice=input(' ')
            chf=choice.lower()
            fin='python -m freegames.'+chf
            os.system(fin)

        if ('what can you do') in message:
            rand="Here's what I can do: "
            speak(audio)
            print('1. Open URL. ')
            print('2. Navigation - Google maps.')
            print('3. Jokes.')
            print('4. Translate Phrases.')
            print('5. Tell you about a person, place and many such things.')
            print('4. Check connection status.')
            print('5. Show system Information.')
            print('6. Play games.')
            print('7. Tell you the time.')
            print('8. Search for Nearby Locations')
            

    # exceptions
    except sr.UnknownValueError:
        print("Oops! I could not understand audio")
        rand='Try Saying It Again...'
        speak(audio)
    except sr.RequestError as e:
        print("Could not request results$; {0}".format(e))
