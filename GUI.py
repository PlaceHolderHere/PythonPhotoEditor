import image_functions
import tkinter as tk

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
PRIMARY_COLOR = "#C3D5EF"
ACCENT_COLOR = "#26384D"
SIDEBAR_WIDTH = 88
NAVBAR_HEIGHT = 64

# Initialization
root = tk.Tk()
root.title("Python Image Editor")
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
root.resizable(False, False)

# NavBar
navbar_frame = tk.Frame(root, bg=ACCENT_COLOR, width=SCREEN_WIDTH, height=NAVBAR_HEIGHT)
navbar_frame.pack(side="top")

# SideBar
sidebar_frame = tk.Frame(root, bg=PRIMARY_COLOR, width=SIDEBAR_WIDTH, height=SCREEN_HEIGHT)
sidebar_frame.pack(side="left")

# Content Area
content_frame = tk.Frame(root)
content_frame.pack(side="right", fill="both", expand=True)

# Main Loop
root.mainloop()
