from pytube import YouTube
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tqdm import tqdm
from os import getcwd


def download(url, path):
    try:
        if len(url) < 1 or len(path) < 1:
            raise ValueError

        url = str(url)

        if(len(url) < 10):
            raise KeyError

        yt = YouTube(url)
        path = str(path)

        yt.streams.filter(only_audio=True, file_extension='mp4').first().download(path)

    except Exception as e:

        print(f"Ha habido un error {e}")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Descargar música")

    path = "/".join(getcwd().split("\\"))
    icono = tk.PhotoImage(file=f"{path}/Descargar Música/yt_imagen.png")
    root.iconphoto(False, icono, icono)
    root.geometry("350x150")

    frame = Frame()
    frame.pack(fill="both")
    frame.config(bg = "blue", width= 300, height=200)    
    tk.Label(frame, text="Escriba la URL", width=50, background="red", foreground="white", font = "Calibri 12").pack()

    urlEntrada = Entry(frame, width=50)
    urlEntrada.pack()

    tk.Label(frame, text="Escriba Dir Mem", width=50, background="red", foreground="white", font = "Calibri 12").pack()
    pathEntrada = Entry(frame, width=50)
    pathEntrada.pack()
    
    button = tk.Button(frame, text = "Descargar", width=20, command= lambda : download(urlEntrada.get(), pathEntrada.get()))
    button.pack()

    #barra_de_progreso = ttk.Progressbar(orient=HORIZONTAL, length=160)

    
    root.mainloop()
