from PIL import Image, ImageFont, ImageDraw

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
carrot = Image.open('carrot_old.png')

for i in range(len(contributors)):
    img = Image.open('scale.png')
    max_x = img.width - 12
    coeff = max_val/max_x
    x = int(contributors[i][1]/coeff)
    if x > img.width - carrot.width:
        x = img.width - carrot.width
    img.paste(carrot, (x, 0), carrot)
    img.save(f'img0{i}.png', 'png')

blank = Image.new('RGBA', (320, 226))
bg = Image.open('bg.png')
top = Image.open('top.png')
bot = Image.open('bot.png')
left = Image.open('left.png')
right = Image.open('right.png')

fnt = ImageFont.truetype('Lobster-Regular.ttf', 20)

for x in range(blank.width // bg.width + 1):
    for y in range(blank.height // bg.height + 1):
        blank.paste(bg, (x * bg.width, y * bg.height))

for y in range((blank.height - top.height - bot.height) // left.height + 1):
    blank.paste(left, (0, top.height + y * left.height), left)
    blank.paste(right, (blank.width - right.width, bot.height + y * right.height), right)

blank.paste(top, (0, 0), top)
blank.paste(bot, (0, (blank.height - bot.height)), bot)

for i in range(len(contributors)):
    img = Image.open(f'img0{i}.png')
    x = blank.width - img.width - right.width
    xt = left.width + 5
    y = ((blank.height - top.height - bot.height) // 8) * (2 * i + 1) - img.height // 2 + top.height
    yt = y + 6
    blank.paste(img, (x, y), img)
    d = ImageDraw.Draw(blank)
    d.text((xt, yt), contributors[i][0], font=fnt)

blank.save('result.png', 'png')
