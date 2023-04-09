from tkinter import *
from PIL import Image, ImageTk
import formas
#imagem = formas.plotarImagem

class TesteImage1:

    def __init__(self, master=None):

        self.widget1 = Frame(master)
        self.widget1.pack()
        
        # imagem = ImageTk.PhotoImage(Image.open("bola.jpg"))
        image = Image.open("image.jpg")
        photo = ImageTk.PhotoImage(image)
        self.imagem = Label(master, text = "adicionando", image = photo)
        self.imagem.image = photo
        self.imagem.pack()

        self.teste = Label(self.widget1, text="testando")
        self.teste.pack()


root = Tk()
TesteImage1(root)
root.mainloop()