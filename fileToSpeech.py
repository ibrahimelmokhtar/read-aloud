from gtts import gTTS       # required to convert text-to-speech
import os                   # required to play audio file


def convertTextToSpeech(textFile, audioFile):
    fullText = ""
    with open(textFile, 'r') as file:
        for line in file.readlines():
            fullText = f"{fullText} {line.strip()}"     # read all the text from the file

    obj = gTTS(text=fullText)
    obj.save(audioFile)
