import cv2
import numpy as np

selected_points = np.zeros((4, 2), np.int16)
counter = 0


def selectedPoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        selected_points[counter] = x, y
        counter += 1


path = input("Enter the path to the image: ")
image = cv2.imread(path)
while True:
    if counter == 4:
        width = selected_points[3][0] - selected_points[0][0]
        height = selected_points[3][1] - selected_points[0][1]
        pts1 = np.float32([selected_points[0], selected_points[1], selected_points[2], selected_points[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        outputImage = cv2.warpPerspective(image, matrix, (width, height))
        cv2.imshow("Output Image", outputImage)
        counter = 0

    for i in range(0, 4):
        cv2.circle(image, (selected_points[i][0], selected_points[i][1]), 3, (0, 255, 0), cv2.FILLED)

    cv2.imshow("Original Image", image)
    cv2.setMouseCallback("Original Image", selectedPoints)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
