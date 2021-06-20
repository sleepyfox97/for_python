import discord
from PIL import Image,ImageFont,ImageDraw
from discord.ext import commands


TOKEN = 'ODU1MzA2MDk3NDM5MDE0OTcy.YMwj4A.FS9WMaDFHii1HqTgaCYfjoRi2eI'


bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('login done!')

@bot.command()
async def text(ctx, *, arg):
    print("text command")
    print(arg)
    await ctx.send(arg)


@bot.command()
async def draw(ctx, * , text = "No text entered"):
    file_path = "./text.png"
    f = open(file_path, "wb")
    img = Image.new("RGB", (256, 256))
    draw = ImageDraw.Draw(img)
    draw.text((0,128),text, fill="white")
    img.save(f)
    await ctx.send(file = discord.File(file_path))

bot.run(TOKEN)

