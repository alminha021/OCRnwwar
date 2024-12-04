import cv2
import pytesseract
import csv
import os

# Configure o caminho do Tesseract se necessário
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# Parâmetros do vídeo
video_path = "C:/Users/raulc/Documents/GitHub/OCRnwwar/input_video.mp4"  # Substitua pelo caminho do seu vídeo
output_csv = "output_data.csv"
# Configuração de intervalo de frames (exemplo: processar 1 a cada 10 frames)
frame_interval = 10

def process_video(video_path, output_csv):
    # Verifica se o arquivo de vídeo existe
    if not os.path.exists(video_path):
        print("O vídeo não foi encontrado. Verifique o caminho.")
        return

    # Inicializa o OpenCV para leitura do vídeo
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Erro ao abrir o vídeo. Verifique o caminho.")
        return

    # Obtém informações do vídeo
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    duration = total_frames / frame_rate

    print(f"Processando vídeo...")
    print(f"Total de Frames: {total_frames}")
    print(f"Frame Rate: {frame_rate} FPS")
    print(f"Duração: {duration:.2f} segundos")

    # Configuração para salvar os dados no CSV
    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Frame", "Texto Extraído"])

        frame_count = 0
        processed_frames = 0

        while True:
            success, frame = cap.read()
            if not success:
                break

            # Processa apenas a cada intervalo de frames
            if frame_count % frame_interval == 0:
                processed_frames += 1
                print(f"Processando frame {frame_count + 1}...")

                # Converte o frame para escala de cinza (melhor para OCR)
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Realiza OCR no frame
                text = pytesseract.image_to_string(gray_frame)

                # Salva o texto no CSV
                writer.writerow([frame_count + 1, text.strip()])

            frame_count += 1

        print(f"Processamento concluído. Frames processados: {processed_frames}")
    
    cap.release()

# Executa o processamento do vídeo
process_video(video_path, output_csv)