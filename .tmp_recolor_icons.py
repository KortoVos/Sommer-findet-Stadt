from PIL import Image
from pathlib import Path

files = [Path('public/icon-food.png'), Path('public/icon-glass.png'), Path('public/icon-music.png')]
target = (191, 22, 30)

for path in files:
    img = Image.open(path).convert('RGBA')
    pixels = img.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]
            if a == 0:
                continue
            pixels[x, y] = target[0], target[1], target[2], a
    img.save(path)
    print(f'updated {path}')
