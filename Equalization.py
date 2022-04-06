from asyncio import SendfileNotAvailableError
from tkinter import CENTER
from turtle import color
from typing import Literal
import cv2 as cv
import Numpy
import numpy as np
import matplotlib.pyplot as plt

def equalize_hist(img, bins_number):
    image = cv.imread('jetplane.tif',0)
    equ = cv.equalizeHist(img, bins_number)

    histogram_equ, bin_edges_equ = np.histogram(equ, bins=bins_number)
    histogram, bin_edges = np.histogram(image, bins=bins_number)

    string = "Plot using " + str(bins_number) + " Bins"
    
    fig = plt.figure(figsize=(10,8))

    plt.title(label = string,
              fontsize = 20,
              color = "red")

    fig.add_subplot(221)
    plt.title('original')
    plt.set_cmap('gray')
    plt.imshow(img)

    fig.add_subplot(222)
    plt.title('HIST 1')
    plt.plot(bin_edges[0:-1],histogram)

    fig.add_subplot(223)
    plt.title('EQUA.')
    plt.set_cmap('gray')
    plt.imshow(equ)

    fig.add_subplot(224)
    plt.title('EQUA__HIST')
    plt.plot(bin_edges_equ[0:-1],histogram_equ)