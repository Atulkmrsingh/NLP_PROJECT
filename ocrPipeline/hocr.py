import sys
from pdf2image import convert_from_path
import pytesseract

def pdf_to_text(pdf_file, output_folder):
    # Convert PDF to images
    images = convert_from_path(pdf_file)

    for i, img in enumerate(images):
        # Save image as a temporary file
        img_path = f"{output_folder}/temp_page_{i+1}.png"
        img.save(img_path, 'PNG')

        # Run Tesseract with default config
        text_data = pytesseract.image_to_string(img)

        # Save OCR-ed text as a text file
        with open(f"{output_folder}/page_{i+1}.txt", 'w') as text_file:
            text_file.write(text_data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pdf_to_text.py input_pdf_file output_folder")
    else:
        pdf_file = sys.argv[1]
        output_folder = sys.argv[2]
        pdf_to_text(pdf_file, output_folder)
