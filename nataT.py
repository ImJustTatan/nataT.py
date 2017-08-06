import discord
import json
from random import choice as choose_from
import logging
from termcolor import colored, cprint

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

with open("config.json") as j:
    config = json.load(j)

bot = discord.Client()

lnbrk = colored('========================', 'red') # line breaks

@bot.event
async def on_ready():
    print(lnbrk)
    cprint('nataT {}'.format(config["version"]), 'green', attrs=['bold'])
    print(lnbrk)
    cprint('INFO\n', attrs=['bold'])
    print(colored('Token: ', attrs=['bold']) + config["token"])
    print(colored('Bot\'s ID: ', attrs=['bold']) + config["bot_id"])
    print(lnbrk)

@bot.event
async def on_channel_delete(channel):
    await bot.send_message(channel.server.default_channel, 'a channel got deleted wtf')

@bot.event
async def on_channel_create(channel):
    await bot.send_message(channel.server.default_channel, 'new channel, yay')

@bot.event
async def on_channel_update(before, after):
    if before.topic == after.topic and before.name != after.name:
        await bot.send_message(after.server.default_channel, '{} got transformed into {}...'.format(before.name, after.name))

    elif before.topic != after.topic and before.name == after.name:
        await bot.send_message(after.server.default_channel, '{}\'s topic has been changed to: `{}`'.format(before.name, after.topic))

    else:
        pass

@bot.event
async def on_member_join(member):
    await bot.send_message(member.server.default_channel, 'A NEW MEMBER HELLO NEW MEMBER AKA {}'.format(member.name.upper()))

@bot.event
async def on_member_remove(member):
    await bot.send_message(member.server.default_channel, 'shit, {} left...'.format(member.nick.lower()))

@bot.event
async def on_server_join(server):
    await bot.send_message(server.default_channel, 'hallo')

@bot.event
async def on_member_ban(member):
    await bot.send_message(member.server.default_channel, '{} just got banned. R.I.P.'.format(member.nick))

@bot.event
async def on_message(message): # here we go
    if message.author == bot.user:
        pass

    # todo

bot.run(config["token"])
        
