import cv2
import numpy as np
import random

camera = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
camera.set(cv2.CAP_PROP_EXPOSURE, -5)

cv2.namedWindow("Image", cv2.WINDOW_GUI_NORMAL)

colors = {
    "red": {"lower": (00, 160, 100), "upper": (5, 255, 255)},
    "green": {"lower": (36, 25, 25), "upper": (86, 255, 255)},
    "orange": {"lower": (7, 150, 150), "upper": (15, 255, 255)},
    "yellow": {"lower": (20, 100, 100), "upper": (30, 255, 255)}
}

list_colors = list(colors)
random.shuffle(list_colors)

def function(lower, upper):
    mask1 = cv2.inRange(hsv, lower, upper)
    mask1 = cv2.erode(mask1, None, iterations=2)
    mask1 = cv2.dilate(mask1, None, iterations=2)

    cnts, _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        (curr_x, curr_y), r = cv2.minEnclosingCircle(c)
        if r > 20:
            cv2.circle(image, (int(curr_x), int(curr_y)), int(r), (0, 255, 255, 2))

        return curr_x, curr_y


while camera.isOpened():
    ret, image = camera.read()
    blurred = cv2.GaussianBlur(image, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
    user_colors = []
    color1 = [function(colors["red"]["lower"], colors["red"]["upper"]), "red"]
    color2 = [function(colors["green"]["lower"], colors["green"]["upper"]), "green"]
    color3= [function(colors["orange"]["lower"], colors["orange"]["upper"]), "orange"]
    color4 = [function(colors["yellow"]["lower"], colors["yellow"]["upper"]), "yellow"]
    user_colors.append(color1)
    user_colors.append(color2)
    user_colors.append(color3)
    user_colors.append(color4)

    if user_colors[0][0] != None and user_colors[1][0] != None and user_colors[2][0] != None and user_colors[3][0] != None:
        user_colors.sort(key = lambda x: x[0][1])
        user_colors = user_colors[::-1]
        user_colors[:2].sort(key = lambda x: x[0][0])
        user_colors[2:].sort(key = lambda x: x[0][0])
        print(user_colors)
    
    if [user_colors[0][1], user_colors[1][1],
        user_colors[2][1], user_colors[3][1]] == list_colors:
        cv2.putText(image, f"You guessed it", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (127,  255, 255))
    else:
        cv2.putText(image, f"Wrong", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (127,  255, 255))


    key = cv2.waitKey(10)
    if key == ord("q"):
        break

    cv2.imshow("Image", image)

camera.release()
cv2.destroyAllWindows
