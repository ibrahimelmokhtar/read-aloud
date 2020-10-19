# read-aloud

A console application where you can enter file name, with file extension, and get audio file containing the text at this file. You can work with .txt, .pdf, or .jpg formats.  
You can think of the following situations as input:
* Plain text file
* Plain PDF file
* Book page picture
* Message screenshot

*Note:*
* *You need to install the used libraries*
* *You need to install [pre-built binary package](https://github.com/UB-Mannheim/tesseract/wiki) from [Tesseract documentation](https://tesseract-ocr.github.io/tessdoc/Home.html),  
and set its path to the following path: **'C:\Program Files\Tesseract-OCR\tesseract.exe'***
* *Files should be placed within the main directory at first*
* *Image files **MUST** be in .jpg format*

## What I learnt

* Converting different files into text files
* Directory/File manipulation using code (Add, Move, Delete, and Open)
* Converting text file into audio file
* Applying RegEx (Regular Expression) to find specific patterns i.e. file extension


## Used libraries

* [**gtts** library](https://pypi.org/project/gTTS/): used to convert text into speech
* [**PyPDF2** library](https://pypi.org/project/PyPDF2/): used to convert pdf into text
* [**PIL** library](https://pypi.org/project/Pillow/): used to process the images
* [**pytesseract** library](https://pypi.org/project/pytesseract/): used to convert image to text
* **re** library: used to apply regular expressions to find file extension
* **shutil** library: used to move files to different directory
* **os** library: used to play audio files from the operating system, and get file path
