
import pytesseract
import cv2
from PIL import Image


class ImageController:

    def __init__(self, image_name, type) -> None:
        self.image = cv2.imread(f'./data_temp/{image_name}.{type}')
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def read_text(self):
        text = pytesseract.image_to_string(self.image)
        return text