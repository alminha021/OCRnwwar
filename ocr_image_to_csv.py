import cv2
import pytesseract
import os

# Configure o caminho da imagem e do arquivo de saída
image_path = "C:/Users/raulc/Documents/GitHub/OCRnwwar/input_image.png"
output_txt = "C:/Users/raulc/Documents/GitHub/OCRnwwar/output_text.txt"

# Configure o caminho do Tesseract, se necessário
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def process_image(image_path, output_txt):
    # Verifica se o arquivo da imagem existe
    if not os.path.exists(image_path):
        print("A imagem não foi encontrada. Verifique o caminho.")
        return

    print(f"Processando a imagem: {image_path}")

    # Carrega a imagem usando OpenCV
    image = cv2.imread(image_path)

    if image is None:
        print("Erro ao abrir a imagem. Verifique o caminho.")
        return

    # Converte a imagem para escala de cinza
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Realiza OCR na imagem
    text = pytesseract.image_to_string(gray_image)

    # Salva o texto extraído em um arquivo
    with open(output_txt, mode='w', encoding='utf-8') as file:
        file.write(text.strip())

    print(f"O texto extraído foi salvo em: {output_txt}")

# Executa o processamento da imagem
process_image(image_path, output_txt)
