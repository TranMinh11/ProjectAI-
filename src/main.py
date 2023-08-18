import tkinter as tk
from tkinter import Label
from PIL import ImageTk, Image
from datetime import datetime


from video_emotion_color_demo import emotion_color
from video_emotion_gender_demo import gender_demo


def run_model_1():
    # Thực thi lệnh để chạy model 1
    # window.withdraw()
    gender_demo()


def run_model_2():
    # Thực thi lệnh để chạy model 2
    # window.withdraw()
    emotion_color()


def on_closing():
    # Hiển thị lại cửa sổ chính khi đóng ứng dụng
    window.deiconify()


def update_time():
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    time_label.config(text=current_time)
    window.after(1000, update_time)


# Tạo cửa sổ giao diện tkinter
window = tk.Tk()
window.title('Detect emotion and gender applications')
window.geometry('800x600')


# Tạo đối tượng Label và hiển thị dòng chữ trong root
label = Label(window, text="Detect emotion and gender applications")
label.pack()  # Sử dụng phương thức pack() để hiển thị widget

image = Image.open("./assests/hus.jpg")
photo = ImageTk.PhotoImage(image)

background_label = Label(window, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

time_label = tk.Label(window, font=("Helvetica", 16))
time_label.pack(anchor="nw", padx= 20, pady= 40)  # Đặt vị trí ở góc trên bên trái và áp dụng padding
update_time()


# Tạo nút cho model 1
button_model_1 = tk.Button(
    window, text='Model detect emotion gender', command=run_model_1, bg='blue', fg='white')
button_model_1.pack(pady=20)
button_model_1.place(x=300, y=300)

# Tạo nút cho model 2
button_model_2 = tk.Button(
    window, text='Model detect emotion color', command=run_model_2, bg='red', fg='white')
button_model_2.pack(pady=20)
button_model_2.place(x=300, y=350)


# window.protocol("WM_DELETE_WINDOW", on_closing)
# Chạy ứng dụng
window.mainloop()
