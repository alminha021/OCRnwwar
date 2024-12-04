import cv2
import pytesseract
import csv
import os

# Configure o caminho do Tesseract se necessário
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Parâmetros do vídeo
video_path = "input_video.mp4"  # Substitua pelo caminho do seu vídeo
output_csv = "output_data.csv"

def process_video(video_path, output_csv):
    # Abrir o vídeo
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Erro ao abrir o vídeo. Verifique o caminho.")
        return

    frame_count = 0
    data_rows = []

    print("Processando vídeo...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        print(f"Processando frame {frame_count}")

        # Extraia texto do frame com OCR
        text = pytesseract.image_to_string(frame)

        # Separe o texto em linhas e adicione ao CSV
        lines = text.split("\n")
        for line in lines:
            if line.strip():  # Ignorar linhas vazias
                data_rows.append([line.strip()])

    # Fechar o vídeo
    cap.release()

    # Salvar dados no CSV
    print("Salvando dados no arquivo CSV...")
    with open(output_csv, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Texto Extraído"])  # Cabeçalho
        writer.writerows(data_rows)

    print(f"Processo concluído. Dados salvos em {output_csv}.")

if __name__ == "__main__":
    if not os.path.exists(video_path):
        print(f"Arquivo de vídeo não encontrado: {video_path}")
    else:
        process_video(video_path, output_csv)
