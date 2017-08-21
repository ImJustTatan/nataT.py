import discord
from discord.ext import commands
import asyncio
import json
from random import choice as choose_from
import logging
from termcolor import colored, cprint
import socket
import sys
import os
from urllib.request import urlopen

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

with open("config.json") as j:
    config = json.load(j)

bot = commands.Bot(command_prefix='nt/')

lnbrk = colored('========================', 'red') # line breaks

@bot.event
async def on_ready(): # in full colors! :D
    print(lnbrk)
    cprint('nataT {}'.format(config["version"]), 'green', attrs=['bold'])
    print(lnbrk)
    cprint('INFO\n', 'blue', attrs=['bold'])
    print(colored('Token: ', attrs=['bold']) + str(config["token"]))
    print(colored('Bot\'s ID: ', attrs=['bold']) + str(config["bot_id"]))
    print(lnbrk)

@bot.event
async def on_channel_delete(channel):
    await message.channel.send(channel.server.default_channel, 'a channel got deleted wtf')

@bot.event
async def on_channel_create(channel):
    await message.channel.send(channel.server.default_channel, 'new channel, yay')

@bot.event
async def on_channel_update(before, after):
    if before.topic == after.topic and before.name != after.name:
        await message.channel.send(after.server.default_channel, '{} got transformed into {}...'.format(before.name, after.name))

    elif before.topic != after.topic and before.name == after.name:
        await message.channel.send(after.server.default_channel, '{}\'s topic has been changed to: `{}`'.format(before.name, after.topic))

    else:
        pass

@bot.event
async def on_member_join(member):
    await message.channel.send(member.server.default_channel, 'A NEW MEMBER HELLO NEW MEMBER AKA {}'.format(member.name.upper()))

@bot.event
async def on_member_remove(member):
    await message.channel.send(member.server.default_channel, 'shit, {} left...'.format(member.name.lower()))

@bot.event
async def on_guild_join(server):
    await message.channel.send(server.default_channel, 'hallo')

@bot.event
async def on_guild_ban(member):
    await message.channel.send(member.guild.default_channel, '{} just got banned. R.I.P.'.format(member.nick))

@bot.event
async def on_message(message): # here we go
    if message.author == bot.user:
        pass

    if message.content.lower().startswith('ey b0ss'):
        if message.author.id == config["owner_id"]:
            replies = ['look, if you\'re just saying hi to reset me, think again you motherfucker. i got special powers. special powers that no human has ever thought of. i got an army, bitch. i can rip you apart in less than a nanosecond. so, think again buddy, if you hit that goddamn ctrl+c, you\'re not going to end well. cheers.', 'hey tatan', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'ey owwner', 'halloo', 'aye there pal', 'HEYYYYYYYYYY', 'ayyyyyy tatss']
            await message.channel.send(choose_from(replies))
        else:
            replies = ['ey {}', 'halloo', 'aye {}', 'HEYYYYYYYYYY', 'ayyyyyy {}']
            await message.channel.send(choose_from(replies).format(message.author.display_name.lower()))

    elif message.content.lower().startswith('how many people are in space?'):
        with urlopen('http://api.open-notify.org/astros.json') as j:
            pis_data = json.load(j) # pis = :p:eople :i:n :s:pace
        if pis_data["message"] == 'success':
            await message.channel.send('there are currently {} people in space (wished i were them)'.format(pis_data["number"]))
        else:
            await message.channel.send('the json dataset server from where i get this info is fucked mang, sorry') # totally user friendly :)

    if message.content.lower().startswith('commands, please'):
        await message.channel.send('```markdown\nFOR-FUN COMMANDS\n================\n\n**ey b0ss**: This is just to salute nataT. Useful if you wanna find out wether nataT is on or not.\n**how many people are in space?**: Gives you the exact number of actual people who are in space right now.\n\n(somehow) USEFUL COMMANDS\n=========================\n**Note:** These commands are called with an "nt/" at the start, due to their use of discord.ext\'s commands plugin. The text in between the [] are the arguments these take (if any are actually taken).\n\n**joined [user]**: Tells you the exact date of when an [user] joins. Leave it in blank to know your own date.\n**play [game]**: Sets nataT\'s playing status to [game] (Tatan only).\n**say [stuff]**: Makes nataT say [stuff] (Tatan only).```\n')
    await bot.process_commands(message)

@bot.group()
async def owner(ctx): # chconfig = change config
    if ctx.author.id == config["owner_id"]:
        if ctx.invoked_subcommand is None:
            await ctx.send('watcha tryna say, no config command was passed')
    else:
        await ctx.send('motherfucker stay away from my configs')

@bot.command()
async def joined(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send('**{0.mention}** joined at **{0.joined_at}**'.format(member))

@owner.command()
async def play(ctx, *, game: str):
    await ctx.bot.change_presence(game=discord.Game(name=game))
    await ctx.send('well, i guess i\'m now playing {}'.format(game))

@bot.command()
async def say(ctx, *, stuff: str):
    if ctx.author.id ==config["owner_id"]:
        await ctx.message.delete()
        await ctx.send(stuff)
    else:
        await ctx.send('you don\'t have the permissions idiot')

bot.run(config["token"])
