from pytube import YouTube
import tkinter as tk
from tkinter import ttk
from os import getcwd
from time import sleep
from tkinter.filedialog import askdirectory
from tkinter import messagebox

def download(url, path):
    try:
        if len(url) < 1 or len(path) < 1:
            raise ValueError

        if(len(url) < 10):
            raise KeyError

        yt = YouTube(str(url))

        yt.streams.filter(only_audio=True, file_extension='mp4').first().download(str(path))
        messagebox.showinfo(message="Downloaded successfully", title="Download Completed")
    except Exception as e:

        print(f"Ha habido un error {e}")

def changeDirectory(pathEntrada):

    dirName = askdirectory()

    pathEntrada.insert(0,dirName)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Download Music")
    root.resizable(False, False)
    root.config(bg = "grey")

    path = "/".join(getcwd().split("\\"))
    icono = tk.PhotoImage(file=f"{path}/yt_imagen.png")
    root.iconphoto(False, icono, icono)
    root.geometry("350x150")

    frame = tk.Frame()
    frame.config(bg = "grey", width= 300, height=350)
    frame.pack(fill="both")
    tk.Label(frame, text="Write the URL", width=50, background="grey", foreground="black", font = "Calibri 12").pack()

    urlEntrada = tk.Entry(frame, width=50)
    urlEntrada.place(x = 4, y = 20)
    urlEntrada.pack()

    tk.Label(frame, text="Directory", width=50, background="grey", foreground="black", font = "Calibri 12").pack()
    
    pathEntrada = tk.Entry(root, width=30)
    pathEntrada.place(relx = 0.06555, rely = 0.5, relwidth=0.5, relheight=0.125)
  
    
    dirButton = tk.Button(root, text= "Change directory" , command= lambda : changeDirectory(pathEntrada))
    dirButton.place(relx = 0.65, rely = 0.5, relheight=0.14)

    downloadButton = tk.Button(root, text = "Download", width=20, command= lambda : download(urlEntrada.get(), pathEntrada.get()))
    downloadButton.place(x = 100, y = 110)
    
    root.mainloop()
