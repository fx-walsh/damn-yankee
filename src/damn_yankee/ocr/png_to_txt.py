import pytesseract
from PIL import Image

# Optional: specify tesseract path (Windows only)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_image(image_path):
    try:
        # Load the image
        image = Image.open(image_path)

        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(image)

        print("Extracted Text:")
        print(text)
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace with your image path
if __name__ == "__main__":
    ocr_image("../data/damn-yankee-data/2004-03-01-2004-06-30/clean/copy0001.pdf_page_2.png")
