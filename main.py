from fileToSpeech import *

textFile = "text-file.txt"
audioFile = "audio.mp3"

# convert text to speech:
convertTextToSpeech(textFile, audioFile)

# play obtained speech:
os.system(audioFile)
