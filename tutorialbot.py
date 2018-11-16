import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '-')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='No Game No Life'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '$ping':
        await client.send_message(message.channel,'pong')
    if message.content == '$nudes':
        em = discord.Embed(description='Hello')
        em.set_image(url='https://media.giphy.com/media/ASd0Ukj0y3qMM/giphy.gif')
        await client.send_message(message.channel, embed=em)
    if ('Hi') in message.content:
       await client.delete_message(message)
    if message.content == '-Sxnssy':
        await client.send_message(message.channel,'Use code sxnssy for 60% off ')
    if message.content == '-RandomPumpkin':
        await client.send_message(message.channel,'He-He')
    if message.content == '-WolfaSharp':
        await client.send_message(message.channel,'Senpai-kun <3')
    if message.content == '-Vedrano':
        await client.send_message(message.channel,'Vedran-oooooooooooo')
    if message.content == '-Toni':
        await client.send_message(message.channel,'NijeToni')
    if message.content == '-Yuriko':
        await client.send_message(message.channel,'My love, He-He')
    if message.content == '-WesDONG':
        await client.send_message(message.channel,'This guy is a fucking god')
    if message.content == '-Ivanche23':
        await client.send_message(message.channel,'Its time to du-du-du-du-du-du-du-dule')
    if message.content == '-Atl.Mato':
        await client.send_message(message.channel,'Watch Infinity War <3')
    if message.content == '-Shocksy':
        await client.send_message(message.channel,'I wana have sex with you <3 (jk)')
    if message.content == '-DadoPLZ':
        await client.send_message(message.channel,'DadoPLZ+Brawlhalla=No life (jk)')
    if message.content == '-BreakTheGame':
        await client.send_message(message.channel,'TheGeyDude')
client.run('NTA1ODE5ODk5NDc4OTMzNTA0.Dsy_0w.-125EJo6tnFcKKrYsxA5fCeT4fk')
