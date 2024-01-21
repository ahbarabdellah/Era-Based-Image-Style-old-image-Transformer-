import tkinter as tk
from tkinter import filedialog
import  cv2
import numpy as np

import random

def add_grain(image, intensity=5):
    """ Add grain effect to the image """
    height, width, _ = image.shape
    noise = np.random.randint(-intensity, intensity, (height, width, 3), dtype=np.int32)
    noisy_image = np.clip(image + noise, 0, 255).astype(np.uint8)
    return noisy_image

def apply_vignette(image, intensity=0.75):
    """ Apply a vignette effect to the image """
    height, width, _ = image.shape
    mask = np.zeros((height, width), dtype=np.uint8)
    y, x = np.ogrid[0:height, 0:width]
    mask = np.sqrt((x - width / 2) ** 2 + (y - height / 2) ** 2)
    mask = (1 - intensity * mask / max(width, height))
    mask = np.clip(mask, 0, 1)
    result = (image * mask[:, :, np.newaxis]).astype(np.uint8)
    return result

def transform_image(image, desaturation, grain_intensity, vignette_intensity):
    """Apply transformations to the image."""
    # Desaturation
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = cv2.addWeighted(image, 1 - desaturation, cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR), desaturation, 0)

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

    transformed_img = transform_image(original_img.copy(), desaturation, grain_intensity, vignette_intensity)
    tk_img = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(transformed_img, cv2.COLOR_BGR2RGB)))
    image_label.config(image=tk_img)
    image_label.image = tk_img  # Keep a reference

def open_image():
    """Open an image and display it."""
    global original_img
    file_path = filedialog.askopenfilename()
    if file_path:
        original_img = cv2.imread(file_path)
        original_img = cv2.resize(original_img, (500, 500))  # Resize for display
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
