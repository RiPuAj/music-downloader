from main import *
import tkinter as tk
from tkinter import ttk
from os import getcwd
from time import sleep
from tkinter import messagebox
from PIL import Image


if __name__ == "__main__":

    # Root config    
    root = tk.Tk()
    root.title("Download Music")
    root.resizable(False, False)
    root.config(bg = "grey")
    root.iconbitmap("images/yt-image.ico")
    root.geometry("350x150")

    # URL label
    tk.Label(root, text="URL:",
             width=10,
             background="grey",
             foreground="black",
             font = "BoldItalic1 13"
             ).place(
                 relx=0.05,
                 rely = 0.1,
                 relwidth=0.15,
                 relheight=0.15
                 )

    # URL entry
    urlEntrada = tk.Entry(root, width=40)
    urlEntrada.place(relx=0.25, rely=0.12)

    # Directory label
    tk.Label(root,
             text="Directory:",
             width=10,
             height=10,
             background="grey",
             foreground="black",
             font = "BoldItalic1 13"
             ).place(
                 relx=0.03,
                 rely = 0.45,
                 relwidth=0.2,
                 relheight=0.15
                 )
    
    # Entry path of a directory where we will save the music
    pathEntrada = tk.Entry(root,
                           width=30
                           )
    
    pathEntrada.place(relx=0.25, rely=0.47)
  
    # Change directory button
    imageUpload = tk.PhotoImage(file = "images/uploader-image.png")
    dirButton = tk.Button(root,
                          image= imageUpload,
                          command= lambda : changeDirectory(pathEntrada),
                          width=20,
                          height=20,
                          background="grey",
                          relief="flat"
                          )
    dirButton.place(relx = 0.84, rely = 0.45, relheight=0.14, relwidth=0.15)

    # Download button
    downloadImage = tk.PhotoImage(file="images/download-image.png")
    downloadButton = tk.Button(root, text = "Download", 
                               width=35,
                               image= downloadImage,
                               font="BoldItalic1 9",
                               command= lambda : download(urlEntrada.get(),pathEntrada.get()),
                               relief="flat",
                               background="grey"
                               )
    downloadButton.place(x = 150, y = 110)
    
    root.mainloop()