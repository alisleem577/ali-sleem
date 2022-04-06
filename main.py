from asyncio import SendfileNotAvailableError
from tkinter import CENTER
from turtle import color
from typing import Literal
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from Equalize_hist import equalize_hist
image = cv.imread('jetplane.tif',0)
equalize_hist(image, 255)
equalize_hist(image, 128)
equalize_hist(image, 64)
plt.show()
