import rasterizacao
import numpy as np
import matplotlib.pyplot as plt
import imagem

ponto = rasterizacao
img = imagem.Imagem
#Resoluções

altura, largura = 100, 100
resolucao1 = altura, largura
resolucao2 = altura*3, largura*3
resolucao3 = altura*6, largura*6
resolucao4 = altura*8, largura*6
resolucao5 = int(altura*19.2), int(largura*10.8)

# EXEMPLO DE RETAS
# vertical
reta1_ponto1 = (-0.5,-0.8)
reta1_ponto2 = (-0.5,0.8)

# horizontal
reta2_ponto1 = (-0.9,0)
reta2_ponto2 = (0.9,0)

# inclinada
reta3_ponto1 = (-0.9,-0.9)
reta3_ponto2 = (0.9,0.9)

reta4_ponto1 = (-0.9,0.9)
reta4_ponto2 = (0.9,-0.9)

# EXEMPLO PONTOS DO TRIANGULO
tri_ponto1 = (-0.5, -0.87)
tri_ponto2 = (0.5, -0.87)
tri_ponto3 = (0, 0.73)

tri2_ponto1 = (-1, 0)
tri2_ponto2 = (0, 0.73)
tri2_ponto3 = (1, 0)

# EXEMPLO PONTOS DO QUADRADO
quadrado_ponto1 = (-0.9, -0.9)
quadrado_ponto2 = (-0.9, 0.9)
quadrado_ponto3 = (0.9, 0.9)
quadrado_ponto4 = (0.9, -0.9)

quadrado2_ponto1 = (-0.5, -0.5)
quadrado2_ponto2 = (-0.5, 0.5)
quadrado2_ponto3 = (0.5, 0.5)
quadrado2_ponto4 = (0.5, -0.5)
# segunda aresta

# HEXAGONO 1

hex_ponto1 = (-0.5, -0.87)
hex_ponto2 = (-0.9, 0)
hex_ponto3 = (-0.5, 0.87)
hex_ponto4 = (0.5, 0.87)
hex_ponto5 = (0.9, 0)
hex_ponto6 = (0.5, -0.87)


#rasterizacao de retas

def reta(reta_ponto1,reta_ponto2,resolucao):
    todos_os_pontos = []
    print(reta_ponto1)
    print(reta_ponto2)
    reta_ponto1 = ponto.Ponto(reta_ponto1[0],reta_ponto1[1],resolucao)
    reta_ponto2 = ponto.Ponto(reta_ponto2[0],reta_ponto2[1],resolucao)
    todos_os_pontos.append(ponto.rasterizacao_de_retas(reta_ponto1,reta_ponto2))

    return todos_os_pontos

# rasterização do triangulo
def triangulo(tri_ponto1,tri_ponto2,tri_ponto3,resolucao):
    
    todos_os_pontos = []
    tri_ponto1 = ponto.Ponto(tri_ponto1[0],tri_ponto1[1],resolucao)
    tri_ponto2 = ponto.Ponto(tri_ponto2[0],tri_ponto2[1],resolucao) 
    tri_ponto3 = ponto.Ponto(tri_ponto3[0],tri_ponto3[1],resolucao)
    todos_os_pontos.append(ponto.rasterizacao_de_retas(tri_ponto1, tri_ponto2))
    todos_os_pontos.append(ponto.rasterizacao_de_retas(tri_ponto2, tri_ponto3))
    todos_os_pontos.append(ponto.rasterizacao_de_retas(tri_ponto3, tri_ponto1))
    
    return todos_os_pontos
# # rasterização do triangulo


