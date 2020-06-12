import discord
import asyncio
import requests

from discord import Game

'''
TODO Check if person started to play a game then check in some db(that will be added later)
if person already played this game - if so - nothing to do, else - add this game to game list
of a person's games.

Make a request to bot - asking if we(current user) have common games with a person(input username)
output is a list of games then people can play tougether.

Other things in this bot are just for init functional play and will be removed or transformed later.
'''

DISCORD_BOT_TOKEN = ''

client = discord.Client()

BTC_PRICE_URL_coinmarketcap = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=RUB'


@client.event
async def on_ready():
    print("I'm up!")
    await client.change_presence(activity=discord.Game("Just Chilling"))


@client.event
async def on_message(message):
    channel = message.channel
    if message.author == client.user:
        return
    if message.content == "hello":
        await message.channel.send(' ^_^')

    if message.content == 'user_list':
        for user in client.users:
            await message.channel.send(user)

    
    if message.content.startswith('$thumb'):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')

    if message.content.startswith('!btcprice'):
        print('[command]: btcprice ')
        btc_price_usd, btc_price_rub = get_btc_price()
        await message.channel.send( 'USD: ' + str(btc_price_usd) + ' | RUB: ' + str(btc_price_rub))

def get_btc_price():
    r = requests.get(BTC_PRICE_URL_coinmarketcap)
    response_json = r.json()
    usd_price = response_json[0]['price_usd']
    rub_rpice = response_json[0]['price_rub']
    return usd_price, rub_rpice

client.run(DISCORD_BOT_TOKEN)
