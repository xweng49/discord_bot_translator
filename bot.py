import discord
import os
from googletrans import Translator

intents = discord.Intents.all()

client = discord.Client(intents=intents)
token = os.environ['token']

translator = Translator()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author==client.user:
        return

    if message.content.startswith('!ts'):
        origin_message = message.content[3:].strip()
        
        if origin_message:
            translation = translator.translate(origin_message, src='en', dest='ja')
            await message.channel.send(f'{translation.text} \n{translation.pronunciation}')
        else:
            await message.channel.send(f'Nothing to translate')

        
        
        

client.run(token)