# # rasterizacao do quadrado
def quadrado(quadrado_ponto1, quadrado_ponto2,quadrado_ponto3, quadrado_ponto4,resolucao):
    
    todos_os_pontos = []
    quadrado_ponto1 = ponto.Ponto(quadrado_ponto1[0],quadrado_ponto1[1],resolucao)
    quadrado_ponto2 = ponto.Ponto(quadrado_ponto2[0],quadrado_ponto2[1],resolucao) 
    quadrado_ponto3 = ponto.Ponto(quadrado_ponto3[0],quadrado_ponto3[1],resolucao)
    quadrado_ponto4 = ponto.Ponto(quadrado_ponto4[0],quadrado_ponto4[1],resolucao)
    todos_os_pontos.append(ponto.rasterizacao_de_retas(quadrado_ponto1, quadrado_ponto2))
    todos_os_pontos.append(ponto.rasterizacao_de_retas(quadrado_ponto2, quadrado_ponto3))
    todos_os_pontos.append(ponto.rasterizacao_de_retas(quadrado_ponto3, quadrado_ponto4))
    todos_os_pontos.append(ponto.rasterizacao_de_retas(quadrado_ponto4, quadrado_ponto1))
    
    return todos_os_pontos

# rasterização de hexagono
def hexagono(hex_ponto1, hex_ponto2,hex_ponto3, hex_ponto4,hex_ponto5, hex_ponto6,resolucao):
    todos_os_pontos = []
    hex_ponto1 = ponto.Ponto(hex_ponto1[0],hex_ponto1[1],resolucao)
    hex_ponto2 = ponto.Ponto(hex_ponto2[0],hex_ponto2[1],resolucao)
    hex_ponto3 = ponto.Ponto(hex_ponto3[0],hex_ponto3[1],resolucao)
    hex_ponto4 = ponto.Ponto(hex_ponto4[0],hex_ponto4[1],resolucao)
    hex_ponto5 = ponto.Ponto(hex_ponto5[0],hex_ponto5[1],resolucao)
    hex_ponto6 = ponto.Ponto(hex_ponto6[0],hex_ponto6[1],resolucao)
    todos_os_pontos.append(ponto.rasterizacao_de_retas(hex_ponto1, hex_ponto2))
    todos_os_pontos.append(ponto.rasterizacao_de_retas(hex_ponto2, hex_ponto3))
    todos_os_pontos.append(ponto.rasterizacao_de_retas(hex_ponto3, hex_ponto4))
    todos_os_pontos.append(ponto.rasterizacao_de_retas(hex_ponto4, hex_ponto5))
    todos_os_pontos.append(ponto.rasterizacao_de_retas(hex_ponto5, hex_ponto6))
    todos_os_pontos.append(ponto.rasterizacao_de_retas(hex_ponto6, hex_ponto1))


def criaImagem(todosPontos, resolucao):
    imag = ''
    imag = np.zeros((resolucao[1], resolucao[0], 3), dtype=np.uint8)
    #print(imag)
    for pontos in todosPontos:
        eixo_x = []
        eixo_y = []
        print(pontos)
        for ponto in pontos:
            #lista = tuple(ponto)
            #imag[int(lista[0]), int(lista[1])] = [255, 0, 0]
            eixo_x.append(int(ponto[0]))
            eixo_y.append(int(ponto[1]))
        # print(eixo_y)
        imag[eixo_y, eixo_x] = [255, 0, 0]
        #plt.plot(eixo_x, eixo_y)
    # plt.imshow(imag)
    #imag[eixo_y, eixo_x] = [255, 0, 0]
    return imag
    
def plotarImagem(escolha):
    match escolha:
        
        case "triangulo":
            salvarGeometricaTodas(tri_ponto1,tri_ponto2,tri_ponto3)
        case "quadrado":
            salvarGeometricaTodas(quadrado_ponto1,quadrado_ponto2,quadrado_ponto3,quadrado_ponto4)
        case "hexagono":
            salvarGeometricaTodas(hex_ponto1,hex_ponto2,hex_ponto3,hex_ponto4,hex_ponto5,hex_ponto6)
        

