import os
from PyPDF2 import PdfMerger
from PIL import Image

infolder = r"E:\Programming\Google  Python\Python-Phase\projects\pdf\pdfs2join"
output_folder = r"E:\Programming\Google  Python\Python-Phase\projects\pdf\mergepdf"
os.makedirs(output_folder, exist_ok=True)

merger = PdfMerger()
temp_files = []
for file in os.listdir(infolder):
    if file.endswith((".jpg", ".jpeg")):
        img_path = os.path.join(infolder, file)
        pdf_path = os.path.join(output_folder, f"{os.path.splitext(file)[0]}.pdf")

        image = Image.open(img_path).rotate(-90) # to rotate it 
        image.convert("RGB").save(pdf_path)

        merger.append(pdf_path)
        temp_files.append(pdf_path)

merged_pdf_path = os.path.join(output_folder, "combined.pdf")
merger.write(merged_pdf_path)
merger.close()

print(f"Merged PDF saved at: {merged_pdf_path}")
for pdf in temp_files:
    os.remove(pdf)


    