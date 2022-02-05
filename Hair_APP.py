import os
import time
from time import sleep 
import cv2
import shutil
from tkinter import filedialog
from tkinter import *
import tkinter.messagebox
from PIL import Image,ImageTk

img_width = 128
img_height = 128

path_image = "assets/representative/my_image/" 
path_empty_image = "system/empty.png"
path_tempfile = "temp.jpg"
path_save = os.getcwd() + "/results"

window = Tk()
window.title("hAIr")
window.dirName = path_save
window.iconbitmap("system/icon.ico")
window.geometry("600x450")
window.configure(padx=20, pady=15)
window.resizable(False, False)

def folder_reset(image_type) : 
    shutil.rmtree(r"assets/representative/my_image/" + image_type + "/male")
    shutil.rmtree(r"assets/representative/my_image/" + image_type + "/female")
    os.mkdir(path_image + image_type + "/male")
    os.mkdir(path_image + image_type + "/female")

def browse():
    window.file = filedialog.askopenfile(
    initialdir = 'path', 
    title = '열기', 
    filetypes = (('JPG (*.jpg)', '*.jpg'),
    ('PNG 3(*.png)', '*.png'),
    ('모든 +파일', '*.*')))
    return window.file

def load_src(gender):
    global gender_1
    path_load = browse()
    if path_load != None :
        path_load = path_load.name
        img1 = Image.open(path_load)
        img1 = img1.resize((img_width, img_height))
        window.photo1 = ImageTk.PhotoImage(img1)
        label_img1.configure(image = window.photo1)
        gender_1 = gender
        folder_reset("src")
        shutil.copy(path_load, path_image + "src/" + gender_1)
        return True
    else :
        return False

def load_ref(gender):
    global gender_2
    path_load = browse()
    if path_load != None :
        path_load = path_load.name
        img2 = Image.open(path_load)
        img2 = img2.resize((img_width, img_height))
        window.photo2 = ImageTk.PhotoImage(img2)
        label_img2.configure(image = window.photo2)
        gender_2 = gender
        folder_reset("ref")
        shutil.copy(path_load, path_image + "ref/" + gender_2)
        return True
    else :
        return False
    
def click_m1():
    if load_src("male") == True : 
        button_m1.configure(bg="cyan")
        button_f1.configure(bg="SystemButtonFace")

def click_f1():
    if load_src("female") == True : 
        button_m1.configure(bg="SystemButtonFace")
        button_f1.configure(bg="pink")

def click_m2():
    if load_ref("male") == True : 
        button_m2.configure(bg="cyan")
        button_f2.configure(bg="SystemButtonFace")

def click_f2():
    if load_ref("female") == True : 
        button_m2.configure(bg="SystemButtonFace")
        button_f2.configure(bg="pink")

def folder_set():
    global path_save
    my_path = filedialog.askdirectory()
    if my_path != "" : 
        path_save = my_path
        window.dirName = path_save
        label_folder.configure(text="결과 저장 위치: " + window.dirName)
    
def folder_open():
    os.startfile(path_save)

def reset():
    img1 = Image.open(path_empty_image)
    img2 = Image.open(path_empty_image)
    img3 = Image.open(path_empty_image)
    img1 = img1.resize((img_width, img_height))
    img2 = img2.resize((img_width, img_height))
    img3 = img3.resize((img_width*2, img_height*2))
    window.photo1 = ImageTk.PhotoImage(img1)
    window.photo2 = ImageTk.PhotoImage(img2)
    window.photo3 = ImageTk.PhotoImage(img3)
    label_img1.configure(image=window.photo1)
    label_img2.configure(image=window.photo2)
    label_img3.configure(image=window.photo3)

def run():
    outfile = open("system/command.bat", "w")
    outfile.write("cd " + os.getcwd() + "\n")
    outfile.write("python main.py --mode align --inp_dir assets/representative/my_image/src/" + gender_1 + " --out_dir assets/representative/my_image/src/" + gender_1 + "\n")
    outfile.write("python main.py --mode align --inp_dir assets/representative/my_image/ref/" + gender_2 + " --out_dir assets/representative/my_image/ref/" + gender_2 + "\n")
    outfile.write("python main.py --mode sample --num_domains 2 --resume_iter 100000 --w_hpf 1 --checkpoint_dir expr/checkpoints/celeba_hq --src_dir assets/representative/my_image/src --ref_dir assets/representative/my_image/ref" + "\n")
    outfile.close()
    os.startfile(os.getcwd() + "/system/command.bat")
    outfile.close()

    while not os.path.isfile(path_tempfile) :
        print(path_tempfile + " not found")
        sleep(1)
    print(path_tempfile + " found!!!")
    img3 = cv2.imread(path_tempfile)
    if os.path.isfile(path_tempfile) :
        os.remove(path_tempfile)
    
    height, width, chennel = img3.shape
    img3 = img3[height//2:height,width//2:width]
    file_result = path_save + "/" + time.strftime("%Y%m%d_%H%M%S") + ".jpg"
    img3 = cv2.imwrite(file_result, img3)
    img3 = Image.open(file_result)
    img3 = img3.resize((img_width*2, img_height*2))
    window.photo3 = ImageTk.PhotoImage(img3)
    label_img3.configure(image=window.photo3)

    tkinter.messagebox.showinfo("hAIr", "합성 결과 파일(" + file_result + ")이 저장되었습니다.")


label1 = Label(window, text="< 성별 및 이미지 선택 >", font="맑은_고딕 16 bold", fg="blue", pady=15)
label2 = Label(window, text="< 이미지 합성 결과 >", font="맑은_고딕 16 bold", fg="blue")
label_img1 = Label(window)
label_img2 = Label(window)
label_img3 = Label(window)
label_b1 = Label(window, text="얼굴(Face)\n이미지 찾아보기")
label_b2 = Label(window, text="헤어(Hair)\n이미지 찾아보기")
label_plus = Label(window, text="+", font="맑은_고딕 40 bold")
label_blank = Label(window, padx=20)
button_m1 = Button(window, text="남성(Male)", command=click_m1, width=15, height=2)
button_f1 = Button(window, text="여성(Female)", command=click_f1, width=15, height=2)
button_m2 = Button(window, text="남성(Male)", command=click_m2, width=15, height=2)
button_f2 = Button(window, text="여성(Female)", command=click_f2, width=15, height=2)
button_run = Button(window, text="이미지 합성하기", command=run, font="돋움 11", bg="darkgreen", fg="white", width=15, height=2)
button_folder_set = Button(window, text="저장 위치\n변경", command=folder_set, height=2)
button_folder_open = Button(window, text="저장 위치\n열기", command=folder_open, height=2)
label_folder = Label(window, text="결과 저장 위치: " + path_save, pady=15)

reset()

label1.grid(row=0, column=0, columnspan=2)

label_img1.grid(row=1, column=0, rowspan=3)
label_b1.grid(row=1, column=1)
button_m1.grid(row=2, column=1)
button_f1.grid(row=3, column=1)

label_plus.grid(row=4, column=0)

label_img2.grid(row=5, column=0, rowspan=3)
label_b2.grid(row=5, column=1)
button_m2.grid(row=6, column=1)
button_f2.grid(row=7, column=1)

label_blank.grid(row=0, column=2)

label2.grid(row=0, column=3, columnspan=3)

label_img3.grid(row=1, column=3, rowspan=6, columnspan=3)
button_run.grid(row=7, column=3)
button_folder_set.grid(row=7, column=4)
button_folder_open.grid(row=7, column=5)
label_folder.grid(row=8, column=0, columnspan=8, sticky=W)

window.mainloop()

