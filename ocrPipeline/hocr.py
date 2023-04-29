import sys
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

def pdf_to_hocr(pdf_file, output_folder):
    # Convert PDF to images
    images = convert_from_path(pdf_file)

    for i, img in enumerate(images):
        # Save image as a temporary file
        img_path = f"{output_folder}/temp_page_{i+1}.png"
        img.save(img_path, 'PNG')

        # Run Tesseract with hOCR config
        hocr_data = pytesseract.image_to_pdf_or_hocr(img_path, extension='hocr')

        # Save hOCR data as an .html file
        with open(f"{output_folder}/page_{i+1}.html", 'wb') as hocr_file:
            hocr_file.write(hocr_data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pdf_to_hocr.py input_pdf_file output_folder")
    else:
        pdf_file = sys.argv[1]
        output_folder = sys.argv[2]
        pdf_to_hocr(pdf_file, output_folder)