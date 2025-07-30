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
def open_new_window():
    img = get_image(url)

    if img:
        new_window = Toplevel()
        new_window.title("Картинка с котиком")
        new_window.geometry("600x480")
        label = Label(new_window, image=img)
        label.pack()
        label.image = img




root = Tk()
root.title("Cats Images")
root.geometry("600x530")





# btn_change = Button(text="Обнови котика", command=change_img)
# btn_change.pack()


menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="загрузить фото", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)

open_new_window()

root.mainloop()