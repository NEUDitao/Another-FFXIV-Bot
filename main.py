#! /usr/bin/python3

import os
import discord
from dotenv import load_dotenv
import i_am

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('!hello'):
        await message.channel.send('Hello!')

    if msg.startswith('!iam'):
        await i_am.handle_iam(message)

    if msg.startswith('!whoami'):
        pass

load_dotenv()
client.run(os.getenv('TOKEN'))
