from PIL import Image, ImageFont, ImageDraw

carrot = Image.open('carrot.png')

for i in range(4):
    img = Image.open('scale.png')
    n = randint(0, 180)
    img.paste(carrot, (n, 0), carrot)
    img.save(f'img0{i}.png', 'png')

blank = Image.new('RGBA', (320, 226))
bg = Image.open('bg.png')
top = Image.open('top.png')
bot = Image.open('bot.png')
left = Image.open('left.png')
right = Image.open('right.png')

fnt = ImageFont.truetype('Lobster-Regular.ttf', 24)

for x in range(blank.width // bg.width + 1):
    for y in range(blank.height // bg.height + 1):
        blank.paste(bg, (x * bg.width, y * bg.height))

for y in range((blank.height - top.height - bot.height) // left.height + 1):
    blank.paste(left, (0, top.height + y * left.height), left)
    blank.paste(right, (blank.width - right.width, bot.height + y * right.height), right)

blank.paste(top, (0, 0), top)
blank.paste(bot, (0, (blank.height - bot.height)), bot)

names = ['Dirael', 'CitizenSilence', 'Romique', 'DobrijTigr']

for i in range(4):
    img = Image.open(f'img0{i}.png')
    x = blank.width - img.width - right.width - 3
    xt = left.width + 5
    y = ((blank.height - top.height - bot.height) // 8) * (2 * i + 1) - img.height // 2 + top.height + (fnt.size + 2)
    yt = y - fnt.size - 2
    blank.paste(img, (x, y), img)
    d = ImageDraw.Draw(blank)
    d.text((xt, yt), names[i], font=fnt)

blank.show()
