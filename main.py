import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import random

# Your existing functions here: add_grain, apply_vignette

def transform_image(image, desaturation, grain_intensity, vignette_intensity):
    """Apply transformations to the image."""
    # Desaturation
    grayscale = image.convert("L").convert("RGB")
    img = Image.blend(image, grayscale, alpha=desaturation)

    # Add grain
    img = add_grain(img, intensity=grain_intensity)

    # Apply vignette
    img = apply_vignette(img, intensity=vignette_intensity)

    return img

def update_image():
    """Update the image based on the slider values."""
    desaturation = desaturation_scale.get() / 100
    grain_intensity = grain_scale.get()
    vignette_intensity = vignette_scale.get() / 100

    transformed_img = transform_image(original_img, desaturation, grain_intensity, vignette_intensity)
    tk_img = ImageTk.PhotoImage(transformed_img)
    image_label.config(image=tk_img)
    image_label.image = tk_img  # Keep a reference

def open_image():
    """Open an image and display it."""
    global original_img
    file_path = filedialog.askopenfilename()
    if file_path:
        original_img = Image.open(file_path)
        original_img.thumbnail((500, 500))  # Resize for display
        update_image()

# Create the main window
root = tk.Tk()
root.title("Image Transformer")

# Add a button to open an image
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

# Add sliders for effects
desaturation_scale = tk.Scale(root, from_=0, to=100, orient='horizontal', label='Desaturation Level')
desaturation_scale.set(10)  # Default value
desaturation_scale.pack()

grain_scale = tk.Scale(root, from_=0, to=20, orient='horizontal', label='Grain Intensity')
grain_scale.set(10)  # Default value
grain_scale.pack()

vignette_scale = tk.Scale(root, from_=0, to=100, orient='horizontal', label='Vignette Intensity')
vignette_scale.set(90)  # Default value
vignette_scale.pack()

# Add a button to apply transformations
transform_button = tk.Button(root, text="Transform Image", command=update_image)
transform_button.pack()

# Label to display the image
image_label = tk.Label(root)
image_label.pack()

# Start the GUI event loop
root.mainloop()
