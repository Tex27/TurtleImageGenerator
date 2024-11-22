import os
from PIL import Image
import turtle
import time

n = input("Nome da imagem: \n > ")
o = input("Opções do desenho \n r - print rápida \n n - normal \n > ")


# cenas da imagem, local onde está converter para RGB e extrair as dimensões em pixeis
img = Image.open(f"./imagens/{n}.png")
img = img.convert("RGBA")
l, a = img.size

#sistema para ver qual o sistema operativo para usar o comando clear

msg = "\nAnalisando imagem"
w = os.name
if w == "nt":
    clear = "cls"
else:
    clear = "clear"

#tem de ser com f string pq o os não aceita variáveis por si só (n sei bem porquê, mas assim funfa)
for i in range(2):
    print(f"{msg} /")
    time.sleep(1)
    os.system(f"{clear}")
    print(f"{msg} -")
    time.sleep(1)
    os.system(f"{clear}")
    print(f"{msg} \\")
    time.sleep(1)
    os.system(f"{clear}")
    print(f"{msg} |")
    time.sleep(1)
    os.system(f"{clear}")
   


time.sleep(1)
print(f"Tamanho da imagem: {l}x{a}")
time.sleep(2.5)

# Criação da Imagem de maneira mais lenta mas mostrando o traçado
if o == "n":
    turtle.shape("classic")
    turtle.speed(0)
    turtle.penup()
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
            
    print("\nA tua bela obra de arte está feita!")
    turtle.done()

# Criação da Imagem de maneira mais rápida mas que apenas mostra a imagem após processar todos os pixeis
elif o == "r":
    turtle.shape("classic")
    turtle.speed(0)
    turtle.penup()
    sum = 0
    turtle.tracer(0, 0)
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
    
    print("\nA tua bela obra de arte está feita!")
    turtle.update()
    turtle.done()
