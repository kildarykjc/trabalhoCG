import tkinter as tk
from tkinter import ttk
import formas
import numpy as np
forma = formas
def janelaLinha():
    janela2 = tk.Toplevel()
    janela2.title('Digite os pontos do Triangulo')
    labelPonto1 = tk.Label(janela2, text='Ponto1 x,y').grid(row=0, column=0)
    labelPonto2 = tk.Label(janela2, text='Ponto2 x,y').grid(row=0, column=1)
    textoPonto1 = tk.Entry(janela2,bg = "light yellow")
    textoPonto1.grid(row=1,column=0)
    textoPonto2 = tk.Entry(janela2,bg = "light yellow")
    textoPonto2.grid(row=1,column=1)
    selecionarResolucao = tk.StringVar()
    comboResolucao = ttk.Combobox(janela2, textvariable=selecionarResolucao)
    comboResolucao['values'] = ["100x100","300x300","600x600","800x600","1920x1080"]
    comboResolucao['state'] = 'readonly'
    comboResolucao.grid(row=2, column=0)
    botaoExec = tk.Button(janela2, text='Executar', command=lambda: executaResolucao(textoPonto1.get(),textoPonto2.get(),comboResolucao.get()))
    botaoExec.grid(row=2,column=1)
    

def janelaTriangulo():
    janela2 = tk.Toplevel()
    janela2.title('Digite os pontos do Triangulo')
    labelPonto1 = tk.Label(janela2, text='Ponto1 x,y').grid(row=0, column=0)
    labelPonto2 = tk.Label(janela2, text='Ponto2 x,y').grid(row=0, column=1)
    labelPonto3 = tk.Label(janela2, text='Ponto3 x,y').grid(row=0, column=2)
    textoPonto1 = tk.Text(janela2,height = 1,width = 9,bg = "light yellow").grid(row=1,column=0)
    textoPonto2 = tk.Text(janela2,height = 1,width = 9,bg = "light yellow").grid(row=1,column=1)
    textoPonto3 = tk.Text(janela2,height = 1,width = 9,bg = "light yellow").grid(row=1,column=2)
    selecionarResolucao = tk.StringVar()
    comboResolucao = ttk.Combobox(janela2, textvariable=selecionarResolucao)
    comboResolucao['values'] = ["100x100","300x300","600x600","800x600","1920x1080"]
    comboResolucao['state'] = 'readonly'
    comboResolucao.grid(row=2)

def janelaQuadrado():
    janela2 = tk.Toplevel()
    janela2.title('Digite os pontos do Triangulo')
    labelPonto1 = tk.Label(janela2, text='Ponto1 x,y').grid(row=0, column=0)
    labelPonto2 = tk.Label(janela2, text='Ponto2 x,y').grid(row=0, column=1)
    labelPonto3 = tk.Label(janela2, text='Ponto3 x,y').grid(row=0, column=2)
    labelPonto4 = tk.Label(janela2, text='Ponto4 x,y').grid(row=0, column=3)
    textoPonto1 = tk.Text(janela2,height = 1,width = 9,bg = "light yellow").grid(row=1,column=0)
    textoPonto2 = tk.Text(janela2,height = 1,width = 9,bg = "light yellow").grid(row=1,column=1)
    textoPonto3 = tk.Text(janela2,height = 1,width = 9,bg = "light yellow").grid(row=1,column=2)
    textoPonto4 = tk.Text(janela2,height = 1,width = 9,bg = "light yellow").grid(row=1,column=3)
    selecionarResolucao = tk.StringVar()
    comboResolucao = ttk.Combobox(janela2, textvariable=selecionarResolucao)
    comboResolucao['values'] = ["100x100","300x300","600x600","800x600","1920x1080"]
    comboResolucao['state'] = 'readonly'
    comboResolucao.grid(row=2)

