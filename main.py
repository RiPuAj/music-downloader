from pytube import YouTube
from tkinter.filedialog import askdirectory
from tkinter import messagebox

def download(url, path):
    try:
        if len(path) < 1:
            raise ValueError("ValueError: Path has 0 lenght")

        if(len(url) < 10):
            raise ValueError("ValueError: URL has not correct length")

        yt = YouTube(str(url))

        yt.streams.filter(only_audio=True, file_extension='mp4').first().download(str(path))
        messagebox.showinfo(message="Downloaded successfully", title="Download Completed")
    except Exception as e:

        print(e)

def changeDirectory(pathEntrada):

    dirName = askdirectory()

    pathEntrada.insert(0,dirName)