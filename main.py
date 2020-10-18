from fileToSpeech import *

pdfFile = "pdf-file.pdf"
audioFile = "audio.mp3"

# convert pdf to text:
convertPDFToSpeech(pdfFile, audioFile)

# play obtained speech:
os.system(audioFile)
