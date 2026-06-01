import image_functions
import tkinter as tk

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
PRIMARY_COLOR = "#C3D5EF"
ACCENT_COLOR = "#26384D"
SIDEBAR_WIDTH = 88
NAVBAR_HEIGHT = 64
PLACEHOLDER_PHOTO = "assets/placeholder-photo.png"

class PythonImageEditor:
    def __init__(self):
        # Variables
        self.photo_path = PLACEHOLDER_PHOTO

        # Tkinter Initialization
        self.root = tk.Tk()
        self.root.title("Python Image Editor")
        self.root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.root.resizable(False, False)

        # NavBar
        self.navbar_frame = tk.Frame(self.root, bg=ACCENT_COLOR, width=SCREEN_WIDTH, height=NAVBAR_HEIGHT)
        self.navbar_frame.pack(side="top", padx=0, pady=0, fill="x")

        # SideBar
        self.sidebar_frame = tk.Frame(self.root, bg=PRIMARY_COLOR, width=SIDEBAR_WIDTH, height=SCREEN_HEIGHT)
        self.sidebar_frame.pack(side="left")

        # Content Area
        self.content_frame = tk.Frame(self.root)
        self.content_frame.pack(side="right", fill="both", expand=True)

        # Photo
        self.photo = tk.PhotoImage(file=self.photo_path)
        self.photo_label = tk.Label(self.content_frame, image=self.photo, width=SCREEN_WIDTH - 320, height=SCREEN_HEIGHT - 180)
        self.photo_label.pack(expand=True)

        # Main Loop
        self.root.mainloop()


if __name__ == "__main__":
    PythonImageEditor()