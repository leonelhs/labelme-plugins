import cv2 as cv


def findContours(image, epsilon=0.0009):
    _, thresh = cv.threshold(image, 175, 255, cv.THRESH_OTSU)
    contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnt = biggestArea(contours)
    points = cv.approxPolyDP(cnt, epsilon * cv.arcLength(cnt, True), True)
    return [point[0].tolist() for point in points]


def biggestArea(contours):
    max_area = 0.0
    max_cnt = None
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > max_area:
            max_area = area
            max_cnt = cnt
    return max_cnt
