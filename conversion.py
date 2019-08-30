# to Import Translator module from googletrans package
from googletrans import Translator
from gtts import gTTS
x=Translator()
# default input taken as english

# giving input for the Source language
source_language=input('Enter Source Language: ')

# give the input word/sentance
word=input('Enter Source word: ')

# giving input for the Destination language
destination_language=input('Enter Destination Language: ')

# "dest=" destination language
y=x.translate(word,src=source_language,dest=destination_language)

# Translated word
z=y.text
print(word,'meaning in ',destination_language,'is: ',z)

# Destination language pronunciation
print(" Pronunciation:", y.pronunciation)

# Converting the Destination language text to speech
tts = gTTS(z)
tts.save('z.mp3')
