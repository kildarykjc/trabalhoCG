from tkinter import ttk
from tkinter import *
from PIL import ImageTk
import formas
from tkinter.messagebox import showinfo
from calendar import month_name

def mostrarImagem(escolhida):
    formas.plotarImagem(escolhida)
    image = ImageTk.PhotoImage(file="image.jpg")
    imagebox.config(image=image)
    imagebox.image = image # save a reference of the image to avoid garbage collection

def digitarPontos(janela):
    
    # create a combobox
    # label
    label = ttk.Label(text="Selecione a Forma")
    label.pack(fill=X, padx=5, pady=5)

    # create a combobox
    selecionarFormas = StringVar()
    forma = ttk.Combobox(janela, textvariable=selecionarFormas)

    forma['values'] = ["Linha","Triangulo","Quadrado","Hexagono"]

    # prevent typing a value
    forma['state'] = 'readonly'

    # place the widget
    forma.pack(fill=X, padx=5, pady=5)


    # bind the selected value changes
    def formaEscolhida(event):
        
        formaGeo = selecionarFormas.get()
        if formaGeo == "Linha":
            Label(janela,text="ponto1 X",anchor=W).place(x=10,y=20,width=100,height=20)
            ponto1X=Entry(janela)
            ponto1X.place(x=10,y=100,width=200,height=20)
            Label(janela,text="ponto1 y",anchor=W).place(x=100,y=20,width=100,height=20)
            ponto1y=Entry(janela)
            ponto1y.place(x=10,y=100,width=200,height=20)
            print("")
        elif formaGeo == "Triangulo":
            print("")
        elif formaGeo == "Quadrado":
            print("")
        else:
            print("")

        # create a combobox
        # label
        label = ttk.Label(text="Selecione a resolucao:")
        label.pack(fill=X, padx=5, pady=5)
        print(selecionarFormas.get())
        # create a combobox
        selecionarResolucao = StringVar()
        resolucao = ttk.Combobox(janela, textvariable=selecionarResolucao)

        # get first 3 letters of every month name
        #forma['values'] = [month_name[m][0:3] for m in range(1, 13)]
        resolucao['values'] = ["100x100","300x300","600x600","800x600","1980x1080"]

        # prevent typing a value
        resolucao['state'] = 'readonly'

        # place the widget
        resolucao.pack(fill=X, padx=5, pady=5)
               
        """ handle the month changed event """
        showinfo(
            title='Result',
            message=f'You selected {selecionarFormas.get()}!'
        )
        resolucao.bind('<<ComboboxSelected>>', "")


    forma.bind('<<ComboboxSelected>>', formaEscolhida)

    # set the current month
    #current_month = date().strftime('%b')
    #forma.set("teste")

    ########################################################################################### Fim Combobox

def coordPontos(formaGeo):
    
    
    if formaGeo == "Linha":
        print("")
    elif formaGeo == "Triangulo":
        print("")
    elif formaGeo == "Quadrado":
        print("")
    else:
        print("")

def janelaTriangulo():
	
	janela2 = Tk().Toplevel()
    
	janela2.title('Pontos do triangulo')
	Label(janela2, text = "Ponto1 x,y").grid(row = 0, column = 0 )
	Label(janela2, text = "Ponto2 x,y").grid(row = 0, column = 1 )
    #Label(janela2, text = "Ponto2 x,y").grid(row = 0, column = 3 )
    #botao_voltar = Button(janela2, text = 'Fechar a janela2', command = janela2.destroy)
	#botao_volta.grid(row = 1, column = 0)


#def Take_input():
   # INPUT = inputtxt.get("1.0", "end-1c")
   # print(INPUT)
   # if(INPUT == "120"):
   #     Output.insert(END, 'Correct')
   # else:
   #     Output.insert(END, "Wrong answer")


root = Tk()
root.title("Trabalho N1 CG")
#root.geometry("500x300")

frame = Frame(root)
frame.pack()

#button = tk.Button(frame, text="Sair", fg="red", command=quit)
#button.pack(side=tk.LEFT)
#
#iLinhas = tk.Button(frame, text="Mostrar imagens com todas linhas", command=lambda: mostrarImagem("linhas"))
#iLinhas.pack(side=tk.LEFT)
#
#iTriangulo = tk.Button(frame, text="Mostrar imagens do triangulo", command=lambda: mostrarImagem("triangulos"))
#iTriangulo.pack(side=tk.LEFT)
#
#iQuadrado = tk.Button(frame, text="Mostrar imagens do quadrado", command=lambda: mostrarImagem("quadrados"))
#iQuadrado.pack(side=tk.LEFT)
#
#iHexagono = tk.Button(frame, text="Mostrar imagens so hexagono", command=lambda: mostrarImagem("hexagonos"))
#iHexagono.pack(side=tk.LEFT)

iFormas = Button(frame, text="Mostrar imagens de todas as formas", command=lambda: mostrarImagem("formas"))
iFormas.pack(side=LEFT)

iManual = Button(frame, text="Digitar pontos", command=lambda: janelaTriangulo())
iManual.pack(side=LEFT)

other = Button(frame, text="Mostrar", command=lambda: show_image("bola.jpg"))
other.pack(side=LEFT)

# label to show the image
imagebox = Label(root)
imagebox.pack()

root.mainloop()