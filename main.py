import os
from PIL import Image
import turtle
import time

def main():
    n = input("Nome da imagem: \n > ")
    escala = int(input("Escala: \n > "))
    opcao = input("Opções do desenho \n r - print rápida \n n - normal \n > ")


    img = Image.open(f"{n}.png")
    img = img.convert("RGBA")
    l, a = img.size


    img = img.resize((l * escala, a * escala), Image.NEAREST)
    l, a = img.size

    w = os.name
    clear = "cls" if w == "nt" else "clear"


    if opcao.lower() == "n":
        time.sleep(1)
        print(f"Tamanho da imagem: {l}x{a}")
        time.sleep(2.5)
        turtle.shape("classic")
        turtle.speed(0)
        turtle.penup()
        desenhar(img, l, a, escala)

        print("\nA tua bela obra de arte está feita!")
        turtle.done()

    elif opcao.lower() == "r":
        time.sleep(1)
        print(f"Tamanho da imagem: {l}x{a}")
        time.sleep(2.5)
        turtle.shape("classic")
        turtle.speed(0)
        turtle.penup()
        turtle.tracer(0, 0)
        desenhar(img, l, a, escala)

        print("\nA tua bela obra de arte está feita!")
        turtle.update()
        turtle.done()

    else:
        print("\n---Opção inválida---")
        time.sleep(1.5)
        os.system(clear)
        main()


def desenhar(img, l, a, escala):
    sum = 1
    iL, iA = 0, 0

    for x in range(0, l):
        iL += 1
        for y in range(0, a):
            px = img.getpixel((x, y))
            color = '#%02x%02x%02x' % (px[0], px[1], px[2])
            print(f"{sum}º px, ({x}x{y}y): {px}")
            pintar_pontos(escala, l, a, xOriginal = x, yOriginal = y, color = color)
            sum += 1
            iA += 1
        iA = 0
    iL = 0
    return


def get_square_coordinates(x, y, escala):
    coordinates = []
    for i in range(x, x + escala):
        for j in range(y, y + escala):
            coordinates.append((i, j))
    return coordinates


def pintar_pontos(escala, l, a, color, xOriginal, yOriginal):

    coordenadasLista = get_square_coordinates(xOriginal, yOriginal, escala)

    for cor in coordenadasLista:
        x_scaled = cor[0]
        y_scaled = cor[1]

        turtle.setpos(x_scaled - l, a - y_scaled)
        turtle.pendown()
        turtle.color(color)
        turtle.begin_fill()
        turtle.dot(2)
        turtle.end_fill()
        turtle.penup()

    return

main()