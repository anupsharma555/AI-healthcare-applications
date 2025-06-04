#%% setup
import pydicom
import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt

# TASK: In the same folder as this .py file you will find a DICOM file
# that is called instance.dcm. Your goal is to save it as a png file. 
# You must apply a WW/WC transform in order to map values to grayscale.

#%% load
# 1. Use pydicom's dcmread method to load the image
dcm = pydicom.dcmread("instance.dcm")

print(f"Modality: {dcm.Modality}")
#%% apply W/L
# 2. Apply WW/WC transform. Keep in mind that pixels are available as 
# NumPy array by accessing .pixel_array field.
# You might want to display the image to check that it comes out right.
# You can use matplotlib's plt.imshow method to display image as 
# grayscale data like so: plt.imshow(pixels, cmap="gray")

pixels = np.copy(dcm.pixel_array)
print(f"min: {np.min(pixels)}, max: {np.max(pixels)}")

wc = 2472
ww = 4144

hu_min = wc - ww/2
hu_max = wc + ww/2

pixels[np.where(pixels < hu_min)] = hu_min
pixels[np.where(pixels > hu_max)] = hu_max
pixels = (pixels - hu_min)/(hu_max-hu_min)

plt.imshow(pixels, cmap="gray")

print(f"min: {np.min(pixels)}, max: {np.max(pixels)}")
#%% save
# 3. You can use PIL's Image.fromarray and .save methods to save a NumPy array as png
# Don't forget that when you are using "L" mode, PIL is expecting your data to 
# be of type uint8 (and in the range of 0-255)

out = (pixels*0xff).astype(np.uint8)
im = Image.fromarray(out, mode="L")
im.save("out.png")

# %%
# This script converts a DICOM medical image file (instance.dcm) to a PNG image using Python. 
# It utilizes the pydicom library to read the DICOM file and extract the pixel data, 
# numpy for numerical operations and windowing/leveling (WW/WC) transformation, and 
# PIL (Python Imaging Library) to save the processed image as a PNG file. 
# The script first loads the DICOM file and prints metadata and pixel value ranges, 
# then applies a window center (WC) and window width (WW) transformation to map the pixel values 
# to a normalized grayscale range suitable for display. 
# Although the script includes a line to display the image using matplotlib.pyplot, 
# its main function is to save the transformed image as an 8-bit grayscale PNG. 
# This workflow is commonly used in medical imaging to convert and visualize DICOM images 
# in standard image formats.

#This script reads a CT DICOM file named instance.dcm using the pydicom library, 
# extracts the pixel data as a NumPy array, and prints the modality and original pixel value range. 
# It then applies a window center (WC) and window width (WW) transformation to map the pixel values 
# to a normalized grayscale range, clipping values outside the specified window and scaling the result
# to [0, 1]. The script optionally displays the processed image using matplotlib, 
# prints the new pixel value range, and finally saves the normalized image as an 8-bit grayscale PNG 
# using the Python Imaging Library (PIL). This workflow is commonly used to convert and visualize 
# medical images from DICOM to standard image formats.