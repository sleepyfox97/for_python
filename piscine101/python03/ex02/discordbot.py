import discord
from PIL import Image,ImageFont,ImageDraw
from discord.ext import commands


TOKEN=""

bot = commands.Bot(command_prefix='!')
flag = 0
open_file_name = ""


@bot.event
async def on_ready():
    print('login done!')

@bot.command()
async def draw(ctx, * , text = "No text entered"):
    print(flag)
    if flag == 1:
        globals()[flag] = 0
        img = Image.open(open_file_name)
        font = ImageFont.truetype("arial.ttf", 24)
        draw = ImageDraw(img)
        draw.text((0,150),text, (0,0,0), font=font)
        imag.save(img)
        await ctx.send(file = dicord.File(open_file_name))
    else: 
        file_path = "./text.png"
        f = open(file_path, "wb")
        img = Image.new("RGB", (256, 256))
        draw = ImageDraw.Draw(img)
        draw.text((0,128),text, fill="white")
        img.save(f)
        await ctx.send(file = discord.File(file_path))
           

@bot.command()
async def setting(ctx, *, text):
    tmp = text.split()
    if tmp[0] == "images" and tmp[1] == "add":
        if ctx.message.attachments:
            file_path = str(ctx.message.attachments[0]).split('/')
            f = open(file_path[-1], "wb")
            await ctx.message.attachments[0].save(f)
            await ctx.send("Successfully added " + file_path[-1])
    elif tmp[0] == "images" and tmp[1] == "list":
        await ctx.send("aa")
    elif tmp[0] == "images" and tmp[1] == "use" and tmp[2]:
        f = open(tmp[2], "wb")
        if f:
            globals()[flag] = 1
            open_file_name = tmp[2]
            await ctx.send("Setting images done")
        else:
            await ctx.send("No such images...")

bot.run(TOKEN)

