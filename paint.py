import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw
import os

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cool Paint App")
        
        # Create a frame for buttons
        button_frame = tk.Frame(root)
        button_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        
        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create buttons
        self.button_clear = tk.Button(button_frame, text="Clear", command=self.clear_canvas)
        self.button_clear.pack(side=tk.LEFT, padx=5)
        
        self.button_save = tk.Button(button_frame, text="Save", command=self.save_canvas)
        self.button_save.pack(side=tk.LEFT, padx=5)
        
        # Initialize PIL Image for drawing
        self.image_width = 800
        self.image_height = 600
        self.image = Image.new("RGB", (self.image_width, self.image_height), "white")
        self.draw = ImageDraw.Draw(self.image)
        
        self.canvas.bind("<Button-1>", self.start_paint)
        self.canvas.bind("<B1-Motion>", self.paint)
        
        self.old_x = None
        self.old_y = None

    def start_paint(self, event):
        self.old_x = event.x
        self.old_y = event.y

    def paint(self, event):
        new_x = event.x
        new_y = event.y
        if self.old_x and self.old_y:
            # Draw on canvas
            self.canvas.create_line(self.old_x, self.old_y, new_x, new_y, fill="black", width=2)
            # Draw on PIL image for saving
            self.draw.line([self.old_x, self.old_y, new_x, new_y], fill="black", width=2)
        self.old_x = new_x
        self.old_y = new_y

    def clear_canvas(self):
        self.canvas.delete("all")
        # Clear PIL image as well
        self.image = Image.new("RGB", (self.image_width, self.image_height), "white")
        self.draw = ImageDraw.Draw(self.image)
    
    def save_canvas(self):
        """Save the current canvas as an image file"""
        try:
            # Open file dialog to choose save location
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[
                    ("PNG files", "*.png"),
                    ("JPEG files", "*.jpg"),
                    ("All files", "*.*")
                ],
                title="Save your drawing"
            )
            
            if file_path:
                # Get canvas dimensions
                canvas_width = self.canvas.winfo_width()
                canvas_height = self.canvas.winfo_height()
                
                # Resize the saved image to match actual canvas size
                if canvas_width > 1 and canvas_height > 1:
                    resized_image = self.image.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
                    resized_image.save(file_path)
                else:
                    # Fallback to original size if canvas dimensions aren't available
                    self.image.save(file_path)
                
                messagebox.showinfo("Success", f"Drawing saved successfully to:\n{file_path}")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save the drawing:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
