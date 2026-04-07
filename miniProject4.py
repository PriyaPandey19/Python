import tkinter as tk
import time
from PIL import Image, ImageTk


#main application window
root= tk.Tk()
root.title("Photo Slideshow Album")
root.geometry("1000x1000")





image_paths=[
    r"\Users\Dell\Pictures\Album\img1.webp",
    r"\Users\Dell\Pictures\Album\img2.webp",
    r"\Users\Dell\Pictures\Album\img3.webp",
    r"\Users\Dell\Pictures\Album\img4.webp",
    r"\Users\Dell\Pictures\Album\img5.webp",
    r"\Users\Dell\Pictures\Album\img6.webp",
]

image_size = (700, 700)
images=[]
for path in image_paths:
    img =Image.open(path)
    img = img.resize(image_size)
    images.append(img)


#convert pil images into tkinter compatable image
final_images=[]
for img in images:
    photo= ImageTk.PhotoImage(img)
    final_images.append(photo)

#label widget to keep photo
image_label = tk.Label(root)
image_label.pack(pady=30)

#slideshow function
def start_slideshow():
    for photo in final_images:
        image_label.config(image=photo)
        image_label.image= photo
        root.update()
        time.sleep(1)

#button
play_button = tk.Button(
    root,
    text="Play the SlideShow",
    font=("Arial", 17),
    command=start_slideshow
)        

play_button.pack(pady=40)

root.mainloop()
