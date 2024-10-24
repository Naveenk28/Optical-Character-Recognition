from fpdf import FPDF
import textwrap
import pytesseract
from PIL import Image

# Set the path to your Tesseract executable
pytesseract.pytesseract.tesseract_cmd ="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def get_text(image_name):
    image = Image.open(image_name)
    text = pytesseract.image_to_string(image)
    return text

output = get_text("image.png")

def createPdf():
    # Create instance of FPDF class
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Set font
    pdf.set_font("Arial", size=12)

    # Set margins (left, top, right)
    pdf.set_margins(10, 10, 10)

    # Split the text into lines and wrap them to fit the page width
    lines = textwrap.wrap(output, width=70)  # Adjust width as needed

    # Output lines to PDF
    for line in lines:
        pdf.multi_cell(0, 10, line)

    # Save the pdf with name .pdf
    pdf.output("output.pdf")

if __name__ == "__main__":
    createPdf()
