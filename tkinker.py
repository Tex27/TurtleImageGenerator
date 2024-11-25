import tkinter as tk
from tkinter import filedialog

def choose_image():
    # Create a hidden root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    
    # Check if the user selected a file
    if file_path:
        print(f"You selected: {file_path}")
    else:
        print("No file was selected.")
    
    return file_path

# Example usage
selected_image = choose_image()
if selected_image:
    print(f"Image path: {selected_image}")
