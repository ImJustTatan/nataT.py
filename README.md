### nataT.py

[![Chat on discord](https://img.shields.io/badge/chat-on%20discord-blue.svg "Tatan's server")](https://discord.gg/sUBbBvx) ![Bot version](https://img.shields.io/badge/version-v0.3-brightgreen.svg "Bot version")

***

**Note:** nataT.py is a complete rewrite from zero of [nataTbot](https://github.com/ImJustTatan/nataTbot), (obviously) coded with Python 3 ([discord.py](https://github.com/Rapptz/discord.py), to be more specific). More info [below](#about-the-change).

---

## A synopsis (again)

nataT is the first bot I've made and my first ever code project (which is the reason why the deprecated version was so messy and non-humanly-readable). It is pretty important for me since (from others' opinions) I can say that nataT is a pretty good bot to mess with. If you wanna see it in action, you can join my [Discord server](https://discord.gg/sUBbBvx). If you wanna build your own nataT, oh boy... Just see [below](#building).

---

## here were some pieces of code but they were completely useless since you could just check his code directly here in GitHub so instead here's a high-resolution pic of nataT's PFP for you to enjoy :)

![nataT's PFP](https://cdn.discordapp.com/attachments/290169252881629187/297845711847030784/Natat.png "PFP made by Vertecks.")

---

## Contributing

Pull requests (and issues showing errors) are completely welcome. They can recommend commands, messages, formatting, etc..

---

## Building

This is something that I've actually been asked to do via Discord, despite how infamous this bot was at the time of writing this (3 stars FTW). I'm not even sure why would anyone want to build such a specific bot, it's not even made for multiple servers... Whatever. If you're really going to try building nataT.py, you're going to need to replace *a lot* of things.

I do plan on making a buildable version, but it's definitively not going to be the same as nataT.

These are the requirements:

- Python 3.5+
- discord.py module (`pip install -U discord.py`)
- termcolor module (`pip install -U termcolor`)
- git (to clone, but you can download the code [from here](https://github.com/ImJustTatan/nataT.py/archive/master.zip) as a .zip file if you're lazy enough to not care about it)
- A Discord bot user. There are dozens of tutorials for this, but you can read [this one](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token) if you want it simple. Special thanks to [reactiflux](https://github.com/reactiflux/) for making it.

Seems like not much, right? Let's build it then. First things first, clone this repo:

`git clone https://github.com/ImJustTatan/nataT.py`

Then, rename `config-example.json` to `config.json`, and finally, edit it with actual info (token, bot ID, owner ID, etc.). If you're going to change one of the names (e.g. `owner_id` with `yourusername_id`), you'd need to replace every instance saying the old name (`owner_id`) with the new name (`yourusername_id`) in the `nataT.py` file.

When you're done with that, next to do is to edit the `nataT.py` strings to match with the config, IDs, names, etc. etc.. For example, if we have:

```python
@bot.event
async def on_message(message):
    if message.content.lower() == 'hello natat':
        await bot.send_message(message.channel, 'etc. etc.')
```
And your bot's name is, to give an example, "Faustino", you change it like this:

```python
@bot.event
async def on_message(message):
    if message.content.lower() == 'hello faustino':
        await bot.send_message(message.channel, 'etc. etc.')
```

And so on. This is the hardest part, depending on how *customized* you want your nataT. When you're done editing, just do `python nataT.py` and you're pretty much done. **Congratulations, you have your own nataT instance!**

---

## About the change

Here I explain why I decided to make nataT from scratch again in Python. It is actually a short story.

I'm not coding nataT in [discord.js](https://github.com/hydrabolt/discord.js) anymore because of how little I know about Node.JS (and JavaScript in general). nataTbot was literally just a copy-paste from tutorials and guides on how to make bots. It was the literal definition of laziness. In fact, nataT's name and original PFP were lazy by themselves, since they were just backward versions of me on Discord.

nataTbot was my first ever interaction with actual code (and not that `print('Hello World!')` crap), and my first ever public project. That was the reason to why the code was so messy, unorganized and crappy, because of my (literally) null experience with JavaScript and the fact that I just copy-pasted everything from guides and stuff.

So, instead of reorganizing the old legacy code and learning JS, I just did a fresh start using a language that I actually know in depth: Python 3. I've actually practiced with Python for Discord bots [before](https://github.com/ImJustTatan/PennyBot), and just with Python code in general, so it isn't such a messy and difficult work to do for me (unlike nataTbot).

And so, this repo was created. I'm keeping [nataTbot](https://github.com/ImJustTatan/nataTbot) in GitHub without licenses for anyone to see, edit and contribute, but it won't longer be supported by me. It is too messy to clean, anyway (I even once showed the token by accident in early commits, and a lot of them weren't even submitted with an updated `package.json`).


**tl;dr:** I'm using Python because it's what I know, and nataTbot was too messy, anyway. I am keeping nataTbot for anyone to edit.

---

nataT.py is licensed under the [MIT License](https://opensource.org/licenses/MIT). As said before, pull requests are completely welcome.

