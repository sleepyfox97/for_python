import discord

TOKEN = 'ODU1MzA2MDk3NDM5MDE0OTcy.YMwj4A.FS9WMaDFHii1HqTgaCYfjoRi2eI'

client = discord.Client()

@client.event
async def on_ready():
    print('login done!')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == 'Hello':
        await message.channel.send('Hello!')

client.run(TOKEN)
