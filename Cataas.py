from tkinter import *
from PIL import ImageTk, Image
import requests
from io import BytesIO

def get_image():
    try:
        response = requests.get(url)
        response.raise_for_status()
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        return ImageTk.PhotoImage(img)
    except Exception as error:
        print(f"Произошла ошибка: {error}")
        return None




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

root.mainloop()