def janelaHexagono():
    janela2 = tk.Toplevel()
    janela2.title('Digite os pontos do Triangulo')
    labelPonto1 = tk.Label(janela2, text='Ponto1 x,y').grid(row=0, column=0)
    labelPonto2 = tk.Label(janela2, text='Ponto2 x,y').grid(row=0, column=1)
    labelPonto3 = tk.Label(janela2, text='Ponto3 x,y').grid(row=0, column=2)
    labelPonto4 = tk.Label(janela2, text='Ponto4 x,y').grid(row=0, column=3)
    labelPonto5 = tk.Label(janela2, text='Ponto5 x,y').grid(row=0, column=4)
    labelPonto6 = tk.Label(janela2, text='Ponto6 x,y').grid(row=0, column=5)
    textoPonto1 = tk.Text(janela2,height = 1,width = 9,bg = "light yellow").grid(row=1,column=0)
    textoPonto2 = tk.Text(janela2,height = 1,width = 9,bg = "light yellow").grid(row=1,column=1)
    textoPonto3 = tk.Text(janela2,height = 1,width = 9,bg = "light yellow").grid(row=1,column=2)
    textoPonto4 = tk.Text(janela2,height = 1,width = 9,bg = "light yellow").grid(row=1,column=3)
    textoPonto5 = tk.Text(janela2,height = 1,width = 9,bg = "light yellow").grid(row=1,column=4)
    textoPonto6 = tk.Text(janela2,height = 1,width = 9,bg = "light yellow").grid(row=1,column=5)
    selecionarResolucao = tk.StringVar()
    comboResolucao = ttk.Combobox(janela2, textvariable=selecionarResolucao)
    comboResolucao['values'] = ["100x100","300x300","600x600","800x600","1920x1080"]
    comboResolucao['state'] = 'readonly'
    comboResolucao.grid(row=2)
def executaResolucao(*args):
    if len(args)==3:
        ponto1 = args[0].split(",") 
        ponto1=list(np.float_(ponto1))
        ponto2 = args[1].split(",")
        ponto2=list(np.float_(ponto2))
        resolucao = args[2].split("x")
        resolucao =  list(np.int_(resolucao))
        formas.gerarImagemDigitada(ponto1,ponto2,resolucao)
    elif len(args)==4:
        ponto1 = args[0].split(",") 
        ponto1=list(np.float_(ponto1))
        ponto2 = args[1].split(",")
        ponto2=list(np.float_(ponto2))
        ponto3 = args[2].split(",")
        ponto3=list(np.float_(ponto3))
        resolucao = args[2].split("x")
        resolucao =  list(np.int_(resolucao))
        formas.gerarImagemDigitada(ponto1,ponto2,ponto3,resolucao)
    elif len(args)==5:
        ponto1 = args[0].split(",") 
        ponto1=list(np.float_(ponto1))
        ponto2 = args[1].split(",")
        ponto2=list(np.float_(ponto2))
        ponto3 = args[2].split(",")
        ponto3=list(np.float_(ponto3))
        ponto4 = args[3].split(",")
        ponto4=list(np.float_(ponto4))
        resolucao = args[2].split("x")
        resolucao =  list(np.int_(resolucao))
        formas.gerarImagemDigitada(ponto1,ponto2,ponto3,ponto4,resolucao)
    else:
        ponto1 = args[0].split(",") 
        ponto1 = list(np.float_(ponto1))
        ponto2 = args[1].split(",")
        ponto2 = list(np.float_(ponto2))
        ponto3 = args[2].split(",")
        ponto3 = list(np.float_(ponto3))
        ponto4 = args[3].split(",")
        ponto4 = list(np.float_(ponto4))
        ponto5 = args[4].split(",")
        ponto5 = list(np.float_(ponto5))
        ponto6 = args[5].split(",")
        ponto6 = list(np.float_(ponto6))
        resolucao = args[2].split("x")
        resolucao =  list(np.int_(resolucao))
        formas.gerarImagemDigitada(ponto1,ponto2,ponto3,ponto4,ponto5,ponto6,resolucao)

janela = tk.Tk()
botaoLinha = tk.Button(janela, text='Gerar Linha', command= janelaLinha)
botaoTriangulo = tk.Button(janela, text='Gerar Triangulo', command= janelaTriangulo)
botaoQuadrado = tk.Button(janela, text='Gerar Quadrado', command= janelaQuadrado)
botaoHexagono = tk.Button(janela, text='Gerar Hexagono', command= janelaHexagono)
botaoLinha.grid(row=0,column=0)
botaoTriangulo.grid(row=0,column=1)
botaoQuadrado.grid(row=0,column=2)
botaoHexagono.grid(row=0,column=3)

janela.mainloop()