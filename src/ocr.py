from pdf2image import convert_from_path
import pytesseract as pt
import numpy as np
import re
import os
import cv2

def deskew(image):

    gray = cv2.bitwise_not(image)
    temp_arr = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    coords = np.column_stack(np.where(temp_arr > 0))
    angle = cv2.minAreaRect(coords)[-1]

    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

if __name__=="__main__":

    # read in file
    pages = convert_from_path(os.path.join('examples', 'example_house_fd.pdf'))

    for i,page in enumerate(pages):
        
        image_name = f"page_{i}.jpg"
        # page.save(image_name, 'JPEG')
        
        # convert to array
        page_arr = np.asarray(page)
    
        # convert to grayscale
        page_arr_gray = cv2.cvtColor(page_arr, cv2.COLOR_BGR2GRAY)

        # deskew
        page_deskew = deskew(page_arr_gray)


        text = pt.image_to_string(page_arr_gray)
        # text = [t.strip() for t in pt.image_to_string(page_arr_gray).split('\n') if t.strip() != '']
        print(text)
        print("-----------------------------------------")

        