def salvarGeometrica(pontosDaArea,resolucao):
    Image = img.criar_imagem_geometrica(pontosDaArea, resolucao)
    pontos_internos = rasterizacao.rasteriza_poligno( pontosDaArea, resolucao[0], resolucao[1])
    for ponto in pontos_internos:
        Image[ponto[1], ponto[0]] = [255, 0, 0]
    
    return Image

def salvarGeometricaTodas(*args):
    print(len(args))
    print((args))

    if len(args)==3:
        Image1 = salvarGeometrica(triangulo(args[0],args[1],args[2],resolucao1),resolucao1)
        Image2 = salvarGeometrica(triangulo(args[0],args[1],args[2],resolucao2),resolucao2)
        Image3 = salvarGeometrica(triangulo(args[0],args[1],args[2],resolucao3),resolucao3)
        Image4 = salvarGeometrica(triangulo(args[0],args[1],args[2],resolucao4),resolucao4)
        Image5 = salvarGeometrica(triangulo(args[0],args[1],args[2],resolucao5),resolucao5)
    elif len(args)==4:
        Image1 = salvarGeometrica(quadrado(args[0],args[1],args[2],args[3],resolucao1),resolucao1)
        Image2 = salvarGeometrica(quadrado(args[0],args[1],args[2],args[3],resolucao2),resolucao2)
        Image3 = salvarGeometrica(quadrado(args[0],args[1],args[2],args[3],resolucao3),resolucao3)
        Image4 = salvarGeometrica(quadrado(args[0],args[1],args[2],args[3],resolucao4),resolucao4)
        Image5 = salvarGeometrica(quadrado(args[0],args[1],args[2],args[3],resolucao5),resolucao5)
    else:
        Image1 = salvarGeometrica(hexagono(args[0],args[1],args[2],args[3],args[4],args[5],resolucao1),resolucao1)
        Image2 = salvarGeometrica(hexagono(args[0],args[1],args[2],args[3],args[4],args[5],resolucao2),resolucao2)
        Image3 = salvarGeometrica(hexagono(args[0],args[1],args[2],args[3],args[4],args[5],resolucao3),resolucao3)
        Image4 = salvarGeometrica(hexagono(args[0],args[1],args[2],args[3],args[4],args[5],resolucao4),resolucao4)
        Image5 = salvarGeometrica(hexagono(args[0],args[1],args[2],args[3],args[4],args[5],resolucao5),resolucao5)

    #Image1 = salvarGeometrica(pontosDaArea,resolucao1)
    #Image2 = salvarGeometrica(pontosDaArea, resolucao2)
    #Image3 = salvarGeometrica(pontosDaArea, resolucao3)
    #Image4 = salvarGeometrica(pontosDaArea, resolucao4)
    #Image5 = salvarGeometrica(pontosDaArea, resolucao5)
    fig = plt.figure(figsize=(15, 10)) 
    rows = 1
    columns = 5
     
     
    fig.add_subplot(rows, columns, 1) 
    plt.imshow(Image1) 
    plt.axis('off') 
    plt.title("100x100") 
    fig.add_subplot(rows, columns, 2) 
    plt.imshow(Image2) 
    plt.axis('off') 
    plt.title("300x300") 
    fig.add_subplot(rows, columns, 3) 
    plt.imshow(Image3) 
    plt.axis('off') 
    plt.title("600x600") 
    fig.add_subplot(rows, columns, 4) 
    plt.imshow(Image4) 
    plt.axis('off') 
    plt.title("800x600")
    fig.add_subplot(rows, columns, 5) 
    plt.imshow(Image5) 
    plt.axis('off') 
    plt.title("1920x1080")
    plt.plot([1, 2])
    plt.savefig('image.jpg')

#salvarGeometricaTodas(quadrado_ponto1,quadrado_ponto2,quadrado_ponto3,quadrado_ponto4)
    
    #plt.imshow(Image1) 
    #plt.axis('off') 
    #plt.title("100x100") 
    ##plt.show()
    #plt.plot([1, 2])
    #plt.savefig('image.jpg')
