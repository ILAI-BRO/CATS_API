from tkinter import *
from PIL import ImageTk, Image
import requests
from io import BytesIO

url = "https://cataas.com/cat"


# Получаем изображение
def get_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img.thumbnail((600, 480),  Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as error:
        print(f"Произошла ошибка: {error}")
        return None


# Изменяем изображение на новое
def change_img():
    img = get_image(url)

    if img:
        label.config(image=img)
        label.image = img

root = Tk()
root.title("Cats Images")
root.geometry("600x530")



label =Label()
label.pack()

# btn_change = Button(text="Обнови котика", command=change_img)
# btn_change.pack()


menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="загрузить фото", command=change_img)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)

change_img()

root.mainloop()