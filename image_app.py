# image_app.py
import tkinter as tk
from PIL import Image, ImageTk
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import image
import numpy as np
import os

class ImageApp:
    class_names = ['banana', 'lemon', 'unknown']
    def __init__(self, root, image_path):

        # load the CNN model
        self.model = tf.keras.models.load_model('my_model.h5')

        self.root = root
        self.root.title("Image Viewer")

        self.image_path = image_path
        self.image = Image.open(self.image_path)
        self.tk_image = ImageTk.PhotoImage(self.image)

        self.label = tk.Label(root, image=self.tk_image)
        self.label.pack()

        self.text_label = tk.Label(root, text="Your Text Label", font=("Helvetica", 16), bg="white")
        self.text_label.place(relx=0.5, rely=0.1, anchor="center")  # Center the label on the image

        self.update_image()

    def update_image(self):
        try:
            # Open the updated image file
            updated_image = Image.open(self.image_path)

            # Create a copy of the updated image to avoid potential issues with file modifications
            updated_image_copy = updated_image.copy()

            # Update the Tkinter PhotoImage object
            self.tk_image.paste(updated_image_copy)

            # feed the image into the CNN
            img = image.load_img(self.image_path, target_size=(180, 180))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)

            predictions = self.model.predict(img_array)
            score = tf.nn.softmax(predictions[0])
            print(score)

            # Update the label with the new image
            self.label.configure(image=self.tk_image)

            # Update the text label
            # new_text = self.class_names[np.argmax(score)]
            new_text = "This image most likely belongs to {} with a {:.2f} percent confidence.".format(self.class_names[np.argmax(score)], 100 * np.max(score))
            self.text_label.configure(text=new_text)

        except Exception as e:
            # Handle the exception (you can customize this part based on your needs)
            print(f"An error occurred: {e}")

        finally:
            # Schedule the next update
            self.root.after(1000, self.update_image)
    
    def load_class_names(self):
        # Check if the folder exists
        if os.path.exists(self.data_folder) and os.path.isdir(self.data_folder):
            # Get a list of subdirectories (folder names) within the "data" folder
            subdirectories = [subdir for subdir in os.listdir(self.data_folder) if os.path.isdir(os.path.join(self.data_folder, subdir))]

            # Print the subdirectories or store them in an array
            print("Subdirectories in 'data' folder:", subdirectories)

            # If you want to store them in an array
            self.class_names = subdirectories
            print("Array of subdirectories:", self.class_names)
        else:
            print(f"The folder '{self.data_folder}' does not exist or is not a directory.")

