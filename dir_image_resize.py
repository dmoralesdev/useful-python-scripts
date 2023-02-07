from PIL import Image
import os

def resize_image(image_path, size):
    original_image = Image.open(image_path)
    resized_image = original_image.resize(size)
    return resized_image

def resize_images_in_directory(directory, size):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(directory, filename)
            resized_image = resize_image(image_path, size)
            resized_image.save(f"resized_{filename}")

directory = input("Enter the path of the directory containing the images: ")
width = int(input("Enter the desired width for the resized images: "))
height = int(input("Enter the desired height for the resized images: "))
size = (width, height)
resize_images_in_directory(directory, size)