# 100strujka1.jpg
from scipy import interpolate
import cv2
import numpy as np
from skimage.filters.thresholding import threshold_sauvola
import testings

import time
import matplotlib.pyplot as plt
from scipy import polyval, polyfit

from scipy.optimize import curve_fit


def exponential_fit(x, a, b, c):
    # print(a*np.exp(-b*x) + c)
    return a * np.exp(-b * x) + c


test = testings.test_class()
cv2.namedWindow("as", cv2.WINDOW_NORMAL)
while True:
    # try:
    frame = cv2.imread("")
    frame = cv2.resize(frame, (int(frame.shape[1] / 2), int(frame.shape[0] / 2)), cv2.INTER_AREA)

    cv2.imshow("frame", frame)

    print("frame.shape", frame.shape)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    x_1 = 0.31
    y_1 = 0.55
    v = 20
    gray = gray[int(gray.shape[0] * y_1 - v):int(gray.shape[0] * y_1 + v),
           int(gray.shape[1] * x_1 - v):int(gray.shape[1] * x_1 + v)]
    y = int(gray.shape[0] / 2)
    x = int(gray.shape[1] / 2)
    v = 15
    L = 0
    R = np.pi
    n_points = (4, 10, 64, 65)
    f = np.sin

    rectDef = gray[int(y - v):int(y + v), int(x - v):int(x + v)]

    fig, ax = plt.subplots(figsize=(10, 8), layout="tight")
    ax.plot(gray[int(y):int(y + 1), :].reshape(1, -1)[0])

    data_y = gray[int(y):int(y + 1), :].reshape(1, -1)[0]
    data_x = [i for i in range(len(data_y))]
    # -----------------Вот ЗДЕСЬ------------
    a, b, c, d, e, f = polyfit(data_x, data_y, 5)
    y_pred = polyval([a, b, c, d, e, f], data_x)
    # ----------------------------------------------
    data_x = np.array(data_x, np.float64)
    print(len(data_x[int(len(data_x) / 2) - 20:int(len(data_x) / 2) + 20]))

    print("y_pred", y_pred)
    print("leny_pred", len(y_pred))

    ax.plot(y_pred)

    plt.ylabel(' числа')

    h, w = rectDef.shape

    cv2.imshow("as", gray)

    plt.show()
    cv2.waitKey(0)
    k = cv2.waitKey(40) & 0xFF
    if k == 27:
        break
