from PIL import Image
import turtle

s = int(input("Tamanho da imagem em px: "))
n = input("Nome da imagem: ")
o = input("Opções do desenho \n r - print rápida \n n - normal \n >")

img = Image.open(f"{n}.png")
img = img.convert("RGBA")

if o == "n":
    turtle.shape("classic")
    turtle.speed("fastest")
    turtle.penup()
    for x in range(0, s):
        for y in range(0, s):
            px = img.getpixel((x, y))
            color = '#%02x%02x%02x' % (px[0], px[1], px[2])
            turtle.setpos(x - 112, 112 - y)
            turtle.pendown()
            turtle.color(color)
            turtle.begin_fill()
            turtle.dot(5)
            turtle.end_fill()
            turtle.penup()
            print(f"{x}x{y}y: {px}")

        turtle.done()

elif o == "r":
    turtle.shape("classic")
    turtle.speed("fastest")
    turtle.penup()
    turtle.tracer(0, 0)
    for x in range(0, s):
        for y in range(0, s):
            px = img.getpixel((x, y))
            color = '#%02x%02x%02x' % (px[0], px[1], px[2])
            turtle.setpos(x - 112, 112 - y)
            turtle.pendown()
            turtle.color(color)
            turtle.begin_fill()
            turtle.dot(5)
            turtle.end_fill()
            turtle.penup()
            print(f"({x}x, {y}y): {px}")

    turtle.update()
    turtle.done()
