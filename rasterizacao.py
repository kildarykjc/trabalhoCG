import math
import numpy as np





class Ponto:
    def __init__(self, x: int, y: int, resolucao: list) -> None:
        self.x, self.y = self.scale_point(x, y, resolucao[0], resolucao[1])

    def scale_point(self, x, y, largura, altura):
        x_dist = 1 - (-1)
        # Distância entre as coordenadas máxima e mínima para y
        y_dist = 1 - (-1)
        scaled_x = ((x / x_dist) + 0.5) * largura
        scaled_y = (1 - ((y / y_dist) + 0.5)) * altura
        return [round(scaled_x), round(scaled_y)]


def calula_delta(ponto_final: int, ponto_inicial: int) -> float:
    return (ponto_final - ponto_inicial)


def produz_fragmento(x: float, y: float) -> list:
    x_medio = (x)
    y_medio = y
    ponto_x_medio = int(x_medio+0.5)
    ponto_y_medio = int(y_medio+0.5)
    return [ponto_x_medio, ponto_y_medio]


def rasterizacao_delta_x_maior_delta_y(ponto1: Ponto, m, b, x2) -> list:
    x1,  y1 = ponto1.x,  ponto1.y
    pontos: list = []
    pontos.append(produz_fragmento(x1, y1))
    if (x1 < x2):
        while (x1 <= x2):
            x1 = x1 + 1
            if (m != 0):
                y1 = math.ceil(m*x1 + b)
            pontos.append(produz_fragmento(x1, y1))
    else:
        aux = x1
        while (x2 <= aux):
            x2 = x2 + 1
            x1 = x1-1
            if (m != 0):
                y1 = math.ceil(m*x1 + b)
            pontos.append(produz_fragmento(x1, y1))
    return pontos


def rasterizacao_delta_y_maior_delta_x(ponto1: Ponto, m, b, ponto2: Ponto) -> list:
    x1,  y1, y2 = ponto1.x,  ponto1.y, ponto2.y

    pontos: list = []
    if (y1 < y2):
        while (y1 <= y2):
            pontos.append(produz_fragmento(x1, y1))
            y1 = y1 + 1
            if (m != 0):
                x1 = ((y1-b)/m)
    else:
        aux = y1
        while y2 <= aux:
            pontos.append(produz_fragmento(x1, y1))
            y2 = y2 + 1
            y1 = y1 - 1
            if (m != 0):
                x1 = math.ceil((y1-b) / m)

    return pontos


def rasterizacao_de_retas(ponto1: Ponto, ponto2: Ponto) -> None:
    primeiro_ponto,  = ponto1,
    pontos: list

    delta_x = calula_delta(ponto2.x, ponto1.x)
    delta_y = calula_delta(ponto2.y, ponto1.y)

    x = primeiro_ponto.x
    y = primeiro_ponto.y
    if (delta_x != 0):
        m = delta_y/delta_x
        b = y - m * x
    else:
        m = 0  # como o x não varia , a reta não possui inclinação
        b = 0

    if (abs(delta_x) > abs(delta_y)):
        pontos = rasterizacao_delta_x_maior_delta_y(
            primeiro_ponto, m, b, ponto2.x)
    else:
        pontos = rasterizacao_delta_y_maior_delta_x(
            primeiro_ponto, m, b, ponto2)

    return pontos

def rasteriza_poligno(arestas, largura, altura):
    img_face_orig = np.zeros((largura, altura, 3), dtype="uint8")
    img_face = np.zeros((largura, altura, 3), dtype="uint8")

    for aresta in arestas:
        for ponto in aresta:
            img_face_orig[ponto[0], ponto[1]] = [1, 1, 1]

    for i in range(altura):
        cont_h = 0
        sava_ponto_h = []
        cont_v = 0
        sava_ponto_v = []
        for j in range(largura - 1):
            # Horizontal
            if np.array_equal(img_face_orig[j, i], [1, 1, 1]):
                cont_h += 1
                if len(sava_ponto_h) > 1:
                    del sava_ponto_h[0]
                sava_ponto_h.append([j, i])
            if cont_h == 2:
                variacao_h = abs(sava_ponto_h[1][1] - sava_ponto_h[0][1])
                for w in range(variacao_h):
                    img_face[i, w + sava_ponto_h[0][1]] = [255, 255, 255]
                cont_h = 1

            # Vertical
            if np.array_equal(img_face_orig[j, i], [1, 1, 1]):
                cont_v += 1
                if len(sava_ponto_v) > 1:
                    del sava_ponto_v[0]
                sava_ponto_v.append([j, i])
            if cont_v == 2:
                variacao_v = sava_ponto_v[1][0] - sava_ponto_v[0][0]
                for z in range(variacao_v):
                    img_face[z + sava_ponto_v[0][0], i] = [255, 255, 255]
                cont_v = 1

    arestas_rasterizadas = []
    for i in range(altura):
        for j in range(largura-1):
            if np.array_equal(img_face[j, i], img_face_orig[j, i]):
                continue

            if np.array_equal(img_face[j, i], [255, 255, 255]):
                arestas_rasterizadas.append([j, i])

    return arestas_rasterizadas

