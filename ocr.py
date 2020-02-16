from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
print("avant")
print(pytesseract.image_to_string(Image.open('/home/olivier/atelier/ruzzle/data/tests/r.tiff')))
print("apres")