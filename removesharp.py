import cv2
import numpy as np

def remove_sharp(image, sigma=3):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (0, 0), sigma)
    
    # Calculate the difference between original and blurred image
    diff = cv2.subtract(gray, blurred)
    
    # Add the difference back to the original image to reduce sharpness
    result = cv2.add(gray, diff)
    
    return result

# Load the input image
input_image = cv2.imread('input_image.jpg')

# Apply the RemoveSharp algorithm
output_image = remove_sharp(input_image)

# Display the input and output images
cv2.imshow('Input Image', input_image)
cv2.imshow('Output Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
