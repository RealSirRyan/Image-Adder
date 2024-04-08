import cv2
import tkinter as tk
from tkinter import filedialog, messagebox

def save_image(image):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        cv2.imwrite(file_path, image)
        messagebox.showinfo("Success", f"Image saved successfully as {file_path}")
    else:
        messagebox.showinfo("Info", "No file selected for saving.")

def load_images(num_images):
    images = []
    for i in range(num_images):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(title=f"Select image {i+1}")
        if file_path:
            img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                print(f"Error loading image {i+1} from path {file_path}")
            else:
                img_16bit = img.astype('uint16')
                images.append(img_16bit)
        else:
            print("No file selected. Skipping...")
    return images

def main():
    num_images = int(input("Enter the number of images: "))
    images = load_images(num_images)
    
    if images:
        image_return = sum(images)
        save_image(image_return)
    
    
   

if __name__ == "__main__":
    main()
