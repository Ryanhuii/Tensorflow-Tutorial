# image_app.py
import tkinter as tk
from PIL import Image, ImageTk

class ImageApp:
    label_value = 0
    def __init__(self, root, image_path):
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

            # Update the label with the new image
            self.label.configure(image=self.tk_image)

            # Update the text label
            self.label_value = self.label_value + 1
            new_text = self.label_value
            self.text_label.configure(text=new_text)

        except Exception as e:
            # Handle the exception (you can customize this part based on your needs)
            print(f"An error occurred: {e}")

        finally:
            # Schedule the next update
            self.root.after(1000, self.update_image)

