
import streamlit as st
from PIL import Image
import numpy as np

# Function to resize the image
def resize_image(image, size):
    resized_image = image.resize(size)
    return resized_image

# Function to convert image to grayscale
def grayscale_conversion(image):
    grayscale_image = image.convert("L")
    return grayscale_image

# Function to crop the image
def crop_image(image, box):
    cropped_image = image.crop(box)
    return cropped_image

# Function to rotate the image
def rotate_image(image, angle):
    rotated_image = image.rotate(angle)
    return rotated_image

# Main function to process the image based on selected techniques
def process_image(image, techniques):
    processed_image = image.copy()
    for technique in techniques:
        if technique == "Resize":
            size = st.sidebar.slider("Resize Size", 10, 1000, 300)
            processed_image = resize_image(processed_image, (size, size))
        elif technique == "Grayscale Conversion":
            processed_image = grayscale_conversion(processed_image)
        elif technique == "Image Cropping":
            left = st.sidebar.slider("Left", 0, image.width, 0)
            top = st.sidebar.slider("Top", 0, image.height, 0)
            right = st.sidebar.slider("Right", left, image.width, image.width)
            bottom = st.sidebar.slider("Bottom", top, image.height, image.height)
            box = (left, top, right, bottom)
            processed_image = crop_image(processed_image, box)
        elif technique == "Image Rotation":
            angle = st.sidebar.slider("Rotation Angle", -180, 180, 0)
            processed_image = rotate_image(processed_image, angle)
    return processed_image

# Main function to run the Streamlit app
def main():
    st.title("Image Processing App")
    
    # Upload image
    uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    
    if uploaded_image is not None:
        st.image(uploaded_image, caption="Original Image", use_column_width=True)
        
        # Select image processing techniques
        techniques = st.sidebar.multiselect("Select Image Processing Techniques", ["Resize", "Grayscale Conversion", "Image Cropping", "Image Rotation"])
        
        # Process the image based on selected techniques
        if st.button("Process Image"):
            image = Image.open(uploaded_image)
            processed_image = process_image(image, techniques)
            st.image(processed_image, caption="Processed Image", use_column_width=True)

if __name__ == "__main__":
    main()