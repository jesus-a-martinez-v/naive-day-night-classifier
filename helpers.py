# Helper functions

import os
import glob
import matplotlib.image as mpimg

import cv2

def load_dataset(image_directory):
    image_list = []
    image_types = {'day', 'night'}
    
    for image_type in image_types:
        for file in glob.glob(os.path.join(image_directory, image_type, '*')):
            image = mpimg.imread(file)
            
            if image is not None:
                image_list.append((image, image_type))
                
     
    return image_list



def standardize_input(image):
    return cv2.resize(image, (1100, 600))


def encode(label):
    numerical_value = 0
    
    if label == 'day':
        numerical_value = 1
        
    return numerical_value


def standardize(image_list):
    
    standard_list = []
    
    for image, label in image_list:
        standardized_image = standardize_input(image)
        binary_label = encode(label)
        
        standard_list.append((standardized_image, binary_label))
        
    return standard_list
        