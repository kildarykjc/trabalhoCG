import tkinter as tk
from PIL import ImageTk
import formas

def mostrarImagem():
    formas.plotarImagem()
    image = ImageTk.PhotoImage(file="image.jpg")
    imagebox.config(image=image)
    imagebox.image = image # save a reference of the image to avoid garbage collection

def show_image(imagefile):
    image = ImageTk.PhotoImage(file=imagefile)
    imagebox.config(image=image)
    imagebox.image = image # save a reference of the image to avoid garbage collection

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="Sair", fg="red", command=quit)
button.pack(side=tk.LEFT)

slogan = tk.Button(frame, text="Gerar Imagem", command=lambda: mostrarImagem())
slogan.pack(side=tk.LEFT)

other = tk.Button(frame, text="Mostrar", command=lambda: show_image("image.jpg"))
other.pack(side=tk.LEFT)

# label to show the image
imagebox = tk.Label(root)
imagebox.pack()

root.mainloop()