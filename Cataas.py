from tkinter import *
from PIL import ImageTk, Image
import requests
from io import BytesIO

root = Tk()
root.title("Cats Images")
root.geometry("600x480")

label =Label()
label.pack()

url = "https://cataas.com/cat"
img = get_image(url)

if img:
    label.config(image=img)
    label.image = img

def get_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image = image.convert("RGB")
    return image


root.mainloop()