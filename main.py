from fileToSpeech import *
from requiredDirectories import *


fileName = "hello-in-EnglishAccent.txt"

print("languages:\t1. 'english'\t2. 'arabic'")
language = 'en-us'      # default language
try:
    languageOption = int(input("Enter a number for your prefered language: "))
    if languageOption == 2:
        language = 'ar'
except:
    pass


directoryName = createRequiredDirectories(fileName)

inputFile = f"{directoryName}\\{fileName}"

fileName, extension = removeFileExtension(fileName)
audioFile = f"audio\\{fileName}\\{fileName}.mp3"
extension = extension[0]


# convert text to speech:
if extension == '.txt':
    convertTextToSpeech(inputFile, audioFile, language)

elif extension == '.pdf':
    convertPDFToSpeech(inputFile, audioFile, language)

else:
    print("Not a valid input format ...")
    sys.exit(0)


# get audio file full path:
audioFilePath = getPath() + '\\' + audioFile

# play obtained speech:
os.system(audioFilePath)
