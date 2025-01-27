import cv2
import os


video_path = "C:\\Users\\nobod\\Videos\\2024-10-12 22-58-05.mkv"
output_folder = 'images\\train\\skin2'
os.makedirs(output_folder, exist_ok=True)
crop_size = 400
cap = cv2.VideoCapture(video_path)
frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    if frame_count % 15 == 0:
        height, width, _ = frame.shape
        x_center = width // 2
        y_center = height // 2
        x_start = x_center - crop_size // 2
        y_start = y_center - crop_size // 2
        x_end = x_start + crop_size
        y_end = y_start + crop_size
        if width >= crop_size and height >= crop_size:
            cropped_frame = frame[y_start:y_end, x_start:x_end]
        else:
            print(f"Кадр слишком мал для обрезки: {frame_count//15}")
            continue
        frame_name = os.path.join(output_folder, f'frame_{frame_count//15:04d}.jpg')
        cv2.imwrite(frame_name, cropped_frame)
    frame_count += 1
cap.release()
print(f'Извлечено и обрезано {frame_count//15} кадров, сохранено в папку {output_folder}')
