import tkinter as tk
from pymsgbox import *
import os
import pytube
from pytube import YouTube
import threading

window = tk.Tk()
window.geometry("400x240")
window.title("Song Downloader")

def execute():
    link = entry.get("1.0","end")
    name = temp.get("1.0","end")
    youtube = pytube.YouTube(link)  
    video = youtube.streams.filter(only_audio = True).first()
    destination = 'C:/Users/super/Desktop/Songs'

    def existFun():
        file = video.download(output_path=destination, filename=name)
        base, ext = os.path.splitext(file)
        new_file = base + '.mp3'
        os.rename(file, new_file)
        alert(text='File saved successfully!!', title='Success', button='OK')
        entry.delete("1.0","end")
        temp.delete("1.0","end")
        
    def notFunc():
        os.mkdir(destination)
        file = video.download(output_path=destination, filename=name)
        base, ext = os.path.splitext(file)
        new_file = base + '.mp3'
        os.rename(file, new_file)
        alert(text='File saved successfully!!', title='Success', button='OK')
        entry.delete("1.0","end")
        temp.delete("1.0","end")
        
    if os.path.isdir(destination):
        t = threading.Thread(target=existFun)
        t.start()
    else:
        t = threading.Thread(target=notFun)
        t.start()
        
label = tk.Label(text = "Enter Youtube link")
label.pack()

entry = tk.Text(window, height=1)
entry.pack()

labelName = tk.Label(text = "Enter file name (without extension): ")
labelName.pack()

temp = tk.Text(window, height=1)
temp.pack()

B = tk.Button(window, text ="Download", command = execute)

B.pack(padx = 5, pady = 5)
window.mainloop()
