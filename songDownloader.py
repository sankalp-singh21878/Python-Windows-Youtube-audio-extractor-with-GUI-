import os
import pytube
from pytube import YouTube  

choice = 0
while(True):
    print("1. Download song\n2. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        video_url = input("Enter the youtube link: ")   
        youtube = pytube.YouTube(video_url)  
        video = youtube.streams.filter(only_audio = True).first()
        destination = 'C:/Users/super/Desktop/Songs'
        if os.path.isdir(destination):
            name = input("Enter file name (without extension): ")
            file = video.download(output_path=destination, filename=name)
            base, ext = os.path.splitext(file)
            new_file = base + '.mp3'
            os.rename(file, new_file)
            print("File saved succesfully!!\n")
        else:
            os.mkdir(destination)
            name = input("Enter file name (without extension): ")
            file = video.download(output_path=destination, filename=name)
            base, ext = os.path.splitext(file)
            new_file = base + '.mp3'
            os.rename(file, new_file)
            print("File saved succesfully!!\n")
    elif choice == 2:
        break
    else:
        print("Wrong choice try again\n")
