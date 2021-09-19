import pytesseract
from PIL import Image

img = Image.open("image_formulas.jpg")
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text = pytesseract.image_to_string(img, lang="eng")
print(text.strip())

with open('formulas_from_image.txt', 'a') as f:
    f.write(text.strip()+"\n")
