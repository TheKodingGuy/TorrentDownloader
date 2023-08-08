import tkinter as tk
from tkinter import filedialog


def filefinder():

    file_path = []

    root = tk.Tk()
    root.withdraw()

    find_path = filedialog.askopenfilename()

    file_path.append(find_path)

    return file_path
