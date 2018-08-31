# imports
import os
import numpy as np
import cv2
import Augmentor
from imgaug import augmenters as iaa

# Constants
HEIGHT = 1600
WIDTH = 876


# Define directory for images
source_directory = 'D:/Users/antho/PycharmProjects/Pluralsight/AugmentImages/source_files'
processed_ok_directory = 'D:/Users/antho/PycharmProjects/Pluralsight/AugmentImages/processed_ok_files'
processed_nok_directory = 'D:/Users/antho/PycharmProjects/Pluralsight/AugmentImages/processed_nok_files'
augmentor_output_directory = 'D:/Users/antho/PycharmProjects/Pluralsight/AugmentImages/source_files/output'

# Augmentor: Create pipeline
p = Augmentor.Pipeline(source_directory)

# Convert to greyscale
p.greyscale(probability=1)

# Contrast
p.random_contrast(probability=1, min_factor=0.7, max_factor=1)

# Brightness
p.random_brightness(probability=1, min_factor=0.95, max_factor=1.05)

# Horizontal translation

# Random rotation
p.rotate(probability=1, max_left_rotation=2, max_right_rotation=2)

p.sample(n=10, multi_threaded=True)

# Imgaug

# Set up operations
seq = iaa.SomeOf((1, None),[iaa.Fliplr(0.5),
                      iaa.Affine(translate_px={"x": (-20, 20), "y": (-20, 20)})])

# Load images into numpy array
image_files = os.listdir(augmentor_output_directory)
file_count = len(image_files)
file_count = len(image_files)

images = np.zeros((file_count, HEIGHT, WIDTH))

for idx in range(file_count):
  img_path = augmentor_output_directory + '\\' + image_files[idx]
  img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
  images[idx, :, :] = img

images_aug = seq.augment_images(images)

# Write images to final directory
for idx in range(file_count):
  destination_file_path = processed_ok_directory + '\\' + image_files[idx]
  cv2.imwrite(destination_file_path, images_aug[idx])




