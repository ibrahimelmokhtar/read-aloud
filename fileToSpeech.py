from gtts import gTTS       # required to convert text-to-speech
import os                   # required to play audio file


def convertTextToSpeech(textFile, audioFile):
    with open(textFile, 'r') as file:
        for line in file.readlines():
            print(line.strip())
            obj = gTTS(text=line)
            obj.save(audioFile)
