import tkinter as tk
from tkinter.filedialog import askdirectory
from PIL import ImageTk, Image
from os import listdir
from os.path import join


class Viewer:

    current_photo = 0
    folder = ""
    photos = []
    total_photos = 0
    status_num = 1

    def __init__(self):
        pass

    def get_photo(self):
        """ Retrieves an image from the photos list with the index of current_photo. Resizes images to fit on screen. """
        photo = ImageTk.PhotoImage(
            Image.open(join(self.folder, self.photos[self.current_photo])).resize(
                (700, 500), Image.ANTIALIAS
            )
        )
        lbl_img.configure(image=photo)
        lbl_img.image = photo

    def progress_bar(self):
        """ Function that displays status bar once a folder has been opened. Displays the 'Image X of Y'. """
        status = tk.Label(
            window,
            text=f"Image {(self.current_photo) + 1} of {len(viewer.photos)}",
            relief=tk.SUNKEN,
        )

        status.grid(row=2, column=0, columnspan=4, sticky="nsew")

    def next_photo(self):
        """ Function tied to the next (>>) button of the interface. Adds one to current_photo, retrieves next photo and updates progress bar. """
        if self.current_photo < self.total_photos:
            self.current_photo += 1
            self.get_photo()
            self.progress_bar()
        elif self.current_photo == self.total_photos:
            self.current_photo = 0
            self.get_photo()
            self.progress_bar()
        else:
            pass

    def prev_photo(self):
        """ Function tied to the previous (<<) button of the interface. Adds one to current_photo, retrieves next photo and updates progress bar. """
        if self.current_photo > 0:
            self.current_photo -= 1
            self.get_photo()
            self.progress_bar()
        else:
            pass

    def open_folder(self):
        """ Opens a folder designated by the user. """
        self.current_photo = 0
        self.folder = askdirectory()
        if (len(listdir(self.folder)) - 1) != 0:
            self.photos = [
                p
                for p in listdir(self.folder)
                if p.endswith(".png") or p.endswith(".jpg") or p.endswith(".gif")
            ]
            self.total_photos = len(self.photos) - 1
            self.get_photo()
            self.progress_bar()
        else:
            lbl_img.configure(
                text=f"'{self.folder}' is empty or contains no photos. Choose another folder."
            )
            lbl_img.image = f"'{self.folder}' is empty or contains no photos. Choose another folder."


viewer = Viewer()

# Begin GUI configuration

window = tk.Tk()
window.title("PyImage")
window.columnconfigure([0, 3], weight=1)
window.rowconfigure([0, 2], weight=1)

# Define buttons and label; previous (<<), open, quit and next (>>).

lbl_img = tk.Label(window)
btn_previous = tk.Button(
    window, width=5, text="\N{MUCH LESS-THAN}", command=viewer.prev_photo
)
btn_open = tk.Button(window, width=10, text="Open Folder", command=viewer.open_folder)
btn_quit = tk.Button(window, width=10, text="Quit", command=window.quit)
btn_next = tk.Button(
    window, width=5, text="\N{MUCH GREATER-THAN}", command=viewer.next_photo
)

# Assign buttons and image label to the interface in order they appear from left to right.

lbl_img.grid(row=0, column=0, columnspan=4)
btn_previous.grid(row=1, column=0, pady=8)
btn_open.grid(row=1, column=1, padx=2, pady=8)
btn_quit.grid(row=1, column=2, padx=2, pady=8)
btn_next.grid(row=1, column=3, pady=8)


# Start Tk event loop

window.mainloop()
