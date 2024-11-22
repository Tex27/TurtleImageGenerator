import os
from PIL import Image
import turtle
import time

def main():
    n = input("Nome da imagem: \n > ")
    option = input("Opções do desenho \n r - print rápida \n n - normal \n > ")


    # cenas da imagem, local onde está converter para RGB e extrair as dimensões em pixeis
    img = Image.open(f"{n}.png")
    img = img.convert("RGBA")
    l, a = img.size

    #sistema para ver qual o sistema operativo para usar o comando clear

    msg = "\nAnalisando imagem"
    w = os.name
    if w == "nt":
        clear = "cls"
    else:
        clear = "clear"



    # Criação da Imagem de maneira mais lenta mas mostrando o traçado
    if option.lower() == "n":
        carregar(msg, clear)
        time.sleep(1)
        print(f"Tamanho da imagem: {l}x{a}")
        time.sleep(2.5)
        turtle.shape("classic")
        turtle.speed(0)
        turtle.penup()
        desenhar(img, l, a)
                
        print("\nA tua bela obra de arte está feita!")
        turtle.done()

    # Criação da Imagem de maneira mais rápida mas que apenas mostra a imagem após processar todos os pixeis
    if option.lower() == "r":
        carregar(msg, clear)
        time.sleep(1)
        print(f"Tamanho da imagem: {l}x{a}")
        time.sleep(2.5)
        turtle.shape("classic")
        turtle.speed(0)
        turtle.penup()
        turtle.tracer(0, 0)
        desenhar(img, l, a)
        
        print("\nA tua bela obra de arte está feita!")
        turtle.update()
        turtle.done()

    else:
        print("\n---Opção inválida---")
        time.sleep(1.5)
        os.system(clear)
        main()

def desenhar(img, l, a):
    sum = 0
    for x in range(0, l):
        for y in range(0, a):
            px = img.getpixel((x, y))
            color = '#%02x%02x%02x' % (px[0], px[1], px[2])
            turtle.setpos(x - 112, 112 - y)
            turtle.pendown()
            turtle.color(color)
            turtle.begin_fill()
            turtle.dot(2)
            turtle.end_fill()
            turtle.penup()
            sum += 1
            print(f"{sum}º px, ({x}x{y}y): {px}")
    return

def carregar(msg, clear):
    #tem de ser com f string pq o os não aceita variáveis por si só n sei bem porquê, mas assim funfa
        for i in range(2):
            print(f"{msg} /")
            time.sleep(1)
            os.system(clear)
            print(f"{msg} -")
            time.sleep(1)
            os.system(clear)
            print(f"{msg} \\")
            time.sleep(1)
            os.system(clear)
            print(f"{msg} |")
            time.sleep(1)
            os.system(clear)
            return
main()