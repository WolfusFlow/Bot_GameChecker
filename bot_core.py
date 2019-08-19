import discord
import asyncio
import requests

DISCORD_BOT_TOKEN = ''

client = discord.Client()

@client.event
async def on_ready():
    print("I'm up!")
    await client.change_presence(game=discord.Game(name='Just Chilling'), #with live wires
                                 status=discord.Status('idle'),
                                 afk=True)


@client.event
async def on_message(message):
    channel = message.channel
    if message.author == client.user:
        return
    if message.content == "hello":
        await channel.message(" ^_^ ")
        # await client.send_message(message.channel, " ^_^")      

client.run(DISCORD_BOT_TOKEN)
