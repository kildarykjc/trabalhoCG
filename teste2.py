from tkinter import ttk
import tkinter as tk
from PIL import ImageTk
import formas
from tkinter.messagebox import showinfo
from calendar import month_name

def mostrarImagem(escolhida):
    formas.plotarImagem(escolhida)
    image = ImageTk.PhotoImage(file="image.jpg")
    imagebox.config(image=image)
    imagebox.image = image # save a reference of the image to avoid garbage collection

def show_image(imagefile):
    image = ImageTk.PhotoImage(file=imagefile)
    imagebox.config(image=image)
    imagebox.image = image # save a reference of the image to avoid garbage collection

def digitarPontos():
    # create a combobox
    # label
    label = ttk.Label(text="Selecione a Forma e sua resolucao:")
    label.pack(fill=tk.X, padx=5, pady=5)

    # create a combobox
    selected_month = tk.StringVar()
    month_cb = ttk.Combobox(root, textvariable=selected_month)

    # get first 3 letters of every month name
    #month_cb['values'] = [month_name[m][0:3] for m in range(1, 13)]
    month_cb['values'] = ["Linha","Triangulo","Quadrado","Hexagono"]

    # prevent typing a value
    month_cb['state'] = 'readonly'

    # place the widget
    month_cb.pack(fill=tk.X, padx=5, pady=5)


    # bind the selected value changes
    def month_changed(event):
        """ handle the month changed event """
        showinfo(
            title='Result',
            message=f'You selected {selected_month.get()}!'
        )


    month_cb.bind('<<ComboboxSelected>>', month_changed)

    # set the current month
    #current_month = date().strftime('%b')
    #month_cb.set("teste")

    ########################################################################################### Fim Combobox

root = tk.Tk()
root.title("Trabalho N1 CG")
#root.geometry("500x300")

frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="Sair", fg="red", command=quit)
button.pack(side=tk.LEFT)

iLinhas = tk.Button(frame, text="Mostrar imagens com todas linhas", command=lambda: mostrarImagem("linhas"))
iLinhas.pack(side=tk.LEFT)

iTriangulo = tk.Button(frame, text="Mostrar imagens do triangulo", command=lambda: mostrarImagem("triangulos"))
iTriangulo.pack(side=tk.LEFT)

iQuadrado = tk.Button(frame, text="Mostrar imagens do quadrado", command=lambda: mostrarImagem("quadrados"))
iQuadrado.pack(side=tk.LEFT)

iHexagono = tk.Button(frame, text="Mostrar imagens so hexagono", command=lambda: mostrarImagem("hexagonos"))
iHexagono.pack(side=tk.LEFT)

iFormas = tk.Button(frame, text="Mostrar imagens de todas as formas", command=lambda: mostrarImagem("formas"))
iFormas.pack(side=tk.LEFT)

iManual = tk.Button(frame, text="Digitar pontos", command=lambda: digitarPontos())
iManual.pack(side=tk.LEFT)

other = tk.Button(frame, text="Mostrar", command=lambda: show_image("bola.jpg"))
other.pack(side=tk.LEFT)

# label to show the image
imagebox = tk.Label(root)
imagebox.pack()

root.mainloop()