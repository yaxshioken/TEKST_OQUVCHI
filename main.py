import pytesseract
from PIL import Image



image = Image.open("photo_2023-10-26_07-33-39.jpg")
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

file_name = image.filename.split('.')[0]

custom_config = r'--oem 3 --psm 3'

text = pytesseract.image_to_string(image, config=custom_config)

print(text)

output_filename = file_name + '.txt'
with open(output_filename, 'w') as f:
    f.write(text)
