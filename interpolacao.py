import numpy as np
from PIL import Image

def criar_imagem_teste(altura=8, largura=8):
    img = np.zeros((altura, largura), dtype=np.uint8)
    for y in range(altura):
        for x in range(largura):
            img[y, x] = int((x + y * largura) * 255 / (altura * largura - 1))
    return img

def vizinho_mais_proximo(src, nova_altura, nova_largura):
    src_altura, src_largura = src.shape
    dst = np.zeros((nova_altura, nova_largura), dtype=np.uint8)

    for y in range(nova_altura):
        for x in range(nova_largura):
            src_y = int(np.round(y * (src_altura - 1) / (nova_altura - 1)))
            src_x = int(np.round(x * (src_largura - 1) / (nova_largura - 1)))

            src_y = max(0, min(src_y, src_altura - 1))
            src_x = max(0, min(src_x, src_largura - 1))

            dst[y, x] = src[src_y, src_x]

    return dst

def bilinear(src, nova_altura, nova_largura):
    src_altura, src_largura = src.shape
    dst = np.zeros((nova_altura, nova_largura), dtype=np.uint8)

    for y in range(nova_altura):
        for x in range(nova_largura):
            src_y_f = y * (src_altura - 1) / (nova_altura - 1)
            src_x_f = x * (src_largura - 1) / (nova_largura - 1)

            y0 = int(np.floor(src_y_f))
            x0 = int(np.floor(src_x_f))
            y1 = min(y0 + 1, src_altura - 1)
            x1 = min(x0 + 1, src_largura - 1)

            dy = src_y_f - y0
            dx = src_x_f - x0

            f00 = src[y0, x0]
            f01 = src[y0, x1]
            f10 = src[y1, x0]
            f11 = src[y1, x1]

            valor = (1.0 - dy) * (1.0 - dx) * f00 + \
                    (1.0 - dy) * dx * f01 + \
                    dy * (1.0 - dx) * f10 + \
                    dy * dx * f11

            dst[y, x] = int(np.round(valor))

    return dst

def imprimir_matriz(nome, img):
    h, w = img.shape
    print(f"{nome} ({h}x{w}):")
    for y in range(h):
        for x in range(w):
            print(f"{img[y, x]:3d}", end=" ")
        print()
    print()

def main():
    print("=" * 50)
    print("Interpolação de Imagens - Aula 3")
    print("=" * 50 + "\n")

    # Criar imagem de teste
    original = criar_imagem_teste(8, 8)
    print("Imagem original (8x8):")
    imprimir_matriz("Original", original)
    Image.fromarray(original, mode='L').save("original.png")

    # Vizinho mais próximo - Ampliação
    vmp_amp = vizinho_mais_proximo(original, 16, 16)
    print("Vizinho mais próximo - Ampliação (16x16):")
    imprimir_matriz("VMP Ampliação", vmp_amp)
    Image.fromarray(vmp_amp, mode='L').save("vmp_ampliacao.png")

    # Vizinho mais próximo - Redução
    vmp_red = vizinho_mais_proximo(original, 4, 4)
    print("Vizinho mais próximo - Redução (4x4):")
    imprimir_matriz("VMP Redução", vmp_red)
    Image.fromarray(vmp_red, mode='L').save("vmp_reducao.png")

    # Bilinear - Ampliação
    bil_amp = bilinear(original, 16, 16)
    print("Interpolação Bilinear - Ampliação (16x16):")
    imprimir_matriz("Bilinear Ampliação", bil_amp)
    Image.fromarray(bil_amp, mode='L').save("bilinear_ampliacao.png")

    # Bilinear - Redução
    bil_red = bilinear(original, 4, 4)
    print("Interpolação Bilinear - Redução (4x4):")
    imprimir_matriz("Bilinear Redução", bil_red)
    Image.fromarray(bil_red, mode='L').save("bilinear_reducao.png")

    print("[OK] Imagens salvas com sucesso!")
    print("  - original.png")
    print("  - vmp_ampliacao.png")
    print("  - vmp_reducao.png")
    print("  - bilinear_ampliacao.png")
    print("  - bilinear_reducao.png")

if __name__ == "__main__":
    main()
