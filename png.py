from PIL import Image

# Создаем изображение с белым фоном
img = Image.new('RGB', (1280, 853), "white")
pixels = img.load()

# Читаем значения из файла task.txt
with open('task.txt', 'r') as file:
    for line in file:
        # Разбиваем строку на координаты и цвета
        parts = line.strip().replace('(', '').replace(')', '').split(':')
        coords = tuple(map(int, parts[0].split(',')))
        color = tuple(map(int, parts[1].split(',')))

        # Позиции в Python начинаются с 0, а не с 1
        x, y = coords[0] - 1, coords[1] - 1
        pixels[x, y] = color

# Сохраняем изображение
img.save('output_image.png')
