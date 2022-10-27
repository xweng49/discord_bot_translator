import discord
import os
from googletrans import Translator

from discord.ext import commands

intents = discord.Intents.all()
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(message)
    if message.author == client.user:
        return

    if message.content.startswith('!ts'):
        # print(message.content.)
        await message.channel.send('hello!')

token = os.environ['token']
client.run(token)
