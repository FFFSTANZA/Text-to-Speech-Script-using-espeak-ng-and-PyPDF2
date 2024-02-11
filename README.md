 ****Text-to-Speech Script using espeak-ng and PyPDF2****

The purpose of this script is to convert text from a specified range of pages in a PDF file to speech using the espeak-ng text-to-speech engine. The script is designed to offer a simple and direct approach to text-to-speech functionality without relying on external Python libraries like gTTS or pyttsx3.

**Key Features:
Modularity and Simplicity:**
The script is modular and easy to understand, consisting of a main function read_pdf to read the PDF file and convert text to speech.
It emphasizes simplicity by leveraging Python's built-in subprocess module to call the external espeak-ng command.

**Page Range Control:**
The script allows the specification of a page range to convert only a portion of the PDF to speech. This is achieved through the start_page and end_page parameters.

**Speaking Rate Customization:**
The speaking rate is a customizable parameter (speaking_rate) that allows users to adjust the speed of speech according to their preferences.

**PDF Text Extraction:**
Utilizes the PyPDF2 library for reading PDF files and extracting text from each page. This ensures compatibility with a wide range of PDF documents.

**External Tool Integration:**
By using the subprocess module, the script integrates with the espeak-ng command-line tool, allowing the conversion of text to speech without relying on additional Python libraries.

**Usage:
PDF File Path:**
Specify the path to the PDF file in the pdf_path variable.

**Page Range:**
Set the start_page and end_page variables to define the range of pages to convert to speech.

**Speaking Rate Adjustment:**
Customize the speaking_rate variable to control the speed of speech.

**Considerations:
Dependency on espeak-ng:**
The effectiveness of this script relies on the availability of the espeak-ng tool on the system. Ensure that espeak-ng is installed before running the script.

**Limited Feature Set:**
While this script provides a straightforward text-to-speech solution, it may lack advanced features and customization options offered by dedicated Python libraries.

**Platform Compatibility:**
The script assumes compatibility with Linux-like systems where espeak-ng is commonly available. Compatibility with other operating systems may require adjustments.
