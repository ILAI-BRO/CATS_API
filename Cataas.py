from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import requests
from io import BytesIO


Allowed_tags = ["sleep", "jump", "eat", "black", "fight", "bengal", "siamese", "cute"]
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
    tag = tag_combo.get()

    url_tag = f"{url}/{tag}" if tag else url
    img = get_image(url_tag)

    if img:
        new_window = Toplevel()
        new_window.title("Картинка с котиком")
        new_window.geometry("600x480")
        label = Label(new_window, image=img)
        label.pack()
        label.image = img

def open_random_img():
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

tag_label = Label(text="Выбери тег")
tag_label.pack()

tag_combo=Combobox(values=Allowed_tags)
tag_combo.pack()

load_button = Button(text="Загрузить картинку по тегу", command=open_new_window)
load_button.pack()

load_random_button = Button(text="Загрузить случайное изображение", command=open_random_img)
load_random_button.pack()


menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="загрузить фото", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)



root.mainloop()