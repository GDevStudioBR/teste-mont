from PyPDF2 import PdfReader
import fitz  # PyMuPDF
import os
import subprocess

# Caminho do arquivo PDF
pdf_path = r"C:\Users\Guilherme\Documents\GitHub\teste-mont\31032025.pdf"

# Diretório de saída para salvar as imagens
output_dir = r"C:\Users\Guilherme\Documents\GitHub\teste-mont\extracted_images"
os.makedirs(output_dir, exist_ok=True)

# Abrir o PDF
pdf_document = fitz.open(pdf_path)
image_list = []

# Extrair imagens do PDF
for page_num in range(len(pdf_document)):
    page = pdf_document[page_num]
    image_blocks = page.get_images(full=True)

    for img_index, img in enumerate(image_blocks):
        xref = img[0]  # Referência da imagem no documento
        base_image = pdf_document.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]

        # Nome do arquivo da imagem
        image_filename = f"figure_{len(image_list) + 1}.{image_ext}"
        image_path = os.path.join(output_dir, image_filename)

        # Salvar a imagem
        with open(image_path, "wb") as img_file:
            img_file.write(image_bytes)

        # Adicionar aos dados extraídos
        image_list.append({"figure": f"Figura {len(image_list) + 1}", "path": image_path})

# Abrir a pasta contendo as imagens no Explorer (Windows)
subprocess.run(f'explorer "{output_dir}"')

# Retornar a lista de imagens extraídas
print(image_list)
print('boa tarde')

print('oiufgdfgfd')