#plotarImagem(criaImagem(reta(reta1_ponto1,reta1_ponto2,resolucao1), resolucao1))


#Image1 = criaImagem(reta(reta1_ponto1,reta1_ponto2,resolucao1), resolucao1)
#Image1 = criaImagem(triangulo(tri_ponto1,tri_ponto2,tri_ponto3,resolucao1), resolucao1)
#Image2 = criaImagem(triangulo(tri_ponto1,tri_ponto2,tri_ponto3,resolucao2), resolucao2)
#Image3 = criaImagem(triangulo(tri_ponto1,tri_ponto2,tri_ponto3,resolucao3), resolucao3)
#Image4 = criaImagem(triangulo(tri_ponto1,tri_ponto2,tri_ponto3,resolucao4), resolucao4)
#Image5 = criaImagem(triangulo(tri_ponto1,tri_ponto2,tri_ponto3,resolucao5), resolucao5)

#Image1 = criaImagem(quadrado(quadrado_ponto1,quadrado_ponto2,quadrado_ponto3,quadrado_ponto4,resolucao1), resolucao1)
#Image2 = criaImagem(quadrado(quadrado_ponto1,quadrado_ponto2,quadrado_ponto3,quadrado_ponto4,resolucao2), resolucao2)
#Image3 = criaImagem(quadrado(quadrado_ponto1,quadrado_ponto2,quadrado_ponto3,quadrado_ponto4,resolucao3), resolucao3)
#Image4 = criaImagem(quadrado(quadrado_ponto1,quadrado_ponto2,quadrado_ponto3,quadrado_ponto4,resolucao4), resolucao4)
#Image5 = criaImagem(quadrado(quadrado_ponto1,quadrado_ponto2,quadrado_ponto3,quadrado_ponto4,resolucao5), resolucao5)
#fig = plt.figure(figsize=(15, 10)) 
#rows = 1
#columns = 1
#
#
#fig.add_subplot(rows, columns, 1) 
#plt.imshow(Image1) 
#plt.axis('off') 
#plt.title("100x100") 
#fig.add_subplot(rows, columns, 2) 
#plt.imshow(Image2) 
#plt.axis('off') 
#plt.title("300x300") 
#fig.add_subplot(rows, columns, 3) 
#plt.imshow(Image3) 
#plt.axis('off') 
#plt.title("600x600") 
#fig.add_subplot(rows, columns, 4) 
#plt.imshow(Image4) 
#plt.axis('off') 
#plt.title("800x600")
#fig.add_subplot(rows, columns, 5) 
#plt.imshow(Image5) 
#plt.axis('off') 
#plt.title("1920x1080")
#plt.plot([1, 2])
#plt.savefig('image.jpg')
#plt.show()

#triangulo(tri2_ponto1,tri2_ponto2,tri2_ponto3)
#quadrado(quadrado_ponto1, quadrado_ponto2,quadrado_ponto3, quadrado_ponto4)
#hexagono(hex_ponto1, hex_ponto2,hex_ponto3, hex_ponto4,hex_ponto5, hex_ponto6)

#imag = np.zeros((resolucao1[0], resolucao1[1], 3), dtype=np.uint8)
##print(imag)
#for pontos in todos_os_pontos:
#    eixo_x = []
#    eixo_y = []
#    print(pontos)
#    for ponto in pontos:
#        lista = tuple(ponto)
#        #imag[int(lista[0]), int(lista[1])] = [255, 0, 0]
#        eixo_x.append(int(ponto[0]))
#        eixo_y.append(int(ponto[1]))
#    # print(eixo_y)
#    imag[eixo_y, eixo_x] = [255, 0, 0]
#    #plt.plot(eixo_x, eixo_y)
## plt.imshow(imag)
#
#plt.imshow(imag) 
#plt.show()