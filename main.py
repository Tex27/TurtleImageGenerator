import os
from PIL import Image
import turtle
import time
import tkinter as tk
from tkinter import filedialog
from tqdm import tqdm


def choose_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Selecione uma Imagem",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if file_path:
        print(f"Selecionou: {file_path}")
    else:
        print("Nenhuma Imagem selecionada.")
    return file_path

def main():
    w = os.name
    clear = "cls" if w == "nt" else "clear"

    print("Escolha como quer selecionar a imagem")
    print("1 - Escreva o nome da imagem (deve estar na pasta './imagens/')")
    print("2 - Selecionar uma imagem via pasta")
    
    escolha = input("Opção: \n > ")
    os.system(clear)
    if escolha == "1":
        n = input("Nome da imagem (sem extensão): \n > ")
        image_path = f"./imagens/{n}.png"
        os.system(clear)
    elif escolha == "2":
        image_path = choose_image()
        if not image_path:
            print("Nenhuma imagem selecionada...")
            os.system(clear)
            return
    else:
        print("\n---Opção inválida---")
        os.system(clear)
        return

    escala = float(input("Escala (ex: 0.5 para reduzir ou 2 para aumentar): \n > "))
    os.system(clear)
    opcao = input("Opções do desenho \n r - Print Rápida \n n - Print Normal \n > ")
    os.system(clear)

    for i in range(0, 3):
        print("Analisando a Imagem... /")
        time.sleep(0.5)
        os.system(clear)
        print("Analisando a Imagem... -")
        time.sleep(0.5)
        os.system(clear)
        print("Analisando a Imagem... \\")
        time.sleep(0.5)
        os.system(clear)
        print("Analisando a Imagem... |")
        time.sleep(0.5)
        os.system(clear)

    try:
        img = Image.open(image_path)
        img = img.convert("RGBA")
    except FileNotFoundError:
        print(f"Imagem não encontrada: {image_path}")
        return

    l, a = img.size
    img = img.resize((int(l * escala), int(a * escala)), Image.NEAREST)
    l, a = img.size

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
    total = l * a
    pixeis_processados = 0
    with tqdm(total=total, desc="Progresso", unit=" px") as progress_bar:
        for x in range(0, l):
            for y in range(0, a):
                px = img.getpixel((x, y))
                color = '#%02x%02x%02x' % (px[0], px[1], px[2])
                tqdm.write(f"{sum}º px, ({x}x{y}y): {px}")
                pintar_pontos(escala, l, a, xOriginal=x, yOriginal=y, color=color)
                sum += 1

                pixeis_processados += 1
                progress_bar.update(1)
        return

def pintar_pontos(escala, l, a, color, xOriginal, yOriginal):
    x_scaled = xOriginal * escala
    y_scaled = yOriginal * escala

    turtle.setpos(x_scaled - l / 2, a / 2 - y_scaled)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.dot(escala * 2)
    turtle.penup()

    return

main()
