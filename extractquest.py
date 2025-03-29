import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import os

pdf_path = r'C:\Users\bajaj.MANANBAJAJ\Saved Games\x6Sv7RsosM3iDyFsMAFQjF.pdf'

output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)


for page_number in range(len(doc)):
    page = doc.load_page(page_number)
    pix = page.get_pixmap(dpi=300)
    image = Image.open(io.BytesIO(pix.tobytes()))
    text = pytesseract.image_to_string(image)
    text_file = os.path.join(output_dir, f'page_{page_number + 1}.txt')
    with open(text_file, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"Processed page {page_number + 1}")

print("Extraction complete. Check the output directory for results.")
