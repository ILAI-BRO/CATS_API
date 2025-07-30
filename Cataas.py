from tkinter import *
from PIL import ImageTk, Image
import requests
from io import BytesIO

def get_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        return ImageTk.PhotoImage(img)
    except Exception as error:
        print(f"Произошла ошибка: {error}")
        return None

def change_img():
    img = get_image(url)

    if img:
        label.config(image=img)
        label.image = img

root = Tk()
root.title("Cats Images")
root.geometry("600x480")

label =Label()
label.pack()

btn_change = Button(text="Обнови котика", command=change_img)
btn_change.pack()

url = "https://cataas.com/cat"

change_img()

root.mainloop()