import discord

TOKEN = ''

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
