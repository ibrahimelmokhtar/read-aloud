import os                   # play audio file
import shutil               # move files
import re                   # Regular Expression: find file extension
import sys                  # exit with no errors


# get program's absolute path:
def getPath():
    path = os.path.abspath(__file__).split("\\")
    path.pop()
    path = '\\'.join(path)

    return path


# try creating all required directories:
def tryCreateDirectory(directoryName):
    try:
        os.makedirs(directoryName)
    except:
        pass


# try moving the file to its similar directory:
def tryMovingFile(fileName, directoryName):
    try:
        shutil.move(fileName, directoryName)
    except:
        print("*** can NOT move that file: File already exists ***")

# remove file extension
def removeFileExtension(fileName):
    # find the extension part using regEx:
    extension = re.findall(r'\.[a-z]{3}', fileName)

    # split string at the found extension then select the first part:
    fileName = fileName.split(extension[0])[0]

    return fileName, extension


def createRequiredDirectories(fileName):
    # create the corresponding directory:
    if fileName.endswith('.txt'):
        directoryName = "text"
    elif fileName.endswith('.pdf'):
        directoryName = "pdf"
    elif fileName.endswith('.jpg'):
        directoryName = "image"
    else:
        print("Undefined file type ...")
        sys.exit(0)

    # try creating the required directories:
    tryCreateDirectory(directoryName)

    # try moving the input file to its corresponding directory:
    tryMovingFile(fileName, directoryName)

    # remove file extension:
    fileName, _ = removeFileExtension(fileName)

    # create a folder inside audio directory with the same file's name:
    audioDir = f"audio/{fileName}"
    tryCreateDirectory(audioDir)

    print("Created required folders ...")
    print(f"Your file has been moved to {directoryName} ...")

    return directoryName
