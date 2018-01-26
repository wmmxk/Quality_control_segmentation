import numpy as np
import cv2
import os
from PIL import Image


def get_contour(img):
    img = img * (255/np.max(img))
    img = Image.fromarray(np.uint8(img))
    img.save("./tmp.jpg")
    img = cv2.imread("./tmp.jpg",0)
    os.remove('./tmp.jpg')
    ret,thresh = cv2.threshold(img,0.7*np.mean(img),255,0) # 0.7*np.mean(img) is threshold for detecting contour; higher values means less contour 
    im2, contours, hierarchy = cv2.findContours(thresh, 1, 2)
    _ = cv2.drawContours(img, contours, -1, (0,255,255), 3)

    contour = (img==0).astype(np.int16)
    return contour

def contour_method(img,polygon):
    '''
    input:
    output:


    '''
    contour = get_contour(img)
    # count how many points on the polygon is in a contour

    mask = contour[tuple(zip(*polygon))]
    return sum(mask)/float(len(polygon))
