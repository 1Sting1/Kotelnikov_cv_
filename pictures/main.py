import cv2
import numpy as np
from skimage.measure import euler_number

cv2.namedWindow("Image", cv2.WINDOW_GUI_NORMAL)
cv2.namedWindow("Test", cv2.WINDOW_GUI_NORMAL)
image = cv2.imread("image.png")

video = cv2.VideoCapture("pictures.avi")
n = 0
while (video.isOpened()):
    ret, frame = video.read()
    if frame is not None:
        cv2.imshow("Image", frame)
        if image is not None:
            image = cv2.resize(image, (frame.shape[1], frame.shape[0]))
    if not ret:
        break
    cv2.putText(frame, f"Number of my images = {n}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))

    res = cv2.absdiff(image, frame)
    res = res.astype(np.uint8)
    percentage = (np.count_nonzero(res) * 100) / res.size

    if percentage > 39 and percentage < 40:
        cv2.imshow("Test", frame)
        n+=1

    if cv2.waitKey(50) == ord("q"):
        break

print(f"Final number of my images = {n}")

video.release()
cv2.destroyAllWindows()
