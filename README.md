# J.A.S.H---a-python-based-AI-Assistant
### This is a sample AI assistant that was a part of my Grade 12 Practical Project. 

Using python programming language an AI (Artifical intelligence) is made to provide various purpose for the user. 
Artificial intelligence (AI), the ability of a digital computer or computer-controlled robot to perform tasks commonly associated with intelligent beings. The term is frequently applied to the project of developing systems endowed with the intellectual processes characteristic of humans, such as the ability to reason, discover meaning, generalize, or learn from past experience. Since the development of the digital computer in the 1940s, it has been demonstrated that computers can be programmed to carry out very complex tasks as, for example, discovering proofs for mathematical theorems or playing chess with great proficiency. Still, despite continuing advances in computer processing speed and memory capacity, there are as yet no programs that can match human flexibility over wider domains or in tasks requiring much everyday knowledge. On the other hand, some programs have attained the performance levels of human experts and professionals in performing certain specific tasks, so that artificial intelligence in this limited sense is found in applications as diverse as medical diagnosis, computer search engines, and voice or handwriting recognition.

Voice assistant can be used in cases of visual impairment and text is also displayed which can be useful in situations of hearing impairment. All our end users need to summon a query and expect the answers they require with the help of a voice engine by Google which we have utilized in our project.

## MODULES INCLUDED :
As we built this project in python we used a number of modules that ensure the working of this project . The modules we included are as follows : 
•	import gTTs          
•	import time	          
•	import playsound  
•	import pyaudio     
•	import speech_recognition as sr
•	import os		   
•	import random	   
•	import webbrowser  
•	import subprocess  
•	import wikipedia
•	import time
•	import translate

## FUNCTIONS INCLUDED:
1. SQL BASED:
•	displayres(are):- To display the details of Restaurants in an area.
•	displayhos(are):- To display the details of Hospitals in an area.
•	displayfuel(are):- To display the details of Fuels Stations in an area.
2. speak(audio):- To convert a given text to mp3 and playing the audio.
3. translate():- To translate given phrases from English to other languages.
4. wiki(s):- To retrieve information from wikipedia.com .

## HARDWARE AND SOFTWARE REQUIREMENTS : 
For this project the system requirements are as follows:
•	IDLE ver.3.7 64bit
•	A good Internet connection
•	Pre-Installed Python modules (AS MENTIONED ABOVE)
•	Chrome web-browser.
•	System Mic
•	System Speaker
•	MySQL Workbench 8.0 CE

##
The code is usually built on the basis of speech recognition and interpretation which is achieved by using gTTs module(Google text to speech) . The project is aimed at providing personal assistance for users. This AI also provides a lot of services from saying the time to cracking jokes (if the user feels bored). It can also surf the internet with the help of the user’s voice command. We are using Google speech recognition API and google text to speech for voice input and output respectively. The system’s microphone and speaker are used as source of input and output respectively. Key features of our project are as follows:-
1. User Greetings: 
•	Commands- Hello, Jash, How are you, Thanks, Your name?
2. Exception handling:
•	Many users tend to play with their voice assistants by using some inappropriate words which are recognized and replied by our assistant.
•	If the internet connection is not proper “Could not request results” will be returned.
•	If the audio is not clear "Oops! I could not understand audio" will be returned.
3. Wikipedia:
•	This function can be invoked by prefixing “tell me about” before the phrase the user actually wants to know about.
Eg: ‘Tell me about Abdul Kalam ’ will return 2 sentences about Abdul Kalam from Wikipedia.com
4. Translate:
•	This function can be invoked by saying “translator”.
Used to translate English to 106 other languages.
5. Connection to SQL Database: 
•	This function can be invoked by saying “search for nearby locations.”
•	The database consists of records of Hospitals, Restaurants and Petrol Stations from 3 areas. [ARUMBAKKAM, ANNA NAGAR, VADAPALANI]
6. Other Functionalities:
•	Shutting down the system: Invoked by “Go to sleep” command.
•	Games: Invoked by “Play some games” command.
•	Time: Invoked by “What is the time now” command.
•	Joke: Invoked by “Tell me a joke” command.
•	Open websites: Invoked by suffixing ‘.com’ behind the website name the user wishes to open.
•	Navigation: Invoked by “open maps” command.
•	System Information: Invoked by “Show me system information” command.


