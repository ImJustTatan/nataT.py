import discord
import json
from random import choice as choose_from
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

with open("config.json") as j:
    config = json.load(j)

bot = discord.Client()

lnbrk = '------------------------' # line breaks

@bot.event
async def on_ready():
    print(lnbrk)
    print('nataT {}'.format(config["version"]))
    print(lnbrk)
    print('INFO\n\n')
    print('Token: {}'.format(config["token"]))
    print('Bot\'s ID: {}'.format(config["bot_id"]))
    print(lnbrk)

@bot.event
async def on_channel_delete():
    await bot.send_message(Server.default_channel, 'a channel got deleted wtf')

@bot.event
async def on_channel_create():
    await bot.send_message(Server.default_channel, 'new channel, yay')

@bot.event
async def on_channel_update():
    if before.topic == after.topic and before.name != after.name:
        await bot.send_message(Server.default_channel, '{} got transformed into {}...'.format(before.name, after.name))

    elif before.topic != after.topic and before.name == after.name:
        await bot.send_message(Server.default_channel, '{}\'s topic has been changed to: `{}`'.format(before.name, after.topic))

    else:
        pass

@bot.event
async def on_member_join():
    await bot.send_message(Server.default_channel, 'A NEW MEMBER HELLO NEW MEMBER AKA {}'.format(member.nick.upper()))

@bot.event
async def on_member_remove():
    await bot.send_message(Server.default_channel, 'shit, {} left...'.format(member.nick))

@bot.event
async def on_server_join():
    await bot.send_message(Server.default_channel, 'hallo')

@bot.event
async def on_member_ban():
    await bot.send_message(Server.default_channel, '{} just got banned. R.I.P.'.format(member.nick))

@bot.event
async def on_message(message): # here we go
    if message.author == bot.user:
        pass

    # todo

bot.run(config["token"])
        
