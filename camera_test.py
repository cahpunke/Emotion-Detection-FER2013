import cv2

# Inisialisasi kamera
cap = cv2.VideoCapture(0)  # 0 biasanya untuk kamera default

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Kamera Real-time', frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()