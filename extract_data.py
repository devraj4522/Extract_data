import re
from matplotlib.pyplot import get
import cv2
import pytesseract
import numpy as np

# Extract string with specified roi
def get_values(img_path, roi, key):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    image_copy = img.copy()
    image_copy = image_copy[roi[1]:roi[3], roi[0]:roi[2]]
    data = pytesseract.image_to_string(image_copy, lang='eng',config='--psm 7')

    # if key=="Invoice date" or key=="Issue Date" or key=="ETA" or key == "ETD":
    #     print(data)
    #     data = re.sub(r"\d+[-]\w+[-]\d", "", data)
    # else:
    data = re.sub(r"[^a-zA-Z0-9 ]", "", data)
    return data   

def get_invoice_data(img_path, data_at_page):
    new_data = dict()
    for key, value in data_at_page.items():
                new_data[key] = get_values(img_path, value, key)
                print(key, new_data[key])
    return new_data