import PyPDF2
import subprocess

def read_pdf(pdf_path, start_page, end_page, speaking_rate=150):
    book = open(pdf_path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    total_pages = pdfReader.numPages
    start_page = max(0, min(start_page, total_pages - 1))
    end_page = min(end_page, total_pages)
    for num in range(start_page, end_page):
        page = pdfReader.getPage(num)
        text = page.extractText()
      
        subprocess.run(['espeak-ng', '-s', str(speaking_rate), text])

    book.close()

if __name__ == "__main__":
    pdf_path = '/home/fffstanza/Downloads/sample.pdf'
    start_page = 7
    end_page = 10  
    speaking_rate = 125

    read_pdf(pdf_path, start_page, end_page, speaking_rate)
