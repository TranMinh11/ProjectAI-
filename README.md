Project is location in 'E:\AI\face'
Step 1: Tạo môi trường ảo bằng package virtualenv của python:
    - Cài đặt: 
            pip install virtualenv (windows)
            sudo apt-get install python3-venv (debian/ubuntu)
    - Tạo môi trường:
            python -m venv env

Step 2: Tải các package cần thiết: pip install -m REQUIREMENTS.txt

Step 3: Kích hoạt môi trường ảo 'env' 
"E:\AI\face\env\Scripts\Activate.ps1"

Step 4: Di chuyển tới thư mục src

Step 5: Chạy chạy chương trình
python .\main.py

-Mở cam trên máy tính, đưa khuôn mặt vào vị trí camera.
-Tự động nhận diện khuôn mặt đưa các trạng thái cảm xúc.