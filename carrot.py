from PIL import Image, ImageFont, ImageDraw


def generate_image(contributors, max_val=2200):
    """
    :param contributors: list of tuples (name:str, value:int)
    :param max_val: int, a limiting value, should be left default in most cases
    :return: a pillow image object
    """
    contributors = sorted(contributors, key=lambda contributor: contributor[1], reverse=True)
    carrot = Image.open('carrot_old.png')

    for i in range(len(contributors)):
        img = Image.open('scale.png')
        max_x = img.width - 12
        coeff = max_val / max_x
        x = int(contributors[i][1] / coeff)
        if x > img.width - carrot.width:
            x = img.width - carrot.width
        img.paste(carrot, (x, 0), carrot)
        img.save(f'img0{i}.png', 'png')

    canvas = Image.new('RGBA', (320, 226))
    bg = Image.open('bg.png')
    top = Image.open('top.png')
    bot = Image.open('bot.png')
    left = Image.open('left.png')
    right = Image.open('right.png')

    fnt = ImageFont.truetype('Lobster-Regular.ttf', 20)

    for x in range(canvas.width // bg.width + 1):
        for y in range(canvas.height // bg.height + 1):
            canvas.paste(bg, (x * bg.width, y * bg.height))

    for y in range((canvas.height - top.height - bot.height) // left.height + 1):
        canvas.paste(left, (0, top.height + y * left.height), left)
        canvas.paste(right, (canvas.width - right.width, bot.height + y * right.height), right)

    canvas.paste(top, (0, 0), top)
    canvas.paste(bot, (0, (canvas.height - bot.height)), bot)

    for i in range(len(contributors)):
        img = Image.open(f'img0{i}.png')
        x = canvas.width - img.width - right.width
        xt = left.width + 5
        y = ((canvas.height - top.height - bot.height) // 8) * (2 * i + 1) - img.height // 2 + top.height
        yt = y + 6
        canvas.paste(img, (x, y), img)
        d = ImageDraw.Draw(canvas)
        d.text((xt, yt), contributors[i][0], font=fnt)
    return canvas


if __name__ == '__main__':
    contributors = []
    max_val = 2200

    for i in range(4):
        name = input(f'Name0{i+1}: ')
        val = None
        while val is None:
            try:
                val = int(input(f'Name0{i+1}\'s vals: '))
            except ValueError:
                print(f'ERROR: Name0{i+1}\'s vals must be an integer.')
        if val > max_val:
            val = max_val
        contributors.append((name, val))

    contributors = sorted(contributors, key=lambda contributor: contributor[1], reverse=True)
    canvas = generate_image(contributors, max_val)
    canvas.save('result.png', 'png')

