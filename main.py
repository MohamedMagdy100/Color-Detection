import cv2
import numpy as np


# Functions needed for the code
def getColor(name, mask, color):
    contours, x = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.arcLength(cnt, True)
        if area > 100:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.putText(frame, name, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)


def nothing():
    pass


# Creating Trackbar
cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("US", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 0, 255, nothing)

cap = cv2.VideoCapture('balls.mp4')

while True:
    # Image
    frame = cv2.imread('Colors.jpg')
    frame = cv2.resize(frame, (640, 480))
    # Video
    # _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Lower HSV Trackbar
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")
    # Upper HSV Trackbar
    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")
    # Setting Boundaries for test
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    # -----------Colors I got from Trackbars -----------
    #Red
    l_b_red = np.array([175, 92, 40])
    u_b_red = np.array([232, 255, 255])
    mask_red = cv2.inRange(hsv, l_b_red, u_b_red)
    getColor("Red",mask_red,(0,0,255))
    #Green
    l_b_green = np.array([50, 64, 0])
    u_b_green = np.array([80, 255, 255])
    mask_green = cv2.inRange(hsv, l_b_green, u_b_green)
    l_b_lightGreen = np.array([35, 56, 163])
    u_b_lightGreen = np.array([52, 238, 255])
    mask_lightGreen = cv2.inRange(hsv, l_b_lightGreen, u_b_lightGreen)
    getColor("Green", mask_green, (50, 255, 0))
    getColor("Light Green", mask_lightGreen, (0, 255, 0))
    #Blue
    l_b_blue = np.array([104, 66, 47])
    u_b_blue = np.array([127, 255, 255])
    mask_blue = cv2.inRange(hsv, l_b_blue, u_b_blue)
    l_b_lightBlue = np.array([85, 106, 153])
    u_b_lightBlue = np.array([109, 255, 255])
    mask_lightBlue = cv2.inRange(hsv, l_b_lightBlue, u_b_lightBlue)
    getColor("Blue", mask_blue, (255, 0, 0))
    getColor("Light Blue", mask_lightBlue, (255, 100, 0))
    #Purple
    l_b_purple = np.array([134, 45, 66])
    u_b_purple = np.array([144, 224, 255])
    mask_purple = cv2.inRange(hsv, l_b_purple, u_b_purple)
    getColor("Purple", mask_purple, (255, 0, 200))
    #Pink
    l_b_pink = np.array([149, 101, 134])
    u_b_pink = np.array([170, 255, 255])
    mask_pink = cv2.inRange(hsv, l_b_pink, u_b_pink)
    getColor("Pink", mask_pink, (255, 0, 255))
    #Yellow
    l_b_yellow = np.array([16, 57, 130])
    u_b_yellow = np.array([35, 255, 255])
    mask_yellow = cv2.inRange(hsv, l_b_yellow, u_b_yellow)
    getColor("Yellow", mask_yellow, (0, 255, 255))
    #Orange
    l_b_orange = np.array([3, 78, 134])
    u_b_orange = np.array([23, 255, 255])
    mask_orange = cv2.inRange(hsv, l_b_orange, u_b_orange)
    getColor("Orange", mask_orange, (0, 165, 255))

    # Testing
    # mask = cv2.inRange(hsv, l_b, u_b)
    # res_track = cv2.bitwise_and(frame, frame, mask=mask)

    # Showing the Image or Video
    cv2.imshow("frame", frame)
    # Result of Masking
    # cv2.imshow("res", res_track)

    key = cv2.waitKey(20)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
