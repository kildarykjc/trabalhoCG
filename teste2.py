import tkinter as tk
from PIL import ImageTk
import formas

def mostrarImagem(escolhida):
    formas.plotarImagem(escolhida)
    #match escolhida:
    #    case "linha":
    #        formas.plotarImagem(1)
    #    case "linhas":
    #        formas.plotarImagem(2)
    #    case "triangulo":
    #        formas.plotarImagem(3)
    #    case "quadrado":
    #        formas.plotarImagem(4)
    #    case "hexagono":
    #        formas.plotarImagem(5)
    #    case "formas":
    #        formas.plotarImagem(6)

    #formas.plotarImagem()
    image = ImageTk.PhotoImage(file="image.jpg")
    imagebox.config(image=image)
    imagebox.image = image # save a reference of the image to avoid garbage collection

def show_image(imagefile):
    image = ImageTk.PhotoImage(file=imagefile)
    imagebox.config(image=image)
    imagebox.image = image # save a reference of the image to avoid garbage collection

root = tk.Tk()
root.title("Trabalho N1 CG")

frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="Sair", fg="red", command=quit)
button.pack(side=tk.LEFT)

iLinha = tk.Button(frame, text="Mostrar imagens da linha", command=lambda: mostrarImagem("linha"))
iLinha.pack(side=tk.LEFT)

iLinhas = tk.Button(frame, text="Mostrar imagens com todas linhas", command=lambda: mostrarImagem("linhas"))
iLinhas.pack(side=tk.LEFT)

iTriangulo = tk.Button(frame, text="Mostrar imagens do triangulo", command=lambda: mostrarImagem("triangulo"))
iTriangulo.pack(side=tk.LEFT)

iQuadrado = tk.Button(frame, text="Mostrar imagens do quadrado", command=lambda: mostrarImagem("quadrado"))
iQuadrado.pack(side=tk.LEFT)

iHexagono = tk.Button(frame, text="Mostrar imagens so hexagono", command=lambda: mostrarImagem("hexagono"))
iHexagono.pack(side=tk.LEFT)

iFormas = tk.Button(frame, text="Mostrar imagens de todas as formas", command=lambda: mostrarImagem("formas"))
iFormas.pack(side=tk.LEFT)

other = tk.Button(frame, text="Mostrar", command=lambda: show_image("bola.jpg"))
other.pack(side=tk.LEFT)

# label to show the image
imagebox = tk.Label(root)
imagebox.pack()

root.mainloop()